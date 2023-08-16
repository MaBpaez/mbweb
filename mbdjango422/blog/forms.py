from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    nombre = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "validate",
                "pattern": "[A-Za-z ]{3,20}",
                "title": "El nombre debe tener mínimo 4 caracteres",
            }
        ),
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "validate"}))
    para = forms.EmailField(widget=forms.EmailInput(attrs={"class": "validate"}))
    mensaje = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"class": "materialize-textarea"})
    )
    politica = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "checkbox"}))

    # Nuestras reglas de validación
    def clean_mensaje(self):
        mensaje = self.cleaned_data["mensaje"]
        num_palabras = len(mensaje.split())

        if num_palabras < 4:
            raise forms.ValidationError("¡ Se requieren mínimo 4 palabras !")
        return mensaje


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body", "politica")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "validate",
                    "pattern": "[A-Za-z ]{3,20}",
                    "title": "El nombre debe tener mínimo 4 caracteres",
                }
            ),
            "email": forms.EmailInput(attrs={"class": "validate"}),
            "body": forms.Textarea(attrs={"class": "materialize-textarea"}),
            "politica": forms.CheckboxInput(
                attrs={"class": "checkbox", "required": True}
            ),
        }

    # Nuestras reglas de validación
    def clean_body(self):
        body = self.cleaned_data["body"]
        num_palabras = len(body.split())

        if num_palabras < 4:
            raise forms.ValidationError("¡ Se requieren mínimo 4 palabras !")
        return body


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'type': 'search', 'placeholder': 'Buscar...',
                                      'aria-label': 'Buscar en el listado de posts'}),
    )
