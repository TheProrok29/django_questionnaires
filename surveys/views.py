from django.shortcuts import render, HttpResponseRedirect
from .models import Survey, Questions, Answers
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse
from django.contrib import messages


@login_required
def surveys(request):
    kwargs = {}
    kwargs['surveys'] = Survey.objects.filter(user=request.user)
    return render(request, 'surveys.html', kwargs)


@login_required
def create(request):
    if request.method == 'GET':
        kwargs = {}
        kwargs['survey_creation_form'] = forms.SurveyCreationForm(
            prefix='survey_creation_form')
        return render(request, 'create.html', kwargs)
    elif request.method == 'POST':
        form = forms.SurveyCreationForm(data=request.POST,
                                        prefix='survey_creation_form')

        if form.is_valid():
            new_survey = form.save(commit=False)
            new_survey.user = request.user
            new_survey.save()

            messages.success(
                request, 'Ankieta została utworzona, możesz przystąpić do tworzenia pytań.')
            return HttpResponseRedirect(reverse('survey',
                                                kwargs={
                                                    'survey_id': new_survey.id
                                                }))
    messages.error(request, 'Niepoprawne wywołanie trasy.')
    return HttpResponseRedirect(reverse('surveys'))


@login_required
def survey(request, survey_id):
    try:
        user_survey = Survey.objects.get(id=survey_id)

        if request.method == 'GET':
            kwargs = {}
            kwargs['survey'] = user_survey
            kwargs['questions'] = Questions.objects.filter(survey=user_survey)
            kwargs['survey_edit_form'] = forms.SurveyCreationForm(prefix='survey_creation_form',
                                                                  instance=user_survey)

            return render(request, 'survey.html', kwargs)
        elif request.method == 'POST':
            form = forms.SurveyCreationForm(data=request.POST,
                                            prefix='survey_creation_form',
                                            instance=user_survey)

            if form.is_valid():
                form.save()
                messages.success(request, 'Dane ankiety zostały zmienione.')
                return HttpResponseRedirect(reverse('survey',
                                                    kwargs={
                                                        'survey_id': survey_id
                                                    }))

    except Survey.DoesNotExist:
        messages.error(request, 'Wybrana ankieta nie istnieje.')
        return HttpResponseRedirect(reverse('surveys'))


@login_required
def delete(request, survey_id):
    try:
        user_survey = Survey.objects.get(id=survey_id)
        user_survey.delete()
        messages.success(request, 'Wybrana ankieta została usunięta.')
        return HttpResponseRedirect(reverse('surveys'))

    except Survey.DoesNotExist:
        messages.error(request, 'Wybrana ankieta nie istnieje.')
        return HttpResponseRedirect(reverse('surveys'))


@login_required
def create_question(request, survey_id):
    try:
        user_survey = Survey.objects.get(id=survey_id)

        if request.method == 'GET':
            kwargs = {}
            kwargs['survey'] = user_survey
            kwargs['question_creation_form'] = forms.QuestionCreationForm(
                prefix='question_creation_form')
            return render(request, 'question_create.html', kwargs)

        elif request.method == 'POST':
            form = forms.QuestionCreationForm(data=request.POST,
                                              prefix='question_creation_form')
            if form.is_valid():
                new_question = form.save(commit=False)
                new_question.survey = user_survey
                new_question.save()
                messages.success(request, 'Pytanie zostało utworzone.')
                return HttpResponseRedirect(reverse('survey',
                                                    kwargs={
                                                        'survey_id': user_survey.id
                                                    }))
    except Survey.DoesNotExist:
        messages.error(request, 'Wybrana ankieta nie istnieje.')
        return HttpResponseRedirect(reverse('surveys'))


@login_required
def delete_question(request, survey_id, question_id):
    try:
        survey_question = Question.objects.get(id=question_id)
        survey_question.delete()
        messages.success(request, 'Wybrane pytanie zostało usunięte.')
    except Questions.DoesNotExist:
        messages.error(request, 'Wybrane pytanie nie istnieje.')

    return HttpResponseRedirect(reverse('survey', kwargs={
        'survey_id': survey_id
    }))
