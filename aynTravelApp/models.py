from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Offer(models.Model):
   
    title = models.CharField(max_length=150,verbose_name='Название турпакета')
    text=CKEditor5Field('Text', config_name='extends', null=True)
    info = models.TextField(blank=True)
    location1 = models.CharField(null=True, max_length=100, verbose_name= "Локация")
    days = models.IntegerField(verbose_name="Сколько дней?")
    nights = models.IntegerField(verbose_name="Сколько ночей?")
    mark = models.IntegerField(verbose_name="оценка")
    price = models.IntegerField(verbose_name="Цена", null=True)
    created_at = models.DateField(auto_now_add=True)
    photo = models.FileField(upload_to='Photos/%Y/%m/%d', verbose_name='фотография турпакета',blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Доступность')
    
    def get_absolute_url(self):
        return reverse('view_offer', kwargs={"offer_id": self.pk})

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'турпакет'
        verbose_name_plural = 'турпакеты'
        ordering = ['title']


class About(models.Model):
    title = models.CharField(max_length=150)
    info = models.TextField(blank=True)
    photo = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    
    class Meta:
        verbose_name = 'информация'
        verbose_name_plural = 'информация'

class Cat(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='город/страна', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'категория турпакета'
        verbose_name_plural = 'категории турпакетов'
        ordering = ['title']

        
class Contact(models.Model):
    info = models.TextField(blank=True)
    address = models.CharField('address',max_length=150)
    TelNum = models.CharField('tel.number',max_length=150)

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'

class Services(models.Model):
    icon = models.ImageField(blank=True, upload_to='Photos/%Y/%m/%d',verbose_name='иконка сервиса')
    title = models.CharField(max_length=100, verbose_name='название сервиса')
    photo = models.ImageField(blank=True, upload_to='Photos/%Y/%m/%d',verbose_name='фотография примера сервиса')
    # use duoble title as in the layout
    availability = models.BooleanField(default=True)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name = 'cервисы'
        verbose_name_plural = 'cервисы'

class BookingForm(models.Model):

    title = models.CharField(max_length=150,verbose_name='Название турпакета')
    title = models.CharField(max_length=150,verbose_name='Название турпакета')
    days = models.IntegerField(verbose_name="Сколько дней?")
