from django.contrib import admin
from .models import Portfolio, PortfolioGallery, ContactLead, PortfolioCategory

class PortfolioGalleryInline(admin.TabularInline):
    model = PortfolioGallery
    extra = 3  # Number of extra images to show

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'duration', 'cost', 'category')
    inlines = [PortfolioGalleryInline]

class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at',)

admin.site.register(ContactLead, ContactLeadAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioCategory)