from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from myapp.forms import CreateForm, EditForm, CreateRoadMap, AnotherCreateForm
from django.views.decorators.csrf import csrf_exempt
from .models import Task, RoadMap


@csrf_exempt
def show_tasks(request):
    tasks = Task.objects.all()
    ctx = {'titles': tasks}
    return render_to_response('tasks.html', ctx)


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        instance = get_object_or_404(RoadMap, rd_id=request.POST.get('road_map'))
        a = Task(title=request.POST.get('title'),
                 estimate=request.POST.get('estimate'),
                 road_map=instance)
        a.save()
        return HttpResponseRedirect('/tasks/')
    form = CreateForm()
    return render_to_response('form1.html', {'form': form})


@csrf_exempt
def edit_task(request, context):
    instance = get_object_or_404(Task, my_id=context)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks/')
    else:
        form = EditForm(instance=instance)
    return render_to_response('form2.html', {'form': form})


@csrf_exempt
def delete_task(request, context):
    get_object_or_404(Task, my_id=context).delete()
    return start(request)

@csrf_exempt
def start(request):
    return render_to_response('start_page.html')


@csrf_exempt
def create_roadmap(request):
    if request.method == 'POST':
        a = RoadMap(rd_id=request.POST.get('rd_id'), name=request.POST.get('name'))
        a.save()
        return HttpResponseRedirect('/start_page/')
    form = CreateRoadMap()
    return render_to_response('create_roadmap.html', {'form': form})


@csrf_exempt
def delete_roadmap(request, context):
    get_object_or_404(RoadMap, rd_id=context).delete()
    return start(request)

@csrf_exempt
def roadmaps(request):
    roads = RoadMap.objects.all()
    ctx = {'roads': roads}
    return render_to_response('roadmaps.html', ctx)

@csrf_exempt
def roadmap(request, context):
    tasks = Task.objects.filter(road_map=context)
    ctx = {'titles': tasks,'context': context}
    return render_to_response('tasks_in_roadmap.html', ctx)

@csrf_exempt
def add_to_roadmap(request, context):

    if request.method == 'POST':
        a = Task(title=request.POST.get('title'),
                 estimate=request.POST.get('estimate'),
                 road_map_id=str(context)
                 )
        a.save()
        return roadmap(request, context)
    form = AnotherCreateForm()
    return render_to_response('form1.html', {'form': form, 'context': context})
