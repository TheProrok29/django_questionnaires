from django.shortcuts import render, HttpResponseRedirect
from .models import Survey
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
                request, 'Ankieta została utworzona, możesz przystąpić do tworzenia pytań')
            return HttpResponseRedirect(reverse('survey',
                                                kwargs={
                                                    'survey_id': new_survey.id
                                                }))
    messages.error(request, 'Niepoprawne wywołanie trasy')
    return HttpResponseRedirect(reverse('surveys'))
