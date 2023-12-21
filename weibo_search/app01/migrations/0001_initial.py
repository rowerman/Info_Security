# Generated by Django 4.2.5 on 2023-12-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="YourModel",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("bid", models.CharField(max_length=12)),
                ("user_id", models.CharField(max_length=20)),
                ("screen_name", models.CharField(max_length=30)),
                ("text", models.CharField(max_length=2000)),
                ("article_url", models.CharField(max_length=100)),
                ("topics", models.CharField(max_length=200)),
                ("at_users", models.CharField(max_length=1000)),
                ("pics", models.CharField(max_length=3000)),
                ("video_url", models.CharField(max_length=1000)),
                ("location", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField()),
                ("source", models.CharField(max_length=30)),
                ("attitudes_count", models.IntegerField()),
                ("comments_count", models.IntegerField()),
                ("reposts_count", models.IntegerField()),
                ("retweet_id", models.CharField(max_length=20)),
                ("ip", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "原神雷电将军",
            },
        ),
    ]