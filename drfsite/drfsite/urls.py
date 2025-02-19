from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter, Route

from women.views import WomenViewSet


# создаём собственный роутер
class CustomReadOnlyRouter(SimpleRouter):
    """
    Класс собственного роутера
    routes - коллекция маршрутов, где каждый элемент списка, это отдельный маршрут созданный с помощью
    класса Route с указанием всех необходимых параметров маршрута
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]


# создаём роутер используя DefaultRouter(), он даёт дополнительные маршруты без префикса
router = CustomReadOnlyRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls) # показывает, какие маршруты присутствуют в роутере


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)) #
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]











# # создам объект класса SimpleRouter - он нужен для построения маршрута, учитывая возможности вью
# router = routers.SimpleRouter()
# # register() - определяет маршрут, точнее его часть, после статичной части, взаимодействуя с моделью через вьюсет
# router.register(r'women', WomenViewSet)
