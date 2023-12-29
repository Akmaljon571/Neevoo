from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Neevoo Doc",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  path('admin', admin.site.urls),
  path('categories', include('categories.urls')),
  path('course', include('course.urls')),
  path('take', include('take.urls')),
  path('video', include('video.urls')),
  path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
