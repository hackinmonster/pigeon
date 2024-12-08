# Generated by Django 5.1.3 on 2024-12-08 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employerprofile",
            old_name="company",
            new_name="company_name",
        ),
        migrations.RenameField(
            model_name="studentprofile",
            old_name="name",
            new_name="full_name",
        ),
        migrations.RemoveField(
            model_name="studentprofile",
            name="school",
        ),
        migrations.AddField(
            model_name="employerprofile",
            name="company_email",
            field=models.EmailField(default="default", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employerprofile",
            name="company_password",
            field=models.CharField(default="default", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studentprofile",
            name="email",
            field=models.EmailField(default="default", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studentprofile",
            name="password",
            field=models.CharField(default="default", max_length=255),
            preserve_default=False,
        ),
    ]
