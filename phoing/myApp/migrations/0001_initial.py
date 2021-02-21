# Generated by Django 3.1.6 on 2021-02-21 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import myApp.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollaborationWithBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=myApp.utils.uuid_name_upload_to)),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField()),
                ('tag_str', models.CharField(blank=True, max_length=50)),
                ('file_attach', models.FileField(upload_to='')),
                ('pay', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('location', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='place.location')),
                ('save_users', models.ManyToManyField(blank=True, related_name='with_brand_save_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=myApp.utils.uuid_name_upload_to)),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField()),
                ('file_attach', models.FileField(upload_to='')),
                ('pay', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('tag_str', models.CharField(blank=True, max_length=50)),
                ('location', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='place.location')),
                ('save_users', models.ManyToManyField(blank=True, related_name='contact_save_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('like_users', models.ManyToManyField(blank=True, related_name='tag_like_users', to=settings.AUTH_USER_MODEL)),
                ('save_users', models.ManyToManyField(blank=True, related_name='tag_save_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=myApp.utils.uuid_name_upload_to)),
                ('desc', models.TextField()),
                ('image_url', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=60000, size=None)),
                ('tag_str', models.CharField(blank=True, max_length=50)),
                ('like_users', models.ManyToManyField(blank=True, related_name='reference_like_users', to=settings.AUTH_USER_MODEL)),
                ('save_users', models.ManyToManyField(blank=True, related_name='reference_save_users', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='references', to='myApp.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=myApp.utils.uuid_name_upload_to)),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField()),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('tag_str', models.CharField(blank=True, max_length=50)),
                ('like_users', models.ManyToManyField(blank=True, related_name='portfolio_like_users', to=settings.AUTH_USER_MODEL)),
                ('save_users', models.ManyToManyField(blank=True, related_name='portfolio_save_users', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='portfolios', to='myApp.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=myApp.utils.uuid_name_upload_to)),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField()),
                ('pay', models.PositiveIntegerField()),
                ('tag_str', models.CharField(blank=True, max_length=50)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_users', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='place.location')),
                ('save_users', models.ManyToManyField(blank=True, related_name='save_users', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='places', to='myApp.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=myApp.utils.uuid_name_upload_to, verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_images', to='myApp.contact')),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_images', to='myApp.portfolio')),
                ('reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reference_images', to='myApp.reference')),
                ('with_artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='with_artist_images', to='myApp.collaborationwithbrand')),
                ('with_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='with_brand_images', to='myApp.collaborationwithbrand')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='contacts', to='myApp.Tag'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_comments', to='myApp.contact')),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_comments', to='myApp.portfolio')),
                ('with_artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='with_artist_comments', to='myApp.collaborationwithbrand')),
                ('with_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='with_brand_comments', to='myApp.collaborationwithbrand')),
            ],
        ),
        migrations.AddField(
            model_name='collaborationwithbrand',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='with_brand', to='myApp.Tag'),
        ),
        migrations.AddField(
            model_name='collaborationwithbrand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='with_brands', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CollaborationWithArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=myApp.utils.uuid_name_upload_to)),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField()),
                ('tag_str', models.CharField(blank=True, max_length=50)),
                ('file_attach', models.FileField(upload_to='')),
                ('pay', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('location', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='place.location')),
                ('save_users', models.ManyToManyField(blank=True, related_name='with_artist_save_users', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='with_artists', to='myApp.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='with_artists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
