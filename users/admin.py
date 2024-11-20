from django.contrib import admin

from carts.admin import CarTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]

    inlines = [CarTabAdmin, OrderTabulareAdmin]
