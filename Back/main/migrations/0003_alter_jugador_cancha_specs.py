# Generated by Django 4.1.3 on 2022-11-28 19:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_jugador_domingo_alter_jugador_jueves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='cancha_specs',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Techada'), (2, 'Aire Libre'), (3, 'Superficie Cemento'), (4, 'Superficie Sintetico'), (5, 'Pared Cemento'), (6, 'Pared Blindex')], max_length=20, null=True),
        ),
    ]
