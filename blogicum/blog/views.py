from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def index(request):
    post_list = Post.objects.published().select_related(
        'category', 'author', 'location'
    ).order_by('-pub_date')[:5]

    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.published().select_related(
            'category', 'author', 'location'
        ),
        id=id
    )

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug
    )

    post_list = Post.objects.published().select_related(
        'author', 'location'
    ).filter(
        category=category
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
