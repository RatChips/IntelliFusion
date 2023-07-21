# Generated by Django 4.2.3 on 2023-07-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ModelList",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("order", models.IntegerField()),
                ("type", models.TextField()),
                ("name", models.TextField()),
                ("url", models.URLField()),
                ("APIKey", models.TextField(default="\\")),
                ("LaunchCompiler", models.FileField(default="\\", upload_to="")),
                ("LaunchPath", models.FileField(default="\\", upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Account", models.CharField(max_length=15)),
                ("Email", models.EmailField(max_length=254)),
                ("Password", models.TextField()),
            ],
        ),
    ]
