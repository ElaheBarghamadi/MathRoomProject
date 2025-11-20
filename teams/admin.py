from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Team, Member


class MemberInline(admin.TabularInline):
    model = Member
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MemberInline]
