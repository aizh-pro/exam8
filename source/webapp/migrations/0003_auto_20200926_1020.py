# Generated by Django 2.2 on 2020-09-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pics', verbose_name='Картинка'),
        ),
    ]
