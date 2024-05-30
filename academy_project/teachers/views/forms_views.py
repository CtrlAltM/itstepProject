from django.shortcuts import render, redirect
from ..forms import ContactForm

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            note = form.cleaned_data['note']
            print("HERE: ", note)

            return redirect("profile")

    else:
        form = ContactForm()

    return render(request, "contact_form.html", {"form": form})


