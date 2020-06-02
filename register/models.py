from django.db import models


class Register(models.Model):
    STD_CHOICES = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Forth', 'Forth')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    std = models.CharField(max_length=100, choices=STD_CHOICES, null=True)
    fees = models.BooleanField(default=False)
    partial_fee=models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    total_fee=models.IntegerField(null=True,default=0)
    fee_recieved=models.IntegerField(null=True,default=0)
    one_time_fee=models.IntegerField(null=True,default=0)
    
    def __str__ (self):
        return self.first_name
    


