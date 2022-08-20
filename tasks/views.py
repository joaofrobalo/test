from django.shortcuts import render

# list of tasks to achieve
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks,
    })

def add(request):
    return render(request, "tasks/add.html")