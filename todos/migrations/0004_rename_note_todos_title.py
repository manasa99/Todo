# Generated by Django 4.1.7 on 2023-04-03 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0003_rename_todo_todos"),
    ]

    operations = [
        migrations.RenameField(model_name="todos", old_name="note", new_name="title",),
    ]