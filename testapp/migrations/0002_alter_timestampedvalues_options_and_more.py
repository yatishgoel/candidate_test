# Generated by Django 5.1.2 on 2024-10-13 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timestampedvalues',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='timestampedvalues',
            name='timestamp',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='timestampedvalues',
            name='value',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-1000000), django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AddIndex(
            model_name='timestampedvalues',
            index=models.Index(fields=['timestamp', 'value'], name='testapp_tim_timesta_c773d7_idx'),
        ),
    ]
