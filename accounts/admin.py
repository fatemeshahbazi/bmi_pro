from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'age']
    list_filter = ('is_admin',)
    search_fields = ('email',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        if not User.objects.filter(username=form.cleaned_data.get('username')):
            obj.set_password(make_password(form.cleaned_data.get('password')))
        obj.save()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
