# Generated by Django 3.2.13 on 2022-05-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_status',
            field=models.CharField(choices=[('Open', 'Open'), ('Responded', 'Responded'), ('Complete', 'Complete')], default=1, max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=2000),
        ),
    ]