from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Offer(models.Model):
   
    title = models.CharField(max_length=150,verbose_name='Название турпакета')
    text=CKEditor5Field('Text', config_name='extends', null=True)
    days = models.IntegerField(verbose_name="Сколько дней?")
    nights = models.IntegerField(verbose_name="Сколько ночей?")
    mark = models.IntegerField(verbose_name="оценка")
    price = models.IntegerField(verbose_name="Цена", null=True)
    created_at = models.DateField(auto_now_add=True)
    category =  models.ForeignKey('Cat', on_delete=models.PROTECT, null=True)
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
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Cat(models.Model):
    city = models.CharField(max_length=150, db_index=True, verbose_name='название турпакета', blank=True)
    country = models.CharField(max_length=150, verbose_name='страна', blank=True)
    mark = models.IntegerField(verbose_name="оценка", null=True)
    photo = models.FileField(upload_to='Photos/%Y/%m/%d', verbose_name='фотография турпакета',blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена", null=True)

    def __str__(self):
        return self.city
    class Meta:
        verbose_name = 'категория турпакета'
        verbose_name_plural = 'категории турпакетов'
        

class ContactForm(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name
        
class Contact(models.Model):
    info = models.TextField(blank=True)
    address = models.CharField('address',max_length=150)
    TelNum = models.CharField('tel.number',max_length=150)

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'

class Operator(models.Model):
    author = models.CharField(max_length=50, verbose_name='Опрератор')
    text = models.TextField('Text', null=True)
    post =  models.CharField(max_length=50, verbose_name='Должность')
    photo = models.FileField(upload_to='Photos/%Y/%m/%d', verbose_name='фотография опрератора',blank=True, null=True)

    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'