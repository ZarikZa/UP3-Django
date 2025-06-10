from django.db import models

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование коллекции')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')
    #buy = models.OneToOneField('clothes',on_delete=models.CASCADE, и чтото ещё)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Clothes(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование позиции')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    #buy = models.OneToOneField('Category', on_delete=models.CASCADE, related_name="buy_clothes", verbose_name='ASD')
    # в кавычках потому что отложенная инициализация так как класс создаётся после использваония

    def __str__(self):
        return f"{self.name} - ({self.price} руб.)"

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'