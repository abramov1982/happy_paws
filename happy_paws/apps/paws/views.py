from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Create your views here.
'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
'''


class KindCreate(CreateView):
    model = Kind
    form_class = KindForm
    success_url = reverse_lazy('index')
    template_name = 'add.html'


class AnimalView(ListView):
    model = Animal
    template_name = 'index.html'


class AnimalDetail(DetailView):
    model = Animal
    template_name = 'detail.html'
    context_object_name = 'animal'


class CuratorDetail(DetailView):
    model = Curator
    template_name = 'detail.html'
    context_object_name = 'curator'


class CuratorUpdate(UpdateView):
    form_class = CuratorForm
    model = Curator
    template_name = 'add.html'
    success_url = reverse_lazy('index')
'''
class DebtorRead(ListView):
    model = Debtor
    template_name = 'lib/list_debtors.html'


class DebtorUpdate(UpdateView):
    form_class = DebtorForm
    model = Debtor
    template_name = 'lib/add_debtor.html'
    success_url = reverse_lazy('list_debtor')
'''