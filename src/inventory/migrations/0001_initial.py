# Generated by Django 5.1.7 on 2025-04-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=125)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
