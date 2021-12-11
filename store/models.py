from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField("*", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    COLORS = (
        ("red", "RED"),
        ("blue", "BLUE"),
        ("green", "GREEN"),
    )
    name = models.CharField("Name", max_length=100)
    slug = models.SlugField("*", max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
        )
    image = models.ImageField("Product image", upload_to='product_images/')
    price = models.PositiveIntegerField("Price", default=0)
    description = models.TextField("About product")
    in_stock = models.PositiveIntegerField("Count", default=1)
    colors = models.CharField("Colors", max_length=50, choices=COLORS)
    stars = models.PositiveIntegerField("Stars", default=0)
    discount = models.CharField("Discount", max_length=10, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-id"]


# Product Images model
class ProductImages(models.Model):
	product = models.ForeignKey(Product,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='product_images')
	image = models.ImageField('Tovar alohida rasmlari',
		upload_to='product_images/',
		blank=True, null=True,)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Tovar rasmlari'
		verbose_name_plural = 'Tovar rasmlari'

