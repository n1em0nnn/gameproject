# Generated by Django 4.2.19 on 2025-03-20 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('birth_year', models.PositiveIntegerField()),
                ('direction', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_teachild_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChildProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('training_group', models.CharField(max_length=100)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('parent_phone_number', models.CharField(max_length=15)),
                ('parent_name', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='profile_teachild.teacher')),
            ],
        ),
    ]
