# Generated by Django 5.0.6 on 2024-06-26 10:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='blogs/')),
                ('Description', models.TextField()),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
