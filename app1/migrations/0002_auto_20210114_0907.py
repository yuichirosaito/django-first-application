# Generated by Django 3.1.5 on 2021-01-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touroku',
            name='text',
            field=models.CharField(default='jhon', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='touroku',
            name='age',
            field=models.IntegerField(),
        ),
    ]
