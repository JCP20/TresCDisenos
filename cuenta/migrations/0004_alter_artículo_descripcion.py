# Generated by Django 4.1.3 on 2022-11-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_artículo_coleccion_delete_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artículo',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
