# Generated by Django 4.2.1 on 2023-06-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_ratting_feedback_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.CharField(max_length=10)),
                ('C_name', models.CharField(max_length=50)),
                ('C_phone', models.CharField(max_length=15)),
                ('C_add', models.CharField(max_length=122)),
                ('C_email', models.CharField(max_length=50)),
                ('C_username', models.CharField(max_length=20)),
            ],
        ),
    ]