from django.contrib import admin
from .models import Position, Sale, CSV
# Register your models here.
# Making a trivial edit to try to trigger sonarqube

admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)
