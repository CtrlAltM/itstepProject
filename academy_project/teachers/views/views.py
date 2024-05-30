from django.http import HttpResponse
from django.template import loader
from ..models import Member, Task
from ..forms import AddMemberForm, AddTaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def team(request):
    members = Member.objects.all().values()
    tasks = Task.objects.all().values()

    if request.method == "POST":
        print("1")
        if 'addmember' in request.POST:
            form = AddMemberForm(request.POST)
            if form.is_valid():
                form.save()
        if 'addtask' in request.POST:
            print("2")
            form = AddTaskForm(request.POST)
            if form.is_valid():
                print("3")
                form.save()
        else: 
            form = AddMemberForm()
    else: 
        form = AddMemberForm()
    
    context = {
        "members": members,
        "tasks": tasks,
        "form": form,
    }
    return render(request, "team.html", context)

@login_required
def taskdetail(request, id):
    task = Task.objects.get(id=id)
    template = loader.get_template("detail.html")
    context = {
        "task": task,
    }
    return HttpResponse(template.render(context, request))
