from django.shortcuts import render, get_object_or_404

from .forms import ProjectForm, RawProjectForm

from .models import Project
# Create your views here.

#def project_create_view(request):
#    my_form = RawProjectForm()  #Create an instance of the class so as to render it out
#    if request.method == "POST":
#        my_form = RawProjectForm(request.POST)
#    if my_form.is_valid():
#        print(my_form.cleaned_data)
#    context = {
#        "form": my_form
#    }
    #print(request.POST)
#    return render(request, "project/project_create.html", context)

def project_create_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, "project/project_create.html", context)

def project_detail_view(request):
    obj = Project.objects.get(id=1)
    context = {
    'object': obj
    }
    return render(request, "project/project_detail.html", context)

def dynamic_lookup_view(request,id):
    #obj = Project.objects.get(id=id)
    obj = get_object_or_404(Project, id=id)
    context = {
        'object': obj
        }
    return render(request, "project/detail.html", context)

#dynamic url routing
#def dynamic_lookup_view(request,id):
 #   obj = Project.objects.get(id=1)
  #  context = {
   #     "object": obj
    #}
     #return render(request, "project/project_detail.html", context)

def project_delete_view(request, id):
    obj = get_object_or_404(Project, id=id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj
    }
    return (request, 'project/project_delete.html', context)

def project_list_view(request):
    queryset = Project.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'project/project_list.html', context)