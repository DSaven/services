# Generated by Django 2.2.7 on 2019-11-08 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('district', models.CharField(max_length=20)),
                ('population', models.IntegerField(default=0)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.Country')),
            ],
        ),
    ]
