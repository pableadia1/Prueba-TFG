# Generated by Django 3.1.4 on 2021-10-17 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0001_initial'),
        ('Jugador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='equipoActual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Equipo.equipo'),
        ),
    ]
