from django.contrib import admin
from django.urls import path, include
from todos.views import home, page1, cliente_login, cadastrar_cliente


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),  # <- adicione essa linha (ajuste 'todos' se o nome do seu app for outro)
    path('page1/', page1),
    path('login/', cliente_login, name='cliente_login'),  # <- adicione essa linha (ajuste 'todos' se o nome do seu app for outro)
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),  # <- adicione essa linha (ajuste 'todos' se o nome do seu app for outro)
]

