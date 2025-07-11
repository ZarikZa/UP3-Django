
from django.conf import settings

from shop.models import Products
class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        products_id = self.basket.keys()

        product_list = Products.objects.filter(pk__in = products_id)

        basket = self.basket.copy()
        for product in product_list:
            basket[str(product.pk)]['product'] = product

        for item in basket.values():
            item['total_price'] = float(item['price']) * int(item['count'])
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'count': 0,
                                       'price': str(product.price)}
        if update_count:
            self.basket[product_id]['count'] = count
        else:
            self.basket[product_id]['count'] += count
        self.save()

    def increase(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['count'] += 1
            self.save()

    def decrease(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            if self.basket[product_id]['count'] > 1:
                self.basket[product_id]['count'] -= 1
                self.save()
            else:
                self.remove(product)

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        return sum(float(item['price']) * int(item['count']) for item in self.basket.values())

    def get_total_quantity(self):
        return sum(item['count'] for item in self.basket.values())

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True
