from django import forms

from online_library.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image'
                }
            )
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def __set_readonly_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class ProfileDeleteForm(CreateProfileForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def __set_readonly_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'



