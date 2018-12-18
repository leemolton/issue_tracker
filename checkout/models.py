from django.db import models

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, default='SOME STRING')
    stripe_id = models.CharField(max_length=255, default='SOME STRING')
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
        
class OrderLineItem(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    
    
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.full_name, self.date)