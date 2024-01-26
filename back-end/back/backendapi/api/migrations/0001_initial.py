# Generated by Django 5.0 on 2023-12-29 18:00

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
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rue', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=255)),
                ('pays', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Avocat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('specialite', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pays', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=255)),
                ('code_postal', models.CharField(max_length=20)),
                ('rue', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.PositiveIntegerField()),
                ('commentaire', models.TextField()),
                ('avocat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.avocat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('creneau_horaire', models.CharField(max_length=255)),
                ('avocat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.avocat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
