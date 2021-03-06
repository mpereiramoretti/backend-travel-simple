# Generated by Django 3.0.3 on 2020-03-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Feminino', 'F'), ('Masculino', 'M'), ('Outro', 'O')], max_length=10, verbose_name='Gênero'),
        ),
    ]
