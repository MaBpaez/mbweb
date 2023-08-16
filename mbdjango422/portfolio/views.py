from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.urls.base import reverse
from core.forms import FormularioModal
from django.conf import settings
from core.views import check_form_modal
from .models import Work, CategoryWork


# Vista para el LISTADO DE LOS TRABAJOS
# =====================================
def portafolio(request, category_id=None, category_name=None):
    category = None
    _category_name = category_name

    object_list = Work.published.all()
    category_list = CategoryWork.objects.all()

    if category_id:
        category = get_object_or_404(CategoryWork, id=category_id)
        object_list = category.get_works.all().filter(status='published')

    # Modal
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    # Paginación
    paginator = Paginator(object_list, 10)  # posts(objects) in each page
    page = request.GET.get("page")
    try:
        works = paginator.page(page)  # todos los objetos de una página

    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        works = paginator.page(1)

    except EmptyPage:
        # if pages is out of range deliver las page of results
        works = paginator.page(paginator.num_pages)

    return render(
        request,
        "portfolio/trabajos.html",
        {
            "page": page,
            "works": works,
            "categories": category_list,
            "form_modal": form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


# Vista para el DETALLE DE UN TRABAJO
# ===================================
# def work_detail(request, year, month, day, work):
#     work = get_object_or_404(
#         Work,
#         slug=work,
#         status="published",
#         publish__year=year,
#         publish__month=month,
#         publish__day=day,
#     )


# Listado de trabajos por categorías
# ===============================
#def get_category(request, category_id, category_name):
#    category = get_object_or_404(CategoryWork, id=category_id)
#    _category_name = category_name
#
#    # todos los posts de la categoria utilizando el related_name
#    object_list = category.get_works.all()
#
#    paginator = Paginator(object_list, 10)  # works in each page
#    page = request.GET.get('page')
#    try:
#        works = paginator.page(page)  # todos los objetos de una página
#
#    except PageNotAnInteger:
#        # if page is not an integer deliver the first page
#        works = paginator.page(1)
#
#    except EmptyPage:
#        # if pages is out of range deliver las page of results
#        works = paginator.page(paginator.num_pages)
#
#    return render(
#        request,
#        'portfolio/trabajos_por_categoria.html',
#        {'category': category, 'page': page, 'works': works},
#    )
