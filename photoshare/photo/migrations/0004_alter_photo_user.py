# Generated by Django 4.0.4 on 2022-06-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_alter_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
