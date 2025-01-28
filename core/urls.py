from carimbos.urls import path
from .views import index, carimbo

urlpatterns = [
    path('', index, name='index'),
    path('carimbo.html', carimbo, name='carimbo'),
]
