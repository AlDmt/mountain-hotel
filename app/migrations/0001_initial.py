# Generated by Django 5.0.1 on 2024-04-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=10)),
                ('internet_usage', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('agree_to_news', models.BooleanField(default=False)),
                ('summary', models.TextField()),
            ],
        ),
    ]
