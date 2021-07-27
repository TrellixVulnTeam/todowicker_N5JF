from django.contrib import admin
from .models import Wicker

class WickerAdmin(admin.ModelAdmin):
    readonly_fields=('created',)

admin.site.register(Wicker,WickerAdmin)
