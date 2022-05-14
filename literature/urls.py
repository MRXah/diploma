from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('detail/<pk>', views.PlaceDV.as_view(), name='view_place'),
    path('create/', views.PlaceCV.as_view(), name='create_place'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
