# Generated by Django 3.2.4 on 2021-08-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
