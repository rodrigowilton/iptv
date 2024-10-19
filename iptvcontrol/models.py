from django.db import models

class Cliente(models.Model):
    cliente = models.CharField(max_length=255)
    mac = models.CharField(max_length=17)  # Formato comum para MAC
    key = models.CharField(max_length=255)
    m3u = models.URLField()  # Pode ser um URL ou um texto dependendo da sua necessidade

    def __str__(self):
        return self.cliente
