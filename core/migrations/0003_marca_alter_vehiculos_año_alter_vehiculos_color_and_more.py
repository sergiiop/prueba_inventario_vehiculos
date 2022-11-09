# Generated by Django 4.1.2 on 2022-11-09 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_propietarios_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='año',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=256)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca'),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelo'),
        ),
    ]
