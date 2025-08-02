from django.db import models


class Instrument(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=10, blank=True) 

    def __str__(self):
        return f"{self.icon} {self.name}"
    



class User(models.Model):
    user_name= models.TextField(max_length= 30)
    name= models.TextField(max_length= 20)
    email = models.EmailField(max_length=100)
    birthdate = models.DateField()
    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return f"{self.user_name}"
    


class Room(models.Model):
    PRIVACY_OPTIONS = [
        ('publica', 'Pública'),
        ('privada', 'Privada'),
    ]

    room_name = models.CharField(max_length=100)
    room_description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salas_creadas')
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