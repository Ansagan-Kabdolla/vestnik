from django.db import models

from django.db import models
from vestnik.settings import MEDIA_URL


class Filepdf(models.Model):
    author = models.CharField(max_length=200, verbose_name="Авторы")
    file = models.FileField(upload_to='', verbose_name="Файл")
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    serius = models.ForeignKey('Predmeti', null=True, on_delete=models.PROTECT, verbose_name='Серия')
    def get_absolute_file_upload_url(self):
        return self.file.url
    def __str__(self):
        return self.author


    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name = "Публикация"
        ordering = ['date']


class Predmeti(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название")
    img_url = models.FileField(upload_to='pred_img', verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Предметы"
        verbose_name = "Предмет"
        ordering = ['date']
