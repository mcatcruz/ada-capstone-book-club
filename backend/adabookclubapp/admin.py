from django.contrib import admin
from .models import Member, MemberGroups, Group, Discussion, Message, Book, BookDiscussions

# Register your models here.
class AdaBookClubAdmin(admin.ModelAdmin):
  list = ('Member', 'Group', 'Discussion', 'Message', 'Book', 'MemberGroups', 'BookDiscussions')

admin.site.register(Member, AdaBookClubAdmin)
admin.site.register(Group, AdaBookClubAdmin)
admin.site.register(Discussion, AdaBookClubAdmin)
admin.site.register(Message, AdaBookClubAdmin)
admin.site.register(Book, AdaBookClubAdmin)
admin.site.register(MemberGroups, AdaBookClubAdmin)
admin.site.register(BookDiscussions, AdaBookClubAdmin)
