# Generated by Django 3.2.6 on 2021-08-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('chuy', 'Chuy'), ('osh', 'Osh'), ('yssyk kul', 'Yssyk-Kul'), ('naryn', 'Naryn'), ('batken', 'Batken'), ('jalal abad', 'Jalal-Abad'), ('talas', 'Talas')], max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('type_order', models.CharField(choices=[('self pickup', 'Self-pickup'), ('delivery', 'Delivery')], max_length=50)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
