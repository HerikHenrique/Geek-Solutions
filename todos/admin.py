from django.contrib import admin
from .models import Cliente

# Define the ClienteAdmin class
class ClienteAdmin(admin.ModelAdmin):
	pass

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)