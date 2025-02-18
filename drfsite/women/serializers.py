import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women



# селиализатор отнаследованный от базового класса Serializer
class WomenSerializer(serializers.Serializer):
    # Вручную пропишем поля для котороый будут сериализироваться
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


    def create(self, validated_data):
        """
        create() - метод для сохранения данных в бд
            validated_data - принимает валидированные данные, которые создаются после валидации во вью
        :return - создаёт запись в бд, при помощи ОРМ функции create
        """
        return Women.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        update() - используется для изменения записей
            В него мы передаём каждое поле как объект instance, потом сохраняем его и возвращаем
        :param instance: объект записи, через именнованный параметр указывается поле с тем же именем
        :return: возвращает объект instance
        """
        instance.title =  validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance


















# # создадим иметацию модели
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# def encode():
#     """
#     encode() - функция кодирования данных в json формат
#     model - объект модели
#     model_sr - объект сериализации объекта модели
#         .data - параметр класса WomenSerializer, возвращает данные (в словаре) объекта класса, а не его самого
#     json - данные в json формате
#         JSONRenderer() - преобразовывает объект сериализации в json строку
#         render() - принимает объект сериализации, чтобы передать его в JSONRenderer()
#     """
#     model = WomenModel('Alex', 'superprogramer')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     """
#     decode() - функция декодирования json данных в словарь
#     stream - json данные
#         io.BytesIO() - обрабатывает json данные
#     data - данные в виде словаря
#         JSONParser() - переводит json данные в словарь
#         parse - обрабатывает json данные и передаёт из в JSONParser()
#     serializer - обект сериализатора с json внутри
#         data - параметр для хранения данных
#     validated_data - параметр в WomenSerializer, который хранит в себе данные, появляется после проверки на валидацию
#     """
#     stream = io.BytesIO(b'{"title":"Alex","content":"superprogramer"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)















# # Сериализатор для таблицы women
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ['title', 'cat_id']