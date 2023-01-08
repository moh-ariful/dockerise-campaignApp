from kampanye.views import KampanyeListView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', KampanyeListView.as_view(), name='kampanye'),

]

