# Generated by Django 2.0.1 on 2018-01-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_code', models.CharField(blank=True, help_text='Location Code', max_length=200, null=True, unique=True)),
            ],
        ),
    ]
