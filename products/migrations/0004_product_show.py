# Generated by Django 4.0.3 on 2022-04-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_actived_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
