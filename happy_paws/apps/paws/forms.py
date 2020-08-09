from django import forms
from .models import *


class KindForm(forms.ModelForm):
    class Meta:
        model = Kind
        fields = '__all__'


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'


class CuratorForm(forms.ModelForm):
    class Meta:
        model = Curator
        fields = '__all__'


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
