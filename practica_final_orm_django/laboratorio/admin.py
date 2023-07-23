from django.contrib import admin

from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_display_links = ['nombre']
    ordering = ['id']

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'f_fabricacion_y', 'p_costo', 'p_venta')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ['nombre', 'laboratorio']
    list_filter = ('nombre','laboratorio')

    def f_fabricacion_y(self, obj):
        return obj.f_fabricacion.year
    
    f_fabricacion_y.short_description = 'f fabricacion'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
