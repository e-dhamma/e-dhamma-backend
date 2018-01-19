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


# class Pali(models.Model):
#     term = models.ForeignKey(Term)
#     pali = models.CharField(max_length=100)


# class Meaning(models.Model):
#     term = models.ForeignKey(Term)
#     root = models.CharField(max_length=100)
#     rootLang =
#     rootDescription = models.CharField(max_length=100)
#     expl =
#     further =


# class Est(models.Model):
#     term = models.ForeignKey(Meaning)
#     est =


# class Eng(models.Model):
#     term = models.ForeignKey(Meaning)
#     eng =


# class Example(models.Model):
#     term = models.ForeignKey(Meaning)
#     original =
#     translation =


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
