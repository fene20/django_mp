# Generated by Django 3.2.9 on 2021-11-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='graphic',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
