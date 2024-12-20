from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
                     
class Page(models.Model):
 title = models.CharField(max_length=200,
    verbose_name="Título")
 content = RichTextUploadingField(verbose_name="Contenido")
 created = models.DateTimeField(auto_now_add=True,
    verbose_name="Fecha de creación")
 updated = models.DateTimeField(auto_now=True,
    verbose_name="Fecha de edición")
 class Meta:
    verbose_name = "página"
    verbose_name_plural = "páginas"
    ordering = ['title']
 def __str__(self):
    return self.title
 order = models.SmallIntegerField(verbose_name="Orden", default=0)
 ordering = ['order','title']
 


