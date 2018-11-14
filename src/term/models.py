from django.db import models
from django.utils.translation import gettext_lazy as _


class _Gender:
    MASCULINE = 'm'
    FEMINE = 'f'
    NEUTER = 'n'
    CHOICES = (
        (MASCULINE, 'meesssgu'),
        (FEMINE, 'naissugu'),
        (NEUTER, 'kesksugu'),
    )


class _WordClass:
    VERB = 'v'
    NOUN = 'n'
    ADJECTIVE = 'a'
    ADVERB = 'd'
    CHOICES = (
        (VERB, 'tegus'),
        (NOUN, 'nimis'),
        (ADJECTIVE, 'omds'),
        (ADVERB, 'määrs')
    )


class Term(models.Model):
    pali = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    gender = models.CharField(_('gender'),  # TODO Do others as this one
        max_length=1, choices=_Gender.CHOICES, blank=True)
    wordClass = models.CharField(
        max_length=1, choices=_WordClass.CHOICES, blank=True, verbose_name=_('word class'))
    def_in_PLS_dict = models.TextField(blank=True, verbose_name=_('definition in PLS dictionary'))

    class Meta:
        verbose_name = _('term')
        verbose_name_plural = _('terms')

    def __str__(self):
        return self.slug


class _RootLang:
    PL = 'p'
    SKR = 's'
    CHOICES = (
        (PL, 'paali'),
        (SKR, 'sanskrit'),
    )


class Meaning(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name=_('term'))
    est = models.CharField(max_length=250, verbose_name=_('in Estonian'))
    eng = models.CharField(max_length=250, blank=True, verbose_name=_('in English'))
    root = models.CharField(max_length=100, blank=True, verbose_name=_('root'))
    rootLang = models.CharField(
        max_length=1, choices=_RootLang.CHOICES, blank=True, verbose_name=_('root language'))
    rootDescription = models.CharField(max_length=100, blank=True, verbose_name=_('root description'))
    expl = models.TextField(blank=True, verbose_name=_('explanation'))
    further = models.TextField(blank=True, verbose_name=_('further explanation'))

    class Meta:
        verbose_name = _('meaning')
        verbose_name_plural = _('meanings')



class Example(models.Model):
    term_meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE)
    original = models.TextField(verbose_name=_('original'))
    translation = models.TextField(verbose_name=_('translation'))

    def __str__(self):
        return self.original + ' -> ' + self.translation
    
    class Meta:
        verbose_name = _('example')
        verbose_name_plural = _('examples')



class Comment(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, verbose_name = _('author'))
    email = models.EmailField(verbose_name = _('email'))
    content = models.TextField(verbose_name = _('content'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name = _('timestamp'))
    approved = models.BooleanField(default=True, verbose_name = _('approved'))

    def __str__(self):
        return self.author + ': ' + self.content

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')



# class TranslatorsChat(models.Model):
#     term = models.ForeignKey(Term, on_delete=models.CASCADE)
#     author = models.CharField(max_length=200)
#     email = models.EmailField()
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.author + ': ' + self.content
