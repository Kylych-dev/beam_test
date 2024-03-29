from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.store.models import Store
from .serializers import StoreSerializer
from utils.customer_logger import log_error, log_warning


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список магазинов.",
        operation_summary="Список магазинов",
        tags=["Магазин"],
        responses={
            200: openapi.Response(description="OK - Список магазинов успешно получен."),
            400: openapi.Response(description="Неверный запрос - Некорректные данные"),
        },
    )
    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as ex:
            log_error(self, ex)
            return Response(
                {"message": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        method="get",
        operation_description="Получить информацию о магазине.",
        operation_summary="Информация о магазине",
        tags=["Магазин"],
        responses={
            200: openapi.Response(description="OK - Информация о магазине успешно получена."),
            404: openapi.Response(description="Не найдено - Магазин не найден"),
        },
    )
    @action(detail=True, methods=['get'])
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404 as ex:
            log_warning(self, ex)
            return Response(
                {"message": "Объект не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        method="put",
        operation_description="Обновить информацию о магазине.",
        operation_summary="Обновление информации о магазине",
        tags=["Магазин"],
        responses={
            200: openapi.Response(description="OK - Информация о магазине успешно обновлена."),
            400: openapi.Response(description="Неверный запрос - Некорректные данные"),
        },
    )
    @action(detail=True, methods=['put'])
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            log_error(self, ex)
            return Response(
                {"message": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
    @swagger_auto_schema(
        method="post",
        operation_description="Создать магазин.",
        operation_summary="Создание магазина",
        tags=["Магазин"],
        responses={
            201: openapi.Response(description="Created - Магазин успешно создан."),
            400: openapi.Response(description="Bad Request - Некорректные данные"),
        },
    )
    @action(detail=False, methods=['post'])
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            log_error(self, ex)
            return Response(
                {"message": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
            )


    @swagger_auto_schema(
        method="delete",
        operation_description="Удалить магазин.",
        operation_summary="Удаление магазина",
        tags=["Магазин"],
        responses={
            204: openapi.Response(description="No Content - Магазин успешно удален."),
            404: openapi.Response(description="Not Found - Магазин не найден"),
        },
    )
    @action(detail=True, methods=['delete'])
    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404 as ex:
            log_warning(self, ex)
            return Response(
                {"message": "Магазин не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )