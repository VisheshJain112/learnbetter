# Generated by Django 3.1.4 on 2021-01-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0047_auto_20210112_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blankpage',
            name='disc',
            field=models.BooleanField(blank=True, default=False, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='disc',
            field=models.BooleanField(blank=True, default=False, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='category',
            name='disc',
            field=models.BooleanField(blank=True, default=False, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='maincourse',
            name='disc',
            field=models.BooleanField(blank=True, default=False, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='post',
            name='disc',
            field=models.BooleanField(blank=True, default=False, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='subcat',
            name='disc',
            field=models.BooleanField(blank=True, default=False, verbose_name='Add In Disclaimer'),
        ),
    ]
