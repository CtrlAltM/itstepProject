# Generated by Django 5.0.3 on 2024-05-27 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('due', models.DateField(auto_now_add=True)),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.member')),
            ],
        ),
    ]
