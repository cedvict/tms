# Generated by Django 2.1 on 2018-08-28 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0017_auto_20180828_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaltestplan',
            old_name='test_run_status',
            new_name='test_plan_status',
        ),
        migrations.RenameField(
            model_name='testplan',
            old_name='test_run_status',
            new_name='test_plan_status',
        ),
    ]