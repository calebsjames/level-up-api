# Generated by Django 3.2 on 2021-05-05 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_rename_number_of_player_game_number_of_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_type',
            new_name='gametype',
        ),
    ]