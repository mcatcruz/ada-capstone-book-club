from django.contrib import admin
from .models import Member, Group, Discussion, Message

# Register your models here.
class AdaBookClubAdmin(admin.ModelAdmin):
  list = ('Member', 'Group', 'Discussion', 'Message')

admin.site.register(Member, AdaBookClubAdmin)
admin.site.register(Group, AdaBookClubAdmin)
admin.site.register(Discussion, AdaBookClubAdmin)
admin.site.register(Message, AdaBookClubAdmin)
# admin.site.register(Book, AdaBookClubAdmin)
