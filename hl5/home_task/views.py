from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from home_task.forms import CreateForm, EditForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        return render_to_response('form2.html', {'form':form})
    form = CreateForm()
    return render_to_response('form1.html', {'form':form})

@csrf_exempt
def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        return render_to_response('form2.html', {'form':form})
    form = EditForm()
    return render_to_response('form2.html', {'form':form})
