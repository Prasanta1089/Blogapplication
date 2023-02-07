# Generated by Django 4.1.4 on 2023-01-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=15)),
                ('timeStamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]