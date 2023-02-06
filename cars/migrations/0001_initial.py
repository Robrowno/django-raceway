# Generated by Django 3.2 on 2022-12-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(blank=True, max_length=40, null=True)),
                ('model', models.CharField(blank=True, max_length=40, null=True)),
                ('variant', models.CharField(blank=True, max_length=40)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('power', models.PositiveIntegerField()),
                ('torque', models.PositiveIntegerField()),
                ('transmission', models.CharField(max_length=80)),
                ('drivetrain', models.IntegerField(choices=[(0, 'FrontEngine-FrontWheelDrive'), (1, 'FrontEngine-RearWheelDrive'), (2, 'MidEngine-RearWheelDrive'), (3, 'AllWheelDrive'), (4, 'RearEngine-RearWheelDrive')], default=None)),
                ('cost_to_hire', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
