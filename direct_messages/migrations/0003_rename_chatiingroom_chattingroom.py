# Generated by Django 4.1.2 on 2022-11-21 14:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("direct_messages", "0002_alter_message_room_alter_message_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ChatiingRoom",
            new_name="ChattingRoom",
        ),
    ]
