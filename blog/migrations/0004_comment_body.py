# Generated by Django 4.2.3 on 2023-10-12 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
