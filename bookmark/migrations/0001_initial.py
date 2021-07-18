# Generated by Django 3.2.5 on 2021-07-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(verbose_name='Site URL')),
            ],
        ),
    ]