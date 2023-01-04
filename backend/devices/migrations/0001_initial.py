# Generated by Django 4.1.4 on 2023-01-01 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('ip_adress', models.GenericIPAddressField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=250)),
                ('unit', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='devices.device')),
            ],
        ),
    ]