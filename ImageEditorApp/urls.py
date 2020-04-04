from django.urls import path
from . import views

app_name = 'ImageEditorApp'


urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.img)
]

