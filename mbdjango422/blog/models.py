from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from taggit.managers import TaggableManager


# Modelo CATEGORIA
class Category(models.Model):
    name = models.CharField("nombre", max_length=100)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de edición", auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.name


# Manager Personalizado
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


# Modelo POST
class Post(models.Model):
    STATUS_CHOICES = (("draft", "Borrador"), ("published", "Publicado"))

    title = models.CharField("titulo", max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, verbose_name="autor", on_delete=models.CASCADE, related_name="blog_posts",
    )

    image = models.ImageField("imagen", upload_to="blog", blank=True, null=True)
    body = RichTextUploadingField("contenido")
    categories = models.ManyToManyField(
        Category, verbose_name="categorías", related_name="get_posts", blank=True,
    )

    publish = models.DateTimeField("fecha de publicación", default=timezone.now)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificación", auto_now=True)
    status = models.CharField(
        "estado", max_length=10, choices=STATUS_CHOICES, default="draft"
    )

    objects = models.Manager()  # el manager por defecto
    published = PublishedManager()  # nuestro manager personalizado.
    tags = TaggableManager()

    class Meta:
        ordering = ["-publish"]

    def get_absolute_url(self):
        return reverse(
            "blog:post-detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

    def __str__(self):
        return self.title


# Modelo COMENTARIO
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField("nombre", max_length=80)
    email = models.EmailField("email")
    body = models.TextField("comentario")

    created = models.DateTimeField("fecha creación", auto_now_add=True)
    updated = models.DateTimeField("fecha actualización", auto_now=True)
    active = models.BooleanField("estado", default=False)
    politica = models.BooleanField(default=False)

    class Meta:
        ordering = ("created",)
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"

    def __str__(self):
        return "Comentario de {} sobre el post {}".format(self.name, self.post)
