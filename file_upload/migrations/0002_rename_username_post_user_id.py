# Generated by Django 4.1 on 2022-08-22 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("file_upload", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="username",
            new_name="user_id",
        ),
    ]