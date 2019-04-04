from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    class Meta:
        verbose_name = 'Ankieta'
        verbose_name_plural = 'Ankiety'

    user = models.ForeignKey(
        User, verbose_name='Użytkownik', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nazwa',
                            max_length=100, null=False, blank=False)
    description = models.TextField(
        verbose_name='Opis', max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


QUESTION_TYPE_CHOICES = (
    (1, 'Otwarte'),
    (2, 'Zamknięte (TAK/NIE)')
)


class Question(models.Model):
    class Meta:
        verbose_name = 'Pytanie'
        verbose_name_plural = 'Pytania'

    survey = models.ForeignKey(
        Survey, verbose_name='Ankieta', on_delete=models.CASCADE)
    q_type = models.IntegerField(verbose_name='Rodzaj pytania',
                                 choices=QUESTION_TYPE_CHOICES)
    name = models.CharField(verbose_name='Nazwa',
                            max_length=100, null=False, blank=False)
    description = models.TextField(
        verbose_name='Opis', max_length=2000, null=True, blank=True)


class Answer(models.Model):
    class Meta:
        verbose_name = 'Odpowiedź'
        verbose_name_plural = 'Odpowiedzi'

    survey = models.ForeignKey(
        Survey, verbose_name='Ankieta', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name='Użytkownik', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Imię ankietowanego',
                                  max_length=80)
    answers = models.TextField(verbose_name='Odpowiedzi')
    created = models.DateTimeField(verbose_name='Utworzono', auto_now_add=True)
