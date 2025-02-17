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
        его метод get() - он принимает и обрабатывает get-запрос
        lst - список со всеми данными из таблицы Women
            values(), чтобы получить список, вместо QuerySet
        return - возвращает данные в json формате
        """
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})



    def post(self, request):
        """
        Описание - благодаря данному методу, мы можем передать словарь в json с ключами - названием полей
        и значеним - значением полей, и таким образом создать новую запись в таблице
        postman->post->Body->raw->json
        метод  post() - он принимает и обрабатывает post-запрос
        post_new - объект модели Women
            Women.objects.create() - создаёт новую запись в таблице с переданными полями
                request.data['<имя поля>'] - определяет поле таблицы
        return - возвращает данные добавленные в таблицу
            model_to_dict - преобразует QuerySet в json

        """
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})


# # вью для таблицы women
# class WomenAPIView(generics.ListAPIView):
#     # передаём все строки таблицы women
#     queryset = Women.objects.all()
#     # сериализатор
#     serializer_class = WomenSerializer