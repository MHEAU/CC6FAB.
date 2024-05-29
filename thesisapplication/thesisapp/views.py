from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.views.generic.list import ListView, BaseListView
from django.views.generic.edit import UpdateView
from thesisapp.models import Thesis
from thesisapp.models import thesisapp_comments
from thesisapp.forms import ThesisForm
from thesisapp.forms import CommentForm
from django.core.paginator import Paginator
from random import randint
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

@method_decorator(login_required, name='dispatch')
class Home(LoginRequiredMixin, View):
    def get(self, request):
        random_thesis_index = randint(0, Thesis.objects.count() - 1)
        random_thesis = Thesis.objects.all()[random_thesis_index]
        random_thesis_comments = thesisapp_comments.objects.filter(theses=random_thesis)

        context = {
            'random_thesis': random_thesis,
            'random_thesis_comments': random_thesis_comments,
        }
        return render(request, 'home.html', context)

class thesis(LoginRequiredMixin, ListView):
    model = Thesis
    template_name = 'thesis.html'
    context_object_name = 'thesis'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        queryset = super().get_queryset().order_by('title')

        if search:
            queryset = queryset.filter(
                Q(callno__icontains=search) |
                Q(title__icontains=search) |
                Q(authors__icontains=search) |
                Q(adviser__icontains=search) |
                Q(abstract__icontains=search) |
                Q(sub_date__icontains=search) |
                Q(college__icontains=search) |
                Q(program__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        
        return context
    
@login_required   
def add_thesis(request):
    if request.method == "POST":
        form = ThesisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Thesis added successfully!')
            return redirect('Thesis')
        else:
            messages.error(request, 'Please complete the required fields.')
            # Render the form with error messages
            return render(request, 'thesis-add.html', {'form': form})
    else:
        form = ThesisForm()
        return render(request, 'thesis-add.html',  {'form': form})


class ThesisUpdateView(LoginRequiredMixin, UpdateView):
    model = Thesis
    form_class = ThesisForm
    context_object_name = 'thesis'
    template_name = 'thesis-edit.html'
    success_url = "/thesis"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
      messages.success(self.request, "Thesis was updated successfully!")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())
    
@login_required 
def delete_thesis(request, id):
    thesis = Thesis.objects.get(callno=id)  
    thesis.delete()
    messages.success(request, 'Thesis deleted successfully!')
    return redirect('Thesis')

@login_required 
def thesis_comments(request, theses_id):
    thesis = get_object_or_404(Thesis, callno=theses_id)
    comments = thesisapp_comments.objects.filter(theses=thesis)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thesis = thesis
            comment.theses = thesis
            comment.save()
            return redirect('Thesisapp_comments', theses_id=theses_id)
    else:
        form = CommentForm()

    context = {
        'thesis': thesis,
        'comments': comments,
        'form': form,
    }
    return render(request, 'comment.html', context)

def login(request, template_name='login.html'):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            error_message = 'Incorrect username or password'

    context = {
        'error_message': error_message,
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('login')