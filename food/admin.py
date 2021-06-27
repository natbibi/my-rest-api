from django.contrib import admin

from .models import Out, OutImage, In
# Register your models here.

class OutImageAdmin(admin.StackedInline):
    model=OutImage

@admin.register(Out)
class OutAdmin(admin.ModelAdmin):
    inlines = [OutImageAdmin]

    class Meta:
        model=Out

@admin.register(OutImage)
class OutImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(In)