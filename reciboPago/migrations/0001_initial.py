# Generated by Django 3.2.6 on 2024-09-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReciboPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEmision', models.DateTimeField(auto_now_add=True)),
                ('pagos', models.ManyToManyField(related_name='recibos', to='pagos.Pago')),
            ],
        ),
    ]
