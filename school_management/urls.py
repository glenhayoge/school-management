from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from student_management import views
from school_management import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
