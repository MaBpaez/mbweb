from django.shortcuts import render, redirect
from core.forms import FormularioModal
from core.views import check_form_modal
from django.conf import settings


def corporateimage(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'graphicdesign/imagen-corporativa.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


def logotipo(request):
    if request.method == 'POST' and 'modal' in request.POST:
        form_modal = check_form_modal(request)
        if 'success' in form_modal:
            return redirect('form_success')
    else:
        form_modal = FormularioModal()

    return render(
        request,
        'graphicdesign/logotipo.html',
        {
            'form_modal': form_modal,
            'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )
