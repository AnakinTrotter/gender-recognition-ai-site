# Generated by Django 3.2.9 on 2021-11-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender_ai_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]