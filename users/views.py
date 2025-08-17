from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # El perfil ya existe gracias a la señal
            profile = user.profile
            profile.bio = form.cleaned_data.get('bio')
            profile.profile_picture = form.cleaned_data.get('profile_picture')
            profile.instruments.set(form.cleaned_data.get('instruments'))
            profile.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Verifica si el usuario existe y la contraseña es correcta
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Crea la sesión
            return redirect("rooms:create_room")  # Redirige a tu página principal
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")

    return render(request, "users/login.html")  # Renderiza tu template del login


def logout_view(request):
    logout(request)
    return redirect("users:login")