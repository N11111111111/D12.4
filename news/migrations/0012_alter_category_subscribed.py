# Generated by Django 4.2 on 2023-06-30 23:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0011_rename_categorythrough_postcategory_postcategory_and_more'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='category',
            name='subscribed',
        ),

        migrations.AddField(
            model_name='category',
            name='subscribed',
            field=models.ManyToManyField(through='news.SubscribedUsersCategory', to=settings.AUTH_USER_MODEL),
        ),
    ]


