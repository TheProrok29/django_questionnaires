from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AnswerNotification

@login_required
def notifications(request):
    kwargs = {}
    kwargs['notifications'] = AnswerNotification.objects.filter(user=request.user).order_by('read')
    return render(request, 'notifications.html', kwargs)

@login_required
def delete(request, notification_id):
    try:
        notification = AnswerNotification.objects.get(id=notification_id)
        notification.delete()
        messages.success(request, 'Powiadomienie zostało usuniete')
    except AnswerNotification.DoesNotExist:
        messages.error(request, 'Wybrane powiadomienie nie istnieje')
    return HttpResponseRedirect(reverse('notifications'))

@login_required
def set_as_read(request):
    AnswerNotification.objects.filter(user=request.user).update(read=True)
    messages.success(request, 'Operacja została wykonana')
    return HttpResponseRedirect(reverse('notifications'))
        