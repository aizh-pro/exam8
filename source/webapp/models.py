from django.contrib.auth import get_user_model
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Еда'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты'),
    ('toys', 'Игрушки'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=20, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES,
                                verbose_name='Категория')
    picture = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')


    def __str__(self):
        return f'{self.name} - {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
        permissions = [
            ('can_have_piece_of_pizza', 'Может съесть кусочек пиццы'),
        ]


DEFAULT_RATE = 0
RATE_CHOICES = ((DEFAULT_RATE, 0),
                ("One", 1),
                ("Two", 2),
                ("Three", 3),
                ("Four", 4),
                ("Five", 5)
)


class Review(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='review', on_delete=models.CASCADE, verbose_name='Продукт')
    text = models.TextField(max_length=2000,verbose_name='Текст')
    rate = models.IntegerField(max_length=20, default=DEFAULT_RATE, choices=RATE_CHOICES,
                                verbose_name='Оценка')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='reviews', verbose_name='Автор')

    def __str__(self):
        return "{}. {}".format(self.pk, self.text)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"