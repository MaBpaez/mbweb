from django.db import models


# Modelo para las REDES SOCIALES
# ==============================
class Link(models.Model):
    key = models.SlugField('nombre clave', max_length=100, unique=True)
    value = models.CharField('red social', max_length=200)
    url = models.URLField('enlace', max_length=200, blank=True, null=True)
    created = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('fecha de edición', auto_now=True)

    class Meta:
        ordering = ['value']
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'

    def __str__(self):
        return self.value
