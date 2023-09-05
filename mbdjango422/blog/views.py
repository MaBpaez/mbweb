import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

from .models import Post, Comment, Category
from .forms import EmailPostForm, CommentForm, SearchForm
from taggit.models import Tag


# Vista para el LISTADO DE LOS POSTS
# ==================================
def post_list(request, tag_slug=None, category_id=None, category_name=None):
    # object_list = Post.published.all()
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#prefetch-related
    object_list = Post.published.prefetch_related('categories')

    tag_list = Tag.objects.all().order_by("name")
    tag = None
    category = None
    canonical = True
    _category_name = category_name
    form_search = SearchForm()

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
        canonical = False

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        # todos los posts de la categoria utilizando el related_name
        object_list = category.get_posts.all()
        canonical = False

    paginator = Paginator(object_list, 10)  # posts(objects) in each page
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)  # todos los objetos de una página

    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
        # if pages is out of range deliver las page of results
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        "blog/list.html",
        {
            "category": category,
            "page": page,
            "posts": posts,
            "tag": tag,
            "tag_list": tag_list,
            "CANONICAL": canonical,
            "form": form_search,
        },
    )


# Vista para el DETALLE DE UN POST
# ================================
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            """reCAPTCHA validation"""
            recaptcha_response = request.POST.get("g-recaptcha-response")
            data = {
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response,
            }
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", data=data
            )
            result = r.json()

            """ if reCAPTCHA returns True """
            if result["success"]:
                print(result)
                print("COMENTARIO ENVIADO CON ÉXITO")

                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)

                # Assign the current post to the comment
                new_comment.post = post

                # Save the comment to the database
                new_comment.save()

                # Redireccionamos a comentario enviado con éxito
                return redirect("blog:comment_sent", commented_post=post.slug)

    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "recaptcha_site_key": settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


# Vista para compartir por EMAIL UN POST
# ======================================
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False
    canonical = False

    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data

            # Enviamos email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) te recomienda leer este post "{}"'.format(
                cd["nombre"], cd["email"], post.title
            )
            message = 'Leer "{}" en {}\n\nMensaje de {}: {}'.format(
                post.title, post_url, cd["nombre"], cd["mensaje"]
            )
            send_mail(subject, message, "info@mbsocialweb.net", [cd["para"]])
            sent = True

    else:
        form = EmailPostForm()

    return render(
        request,
        "blog/share.html",
        {
            "post": post,
            "form": form,
            "sent": sent,
            "CANONICAL": canonical,
        },
    )


# Vista para Comentario enviado con éxito
# =======================================
def comment_successfully(request, commented_post):
    post = get_object_or_404(Post, slug=commented_post, status="published")
    canonical = False

    return render(
        request,
        "blog/comment-successfully.html",
        {"post": post, "CANONICAL": canonical},
    )


# Listado de posts por categorías
# ===============================
# def get_category(request, category_id):
# category = get_object_or_404(Category, id=category_id)

# todos los posts de la categoria utilizando el related_name
# object_list = category.get_posts.all()

# paginator = Paginator(object_list, 10)  # posts in each page
# page = request.GET.get('page')
# try:
# posts = paginator.page(page)  # todos los objetos de una página

# except PageNotAnInteger:
# if page is not an integer deliver the first page
# posts = paginator.page(1)

# except EmptyPage:
# if pages is out of range deliver las page of results
# posts = paginator.page(paginator.num_pages)

# return render(request, 'blog/posts_by_category.html', {
#  'category': category,
#  'page': page,
#  'posts': posts
# })


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    # tag_list = Tag.objects.all().order_by('name')

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            # Búsqueda
            results = set(
                Post.published.prefetch_related('categories').filter(
                    Q(title__icontains=query)
                    | Q(body__icontains=query)
                    | Q(tags__name=query)
                )
            )
            # print(results)

    return render(
        request, "blog/search.html", {"query": query, "form": form, "results": results}
    )
