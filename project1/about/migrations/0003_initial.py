# Generated by Django 4.2.11 on 2024-05-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0002_delete_infos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=400)),
                ('birthday', models.DateField()),
                ('website', models.URLField()),
                ('phone', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('disponibility', models.CharField(choices=[('A', 'available'), ('U', 'unavailable')], max_length=1)),
                ('details', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
