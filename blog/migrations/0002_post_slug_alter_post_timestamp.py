# Generated by Django 4.1.4 on 2023-01-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateField(blank=True),
        ),
    ]