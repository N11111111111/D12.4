# Generated by Django 4.2 on 2023-07-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_category_subscribed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postCategory',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='postCategory',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subscribeduserscategory',
            old_name='postCategory',
            new_name='category',
        ),
    ]
