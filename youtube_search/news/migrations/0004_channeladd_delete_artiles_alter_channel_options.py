# Generated by Django 4.1.4 on 2023-01-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_delete_comchenn0_delete_comchenn1_delete_comchenn2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelAdd',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('channel_url', models.TextField(unique=True)),
                ('channel_name', models.TextField(unique=True)),
                ('channel_desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Предложенный канал',
                'verbose_name_plural': 'Предложенные каналы',
                'db_table': 'channel_add',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Artiles',
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'managed': False, 'verbose_name': 'Канал', 'verbose_name_plural': 'Каналы'},
        ),
    ]
