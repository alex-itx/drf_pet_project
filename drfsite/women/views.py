from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women
from .serializers import WomenSerializer



# вью для таблицы women с использованием ListCreateAPIView
class WomenAPIList(generics.ListCreateAPIView):
    """
    ListCreateAPIView - класс для чтения (get-запрос) и создания списка данных (post-запрос)
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# вью для таблицы women с использованием UpdateAPIView
class WomenAPIUpdate(generics.UpdateAPIView):
    """
    UpdateAPIView - класс для изменения записи таблицы (put/patch-запрос)
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# вью для таблицы women с использованием RetrieveUpdateDestroyAPIView
class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView - класс для чтения, изменения и удаления отдельной записи таблицы
    (get, put/patch, delete -запрос)
    """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
















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
