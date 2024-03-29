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
    permission_classes = [permissions.IsAuthenticated]

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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

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
        method="get",
        operation_description="Получить информацию о продукте.",
        operation_summary="Информация о продукте",
        tags=["Продукт"],
        responses={
            200: openapi.Response(description="OK - Информация о продукте успешно получена."),
            404: openapi.Response(description="Не найдено - Продукт не найден"),
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
