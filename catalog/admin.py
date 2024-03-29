# Register your models here.
from catalog.models import Author, Book, BookInstance, Genre
from django.contrib import admin

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name','last_name',('date_of_birth','date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
  model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_filter = ('status', 'due_back')

  fieldsets = (
    (None, {
      'fields': ('book','imprint','id')
    }),
    ('Availability', {
      'fields': ('status', 'due_back')
    })
  )
