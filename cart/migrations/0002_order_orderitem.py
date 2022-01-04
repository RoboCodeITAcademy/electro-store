# Generated by Django 3.2.6 on 2022-01-04 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familya')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon')),
                ('telegram_id', models.CharField(blank=True, max_length=50, verbose_name='Telegram ID')),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(choices=[('andijon', 'ANDIJON'), ('buxoro', 'BUXORO'), ('fargona', "FARG'ONA"), ('jizzax', 'JIZZAX'), ('xorazm', 'XORAZM'), ('namangan', 'NAMANGAN'), ('navoiy', 'NAVOIY'), ('samarqand', 'SAMARQAND'), ('surxandaryo', 'SURXANDARYO'), ('sirdaryo', 'SIRDARYO'), ('toshkent', 'TOSHKENT'), ('qashqadaryo', 'QASHQADARYO'), ('nukus', 'NUKUS')], max_length=80, verbose_name='Viloyat')),
                ('address', models.CharField(max_length=80, verbose_name='Tuman')),
                ('street', models.CharField(max_length=150, verbose_name="Ko'cha va uy manzili")),
                ('postal_code', models.CharField(max_length=50, verbose_name='Pochta indeksi')),
                ('payment_method', models.CharField(choices=[('cash', 'NAQD'), ('click', 'CLICK'), ('payme', 'PAYME'), ('oson', 'OSON')], max_length=50, verbose_name="To'lov turi")),
                ('message', models.TextField(blank=True, verbose_name="Qo'shimcha xabar")),
                ('payed', models.BooleanField(default=False, verbose_name="To'lov xolati")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Xaridor')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familya')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon')),
                ('telegram_id', models.CharField(blank=True, max_length=50, verbose_name='Telegram ID')),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=80, verbose_name='Viloyat')),
                ('address', models.CharField(max_length=80, verbose_name='Tuman')),
                ('street', models.CharField(max_length=150, verbose_name="Ko'cha va uy manzili")),
                ('postal_code', models.CharField(max_length=50, verbose_name='Pochta indeksi')),
                ('payment_method', models.CharField(max_length=50, verbose_name="To'lov turi")),
                ('message', models.TextField(blank=True, verbose_name="Qo'shimcha xabar")),
                ('payed', models.BooleanField(default=False, verbose_name="To'lov xolati")),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Xaridor')),
            ],
            options={
                'verbose_name': 'Buyurtma Tovar',
                'verbose_name_plural': 'Buyurtma Tovarlar',
                'ordering': ['-id'],
            },
        ),
    ]