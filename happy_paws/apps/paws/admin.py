from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    pass


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Curator)
class CuratorAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass
