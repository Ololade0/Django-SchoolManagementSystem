from django.http import HttpResponse
from django.shortcuts import render, redirect

from playground.forms import SchoolForm
from playground.models import School


def index(request):
    school = School.objects.all()
    return render(request, 'school/index.html', context={'school': school})


def createSchool(request):
    form = SchoolForm()
    if request.method == 'DELETE':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
        else:
            return HttpResponse("Your form is wrong")


# def school_details(request, pk):
#     school = get_object_or_404(School, pk=pk)
#     return render(request, "school_detail.html", context={"school": school})


def update_school(request, id):
    id = int(id)
    try:
        updatedSchool = School.objects.get(id=id)
    except School.DoesNotExist:
        return redirect('index')
    school_form = SchoolForm(request.POST or None, instance=updatedSchool)
    if school_form.is_valid():
        school_form.save()
        return redirect('index')


def delete_school(request, id):
    id = int(id)
    try:
        deletedSchool = School.objects.get(id=id)
    except School.DoesNotExist:
        return redirect('index')
    deletedSchool.delete()
    return redirect('index')
