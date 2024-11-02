# Generated by Django 5.1.2 on 2024-11-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentprofile",
            name="name",
            field=models.CharField(default="Unknown", max_length=60),
        ),
        migrations.AlterField(
            model_name="employerprofile",
            name="company",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="school",
            field=models.CharField(max_length=100),
        ),
    ]
