from django.db import models

class Offer(models.Model):
    photo = models.FileField(upload_to='Photos/%Y/%m/%d', verbose_name='фотография города(страны)',blank=True, null=True)
    # photo = models.ImageField(upload_to='Photos/%Y/%m/%d', verbose_name='фотография города(страны)',blank=True)
    title = models.CharField(max_length=150,verbose_name='Nazvanie tur paketa')
    created_at = models.DateField(auto_now_add=True)
    info = models.TextField(blank=True)
    location1 = models.CharField(null=True, max_length=100, verbose_name= "Lokatsiya")
    days = models.IntegerField(verbose_name="Days")
    mark = models.IntegerField(verbose_name="Otsenka")
    nights = models.IntegerField(verbose_name="Nights")
    price = models.IntegerField(verbose_name="Цена", null=True)
    category =  models.ForeignKey('Cat', on_delete=models.PROTECT, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Доступность')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
        ordering = ['title']


class About(models.Model):
    title = models.CharField(max_length=150)
    info = models.TextField(blank=True)
    photo = models.ImageField(upload_to='Photos/%Y/%m/%d', blank=True)
    
    class Meta:
        verbose_name = 'информация'
        verbose_name_plural = 'информации'

class Cat(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='город/страна', blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'категория предложений'
        verbose_name_plural = 'категории предложений'
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


