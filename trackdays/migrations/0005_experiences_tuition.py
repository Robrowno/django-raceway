# Generated by Django 3.2 on 2022-12-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackdays', '0004_auto_20221222_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('itinerary', models.CharField(max_length=500)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('level', models.IntegerField(choices=[(0, 'Bronze'), (1, 'Silver'), (2, 'Gold')], default=None)),
                ('description', models.CharField(max_length=300)),
                ('itinerary', models.CharField(max_length=500)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Tuition',
            },
        ),
    ]
