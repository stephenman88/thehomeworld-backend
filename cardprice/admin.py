from django.contrib import admin
from .models import TcgPlayerCard, TcgPlayerSet, IndexCard, IndexEdition, IndexSet
# Register your models here.

admin.site.register(TcgPlayerCard)
admin.site.register(TcgPlayerSet)
admin.site.register(IndexCard)
admin.site.register(IndexEdition)
admin.site.register(IndexSet)