# Generated by Django 3.0.3 on 2020-03-01 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='available_places',
        ),
        migrations.RemoveField(
            model_name='host',
            name='bedroom_name',
        ),
        migrations.RemoveField(
            model_name='host',
            name='busy_dates',
        ),
        migrations.RemoveField(
            model_name='host',
            name='purchased',
        ),
        migrations.AlterField(
            model_name='host',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='host',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('maximum_guests', models.IntegerField(verbose_name='Número de hóspedes')),
                ('busy_dates', models.TextField(verbose_name='Datas reservadas')),
                ('purchased', models.BooleanField(verbose_name='Vendido')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosts.Host')),
            ],
        ),
    ]
