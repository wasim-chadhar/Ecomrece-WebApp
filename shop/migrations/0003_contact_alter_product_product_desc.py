# Generated by Django 4.1 on 2022-10-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image_product_product_catageory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('query_desc', models.CharField(max_length=700)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=700),
        ),
    ]