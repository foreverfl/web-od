# Generated by Django 5.0 on 2023-12-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_isbn', models.CharField(max_length=255)),
                ('request_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('comment_created_date', models.DateTimeField(auto_now_add=True)),
                ('comment_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('inquiry_id', models.AutoField(primary_key=True, serialize=False)),
                ('inquiry_category', models.CharField(default='Others', max_length=255)),
                ('inquiry_title', models.CharField(max_length=255)),
                ('inquiry_content', models.TextField(blank=True, null=True)),
                ('inquiry_response', models.TextField(blank=True, null=True)),
                ('inquiry_created_date', models.DateTimeField(auto_now_add=True)),
                ('inquiry_answered_date', models.DateTimeField(blank=True, null=True)),
                ('inquiry_is_answered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=255)),
                ('post_content', models.TextField()),
                ('post_created_date', models.DateTimeField(auto_now_add=True)),
                ('post_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRequestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
