from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ChannelAdd(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True, db_index=True, verbose_name='SLUG')
    channel_url = models.TextField(unique=True, verbose_name='Ссылка на канал')
    channel_name = models.TextField(unique=True, verbose_name='Название канала')
    channel_desc = models.TextField(blank=True, null=True, verbose_name='Описание канала')
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "ChannelAdd"
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def get_absolute_url(self):
        return '/news/create'

    def __str__(self):
        return self.channel_name


class Channel(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    channel_url = models.TextField(unique=True)
    channel_name = models.TextField(unique=True)
    channel_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channel'
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class Chen0(models.Model):
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    video_id = models.IntegerField(blank=True, null=True)
    com = models.TextField(blank=True, null=True)  # This field type is a guess.
    us = models.TextField(blank=True, null=True)  # This field type is a guess.
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chen0'


class Chen1(models.Model):
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    video_id = models.IntegerField(blank=True, null=True)
    com = models.TextField(blank=True, null=True)  # This field type is a guess.
    us = models.TextField(blank=True, null=True)  # This field type is a guess.
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chen1'


class Chen2(models.Model):
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    video_id = models.IntegerField(blank=True, null=True)
    com = models.TextField(blank=True, null=True)  # This field type is a guess.
    us = models.TextField(blank=True, null=True)  # This field type is a guess.
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chen2'


class VidDate0(models.Model):
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    video_id = models.IntegerField(blank=True, null=True)
    load_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_date0'


class VidDate1(models.Model):
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    video_id = models.IntegerField(blank=True, null=True)
    load_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_date1'


class VidDate2(models.Model):
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    video_id = models.IntegerField(blank=True, null=True)
    load_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_date2'
