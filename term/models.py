from django.db import models


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
    slug = models.SlugField()
    gender = models.CharField(
        max_length=1, choices=_Gender.CHOICES, blank=True)
    wordClass = models.CharField(
        max_length=1, choices=_WordClass.CHOICES, blank=True)
    
    def __str__(self):
        return self.slug

class Pali(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    pali = models.CharField(max_length=100)

class _RootLang:
    PL = 'pl'
    SKR = 'skr'
    CHOICES = (
        (PL, 'paali'),
        (SKR, 'sanskrit'),
    )

class Meaning(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    root = models.CharField(max_length=100, blank=True)
    rootLang = models.CharField(
        max_length=1, choices=_RootLang.CHOICES, blank=True)
    rootDescription = models.CharField(max_length=100, blank=True)
    expl = models.TextField(blank=True)
    further = models.TextField(blank=True)


class Est(models.Model):
    term = models.ForeignKey(Meaning, on_delete=models.CASCADE)
    est = models.CharField(max_length=100)


class Eng(models.Model):
    term = models.ForeignKey(Meaning, on_delete=models.CASCADE)
    eng = models.CharField(max_length=100)


class Example(models.Model):
    term = models.ForeignKey(Meaning, on_delete=models.CASCADE)
    original = models.TextField()
    translation = models.TextField()


class Comment(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class TranslatorsChat(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
