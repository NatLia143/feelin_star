from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import RoomForm

@login_required
def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            # el creador es el usuario logueado -> su profile
            room.creator = request.user.profile  
            room.save()
            form.save_m2m()  # guardar instrumentos seleccionados
            return redirect(room.url_jitsi)  # redirige a la página principal o donde quieras
    else:
        form = RoomForm()

    return render(request, "rooms/create_room.html", {"form": form})