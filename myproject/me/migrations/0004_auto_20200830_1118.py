# Generated by Django 3.0.8 on 2020-08-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_auto_20200830_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='till_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]