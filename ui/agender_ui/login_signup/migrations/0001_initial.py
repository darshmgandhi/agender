# Generated by Django 3.2.9 on 2021-11-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(db_column='Uid', max_length=30, primary_key=True, serialize=False)),
                ('email_id', models.TextField(db_column='Email_id', unique=True)),
                ('password', models.TextField(db_column='Password')),
                ('name', models.TextField(db_column='Name')),
                ('no_of_attempts', models.IntegerField(db_column='No_of_attempts')),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]