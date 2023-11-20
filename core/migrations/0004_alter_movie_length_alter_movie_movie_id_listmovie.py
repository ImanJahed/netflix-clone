# Generated by Django 4.2.7 on 2023-11-20 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_movie_length_alter_movie_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.UUIDField(default=uuid.UUID('a43c3706-6deb-4f9c-a46e-b1a74d303c96')),
        ),
        migrations.CreateModel(
            name='ListMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_list', to='core.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
