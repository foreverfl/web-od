# Generated by Django 5.0 on 2024-01-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_id", models.AutoField(primary_key=True, serialize=False)),
                ("book_title", models.CharField(max_length=255)),
                ("book_genre", models.CharField(default="Others", max_length=255)),
                (
                    "book_image_path",
                    models.ImageField(blank=True, upload_to="book_images/"),
                ),
                ("book_author", models.CharField(max_length=255)),
                ("book_publisher", models.CharField(max_length=255)),
                ("book_publication_date", models.DateField()),
                (
                    "book_content_path",
                    models.FileField(null=True, upload_to="book_contents/"),
                ),
                (
                    "book_voice_path",
                    models.FileField(null=True, upload_to="book_voices/"),
                ),
                ("book_description", models.TextField()),
                ("book_likes", models.IntegerField(default=0)),
                ("book_isbn", models.CharField(max_length=255)),
                ("book_view_count", models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TemporaryFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "temp_voice_image_path",
                    models.ImageField(null=True, upload_to="tmp/"),
                ),
                (
                    "temp_voice_sample_path",
                    models.FileField(null=True, upload_to="tmp/"),
                ),
                ("temp_voice_rvc_path", models.FileField(null=True, upload_to="tmp/")),
            ],
        ),
        migrations.CreateModel(
            name="Voice",
            fields=[
                ("voice_id", models.AutoField(primary_key=True, serialize=False)),
                ("voice_name", models.CharField(max_length=255)),
                ("voice_like", models.IntegerField(default=0)),
                ("voice_path", models.FileField(null=True, upload_to="voice_rvcs/")),
                (
                    "voice_image_path",
                    models.ImageField(blank=True, upload_to="voice_images/"),
                ),
                (
                    "voice_sample_path",
                    models.FileField(null=True, upload_to="voice_sample/"),
                ),
                ("voice_created_date", models.DateTimeField(auto_now_add=True)),
                ("voice_is_public", models.BooleanField(default=False)),
            ],
        ),
    ]
