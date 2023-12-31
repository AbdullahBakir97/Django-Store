# Generated by Django 4.2.5 on 2023-12-27 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_code


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='accounts')),
                ('code', models.CharField(default=utils.generate_code.generate_code, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary')], max_length=12)),
                ('phone', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
