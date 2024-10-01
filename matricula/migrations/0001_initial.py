# Generated by Django 3.2.6 on 2024-09-30 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('fechaPrematricula', models.DateTimeField()),
                ('fechaLimite', models.DateTimeField()),
                ('periodoAcademico', models.CharField(max_length=50)),
                ('pago', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pagos.pago')),
            ],
        ),
    ]
