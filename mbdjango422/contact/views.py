from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from core.forms import FormularioModal
from django.conf import settings
from core.views import check_form_modal


@cache_page(60 * 2)
def contact(request):
    if request.method == 'POST':
        form = check_form_modal(request)
        if 'success' in form:
            return redirect('form_success')
    else:
        form = FormularioModal()

    return render(
        request,
        'contact/contacto.html',
        {'form': form, 'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY},
    )
