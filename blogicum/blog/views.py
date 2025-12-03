from django.shortcuts import render

posts = [
    # ... ваш список постов ...
]


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, id):
    """Детальная страница поста."""
    template = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категории."""
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
