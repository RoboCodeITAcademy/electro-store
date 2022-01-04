from django.db import models
from store.models import Product
from django.contrib.auth.models import User
# Create your models here.
class CardProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_products'
    )
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name)


class Cart(models.Model):
    products = models.ManyToManyField(CardProduct, related_name='products')
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def add(self,product_id,qty):
        product = Product.objects.get(id=product_id)
        price = product.price * qty
        self.products.create(
            product=product,
            quantity=qty,
            price=price
        )
        self.total_quantity += qty
        self.total_price += price
        self.save()
        return True
    #
    def deleteItem(self, product_id,qty):
        product = Product.objects.get(id=product_id)
        p_id = product.id
        for item in self.products.all():
            if item.product.id == p_id:
                item.delete()
        price = product.price * qty
        # self.products.remove(product)
        self.total_quantity -= qty
        self.total_price -= price
        self.save()
        return True

    def removeAllItems(self):
        self.delete()


    def __str__(self):
        return f"Cart = {self.id}"
    
class Order(models.Model):
    PAYMENTS = (
    ('cash','NAQD'),
    ('click','CLICK'),
    ('payme','PAYME'),
    ('oson','OSON'),
    )
    STATES = (
    ('andijon','Andijon'.upper()),
    ('buxoro','Buxoro'.upper()),
    ('fargona',"Farg'ona".upper()),
    ('jizzax',"Jizzax".upper()),
    ('xorazm',"Xorazm".upper()),
    ('namangan',"Namangan".upper()),
    ('navoiy',"Navoiy".upper()),
    ('samarqand',"Samarqand".upper()),
    ('surxandaryo',"Surxandaryo".upper()),
    ('sirdaryo',"Sirdaryo".upper()),
    ('toshkent',"Toshkent".upper()),
    ('qashqadaryo',"Qashqadaryo".upper()),
    ('nukus',"Nukus".upper()),
    )
    user = models.OneToOneField(User, verbose_name='Xaridor', on_delete=models.CASCADE, null=True)
    first_name = models.CharField('Ism', max_length=100)
    last_name = models.CharField('Familya', max_length=100)
    phone = models.CharField('Telefon', max_length=50)
    telegram_id = models.CharField('Telegram ID', max_length=50, blank=True)
    email = models.EmailField()
    state = models.CharField('Viloyat', max_length=80, choices=STATES)
    address = models.CharField('Tuman', max_length=80)
    street = models.CharField("Ko'cha va uy manzili", max_length=150)
    postal_code = models.CharField('Pochta indeksi', max_length=50)
    payment_method = models.CharField("To'lov turi", max_length=50, choices=PAYMENTS)
    message = models.TextField("Qo'shimcha xabar", blank=True)
    products = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    total = models.CharField(max_length=10)

    payed = models.BooleanField("To'lov xolati", default=False)

    class Meta:
        verbose_name='Buyurtma'
        verbose_name_plural='Buyurtmalar'
        ordering = ['-id']

    def __str__(self):
        return f"{self.first_name}"


class OrderItem(models.Model):
	user = models.OneToOneField(User, verbose_name='Xaridor', on_delete=models.CASCADE)
	products = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	first_name = models.CharField('Ism', max_length=100)
	last_name = models.CharField('Familya', max_length=100)
	phone = models.CharField('Telefon', max_length=50)
	telegram_id = models.CharField('Telegram ID', max_length=50, blank=True)
	email = models.EmailField()
	state = models.CharField('Viloyat', max_length=80)
	address = models.CharField('Tuman', max_length=80)
	street = models.CharField("Ko'cha va uy manzili", max_length=150)
	postal_code = models.CharField('Pochta indeksi', max_length=50)
	payment_method = models.CharField("To'lov turi", max_length=50,)
	message = models.TextField("Qo'shimcha xabar", blank=True)
 
    

	payed = models.BooleanField("To'lov xolati", default=False)

	class Meta:
		verbose_name='Buyurtma Tovar'
		verbose_name_plural='Buyurtma Tovarlar'
		ordering = ['-id']

	def __str__(self):
		return f"{self.first_name}"