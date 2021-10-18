from django.views.generic import DetailView, ListView

from .models import Produto

class ProdutoListView(ListView):
    model = Produto

class ProdutoDetailView(DetailView):
    model = Produto