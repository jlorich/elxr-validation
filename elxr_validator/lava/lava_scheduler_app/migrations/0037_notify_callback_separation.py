# Generated by Django 1.10.7 on 2018-04-27 09:20
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("lava_scheduler_app", "0036_remove_is_pipeline")]

    operations = [
        migrations.CreateModel(
            name="NotificationCallback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=200,
                        null=True,
                        verbose_name="Callback URL",
                    ),
                ),
                (
                    "method",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "GET"), (1, "POST")],
                        default=None,
                        null=True,
                        verbose_name="Callback method",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=200,
                        null=True,
                        verbose_name="Callback token",
                    ),
                ),
                (
                    "dataset",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "minimal"),
                            (1, "logs"),
                            (2, "results"),
                            (3, "all"),
                        ],
                        default=None,
                        null=True,
                        verbose_name="Callback dataset",
                    ),
                ),
                (
                    "content_type",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "urlencoded"), (1, "json")],
                        default=None,
                        null=True,
                        verbose_name="Callback content-type",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="notification", name="callback_content_type"),
        migrations.RemoveField(model_name="notification", name="callback_dataset"),
        migrations.RemoveField(model_name="notification", name="callback_method"),
        migrations.RemoveField(model_name="notification", name="callback_token"),
        migrations.RemoveField(model_name="notification", name="callback_url"),
        migrations.AddField(
            model_name="notificationcallback",
            name="notification",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="lava_scheduler_app.Notification",
                verbose_name="Notification",
            ),
        ),
    ]
