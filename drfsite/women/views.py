from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer

# Представление стандартного класса APIView
class WomenAPIView(APIView):
    def get(self, request):
        """
        метод get() - он принимает и обрабатывает get-запрос
        w - список со всеми данными из таблицы Women
        return - возвращает сериализованные данные
            many=True передаёт значения списком
        """
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})



    def post(self, request):
        """
        Описание - благодаря данному методу, мы можем передать словарь в json с ключами - названием полей
        и значеним - значением полей, и таким образом создать новую запись в таблице
        postman->post->Body->raw->json
        метод  post() - он принимает и обрабатывает post-запрос
        serializer - хранит в себе данные из запроса, чтобы потом валидировать их
        post_new - объект модели Women
            Women.objects.create() - создаёт новую запись в таблице с переданными полями
                request.data['<имя поля>'] - определяет поле таблицы
        return - возвращает данные добавленные в таблицу
            model_to_dict - преобразует QuerySet в json

        """
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid()

        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )

        return Response({'post': WomenSerializer(post_new).data})


# # вью для таблицы women
# class WomenAPIView(generics.ListAPIView):
#     # передаём все строки таблицы women
#     queryset = Women.objects.all()
#     # сериализатор
#     serializer_class = WomenSerializer