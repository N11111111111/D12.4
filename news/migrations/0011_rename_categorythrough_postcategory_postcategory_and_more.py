# Generated by Django 4.2 on 2023-06-30 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_rename_postcategory_subscribeduserscategory_categorythrough_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='categoryThrough',
            new_name='postCategory',
        ),
        migrations.RenameField(
            model_name='subscribeduserscategory',
            old_name='categoryThrough',
            new_name='postCategory',
        ),
    ]
