from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from lib.views import IndexTemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("letter/", include("letter.urls")),
    path("daily/", include("daily.urls")),

    path("", IndexTemplateView.as_view(), name="index"),

    path('login', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

