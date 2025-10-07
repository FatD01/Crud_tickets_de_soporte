from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoria")
    propiedad= models.CharField(max_length=100, default= 'General', verbose_name="Propiedad o Tipo")
    icono = models.ImageField(upload_to='categorias/', null=True, blank=True, verbose_name="Ícono de la Categoría") # Imagen
    activa = models.BooleanField(default=True, verbose_name="¿Está Activa?")
    # Campos: nombre, propiedad, icono, activa (4 campos)

    def __str__(self):
        return self.nombre
    
class Ticket(models.Model):
    ESTADO_CHOICES = [
        ('ABIERTO', 'Abierto'),
        ('PROCESO', 'En Proceso'),
        ('CERRADO', 'Cerrado'),
    ]
        
    titulo = models.CharField(max_length=200, verbose_name="Título del Ticket")
    descripcion = models.TextField(verbose_name="Descripción del Problema")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ABIERTO', verbose_name="Estado Actual")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    
    # CLAVE FORÁNEA (Relación)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Categoría Asignada"
    )
    
    adjunto = models.ImageField(upload_to='tickets/', null=True, blank=True, verbose_name="Adjuntar Evidencia") # Imagen
    # Campos: titulo, descripcion, estado, fecha_creacion, categoria (FK), adjunto (6 campos)

    def __str__(self):
        return f"Ticket #{self.id}: {self.titulo}"