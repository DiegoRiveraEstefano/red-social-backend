# Generated by Django 4.2.2 on 2023-07-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.CharField(default=0, max_length=128, primary_key=True, serialize=False),
        ),
    ]