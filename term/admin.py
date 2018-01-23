from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Term, Pali, Meaning, Est, Eng, Example, Comment, TranslatorsChat

class PaliAdmin(admin.TabularInline):
    model = Pali
    inlines = ()
    extra = 1
class ExampleAdmin(NestedStackedInline):
    model = Example
    inlines = ()
    extra = 1
class EngAdmin(NestedStackedInline):
    model = Eng
    extra = 1
class EstAdmin(NestedStackedInline):
    model = Est
    inlines = ()
    extra = 1

class MeaningAdmin(NestedStackedInline):
    model = Meaning
    extra = 1
    inlines = (EstAdmin, EngAdmin, ExampleAdmin)
class CommentAdmin(admin.TabularInline):
    model = Comment
    inlines = ()
    extra = 1


class TranslatorsChatAdmin(admin.TabularInline):
    model = TranslatorsChat
    inlines = ()
    extra = 1


class TermAdmin(NestedModelAdmin):
    save_on_top = True
    search_fields = ('id',)
    inlines = (PaliAdmin, MeaningAdmin, CommentAdmin, TranslatorsChatAdmin)


admin.site.register(Term, TermAdmin)
