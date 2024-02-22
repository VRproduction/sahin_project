from django.contrib import admin
from .models import *

MAX_OBJECTS = 1

@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

admin.site.register(Service)
admin.site.register(Project)

class PunktInline(admin.TabularInline):
    model = Punkt

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    inlines = [PunktInline, ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
class WhyChoosePunktInline(admin.TabularInline):
    model = WhyChooseUsPunkt

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):

    inlines = [WhyChoosePunktInline, ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
class ProcessPunktInline(admin.TabularInline):
    model = ProcessPunkt

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):

    inlines = [ProcessPunktInline, ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(Team)
admin.site.register(Contact)