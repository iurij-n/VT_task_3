# Generated by Django 4.1.4 on 2023-01-02 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_alter_features_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='devices.device'),
        ),
    ]
