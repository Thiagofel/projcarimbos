from django.contrib import admin
from .models import Cliente, Carimbo

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'format_data_nascimento', 'login', 'senha_login')

    def format_data_nascimento(self, obj):
            return obj.data_nascimento.strftime('%d/%m/%Y')
    
    format_data_nascimento.short_description = 'data_nascimento'  # Nome da coluna no Django Admin
    
class CarimboAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carimbo')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carimbo, CarimboAdmin)