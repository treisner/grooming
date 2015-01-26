from django.db import models
from customers.django_orm import CredentialsField
from django.contrib.auth.models import User
from django.contrib import admin
from django_localflavor_us.models import PhoneNumberField
from django.core.urlresolvers import reverse



XSMALL='XS'
SMALL='SM'
MEDIUM='MD'
LARGE='LG'
XLARGE='XL'
SHORT='SH'
LONG='LH'
ANY='ANY'
SIZE=[
    (XSMALL,'XS Less than 15lb'),
    (SMALL,'SM 15lb to 30lb'),
    (MEDIUM,'MD 30lb to 50lb'),
    (LARGE,'LG 50lb to 100lb'),
    (XLARGE,'XL More that 100lb'),
    (ANY,'All sizes the same'),
]
HAIR=[(LONG,"Long Hair"),(SHORT,"SHORT HAIR"),(ANY,'All sizes the same'),]

class Customer(models.Model):
    first_name = models.CharField(max_length=15,default="")
    last_name = models.CharField(max_length=15, blank=False,default="")
    home_phone = PhoneNumberField(blank=False, unique=True)
    work_phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    veterinarian = models.CharField(max_length=30,blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering=['last_name','first_name']

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    name = property(_get_full_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})

class Service(models.Model):
    service = models.CharField(max_length=15, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    description = models.TextField(blank=True)
    size = models.CharField(choices=SIZE, max_length=4,default=ANY)
    class Meta:
        unique_together=("service","size")
        ordering = ['service','-price']

    def get_price(self):
        return self.price

    def __str__(self):
        return self.service

class Breed(models.Model):
    breed = models.CharField(max_length=30, blank=False, unique=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='/media/customers/',blank=True,null=True)
    size = models.CharField(choices=SIZE, max_length=4,default=ANY)

    class Meta:
        ordering = ['breed']

    def __str__(self):
        return self.breed

class Pet(models.Model):
    M = 'M'
    F = 'F'
    U = 'U'
    SEX = (
        (M, 'M'),
        (F, 'F'),
        (U, 'Unspecified')
    )
    name = models.CharField(max_length=10, blank=False)
    breed = models.ForeignKey(Breed,default=-1)
    sex = models.CharField(choices=SEX, max_length=1,default=U)
    birthday = models.DateField(blank=True)
    owner = models.ForeignKey(Customer)
    vaccinated = models.NullBooleanField(default=False)
    noisy = models.NullBooleanField(default=False)
    bites = models.NullBooleanField(default=False)
    shy = models.NullBooleanField(default=False)
    soils_cage = models.NullBooleanField(default=False)
    arthritic = models.NullBooleanField(default=False)
    epileptic = models.NullBooleanField(default=False)
    overweight = models.NullBooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering=['name','owner']
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pet_detail', kwargs={'pk': self.pk})

class Call(models.Model):
    phone_number = PhoneNumberField(blank=False)
    caller_id_name = models.CharField(max_length=30, blank=False)
    rang_at = models.DateTimeField()
    customer = models.ForeignKey(Customer)

    def __str__(self):
        callid = "{} from {} {}".format(self.rang_at,self.phone_number,self.caller_id_name)
        return callid


class Appointment(models.Model):
    gcalid = models.CharField(max_length=255,unique=True) #Google Calendar ID
    pet = models.ForeignKey(Pet)
    when = models.DateTimeField(blank=False)
    notes = models.TextField(blank=True)
    todo = models.CharField(max_length=64,blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2,blank=True)
    def __str__(self):
        return self.gcalid

    class Meta:
        ordering=['when']

class AppointmentDetail(models.Model):
    appointment = models.ForeignKey(Appointment)
    service = models.ForeignKey(Service)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    do_it=models.NullBooleanField(default=False)

    class Meta:
        unique_together=(("appointment","service"),)


# Google calendar authentication

class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()

class CredentialsAdmin(admin.ModelAdmin):
    pass
