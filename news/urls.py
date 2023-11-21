from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_homes, name = 'news_homes' ),
    path('create', views.create, name = 'create' ),
    path('<int:pk>', views.NewsDatailView.as_view(), name= 'news_datail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name= 'news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name= 'news_delete'),

]
    