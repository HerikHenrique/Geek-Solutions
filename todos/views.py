from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import EmailLoginForm
from .models import Cliente
from django import forms

# Create your views here.
def home(request):
 return render(request, "todos/home.html")

def page1(request):
 return render(request, "todos/page1.html")

def cliente_login(request):
    erro = None
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    erro = "E-mail ou senha inválidos."
            except User.DoesNotExist:
                erro = "E-mail ou senha inválidos."
    else:
        form = EmailLoginForm()
    return render(request, "todos/cliente_login.html", {"form": form, "erro": erro})

class ClienteCadastroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'rg', 'cpf', 'endereco', 'telefone', 'email_cliente']

def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_login')
    else:
        form = ClienteCadastroForm()
    return render(request, "todos/cadastrar_cliente.html", {"form": form})
