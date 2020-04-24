from accounts.forms import UserCreationForm, UserChangeForm
from accounts.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	list_display = ('username', 'name', 'email', 'is_active')
	list_filter = ('username', 'name', 'email', 'is_active')
	fieldsets = (
		(None, {'fields': ('name', 'username', 'email', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_active')})
	)
	search_fields = ('username',)
	ordering = ('username',)


admin.site.register(User, UserAdmin)

