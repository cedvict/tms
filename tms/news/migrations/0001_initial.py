# Generated by Django 2.1 on 2018-09-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('upd_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
            options={
                'db_table': 'news_tab',
            },
        ),
    ]
