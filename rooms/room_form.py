from django import forms
from .models import Instrument
from .models import Room


class RoomForm(forms.ModelForm):

    room_name = forms.CharField(max_length=100, label="Nombre de la sala:")
    room_description = forms.CharField(widget=forms.Textarea, required=False, label="Descripción de la sala:")
    required_instruments = forms.ModelMultipleChoiceField(queryset=Instrument.objects.all(), required=False, label="Instrumentos requeridos:")
    privacy = forms.ChoiceField(choices=Room.PRIVACY_OPTIONS, initial='publica', label="Privacidad:")

    class Meta:
        model = Room 
        fields = ['room_name', 'room_description', 'required_instruments', 'privacy']

