# Generated by Django 5.0 on 2023-12-18 12:52

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('oauth_provider', models.CharField(max_length=255)),
                ('oauth_identifier', models.CharField(blank=True, max_length=255, null=True)),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.CharField(max_length=255)),
                ('user_phone_number', models.CharField(max_length=255)),
                ('user_created_date', models.DateTimeField(auto_now_add=True)),
                ('user_updated_date', models.DateTimeField(auto_now=True)),
                ('user_book_history', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('user_favorite_books', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
                ('user_favorite_voices', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_subscribed', models.BooleanField(default=False)),
                ('sub_start_date', models.DateTimeField(blank=True, null=True)),
                ('sub_end_date', models.DateTimeField(blank=True, null=True)),
                ('sub_payment_status', models.CharField(blank=True, default='pending', max_length=255, null=True)),
                ('sub_billing_key', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
