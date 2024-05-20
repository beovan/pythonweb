# Generated by Django 5.0.4 on 2024-05-20 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='app.category'),
        ),
    ]
