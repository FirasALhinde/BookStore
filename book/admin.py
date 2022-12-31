from django.contrib import admin
from.models import Book,Category,Auther
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display =['id','name','category','auther']
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Auther)

