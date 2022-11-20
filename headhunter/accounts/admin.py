from django.contrib import admin
from accounts.models import Account



class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone', 'email', 'avatar', 'birthday')
    search_fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'avatar', 'birthday')
    fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'avatar', 'birthday')


admin.site.register(Account, AccountAdmin)