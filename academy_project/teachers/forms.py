from django import forms
from .models import Note, Member, Task

class ContactForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=254)
    note = forms.CharField(max_length=5000)
    class Meta:
        model = Note
        fields = ('email', 'subject', 'note')

class AddMemberForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Jan'}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Novak'}))
    class Meta:
        model = Member
        fields = ('first_name', 'last_name')

class AddTaskForm(forms.ModelForm):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    due = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    assigned = forms.ModelChoiceField(queryset=Member.objects.all())
    class Meta:
        model = Task
        fields = ('name', 'description', 'assigned', 'due')

