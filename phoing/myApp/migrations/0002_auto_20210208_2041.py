# Generated by Django 3.1.6 on 2021-02-08 11:41

from django.db import migrations, models
import myApp.utils


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('photographer', 'photographer'), ('model', 'model'), ('HairMakeup', 'HairMakeup'), ('stylist', 'stylist'), ('other use', 'other use')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to=myApp.utils.uuid_name_upload_to),
        ),
    ]
