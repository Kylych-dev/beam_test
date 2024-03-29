from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404

from apps.accounts.models import CustomUser
from .serializers import CustomUserSerializer
from utils.customer_logger import log_error, log_warning


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        method="get",
        operation_description="Получить список пользователей.",
        operation_summary="Получить список пользователей",
        operation_id="list_user",
        tags=["Пользователь"],
        responses={
            200: openapi.Response(description="OK - Список пользователей получено успешно."),
            401: openapi.Response(description="Ошибка аутентификации"),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
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
                {"Сообщение": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        method="post",
        operation_description="Создать пользователя.",
        operation_summary="Создать пользователя.",
        operation_id="create_user",
        tags=["Пользователь"],
        # request_body=openapi.Schema(
        #     type=openapi.TYPE_OBJECT,
        #     required=["email", "password"],
        #     properties={
        #         'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
        #         'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль пользователя'),
        #     },
        # ),
        responses={
            201: openapi.Response(description="Created - Пользователь создан успешно."),
            400: openapi.Response(description="Bad Request - Некорректный запрос"),
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
                {"Сообщение": str(ex)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        method="get",
        operation_description="Получить профиль пользователя.",
        operation_summary="Получить профиль пользователя.",
        operation_id="detail_user",
        tags=["Пользователь"],
        responses={
            200: openapi.Response(description="OK - Профиль пользователя получено."),
            401: openapi.Response(description="Ошибка аутентификации"),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
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
                {"Сообщение": "Объект не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        method="put",
        operation_description="Обновить данные пользователя.",
        operation_summary="Обновить данные пользователя.",
        operation_id="update_user",
        tags=["Пользователь"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "password"],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль пользователя'),
            },
        ),
        responses={
            200: openapi.Response(description="OK - Профиль пользователя обновлен успешно."),
            401: openapi.Response(description="Ошибка аутентификации"),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
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
                {"Сообщение": str(ex)}, 
                status
            )
        

    @swagger_auto_schema(
        method="delete",
        operation_description="Удалить пользователя.",
        operation_summary="Удаление пользователя",
        operation_id="delete_user",
        tags=["Пользователь"],
        responses={
            204: openapi.Response(description="No Content - Пользователь успешно удален."),
            404: openapi.Response(description="Not Found - Пользователь не найден"),
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
                {"Сообщение": "Пользователь не найден"}, 
                status=status.HTTP_404_NOT_FOUND
            )