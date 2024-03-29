from django.urls import path
from rest_framework.routers import DefaultRouter

from api.auth.views import CustomUserViewSet

from api.v1.product.views import CategoryViewSet, ProductViewSet
from api.v1.store.views import StoreViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        
        # user
        path("user/", CustomUserViewSet.as_view({"get": "list"}), name="user-list"),
        path("user/create/", CustomUserViewSet.as_view({"post": "create"}), name="user-create"),
        path("user/update/<int:pk>/", CustomUserViewSet.as_view({"put": "update"}), name="user-update"),
        path("user/delete/<int:pk>/", CustomUserViewSet.as_view({"delete": "destroy"}), name="user-delete"),


        # category
        path("category/", CategoryViewSet.as_view({"get": "list"}), name="category-list"),
        path("category/create/", CategoryViewSet.as_view({"post": "create"}), name="category-create"),
        path("category/update/<pk>/", CategoryViewSet.as_view({"put": "update"}), name="category-update"),
        path("category/delete/<pk>/", CategoryViewSet.as_view({"delete": "destroy"}), name="category-delete"),


        # product
        path("product/", ProductViewSet.as_view({"get": "list"}), name="product-list"),
        path("product/create/", ProductViewSet.as_view({"post": "create"}), name="product-create"),
        path("product/update/<pk>/", ProductViewSet.as_view({"put": "update"}), name="product-update"),
        path("product/delete/<pk>/", ProductViewSet.as_view({"delete": "destroy"}), name="product-delete"),


        # Store
        path("store/", StoreViewSet.as_view({"get": "list"}), name="store-list"),
        path("store/create/", StoreViewSet.as_view({"post": "create"}), name="store-create"),
        path("store/update/<uuid:pk>/", StoreViewSet.as_view({"put": "update"}), name="store-update"),
        path("store/delete/<uuid:pk>/", StoreViewSet.as_view({"delete": "delete"}), name="store-delete"),
    ]
)



'''


1. развернуть бэкенд на django
2. реализовать несколько CRUD, со связями - один к одному, много ко многим, один ко многим, 
    многие к одному (можно на примере пользователей или товаров)
3. реализовать веб сокеты
4. реализовать REST API, документировать с помощью swagger или любой другой инструмент
5. предоставить как результат веб страницу на которой можно кнопками проверить CRUD сущностей 
    и связи между ними, на этой же странице должна быть демонстрация привязки сокетов к CRUD 
    например при создании пользователя - всем остальным пользователям приходит уведомление с
    помощью сокетов о том, что создан новый юзер."

'''