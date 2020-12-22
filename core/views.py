from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages

from .forms import CommentForm

from .models import Thread, Comment

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))


def home(request):
    home_threads = Thread.objects.filter(show_in_home=True)
    comments = Thread.objects.filter(comments=Thread)


    context = {
        'home_threads': home_threads,
        'threads': threads,
        'comments': comments
    }
    return render(request, 'site/home.html', context)


class ThreadListView(ListView):
    model = Thread
    template_name = 'site/home.html'
    context_object_name = 'threads'
    ordering = ['-date_posted']
    paginate_by = 5


class ThreadCreateView(CreateView):
    model = Thread
    fields = ('title', 'content', 'date_posted', 'last_modified', 'thread_author', 'show_in_home')
    def form_valid(self, form):
        #form.instance.thread_author = self.request.user
        slug = form.instance.title.translate({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_"}).replace(" ", "+")
        slug = slug[:15]
        if slug[-1] == "+":
            form.instance.slug = slug[:-1]   
        else:
            form.instance.slug = slug    
        if Thread.objects.filter(slug=slug).exists():
            form.instance.slug = slug[:15] + get_random_string(3)
        return super().form_valid(form)

        #if form.instance.auth_key == settings.REACT_SECRET_KEY:
        #    form.instance.auth_key = 'no secret key for u bud :)'
        #    return super().form_valid(form)


        #else:
        #    json_error = "{'error': 'unauthorized'}"
        #    return HttpResponse(json_error)

#class ThreadDetailView(DetailView):
#    model = Thread

class ThreadUpdateView(UpdateView):
    model = Thread
    fields = ['title', 'content', 'show_in_home', 'auth_key']

    def form_valid(self, form):
        form.instance.thread_author = self.request.user
        #if form.instance.auth_key == settings.REACT_SECRET_KEY:
        #    form.instance.auth_key = 'no secret key for u bud :)'
        #    return super().form_valid(form)
        #else:
        #    json_error = "{'error': 'unauthorized'}"
        #    return HttpResponse(json_error)

    #def test_func(self):
    #    thread = self.get_object()
    #    if self.request.user == thread.author:
    #        return True
    #    return False


def DeleteThread(request, pk):
    model = Thread
    field = 'auth_key'

    if request.method == "POST":
        if request.POST.get('auth_key') == settings.REACT_SECRET_KEY:
            #auth_key = 'no secret key for u bud :)'
            query = Thread.objects.get(pk=pk)
            query.delete()
            return redirect('home') and HttpResponse("{'message': 'success'}")
        else:
            json_error = "{'error': 'unauthorized'}"
            return HttpResponse(json_error)

    return render(request, "core/thread_confirm_delete.html")

#class UserThreadListView(ListView):
#    model = Thread
#    template_name = 'site/user_threads.html'
#    context_object_name = 'threads'
#    ordering = ['-date_posted']
#    paginate_by = 3


    #def get_queryset(self):
    #    user = get_object_or_404(User, username=self.kwargs.get('username'))
    #    return Thread.objects.filter(author=user).order_by('-date_posted')

# Comments

class CommentCreateView(CreateView):
    model = Comment
    fields = ('content', 'date_posted', 'last_modified', 'comment_author', 'thread', 'active')


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('content', 'date_posted', 'last_modified', 'comment_author', 'thread', 'active')



def DeleteComment(request, pk):
    model = Comment
    field = 'pk'

    if request.method == "POST":
        pk = request.POST.get('pk')
        query = Comment.objects.get(pk=pk)
        query.delete()
        return redirect('home') and HttpResponse("{'message': 'success'}")
    else:
        return HttpResponse("{'error': 'invalid_method'}")    

    return render(request, "core/thread_confirm_delete.html")

