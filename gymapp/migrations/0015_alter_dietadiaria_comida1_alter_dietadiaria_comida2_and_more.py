# Generated by Django 5.0.1 on 2024-05-19 17:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0014_alter_macros_calorias_alter_macros_carbohidratos_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietadiaria',
            name='comida1',
            field=models.CharField(default=None, max_length=21),
        ),
        migrations.AlterField(
            model_name='dietadiaria',
            name='comida2',
            field=models.CharField(default=None, max_length=21),
        ),
        migrations.AlterField(
            model_name='dietadiaria',
            name='comida3',
            field=models.CharField(default=None, max_length=21),
        ),
        migrations.AlterField(
            model_name='dietadiaria',
            name='comida4',
            field=models.CharField(default=None, max_length=21),
        ),
        migrations.AlterField(
            model_name='dietadiaria',
            name='comida5',
            field=models.CharField(default=None, max_length=21),
        ),
        migrations.AlterField(
            model_name='dietadiaria',
            name='comida6',
            field=models.CharField(default=None, max_length=21),
        ),
        migrations.CreateModel(
            name='Dieta_Semanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunes', models.JSONField()),
                ('martes', models.JSONField()),
                ('miercoles', models.JSONField()),
                ('jueves', models.JSONField()),
                ('viernes', models.JSONField()),
                ('sabado', models.JSONField()),
                ('domingo', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rutina_Semanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunes', models.JSONField()),
                ('martes', models.JSONField()),
                ('miercoles', models.JSONField()),
                ('jueves', models.JSONField()),
                ('viernes', models.JSONField()),
                ('sabado', models.JSONField()),
                ('domingo', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
