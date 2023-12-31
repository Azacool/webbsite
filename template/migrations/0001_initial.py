# Generated by Django 4.2.7 on 2023-11-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=False, max_length=30)),
                ('last_name', models.CharField(blank=True, default=False, max_length=30)),
                ('image', models.ImageField(upload_to='template/static/images/')),
            ],
        ),
    ]
