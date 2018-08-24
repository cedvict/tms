# Generated by Django 2.1 on 2018-08-22 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'component_tab',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('upd_date', models.DateTimeField(verbose_name='date updated')),
            ],
            options={
                'db_table': 'project_tab',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'role_tab',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('estimate_in_minute', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
                ('test_case_type', models.IntegerField(choices=[(1, 'tier 1'), (2, 'tier 2'), (3, 'tier 3'), (2, 'tier 4'), (3, 'tier 5')])),
                ('test_case_platform', models.IntegerField(choices=[(1, 'Generic'), (2, 'Android'), (3, 'iOS'), (4, 'Web'), (5, 'Others')])),
                ('preconditions', models.CharField(max_length=200)),
                ('test_steps', models.CharField(max_length=2000)),
                ('expected_result', models.CharField(max_length=500)),
                ('actual_result', models.CharField(max_length=500)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='console.Component')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='console.Project')),
            ],
            options={
                'db_table': 'test_case_tab',
            },
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tester_tab',
            },
        ),
        migrations.CreateModel(
            name='TestPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('upd_date', models.DateTimeField(verbose_name='date updated')),
            ],
            options={
                'db_table': 'test_plan_tab',
            },
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('upd_date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='console.Project')),
                ('test_plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='console.TestPlan')),
            ],
            options={
                'db_table': 'test_run_tab',
            },
        ),
        migrations.AddField(
            model_name='component',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.Project'),
        ),
    ]