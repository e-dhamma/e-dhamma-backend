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
    extra = 0
    readonly_fields = ['author', 'email', 'content']
    exclude = ['approved']


class TermAdmin(NestedModelAdmin):
    save_on_top = True
    search_fields = ('id',)
    inlines = (MeaningAdmin, CommentAdmin)
    list_display = ('pali',)
    prepopulated_fields = {'slug': ('pali',), }


admin.site.register(Term, TermAdmin)

# -----


class ApproveCommentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('term', 'content', 'approved')
    list_editable = ('approved',)
    list_filter = ('approved', 'timestamp', 'author')


admin.site.register(Comment, ApproveCommentAdmin)
