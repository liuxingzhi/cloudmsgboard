# Generated by Django 2.0.5 on 2018-07-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MsgBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=64)),
                ('receiver', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=1024)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
