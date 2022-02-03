# Generated by Django 4.0.1 on 2022-01-15 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category_fk',
            field=models.ForeignKey(db_column='category_fk', default=1, on_delete=django.db.models.deletion.CASCADE, to='product_category.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='descriptions',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sold_out_yn',
            field=models.BooleanField(default=False),
        ),
    ]
