# Generated by Django 3.0 on 2020-01-31 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
