import re
from django import forms


# Regex Pattern (Detects URLs with or without HTTP/WWW)
NOURL_PATTERN = (
    r'/((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z0-9\&\.\/\?\:@\-_=#])*/'
)


class FormularioModal(forms.Form):
    nombre = forms.CharField(max_length=20)

    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'tel',
                'class': 'validate',
                'pattern': '[0-9]{9}',
                'title': 'Introduzca solo números sin espacios',
            }
        ),
        max_length=10,
    )

    email = forms.EmailField(
        max_length=100, widget=forms.EmailInput(attrs={'class': 'validate'})
    )

    asunto = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'validate', 'pattern': '[A-Za-z ]{4,50}'}),
    )

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'materialize-textarea'})
    )

    politica = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    # esta es la forma de indica la documentación.
    nombre.widget.attrs.update(
        {
            'class': 'validate',
            'pattern': '[A-Za-z ]{3,20}',
            'title': 'El nombre debe tener mínimo 4 caracteres',
        }
    )

    # Nuestras reglas de validación
    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        match = re.search(NOURL_PATTERN, mensaje)
        num_palabras = len(mensaje.split())

        if match:
            raise forms.ValidationError('¡ No se permiten enlaces. !')

        if num_palabras < 4:
            raise forms.ValidationError('¡ Se requieren mínimo 4 palabras. !')

        return mensaje
