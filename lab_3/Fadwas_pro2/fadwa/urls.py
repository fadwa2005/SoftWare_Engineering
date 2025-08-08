# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
# ]
from django.contrib import admin
from django.urls import path
from . import views  # إذا كانت views في نفس المجلد مع urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
