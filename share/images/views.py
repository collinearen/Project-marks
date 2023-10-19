import redis
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from account.models import Profile
from actions.utils import create_action, delete_action
from .forms import ImageCreateForm
from .models import Image
from django.db import transaction
from actions.models import Action

# соединить с redis
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data

            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user

            # Обновляем информацию в модели Profile, что пользователь, добавивший новую фотографию, считается активным
            profile = Profile.objects.get_or_create(user=request.user)[0]
            profile.active = True
            profile.save()

            new_image.save()
            create_action(request.user, 'поделился', new_image)
            messages.success(request, 'Изображение успешно сохранено!')
            # redirect to new created image detail view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    # increment total image views by 1
    total_views = r.incr(f'image:{image.id}:views')
    # increment image ranking by 1
    r.zincrby('image_ranking', 1, image.id)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_views': total_views})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'лайкнул', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 5)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')

    # <-- rating -->
    image_ranking = r.zrange('image_ranking', 0, -1, desc=True)[10:]
    image_ranking_ids = [int(id) for id in image_ranking]

    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            # If AJAX request and page out of range
            # return an empty page
            return HttpResponse('')
        # If page out of range return last page of results
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request,
                      'images/image/list_images.html',
                      {'section': 'images',
                       'images': images,
                       'most_viewed': most_viewed
                       })
    return render(request,
                  'images/image/list.html',
                  {'section': 'images',
                   'images': images,
                   'most_viewed': most_viewed
                   })


@login_required
def image_ranking(request):
    # get image ranking dictionary

    return render(request,
                  'images/image/ranking.html',
                  {'section': 'images',
                   'most_viewed': most_viewed})


@login_required
def user_images_list(request, user_id):
    user = User.objects.get(id=user_id)
    cur_user = request.user
    if user_id == cur_user.id:
        images = Image.objects.filter(user=user)
        paginator = Paginator(images, 8)
        page = request.GET.get('page')
        images_only = request.GET.get('images_only')
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            images = paginator.page(1)
        except EmptyPage:
            if images_only:
                # If AJAX request and page out of range
                # return an empty page
                return HttpResponse('')
            # If page out of range return last page of results
            images = paginator.page(paginator.num_pages)
        if images_only:
            return render(request,
                          'images/image/user_image_list.html',
                          {'section': 'images',
                           'images': images})
        return render(request,
                      'images/image/user_image_list.html',
                      {'section': 'images',
                       'images': images})
    else:
        return render(request, "images/notfound/NotFound.html")


def delete(request, id_image):
    '''
    Здесь мы используем менеджер транзакций для обеспечения атомарности операции удаления,
    а также фильтр для выбора записей,
    которые нужно удалить. Если во время удаления возникнет ошибка,
    транзакция будет откачена и исключение будет обработано.
    Здесь мы получаем image_id картинки, которую пользователь хочет удалить,
     и через этот image_id мы удаляем ее в таблице Image и все записи в Actions, связанные с этой картиной
    '''
    try:
        with transaction.atomic():
            image = Image.objects.get(id=id_image)
            image.delete()
            Action.objects.filter(target_id=id_image).delete()
    except Exception as e:
        print(e)
    return render(request, 'images/image/delete_success.html')
