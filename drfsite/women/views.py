from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer





class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes - ограничения пользователя
    # IsAuthenticatedOrReadOnly - только для чтения если не авторизован
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, ) # делаем доступ на страницу только авторизованным по токе ну

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )






















































































# # вью для таблицы women с использованием ModelViewSet
# class WomenViewSet(viewsets.ModelViewSet):
#     """
#     ModelViewSet - класс вьюсет, берет на себя весь функционал всех классов вью с моделью
#     благодаря тому, что использует множество миксинов:
#         mixins.CreateModelMixin, - создание записи
#         mixins.RetrieveModelMixin, - выделение записи
#         mixins.UpdateModelMixin, - изменение записи
#         mixins.DestroyModelMixin, - удаление записи
#         mixins.ListModelMixin, - чтение списка записей
#     """
#     # queryset = Women.objects.all() # Если у нас есть собственное определение вывода записей, queryset не нужен
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         """
#         Если нам нужно собственное определение вывода записей, создаётся специальный метод для вывода
#         :return 1: возвращает первые три записи таблицы
#         :return 1: возвращает конкретную запись
#         Если у нас нет в классе параметра queryset, в роутере обязательно нужно указать параметр basename
#         pk - забирает индекс из реквеста на слуйчай, если мы хотим иметь возможность обращаться к конкретной записи
#         после этого осуществляется проверка на совпадение айдишника в таблице
#         """
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)
#
#     @action(methods = ['get'], detail=True)
#     def category(self, requests, pk=None):
#         """
#         @action - декоратор из библиотеки rest_framework, он нужен для того, чтобы определить новый
#         маршрут внутри роутера. В данном случае women/category
#             methods - определяет какие методы запроса, можно использовать в маршруте
#             detail - определяет, можно ли обращаться к конкретной записи, например по pk women/2/category
#         category() - функция в которой мы определяем - что будет возвращаться в маршруте
#         Название функции и будет являться префиксом url
#             pk - параметр который определяет параметр маршрута по индексу таблицы
#         cats - берёт запись (будем передовать конкретную запись таблицы)
#         """
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# # вью для таблицы women с использованием ListCreateAPIView
# class WomenAPIList(generics.ListCreateAPIView):
#     """
#     ListCreateAPIView - класс для чтения (get-запрос) и создания списка данных (post-запрос)
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # вью для таблицы women с использованием UpdateAPIView
# class WomenAPIUpdate(generics.UpdateAPIView):
#     """
#     UpdateAPIView - класс для изменения записи таблицы (put/patch-запрос)
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # вью для таблицы women с использованием RetrieveUpdateDestroyAPIView
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     RetrieveUpdateDestroyAPIView - класс для чтения, изменения и удаления отдельной записи таблицы
#     (get, put/patch, delete -запрос)
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



# # вью для таблицы women
# class WomenAPIView(generics.ListAPIView):
#     # передаём все строки таблицы women
#     queryset = Women.objects.all()
#     # сериализатор
#     serializer_class = WomenSerializer





# # Представление стандартного класса APIView
# class WomenAPIView(APIView):
#     def get(self, request):
#         """
#         метод get() - он принимает и обрабатывает get-запрос
#         w - список со всеми данными из таблицы Women
#         return - возвращает сериализованные данные
#             many=True передаёт значения списком
#         """
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#
#
#     def post(self, request):
#         """
#         Описание - благодаря данному методу, мы можем передать словарь в json с ключами - названием полей
#         и значеним - значением полей, и таким образом создать новую запись в таблице
#         postman->post->Body->raw->json
#         метод  post() - он принимает и обрабатывает post-запрос
#         serializer - хранит в себе данные из запроса, чтобы потом валидировать их,
#         а потом сохранить как объект модели
#         return - возвращает данные добавленные в таблицу
#
#         """
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid()
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         """
#         put() - используется для изменения записей в бд
#         в функции сначала определяется поле из запроса (равное конвертеру),
#         после проверяется есть ли оно в таблице,
#         если есть записываем строку с таким полем,
#         далее селиалезируем строку,
#         сохраняем её - вызываем метод update из сериализатора
#
#         :return: возвращаем сериализованные данные
#         """
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
