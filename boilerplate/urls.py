from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Boilerplate Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Boilerplate"