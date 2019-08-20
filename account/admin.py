from django.contrib import admin
from .models import Account
# Register your models here.
from .forms import AccountChangeForm, AccountCreateForm


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    form = AccountChangeForm
    add_form = AccountCreateForm

    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username')

    filter_horizontal = ('groups', 'user_permissions')


    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('username', 'date_joined', 'thumbnail')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', ' password1', 'password2')
        }),
    )

    ordering = ('-last_login',)
