# Generated by Django 4.1.2 on 2022-11-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_ticket_hora_entrada_alter_ticket_hora_salida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='valor',
            field=models.FloatField(default=0, null=True),
        ),
    ]
