# Generated by Django 5.0.6 on 2024-06-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('nickName', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]