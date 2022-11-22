# Generated by Django 4.1.3 on 2022-11-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0002_rename_productos_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artículo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('tipo_articulo', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('fotos', models.ImageField(upload_to='')),
                ('talla', models.CharField(max_length=20)),
                ('cant_disponible_por_talla', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('vigencia_coleccion', models.CharField(max_length=200)),
                ('tipos_prenda_col', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
    ]
