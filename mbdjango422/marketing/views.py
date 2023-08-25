from django.shortcuts import render, redirect
from django.conf import settings
from core.forms import FormularioModal
from core.views import check_form_modal


def ads(request):
    if request.method == 'POST' and'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'marketing/google-ads.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def emailMarketing(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'marketing/email-marketing.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def socialAds(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'marketing/social-ads.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def seo(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'marketing/seo.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def business(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'marketing/google-business.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def analiticWeb(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'marketing/analitica-web.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )
