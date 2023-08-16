from django.shortcuts import render, redirect
from django.conf import settings
from core.forms import FormularioModal
from core.views import check_form_modal


def webmedida(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'webdesign/web-a-medida.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def hosting(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'webdesign/hosting.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def landingpage(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'webdesign/landing.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def customblog(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'webdesign/blog-personalizado.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def portfolio(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'webdesign/portfolio.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def webmaintenance(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'webdesign/mantenimiento-web.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )
