# Generated by Django 5.0.3 on 2024-05-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_alter_task_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
    ]
