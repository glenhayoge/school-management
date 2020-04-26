from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from student_management import views
from school_management import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
