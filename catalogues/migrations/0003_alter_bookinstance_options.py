# Generated by Django 5.1.3 on 2024-11-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogues", "0002_bookinstance_borrower"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": (("can_mark_returned", "they can mark returened"),),
            },
        ),
    ]
