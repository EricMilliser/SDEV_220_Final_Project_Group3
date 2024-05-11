from django.db import models

# Create your models here.



from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isAvailable = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])

    def __str__(self):
        return self.name
    

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"
    
    @property
    def total(self):
        return self.quantity * self.item.price