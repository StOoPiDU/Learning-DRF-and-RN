from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FGFPostViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'fgfposts', FGFPostViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]