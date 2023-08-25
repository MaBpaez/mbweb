from django.shortcuts import render, redirect
from django.conf import settings
from core.forms import FormularioModal
from core.views import check_form_modal


def fbshop(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        "socialmedia/facebook.html",
        {
            "form_modal": form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def appsfb(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        "socialmedia/aplicaciones-facebook.html",
        {
            "form_modal": form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def smcontent(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        "socialmedia/contenido-redes-sociales.html",
        {
            "form_modal": form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def creationnetwork(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        "socialmedia/redes-sociales.html",
        {
            "form_modal": form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )
