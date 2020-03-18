from django.contrib import admin

from .models import District,Divisions,Category,Chondokotha

class ChondokothaAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'district_name', 'division_name']


admin.site.register(District)
admin.site.register(Divisions)
admin.site.register(Category)



admin.site.register(Chondokotha, ChondokothaAdmin)

