from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from django.views import generic as views

from online_library.library.forms import CreateProfileForm, BookForm, ProfileDeleteForm
from online_library.library.models import Profile, Book


class NavMixin(object):
    def get_context_data(self, **kwargs):
        context = super(NavMixin, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        return context


class IndexView(views.CreateView):
    form_class = CreateProfileForm
    model = Profile
    template_name = 'home-no-profile.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class DashboardView(NavMixin, views.ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'home-with-profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     profile = Profile.objects.all()
    #     context['profile'] = profile
    #     return context


class AddBookView(NavMixin, views.CreateView):
    context_object_name = 'books'
    model = Book
    fields = '__all__'
    template_name = 'add-book.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Title'
            }
        )
        form.fields['picture'].widget = forms.URLInput(
            attrs={
                'placeholder': 'Picture'
            }
        )
        form.fields['type'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Type'
            }
        )
        form.fields['description'].widget = forms.Textarea(
            attrs={
                'placeholder': 'Description'
            }
        )
        return form

    def get_success_url(self):
        return reverse_lazy('dashboard')


class BookDetailView(NavMixin, views.DetailView):
    model = Book
    template_name = 'book-details.html'


class BookEditView(NavMixin, views.UpdateView):
    context_object_name = 'books'
    model = Book
    fields = '__all__'
    template_name = 'edit-book.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class BookDeleteView(NavMixin, views.DeleteView):
    model = Book
    template_name = 'delete-book.html'

    def get_context_data(self, **kwargs):
        context = super(BookDeleteView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            form = BookForm(instance=self.object)
        else:
            form = BookForm(self.request.POST)
            if form.is_valid():
                form.save()
        context['form'] = form
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard')


class ProfileView(NavMixin, views.ListView):
    model = Profile
    template_name = 'profile.html'


class EditProfileView(NavMixin, views.UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class DeleteProfileView(NavMixin, views.DeleteView):
    model = Profile
    template_name = 'delete-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            form = ProfileDeleteForm(instance=self.object)

        else:
            form = ProfileDeleteForm(self.request.POST)
            if form.is_valid():
                form.save()

        context['form'] = form
        return context

    def get_success_url(self):
        return reverse_lazy('index')





