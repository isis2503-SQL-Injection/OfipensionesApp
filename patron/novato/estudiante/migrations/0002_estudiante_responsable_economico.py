# Generated by Django 4.2.15 on 2024-11-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("responsableEconomico", "0001_initial"),
        ("estudiante", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="estudiante",
            name="responsable_economico",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="estudiantes",
                to="responsableEconomico.responsableeconomico",
            ),
        ),
    ]
