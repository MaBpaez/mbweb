import requests
import json


def enviar_notificacion(
    request, objeto, key, contents_es, web_buttons_text, url_objeto=None
):
    if not url_objeto:
        url_objeto = objeto.get_absolute_url()

    header = {
        "Content-Type": "application/json",
        "Authorization": "Basic NjNkY2UzNTQtZDVlMy00MjE2LWI2YWQtMDYwZTA4MjVhMTAz",
        "accept": "application/json",
    }

    payload = {
        "excluded_segments": ["Inactive Users"],
        "delayed_option": "immediate",
        "headings": {
            "en": objeto.title,
            "es": objeto.title,
        },
        "contents": {"es": contents_es, "en": "New Article in our blog"},
        "web_url": f"http://{request.get_host()}{url_objeto}",
        "app_id": "ad0f712d-fa32-4ff6-95d5-937f35459109",
        "filters": [
            {"field": "tag", "key": key, "relation": "=", "value": "1"},
        ],
        "web_buttons": [
            {
                "id": "read-more-button",
                "text": web_buttons_text,
                "icon": "http://i.imgur.com/MIxJp1L.png",
                "url": f"http://{request.get_host()}{url_objeto}",
            },
        ],
    }

    response = requests.post(
        "https://onesignal.com/api/v1/notifications",
        headers=header,
        data=json.dumps(payload),
    )

    print(response.status_code, response.reason)
    print(response.text)
