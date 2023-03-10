# Generated by Django 4.1.7 on 2023-02-27 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'BlogsList',
                'verbose_name_plural': 'BlogsLists',
            },
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=255)),
                ('Owner', models.CharField(max_length=255, null=True)),
                ('blog_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.blogs')),
            ],
            options={
                'verbose_name': 'Blogs',
                'verbose_name_plural': 'Blogers',
            },
        ),
    ]
