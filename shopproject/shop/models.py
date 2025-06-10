from django.db import models

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')

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

class CountryProivodstva(models.Model):
    country = models.CharField(max_length=MAX_LENGTH, verbose_name='Страна производства')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Brand(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название бренда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Products(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование позиции')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    country = models.ForeignKey(CountryProivodstva, on_delete=models.PROTECT, verbose_name='Страна производства')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')

    def __str__(self):
        return f"{self.name} - ({self.price} руб.)"

    class Meta:
        verbose_name = 'Сантехника'
        verbose_name_plural = 'Сантехники'

class Clients(models.Model):
    clientName = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя клиента')
    clientSurname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия клиента')
    clientMiddleName = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Отчество клиента')
    login = models.CharField(max_length=MAX_LENGTH, verbose_name='Логин')
    password = models.CharField(max_length=MAX_LENGTH, verbose_name='Пароль')

    def __str__(self):
        return f"{self.clientName} {self.clientSurname} {self.clientMiddleName}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар')
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Клиент')
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка', default=5)
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f"Отзыв от {self.client} на {self.product}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Wishlist(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f"{self.client} - {self.product}"

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт')
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    kolvo = models.IntegerField(verbose_name='Количетсво')

    def __str__(self):
        return f"{self.product} {self.client}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Bill(models.Model):
    cart = models.ManyToManyField(Cart, verbose_name='Корзина')
    priceBill = models.FloatField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')

    def __str__(self):
        return f"{self.cart} {self.create_date}"

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
