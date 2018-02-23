# Generated by Django 2.0.2 on 2018-02-23 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tema', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('title', models.CharField(max_length=80, verbose_name='TITLE')),
                ('url', models.URLField(verbose_name='url')),
                ('description', models.CharField(help_text='simple description text', max_length=200, verbose_name='DESCRIPTION')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateField(default=None, null=True)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tema.Tema')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modify_date'],
            },
        ),
    ]
