# Generated by Django 4.0.2 on 2022-03-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=200)),
                ('day', models.DateField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
