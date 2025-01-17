# Generated by Django 4.0.1 on 2022-01-06 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('product_pk', models.ForeignKey(db_column='product_fk', on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
