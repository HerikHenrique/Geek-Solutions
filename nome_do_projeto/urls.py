from django.contrib import admin
from django.urls import path, include
from todos.views import home, page1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),  # <- adicione essa linha (ajuste 'todos' se o nome do seu app for outro)
    path('page1/', page1), 
]

