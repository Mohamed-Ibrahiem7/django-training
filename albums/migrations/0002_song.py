# Generated by Django 4.1.2 on 2022-11-08 12:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('audio', models.FileField(upload_to='audio/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
    ]