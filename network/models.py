from django.db import models


class NetworkNode(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)

    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clients'
    )
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def level(self):
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level

    def __str__(self):
        return self.name


class Product(models.Model):
    node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.model})"
