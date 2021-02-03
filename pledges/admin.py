from django.contrib import admin
from .models import Pledge


class PledgeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Pledge, PledgeAdmin)
