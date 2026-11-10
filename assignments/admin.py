from django.contrib import admin
from .models import About, SocialLink

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True  # Allow adding if no About instance exists
        return False  # Prevent adding if an About instance already exists

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)