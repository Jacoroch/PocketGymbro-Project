# Generated by Django 5.0.1 on 2024-02-20 03:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoMuscular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('N1', 'Principiante'), ('N2', 'Intermedio'), ('N3', 'Avanzado')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('VE', 'Velocidad'), ('FU', 'Fuerza'), ('HI', 'Hipertrofia'), ('SA', 'Salud')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='EjercicioRecuperacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('grupos_musculares', models.ManyToManyField(to='gymapp.grupomuscular')),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('grupos_musculares', models.ManyToManyField(to='gymapp.grupomuscular')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dias_entrenando', models.IntegerField()),
                ('experiencia_entrenamiento', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('objetivos', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_entrenamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.tipoentrenamiento')),
            ],
        ),
        migrations.CreateModel(
            name='PlanEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.IntegerField()),
                ('repeticiones', models.IntegerField()),
                ('orden', models.IntegerField()),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.ejercicio')),
            ],
        ),
        migrations.CreateModel(
            name='PlanEjercicioRecuperacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField()),
                ('ejercicio_recuperacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.ejerciciorecuperacion')),
            ],
        ),
        migrations.CreateModel(
            name='PlanEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_semana', models.IntegerField()),
                ('ejercicios', models.ManyToManyField(through='gymapp.PlanEjercicio', to='gymapp.ejercicio')),
                ('ejercicios_recuperacion', models.ManyToManyField(through='gymapp.PlanEjercicioRecuperacion', to='gymapp.ejerciciorecuperacion')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.nivel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.perfil')),
                ('tipo_entrenamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.tipoentrenamiento')),
            ],
        ),
        migrations.AddField(
            model_name='planejerciciorecuperacion',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.planentrenamiento'),
        ),
        migrations.AddField(
            model_name='planejercicio',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.planentrenamiento'),
        ),
        migrations.CreateModel(
            name='PlanNutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dieta', models.TextField()),
                ('plan_entrenamiento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gymapp.planentrenamiento')),
            ],
        ),
    ]
