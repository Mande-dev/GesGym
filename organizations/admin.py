from django.contrib import admin
from .models.gym import Gym
from .models.module import Module
from .models.gym_module import GymModule
from .models.organization import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = ("name", "is_active", "created_at")

    search_fields = ("name",)


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):

    list_display = ("name", "organization", "subdomain", "is_active")

    search_fields = ("name", "subdomain")

    list_filter = ("organization",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):

    list_display = ("code", "name")


@admin.register(GymModule)
class GymModuleAdmin(admin.ModelAdmin):

    list_display = ("gym", "module", "is_active")

    list_filter = ("module",)