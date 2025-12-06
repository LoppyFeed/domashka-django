from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ReviewForm
from .models import Review

POSTS = [
    {
        'slug': 'welcome-to-django',
        'title': 'Первые шаги с Django',
        'summary': 'Как устроен проект, зачем нужны настройки и что можно развернуть за 5 минут.',
        'author': 'Команда курса',
        'content': """
            Django помогает быстро собирать полнофункциональные веб-приложения за счет готовых
            компонентов: ORM, маршрутизации, шаблонов и админки. В этом мини-посте мы
            напоминаем, что начинать лучше всего с виртуального окружения, настройки SECRET_KEY
            и первого запуска `runserver`. Остальное вы постепенно добавите по мере прохождения
            курса.
        """,
    },
    {
        'slug': 'templates-and-static',
        'title': 'Шаблоны и статика',
        'summary': 'Подключаем базовый шаблон, наследуем страницы и добавляем немного стилей.',
        'author': 'Команда курса',
        'content': """
            Наследование шаблонов в Django позволяет переиспользовать шапку, футер и общий каркас
            страниц. Объявите `{% block content %}` в базовом шаблоне и расширяйте его в
            дочерних файлах. Статические файлы складывайте в папку `static/` и подключайте
            через тег `{% load static %}`. Так дизайн будет единообразным.
        """,
    },
    {
        'slug': 'guestbook',
        'title': 'Гостевая книга с проверкой',
        'summary': 'Добавляем форму, модель и модерацию отзывов.',
        'author': 'Команда курса',
        'content': """
            Модель отзывов помогает собирать обратную связь от пользователей. Добавьте булевое
            поле `is_verified`, чтобы администратор решал, какой текст показать на сайте. Форма
            на странице создаёт новую запись, а список выводит только проверенные отзывы.
            Так вы защищаете аудиторию от случайного спама.
        """,
    },
]


def home(request):
    return render(request, 'blog/home.html', {'posts': POSTS})


def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, slug: str):
    try:
        post = next(post for post in POSTS if post['slug'] == slug)
    except StopIteration as exc:
        raise Http404('Пост не найден') from exc
    return render(request, 'blog/post_detail.html', {'post': post})


def reviews(request):
    approved_reviews = Review.objects.filter(is_verified=True)
    form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Отзыв отправлен. После проверки он появится на странице.')
        return redirect('blog:reviews')

    return render(
        request,
        'blog/reviews.html',
        {'reviews': approved_reviews, 'form': form},
    )
