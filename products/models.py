import random
from django.db import models
import os
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 99999999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{instance.id}-{instance.title}.{rand_name}{ext}"
    return f"products/{final_name}"


class ProductManageObjects(models.Manager):
    def get_product_by_id(self, productID):
        qs = self.get_queryset().filter(id=productID)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_active_products(self):
        return self.get_queryset().filter(actived=True)

    def get_active_show_products(self):
        return self.get_queryset().filter(actived=True, show=True)

    # def all(self):
    #    return self.get_queryset().filter(id=2)


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    actived = models.BooleanField(default=False)
    show = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    objects = ProductManageObjects()

    def __str__(self):
        return self.title

    def product_url(self):
        return f"/products/{self.slug}"


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
