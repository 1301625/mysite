# Generated by Django 2.0.3 on 2019-08-20 09:03

import django.core.validators
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/profile'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(help_text='Requierd. 30 characters or fewer. Letters, digits and ./+/-/_ only', max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.+-]+$', 'Enter a valid username.', 'invalid')], verbose_name='username'),
        ),
    ]