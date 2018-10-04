from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from django.db import models


class News(models.Model):

	types = (
    (1, 'Regional'),
    (2, 'Internacional')
  )

	titulo = models.CharField(max_length=255, blank=False, verbose_name='título')
	descricao = models.TextField(verbose_name='descrição', blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tipo = models.IntegerField(choices=types, verbose_name='É uma notícia')
	image = models.ImageField(blank=False, verbose_name='Adicionar imagem')

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'notícia'
		verbose_name_plural = 'notícias'
