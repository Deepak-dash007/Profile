# Generated by Django 3.0.8 on 2020-09-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0016_message_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('likes', models.IntegerField(default=0, max_length=10)),
                ('repo_link', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('tech', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]