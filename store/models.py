from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unite_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
class Custormer(models.Model):
    # email (unique)
    # birth_date (nullable)

    # if we want to change the bronze, we can just change in one place
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'GOld')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # email = models.EmailField(max_length=254)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    # birth_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING, 'PENDING'),
        (PAYMENT_COMPLETE, 'COMPLETE'),
        (PAYMENT_FAILED, 'FAILED')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING  )
    placed_by = models.ForeignKey(Custormer, on_delete=models.PROTECT)

class OrederItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    # price could change, save the price put in
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    # address = models.OneToOneField(Custormer, on_delete=models.CASCADE, primary_key=True)
    address = models.ForeignKey(Custormer, on_delete=models.CASCADE)


class Cart(models.Model):
    carted_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
class Item(models.Model):
    item_name = models.CharField(max_length=255)


