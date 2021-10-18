from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    categoria = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("deposit:detail", kwargs={"slug":self.slug})