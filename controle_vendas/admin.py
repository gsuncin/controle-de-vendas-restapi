from django.contrib import admin
from .models import Produto, Pedido, Lote, Cliente

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Lote)
admin.site.register(Cliente)
