from django.urls import reverse_lazy
from django.views import generic
from .room_form import RoomForm

class RoomFormView(generic.FormView):
    template_name = "rooms/create_room.html"
    form_class = RoomForm
    success_url = reverse_lazy('create_room')


    def form_valid(self, form):

        room = form.save(commit=False)
        room.save()  # primero guarda el objeto

        # luego guarda los instrumentos (ManyToMany)
        form.save_m2m()

        return super().form_valid(form)
    