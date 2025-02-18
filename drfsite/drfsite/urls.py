from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from women.views import WomenViewSet

# создам объект класса SimpleRouter - он нужен для построения маршрута, учитывая возможности вью
router = routers.SimpleRouter()
# register() - определяет маршрут, точнее его часть, после статичной части и передаём вью
router.register(r'women', WomenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)) #
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
