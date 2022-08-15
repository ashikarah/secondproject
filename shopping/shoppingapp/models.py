from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery', blank=True)

    def get_url(self):
        return reverse('shopping:products_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='pic', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shopping:productdetail', args=[self.category.slug, self.slug])
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)

