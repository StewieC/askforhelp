from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from education.models import Article
from .models import Conversation
from .forms import ConversationMessageForm


@login_required
def new_conversation(request, item_pk):
    article = get_object_or_404(Article, pk=item_pk)

    if article.author == request.user:
        return redirect('education:index')

    conversations = Conversation.objects.filter(article=article).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(article=article)
            conversation.members.add(request.user)
            conversation.members.add(article.author)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html',{
     'form': form,
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
    })


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detail', pk=pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html',{
        'conversation': conversation,
        'form': form,
    })
