from django.views.generic import ListView
from .models import Kampanye

# Create your views here.
class KampanyeListView(ListView):
    model = Kampanye
    template_name = "kampanye.html"
