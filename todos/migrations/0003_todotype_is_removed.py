# Generated by Django 4.0.3 on 2022-03-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_is_removed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotype',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]