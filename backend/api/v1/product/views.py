from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.product.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from utils.customer_logger import log_error, log_warning


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список категорий.",
        operation_summary="Список категорий",
        tags=["Категория"],
        responses={
            200: openapi.Response(description="OK - Список категорий успешно получен."),
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
        method="put",
        operation_description="Обновить информацию о категории.",
        operation_summary="Обновление категории",
        tags=["Категория"],
        responses={
            200: openapi.Response(description="OK - Категория успешно обновлена."),
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
        operation_description="Создать категорию.",
        operation_summary="Создание категории",
        tags=["Категория"],
        responses={
            201: openapi.Response(description="Created - Категория успешно создана."),
            400: openapi.Response(description="Неверный запрос - Некорректные данные"),
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
        operation_description="Удалить категорию.",
        operation_summary="Удаление категории",
        tags=["Категория"],
        responses={
            204: openapi.Response(description="No Content - Категория успешно удалена."),
            404: openapi.Response(description="Not Found - Категория не найдена"),
        },
    )
    @action(detail=True, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404 as ex:
            log_warning(self, ex)
            return Response(
                {"message": "Категория не найдена"}, 
                status=status.HTTP_404_NOT_FOUND
            )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список продуктов.",
        operation_summary="Список продуктов",
        tags=["Продукт"],
        responses={
            200: openapi.Response(description="OK - Список продуктов успешно получен."),
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
        method="post",
        operation_description="Создать продукт.",
        operation_summary="Создание продукта",
        tags=["Продукт"],
        responses={
            201: openapi.Response(description="Created - Продукт успешно создан."),
            400: openapi.Response(description="Неверный запрос - Некорректные данные"),
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
        method="put",
        operation_description="Обновить информацию о продукте.",
        operation_summary="Обновление продукта",
        tags=["Продукт"],
        responses={
            200: openapi.Response(description="OK - Продукт успешно обновлен."),
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
        method="delete",
        operation_description="Удалить продукт.",
        operation_summary="Удаление продукта",
        tags=["Продукт"],
        responses={
            204: openapi.Response(description="No Content - Продукт успешно удален."),
            404: openapi.Response(description="Not Found - Продукт не найден"),
        },
    )
    @action(detail=True, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404 as ex:
            log_warning(self, ex)
            return Response(
                {"message": "Продукт не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )