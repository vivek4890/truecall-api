# Generated by Django 3.1.2 on 2020-10-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecaller_api', '0002_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
