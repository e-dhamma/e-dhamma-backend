from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Term, Meaning, Example, Comment


class ExampleAdmin(NestedStackedInline):
    model = Example
    inlines = ()
    extra = 1


class MeaningAdmin(NestedStackedInline):
    model = Meaning
    extra = 1
    inlines = (ExampleAdmin,)


class CommentAdmin(admin.TabularInline):
    model = Comment
    inlines = ()
    extra = 1


# class TranslatorsChatAdmin(admin.TabularInline):
#     model = TranslatorsChat
#     inlines = ()
#     extra = 1


class TermAdmin(NestedModelAdmin):
    save_on_top = True
    search_fields = ('id',)
    inlines = (MeaningAdmin, CommentAdmin)


admin.site.register(Term, TermAdmin)
