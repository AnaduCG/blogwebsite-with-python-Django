# Generated by Django 4.1.5 on 2023-01-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(),
        ),
    ]
