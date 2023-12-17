from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdminBase

@register(get_user_model())
class UserAdmin(UserAdminBase):

    def get_queryset(self, request):
        """do not show the superuser account on the users list"""
        qs = super().get_queryset(request)
        return qs.exclude(is_superuser=True)
    
    list_display = ['first_name','last_name','email','is_active','is_staff']
    list_editable = ['is_active','is_staff']
    readonly_fields = ['date_created','date_modified']
    list_display_links = ['first_name','last_name','email']
    list_filter= ['is_active','is_staff']
    search_fields = ['first_name','last_name','email']
    fieldsets = (
        ("Personal Info", {
            "fields": (
                'first_name',
                'last_name'
            ),
        }),
        ("Contact Info", {
            "fields": (
                'email',
            ),
        }),
        ("Privilages", {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups'
            ),
        }),
        ("Password", {
            "fields": (
                'password',
            ),
        }),
        ("Other Info", {
            "fields": (
                'date_created',
                'date_modified',
            ),
        }),
    )
    add_fieldsets  = (
        ("Personal Info", {
            "fields": (
                'first_name',
                'last_name'
            ),
        }),
        ("Contact Info", {
            "fields": (
                'email',
            ),
        }),
        ("Privilages", {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
        ("Password", {
            "fields": (
                'password1',
                'password2',
            ),
        }),
    )
    ordering = ['email']