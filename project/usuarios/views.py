from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Usuario

# Create your views here.
from django.views import View


class RegisterUser(View):
    template_name = 'register_user.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = UserForm(request.POST)

        dados_form = form.data

        if form.is_valid():
            novo_usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
            usuario = Usuario(user_name=dados_form['nome'],
                              user_last_name=dados_form['sobrenome'],
                              user_birthday=dados_form['data'],
                              user_cellphone_number=dados_form['telefone'],
                              user_habilities=dados_form['habilidades'],
                              user_usuario=novo_usuario)

            usuario.save()
            return redirect('ctsp:index')

        return render(request, self.template_name, {"form": form})