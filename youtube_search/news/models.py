from django.db import models


# Create your models here.


class ChannelAdd(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    channel_url = models.TextField(unique=True)
    channel_name = models.TextField(unique=True)
    channel_desc = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return '/news/create'

    class Meta:
        managed = False
        db_table = 'channel_add'
        verbose_name = 'Предложенный канал'
        verbose_name_plural = 'Предложенные каналы'


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
    channel_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    com = models.TextField(blank=True, null=True)  # This field type is a guess.
    us = models.TextField(blank=True, null=True)  # This field type is a guess.
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chen0'


class Chen1(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    com = models.TextField(blank=True, null=True)  # This field type is a guess.
    us = models.TextField(blank=True, null=True)  # This field type is a guess.
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chen1'


class Chen2(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    com = models.TextField(blank=True, null=True)  # This field type is a guess.
    us = models.TextField(blank=True, null=True)  # This field type is a guess.
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chen2'


class VidDate0(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    load_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_date0'


class VidDate1(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    load_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_date1'


class VidDate2(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    load_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vid_date2'
