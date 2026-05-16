from django.contrib import admin
from .models import Books
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date') # Shows columns for these fields
    search_fields = ('title',) # Django will now search through book titles!
    list_filter = ('publication_date',) # This adds the sidebar [cite: 179]
    date_hierarchy = 'publication_date' # Top navigation bar [cite: 182, 188]
admin.site.register(Books, BookAdmin)