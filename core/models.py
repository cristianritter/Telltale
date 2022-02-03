from ast import Eq
from django.db import models
from django.forms import CharField

# Create your models here.

class Armario(models.Model):
    pass

class Equipamento(models.Model):
    descricao = models.CharField('descrição', max_length=200)
    serial_number = models.CharField('serialnumber', max_length=50)
    RFID_tag_id = models.CharField('RFID_tag_id', max_length=50)
    default_locale = models.CharField('default_locale', max_length=50)
    current_locale = models.CharField('current_locale', max_length=50)
    status = models.BooleanField('status')
    
    # O que tem dentro de um armário ?
    # camera microfone sangan extensao cabos baterias pilhas drone celular live u 
    # como sao carregadas as baterias
    # como sao carregadas as pilhas
    # os equipamentos ficam fixos em cada armario ou podem ser trocados de lugar, exceções?


class Camera(Equipamento):
    pass

class Microfone(Equipamento):
    pass

class SunGun(Equipamento):
    pass

class Extensao(Equipamento):
    pass

class Cabo(Equipamento):
    pass

class Bateria(Equipamento):
    pass

class Pilha(Equipamento):
    pass

class Drone(Equipamento):
    pass

class Celular(Equipamento):
    pass

class LiveU(Equipamento):
    pass

