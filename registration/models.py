from django.db import models
from django.utils import timezone

# Define a tuple for choices to be used in models and forms
BLOOD_GROUP_CHOICES = (
    ('O +ve', 'O +ve'), ('O -ve', 'O -ve'),
    ('A +ve', 'A +ve'), ('A -ve', 'A -ve'),
    ('B +ve', 'B +ve'), ('B -ve', 'B -ve')
)

TSHIRT_SIZE_CHOICES = (
    ('S', 'S - Small'), ('M', 'M - Medium'), ('L', 'L - Large'),
    ('XL', 'XL - Extra Large'), ('XXL', 'XXL - Extra Extra Large'),
    ('XXXL', 'XXXL - Extra Extra Extra Large')
)

PAYMENT_METHOD_CHOICES = (
    ('bkash', 'Bkash'), ('nagad', 'Nagad'), ('handcash', 'Hand Cash')
)


class Registrant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    mobile = models.CharField(max_length=20)
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    profession = models.CharField(max_length=100)
    tshirt_size = models.CharField(max_length=5, choices=TSHIRT_SIZE_CHOICES)
    spouse_check = models.BooleanField(default=False)
    child_checkbox = models.BooleanField(default=False)
    number_of_children = models.IntegerField(default=0, blank=True, null=True)
    payment_method = models.CharField(
        max_length=10, choices=PAYMENT_METHOD_CHOICES)
    hand_cash_to = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    total_member = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False, verbose_name='Approved')
    registration_date = models.DateTimeField(
        default=timezone.now, verbose_name='Date of Registration')
    unique_id = models.CharField(max_length=10, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            prefix = 'CCHS'
            year = timezone.now().strftime('%Y')
            last_registrant = Registrant.objects.filter(unique_id__startswith=prefix + year).order_by('unique_id').last()
            if last_registrant:
                last_id_number = int(last_registrant.unique_id[-2:])  # Assuming the last two digits are the incrementing part
                new_id_number = last_id_number + 1
            else:
                new_id_number = 1
            self.unique_id = '{prefix}{year}{id:02d}'.format(prefix=prefix, year=year, id=new_id_number)
        super(Registrant, self).save(*args, **kwargs)


    def __str__(self):
        return self.full_name
