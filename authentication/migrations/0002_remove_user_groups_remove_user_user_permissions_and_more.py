# Generated by Django 4.2.2 on 2023-07-21 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
