# Generated by Django 2.2.2 on 2019-06-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente_id', models.IntegerField()),
                ('nom_ingrediente', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_id', models.IntegerField()),
                ('nom_pizza', models.CharField(max_length=30)),
            ],
        ),
    ]
