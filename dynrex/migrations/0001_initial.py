# Generated by Django 2.2.5 on 2020-07-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content_name', models.CharField(max_length=150)),
                ('content_type', models.CharField(max_length=150)),
                ('status', models.SmallIntegerField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'content',
            },
        ),
    ]