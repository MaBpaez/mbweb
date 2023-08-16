"""
Procesador de contexto para tener en todos los templates los enlaces a las
redes sociales
"""
from django.core.cache import cache
from .models import Link


def ctx_dict(request):
    """funcion para el diccionario de contexto de redes sociales"""

    ctx = {}
    Links = cache.get("links")
    if not Links:
        Links = Link.objects.all()
        cache.set("links", Links, 60 * 15)

    for link in Links:
        ctx[link.key] = link.url

    return ctx
