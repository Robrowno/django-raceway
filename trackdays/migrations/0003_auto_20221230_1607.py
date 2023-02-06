# Generated by Django 3.2 on 2022-12-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackdays', '0002_auto_20221229_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackday',
            name='layout_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trackday',
            name='layout',
            field=models.IntegerField(choices=[(0, 'GP'), (2, 'Indy'), (1, 'National')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdaybooking',
            name='additional_drivers',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdaybooking',
            name='helmet_hire',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdaybooking',
            name='hospitality_packs',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdaybooking',
            name='paddock_hire',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdaybooking',
            name='tuition',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdayrequest',
            name='car_hire_required',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdayrequest',
            name='hospitality',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='trackdayrequest',
            name='pitlanes',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='level',
            field=models.IntegerField(choices=[(2, 'Gold'), (0, 'Bronze'), (1, 'Silver')], default=None),
        ),
    ]
