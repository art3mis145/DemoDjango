# Generated by Django 4.0.5 on 2022-06-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp1', '0005_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mssv', models.BigIntegerField(verbose_name=50)),
                ('bday', models.DateTimeField(verbose_name='birthday')),
            ],
        ),
    ]
