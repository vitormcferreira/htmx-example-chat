from http import HTTPStatus

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from accounts import models as account_models

from . import forms, models


@require_http_methods(['GET'])
@login_required
def chat(request: HttpRequest) -> HttpResponse:
    chat_messages = models.Message.objects.all()
    chat_message_count = models.Message.objects.count()
    form = forms.MessageForm()
    context = {
        'chat_messages': chat_messages,
        'form': form,
        'chat_message_count': chat_message_count,
    }
    return render(
        request,
        'chats/chat.html',
        context,
    )


@require_http_methods(['POST'])
@login_required
def send_message(request: HttpRequest) -> HttpResponse:
    form = forms.MessageForm(request.POST or None)
    if form.is_valid():
        chat_message: models.Message = form.save(commit=False)
        chat_message.user = request.user
        chat_message.save()
        return render(
            request,
            'chats/fragments/send_message.html',
            {'form': form, 'chat_message': chat_message},
        )
    else:
        return HttpResponse(status=HTTPStatus.BAD_REQUEST)


@require_http_methods(['GET'])
@login_required
def get_messages(request: HttpRequest, user_pk) -> HttpResponse:
    message_pk = request.GET.get('message_pk', 0)
    user = get_object_or_404(account_models.User, pk=user_pk)

    chat_messages = models.Message.objects.order_by('pk').filter(pk__gt=message_pk)
    received_messages_count = chat_messages.filter(~Q(user=user)).count()
    chat_message_count = models.Message.objects.count()

    if received_messages_count > 0:
        messages.info(request, f'You received {received_messages_count} message(s).')

    return render(
        request,
        'chats/fragments/get_messages.html',
        {'chat_messages': chat_messages, 'chat_message_count': chat_message_count},
    )


@require_http_methods(['DELETE'])
@login_required
def remove_message(request: HttpRequest, pk) -> HttpResponse:
    # TODO
    models.Message.objects.filter(user=request.user, pk=pk).delete()
    return HttpResponse()
