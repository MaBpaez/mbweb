import json
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_http_methods
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.cache import cache_page
from django.template import RequestContext

from fcm_django.models import FCMDevice
from blog.models import Post
from .forms import FormularioModal


@csrf_exempt
@require_http_methods(["POST"])
def save_token(request):
    body = request.body.decode("utf-8")
    bodyDict = json.loads(body)
    print(bodyDict)
    token = bodyDict["toke"]
    exist = FCMDevice.objects.filter(registration_id=token, active=True)

    if exist:
        return HttpResponseBadRequest(json.dumps({"mensaje": "El token ya existe"}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    # solo si el usuario esta autenticado
    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({"mensaje": "Token guardado"}))
    except:
        return HttpResponseBadRequest(
            json.dumps({"mensaje": "No se ha podido guardar"})
        )


# Vista para comprobar y validar FORMULARIO MODAL Y CONTACTO
# =========================================================
def check_form_modal(request):
    form_modal = FormularioModal(request.POST)  # vinculamos el formulario
    if form_modal.is_valid():
        """reCAPTCHA validation"""
        recaptcha_response = request.POST.get("g-recaptcha-response")
        data = {
            "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            "response": recaptcha_response,
        }
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
        result = r.json()

        """ if reCAPTCHA returns True """
        if result["success"]:
            print(result)
            print("FORMULARIO ENVIADO CON EXITO")
            cd = form_modal.cleaned_data  # obtenemos los datos limpios
            # Enviamos los datos
            send_mail(
                f"Asunto: {cd['asunto']}",
                f"Nombre: {cd['nombre']}\nTeléfono: {cd['telefono']}\nCorreo "
                f"electrónico: {cd['email']}\nPolítica Privacidad: {cd['politica']}\n"
                f"Mensaje:\n\n{cd['mensaje']}",
                "info@mbsocialweb.net",
                ["bravopaezm.15@gmail.com"],
            )
            return result
        # messages.error(request, "ReCAPTCHA no válido. Inténtalo de nuevo.")

    return form_modal


# Vista para Formulario enviado con éxito
# =======================================
def form_successfully(request):
    return render(request, "core/form-succesfylly.html")


# Vista para HOME
# ===============
def home(request):
    blog_slider_posts = cache.get("blog_slider_posts")

    if not blog_slider_posts:
        blog_slider_posts = Post.published.order_by("-publish")[:6]
        cache.set("blog_slider_posts", blog_slider_posts, 60 * 15)

    if request.method == "POST" and "modal" in request.POST:
        form_modal = check_form_modal(request)
        form = FormularioModal()
        if "success" in form_modal:
            return redirect("form_success")

    elif request.method == "POST":
        form = check_form_modal(request)
        form_modal = FormularioModal()
        if "success" in form:
            return redirect("form_success")

    else:
        form_modal = FormularioModal()
        form = FormularioModal()

    return render(
        request,
        "core/home.html",
        {
            "slider_posts": blog_slider_posts,
            "form_modal": form_modal,
            "form": form,
            "recaptcha_site_key": settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


# Vista para página de error_404
# ==============================
def error_404_view(request, exception, template_name="core/error_404.html"):
    response = render(request, "core/error_404.html")
    response.status_code = 404
    return response


# Vista para robots.txt
# =====================
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "crawl-delay: 1",
        "Disallow: /admin/",
        "Disallow: /formulario-enviado/",
        "Disallow: /save-token/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
