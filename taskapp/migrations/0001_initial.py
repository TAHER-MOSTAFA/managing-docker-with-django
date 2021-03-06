# Generated by Django 3.1.1 on 2020-09-22 12:01

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
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Docker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContainerName', models.CharField(max_length=30)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.image')),
                ('user', models.ManyToManyField(related_name='instaces', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
