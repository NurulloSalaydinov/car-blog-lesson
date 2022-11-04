from django.contrib import admin
from .models import Brand, Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Brand)
admin.site.register(Comment)

