# Generated by Django 3.2 on 2023-01-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackdays', '0004_auto_20221230_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackday',
            name='layout',
            field=models.IntegerField(choices=[(0, 'GP'), (2, 'Indy'), (1, 'National')], default=0),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='itinerary',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='level',
            field=models.IntegerField(choices=[(1, 'Silver'), (0, 'Bronze'), (2, 'Gold')], default=None),
        ),
    ]