from django.urls import path

from online_library.library.views import IndexView, DashboardView, \
    AddBookView, BookDetailView, BookEditView, \
    BookDeleteView, ProfileView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add/', AddBookView.as_view(), name='add book'),
    path('details/<int:pk>/', BookDetailView.as_view(), name='book detail'),
    path('edit/<int:pk>/', BookEditView.as_view(), name='book edit'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile-delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
]