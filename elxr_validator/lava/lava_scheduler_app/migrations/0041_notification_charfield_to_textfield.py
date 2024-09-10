# Generated by Django 1.11.20 on 2019-05-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("lava_scheduler_app", "0040_change_device_type_alias")]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="conditions",
            field=models.TextField(
                blank=True,
                default=None,
                max_length=400,
                null=True,
                verbose_name="Conditions",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="query_name",
            field=models.TextField(
                blank=True,
                default=None,
                max_length=1024,
                null=True,
                verbose_name="Query name",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="template",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Template name"
            ),
        ),
        migrations.AlterField(
            model_name="notificationcallback",
            name="token",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Callback token"
            ),
        ),
        migrations.AlterField(
            model_name="notificationcallback",
            name="url",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Callback URL"
            ),
        ),
        migrations.AlterField(
            model_name="notificationrecipient",
            name="email",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="recipient email"
            ),
        ),
        migrations.AlterField(
            model_name="notificationrecipient",
            name="irc_handle",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="IRC handle"
            ),
        ),
        migrations.AlterField(
            model_name="notificationrecipient",
            name="irc_server",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="IRC server"
            ),
        ),
    ]
