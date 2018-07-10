from django import forms
from .models import User


class UserForm(forms.Form):
    nome = forms.CharField(required=True)
    sobrenome = forms.CharField(required=True)
    data = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    habilidades = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    confirmsenha = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(UserForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(email=self.data['email']).exists()

        if user_exists:
            self.adiciona_erro('Esse email ja foi cadastrado')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
