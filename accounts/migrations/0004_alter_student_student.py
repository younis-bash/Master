# Generated by Django 3.2.13 on 2022-06-09 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220609_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]
