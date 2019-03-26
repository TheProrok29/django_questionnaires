from django.shortcuts import render
from .models import Survey
from django.contrib.auth.decorators import login_required


@login_required
def surveys(request):
    kwargs = {}
    kwargs['surveys'] = Survey.objects.filter(user=request.user)
    return render(request, 'surveys.html', kwargs)
