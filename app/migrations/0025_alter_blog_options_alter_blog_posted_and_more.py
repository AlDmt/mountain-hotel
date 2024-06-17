# Generated by Django 5.0.6 on 2024-06-17 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['posted'], 'verbose_name': 'статья блога', 'verbose_name_plural': 'статьи блога'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 6, 17, 20, 40, 43, 921913), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 6, 17, 20, 40, 43, 922417), verbose_name='Дата комментария'),
        ),
    ]
