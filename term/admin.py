from django.contrib import admin

from .models import Term
from .models import Comment
from .models import TranslatorsChat


class CommentAdmin(admin.TabularInline):
    model = Comment
    extra = 1


class TranslatorsChatAdmin(admin.TabularInline):
    model = TranslatorsChat
    extra = 1


class TermAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('id',)
    inlines = (CommentAdmin, TranslatorsChatAdmin)


admin.site.register(Term, TermAdmin)
