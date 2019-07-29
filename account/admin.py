from django.contrib import admin
from .models import Account
# Register your models here.
from account import forms
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    form = forms.AccountCreateForm
    add_form = forms.AccountChangeForm

    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username')


    filter_horizontal = ('groups', 'user_permissions')


    fieldsets = (
        (None, {'fields': ('email' , 'password')}),
        (('Personal info'), {'fields': ('username', 'date_joined')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups' , 'user_permissions')})
    )

    
    add_fieldsets = (
        (None , {
            'classes': ('wide',),
            'fields': ('email', 'username', ' password1', 'password2')
        }),
    )

    ordering = ('-last_login',)
