# Generated by Django 5.1.2 on 2024-10-12 07:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentalHealthDiary", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mentalhealthdirary",
            name="id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=50,
                primary_key=True,
                serialize=False,
                verbose_name="id",
            ),
        ),
    ]