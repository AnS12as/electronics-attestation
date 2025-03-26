from django.contrib import admin
from .models import NetworkNode, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city', 'country')
    actions = [clear_debt]
    readonly_fields = ('created_at',)

    def supplier_link(self, obj):
        if obj.supplier:
            return f"{obj.supplier.name} (уровень {obj.supplier.level()})"
        return "—"

    supplier_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'node')
    list_filter = ('release_date', 'node__city')
    search_fields = ('name', 'model')
