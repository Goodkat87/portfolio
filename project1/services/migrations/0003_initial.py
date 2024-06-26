# Generated by Django 4.2.11 on 2024-05-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('icon', models.CharField(choices=[('briefcase', 'briefcase'), ('card-checklist', 'checklist'), ('bar-chart', 'bar-chart'), ('binoculars', 'binoculars'), ('brightness-high', 'brightness-high'), ('calendar4-week', 'calendar4-week')], max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
