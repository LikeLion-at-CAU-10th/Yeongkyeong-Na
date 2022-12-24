# Generated by Django 4.0.6 on 2022-08-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Likelion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=31, unique=True)),
                ('part', models.CharField(choices=[('기획', '기획'), ('백엔드', '백엔드'), ('프론트엔드', '프론트엔드')], default='백엔드', max_length=31)),
                ('role', models.CharField(choices=[('운영진', '운영진'), ('멤버', '멤버')], default='멤버', max_length=31)),
                ('major', models.CharField(default='', max_length=31)),
            ],
        ),
    ]