# Generated by Django 1.9.4 on 2016-06-15 13:26
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lava_scheduler_app", "0017_custompermissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                    "type",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "regression"), (1, "progression")],
                        default=None,
                        null=True,
                        verbose_name="Type",
                    ),
                ),
                (
                    "job_status_trigger",
                    models.CommaSeparatedIntegerField(
                        choices=[
                            (0, "Submitted"),
                            (1, "Running"),
                            (2, "Complete"),
                            (3, "Incomplete"),
                            (4, "Canceled"),
                            (5, "Canceling"),
                        ],
                        default=2,
                        max_length=30,
                        verbose_name="Job status trigger",
                    ),
                ),
                (
                    "verbosity",
                    models.IntegerField(
                        choices=[(0, "verbose"), (1, "quiet"), (2, "status-only")],
                        default=1,
                    ),
                ),
                (
                    "template",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=50,
                        null=True,
                        verbose_name="Template name",
                    ),
                ),
                (
                    "blacklist",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=400,
                        null=True,
                        verbose_name="Test Case blacklist",
                    ),
                ),
                (
                    "time_sent",
                    models.DateTimeField(auto_now_add=True, verbose_name="Time sent"),
                ),
                (
                    "query_name",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=1024,
                        null=True,
                        verbose_name="Query name",
                    ),
                ),
                (
                    "conditions",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=400,
                        null=True,
                        verbose_name="Conditions",
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "query_owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Query owner",
                    ),
                ),
                (
                    "test_job",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lava_scheduler_app.TestJob",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NotificationRecipient",
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
                    "email",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=100,
                        null=True,
                        verbose_name="recipient email",
                    ),
                ),
                (
                    "irc_handle",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=40,
                        null=True,
                        verbose_name="IRC handle",
                    ),
                ),
                (
                    "irc_server",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=40,
                        null=True,
                        verbose_name="IRC server",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "sent"), (1, "not sent")],
                        default=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "method",
                    models.IntegerField(
                        choices=[(0, "email"), (1, "irc")],
                        default=0,
                        verbose_name="Method",
                    ),
                ),
                (
                    "notification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lava_scheduler_app.Notification",
                        verbose_name="Notification",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Notification user recipient",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="notificationrecipient",
            unique_together={("user", "notification")},
        ),
    ]
