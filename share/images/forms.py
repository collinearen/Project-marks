import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    description = forms.Textarea()
    url_user = forms.URLField(label="Ссылка на вебсайт", required=False)

    class Meta:
        model = Image
        fields = ['title', 'url', 'url_user', 'description']
        widgets = {
            'url': forms.HiddenInput(),
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL-адрес не соответствует допустимым расширениям изображений.')
        return url

    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'f{name}.{extension}'
        # download image from the given URL
        response = requests.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image
