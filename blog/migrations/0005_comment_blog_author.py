# Generated by Django 4.2.5 on 2023-10-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]