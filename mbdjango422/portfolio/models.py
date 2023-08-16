from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# from django.urls import reverse


# MODELOS DEL PORTAFOLIOS
# =======================

# Modelo CATEGORIA
class CategoryWork(models.Model):
    name = models.CharField("nombre", max_length=100)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de edición", auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "categoría portafolio"
        verbose_name_plural = "categorías portafolio"

    def __str__(self):
        return self.name


# Manager Personalizado
class PublishedWorkManager(models.Manager):
    def get_queryset(self):
        return super(PublishedWorkManager, self).get_queryset().filter(status="published")


# Modelo POST
class Work(models.Model):
    STATUS_CHOICES = (("draft", "Borrador"), ("published", "Publicado"))

    title = models.CharField("titulo", max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User,
        verbose_name="autor",
        on_delete=models.CASCADE,
        related_name="portfolio_works",
    )

    image = models.ImageField("imagen", upload_to="portfolio", blank=True, null=True)
    body = RichTextUploadingField("contenido")
    categories = models.ManyToManyField(
        CategoryWork,
        verbose_name="categorías",
        related_name="get_works",
        blank=True,
    )

    publish = models.DateTimeField("fecha de publicación", default=timezone.now)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificación", auto_now=True)
    timeread = models.CharField("tiempo lectura", max_length=40)
    status = models.CharField(
        "estado", max_length=10, choices=STATUS_CHOICES, default="draft"
    )

    objects = models.Manager()  # el manager por defecto
    published = PublishedWorkManager()  # nuestro manager personalizado.

    class Meta:
        ordering = ["-publish"]
        verbose_name = "trabajo"
        verbose_name_plural = "trabajos"

    # def get_absolute_url(self):
    #     return reverse(
    #         "portfolio:work-detail",
    #         args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
    #     )

    def __str__(self):
        return self.title
