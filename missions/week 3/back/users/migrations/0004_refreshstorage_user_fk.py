# Generated by Django 4.0.1 on 2022-01-22 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_refreshstorage'),
    ]

    operations = [
        migrations.AddField(
            model_name='refreshstorage',
            name='user_fk',
            field=models.ForeignKey(db_column='user_fk', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]