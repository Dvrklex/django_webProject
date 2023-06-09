# Generated by Django 4.2 on 2023-05-08 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Categoria')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('udpated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria Producto',
                'verbose_name_plural': 'Categorias Productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Producto')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda', verbose_name='Imagen')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('disponibilidad', models.BooleanField(default=True, verbose_name='Disponibilidad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoriaproducto', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
