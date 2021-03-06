# Generated by Django 2.2.4 on 2020-04-10 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predmeti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img_url', models.FileField(upload_to='pred_img', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Filepdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Авторы')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('serius', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='publication.Predmeti', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['date'],
            },
        ),
    ]
