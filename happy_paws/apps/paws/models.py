from django.db import models

# Create your models here.


# Вид (кошка, собака, etc.)
class Kind(models.Model):
    kind = models.CharField(max_length=20, verbose_name='Вид')

    def __str__(self):
        return self.kind

    def get_absolute_url(self):
        return 'kind/%i' % self.pk

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'


# Порода (овчарка, гончая, вислоухая, etc)
class Breed(models.Model):
    breed = models.CharField(max_length=30, verbose_name='Порода')
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, verbose_name='Вид')

    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return 'breed/%i' % self.pk

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


# Куратор животного
class Curator(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя куратора')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=30, verbose_name='e-mail')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'curator/%i' % self.pk

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


# Животное
class Animal(Breed):
    class StatusChoice(models.TextChoices):
        miss = ('В приюте', 'В приюте')
        home = ('Обрёл дом', 'Обрёл дом')
        unknown = ('Неизвестно', 'Неизвестно')

    nickname = models.CharField(max_length=30, verbose_name='Кличка')
    age = models.SmallIntegerField(verbose_name='Возраст')
    description = models.TextField(verbose_name='Описание')
    title = models.CharField(max_length=50, verbose_name='Краткое описание')
    curator = models.ForeignKey(Curator, on_delete=models.PROTECT, verbose_name='Куратор')
    image = models.ImageField(upload_to='animals/', blank=True, verbose_name='Фотография')
    status = models.CharField(max_length=10,
                              choices=StatusChoice.choices,
                              default=StatusChoice.unknown,
                              verbose_name='Статус')

    def get_image(self):
        if not self.image:
            self.cover = 'paws.jpeg'
            return self.image
        else:
            return self.image

    def __str__(self):
        return f'{self.breed} {self.nickname}'

    def get_absolute_url(self):
        return 'animal/%i' % self.pk

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
