# Generated by Django 4.0 on 2022-01-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CircuitData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GSP', models.CharField(max_length=100)),
                ('Node', models.CharField(max_length=100)),
                ('Substation', models.CharField(max_length=100)),
            ],
        ),
    ]
