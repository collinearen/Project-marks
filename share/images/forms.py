import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    title = forms.CharField(label="Название", )
    description = forms.Textarea()
    leave_url = forms.BooleanField(required=False, label="Оставить ссылку на вебсайт?")

    class Meta:
        model = Image
        fields = ['title', 'leave_url', 'url', 'website_url', 'description']
        widgets = {
            'url': forms.HiddenInput(),
            'website_url': forms.HiddenInput(),

        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL-адрес не соответствует допустимым расширениям изображений')
        return url

    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)

        image_url = self.cleaned_data['url']
        if not self.cleaned_data['leave_url']:
            image.website_url = ""
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'f{name}.{extension}'
        # Загрузка изображения с указанного URL
        response = requests.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image
