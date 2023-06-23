from django.urls import path
from . views import home_view, page1_view, page2_view, id_view

urlpatterns = [
    path('', home_view, name='home'),
    path('page1/', page1_view, name='page1'),
    path('page2/', page2_view, name='page2'),
    path('<int:pk>/', id_view, name='id'),
]
