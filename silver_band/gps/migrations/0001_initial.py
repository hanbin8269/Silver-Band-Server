# Generated by Django 3.1.2 on 2020-10-27 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20201015_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_x', models.FloatField()),
                ('loc_y', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('wearer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.wearer')),
            ],
        ),
    ]
