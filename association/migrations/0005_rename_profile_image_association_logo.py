# Generated by Django 5.1.1 on 2024-10-13 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0004_remove_user_slug_association_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='association',
            old_name='profile_image',
            new_name='logo',
        ),
    ]