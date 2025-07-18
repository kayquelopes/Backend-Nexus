# Generated by Django 5.1.7 on 2025-06-14 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_hq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hq',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.autor'),
        ),
        migrations.AlterField(
            model_name='hq',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.editora'),
        ),
        migrations.AlterField(
            model_name='hq',
            name='frequencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.frequencia'),
        ),
        migrations.AlterField(
            model_name='hq',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.genero'),
        ),
        migrations.AlterField(
            model_name='hq',
            name='idioma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.idioma'),
        ),
        migrations.AlterField(
            model_name='hq',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.status'),
        ),
    ]
