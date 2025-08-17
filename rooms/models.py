from django.db import models

from instruments.models import Instrument
from users import models as users

class Room(models.Model):
    PRIVACY_OPTIONS = [
        ('publica', 'Pública'),
        ('privada', 'Privada'),
    ]

    room_name = models.CharField(max_length=100)
    room_description = models.TextField(blank=True)
    creator = models.ForeignKey(users.Profile, on_delete=models.CASCADE, related_name='salas_creadas')
    required_instruments = models.ManyToManyField(Instrument, blank=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY_OPTIONS, default='publica')
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    url_jitsi = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.url_jitsi:
            clean_name = self.room_name.replace(" ", "_")
            self.url_jitsi = f"https://meet.jit.si/{clean_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.room_name