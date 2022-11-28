# Generated by Django 4.1.3 on 2022-11-28 22:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_jugador_cancha_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complejo',
            name='cancha_specs',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('T', 'Techada'), ('AL', 'Aire Libre'), ('SC', 'Superficie Cemento'), ('SS', 'Superficie Sintetico'), ('PC', 'Pared Cemento'), ('PB', 'Pared Blindex')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='cancha_specs',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('T', 'Techada'), ('AL', 'Aire Libre'), ('SC', 'Superficie Cemento'), ('SS', 'Superficie Sintetico'), ('PC', 'Pared Cemento'), ('PB', 'Pared Blindex')], max_length=30, null=True),
        ),
    ]
