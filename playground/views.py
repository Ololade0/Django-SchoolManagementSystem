from django.http import HttpResponse
from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet

from playground.forms import MyUserCreationForm, SchoolForm
from playground.models import User, School, Student, Message, Course, Result
from schoolproject.serializers import SchoolSerializers, StudentSerializers, CourseSerializers, ResultSerializers


def index(request):
    # school = School.objects.all()
    return render(request, 'school/index.html')


def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'school/registration.html', {'form': form})


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'school/registration.html', context)


def logoutUser(request):
    logout(request)
    return redirect('playground:home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    schools = School.objects.filter(
        Q(school_name__icontains=q) |
        Q(school_email__icontains=q)
        # Q(__icontains=q)
    )

    students = Student.objects.all()[0:5]
    school_count = schools.count()
    school_messages = Message.objects.filter(
        Q(student__message__body__icontains=q))[0:3]
      # Q(body__name__icontains=q))[0:3]

    context = {'school': schools, 'student': students,
               'school_count': school_count, 'school_messages': school_messages}
    return render(request, 'school/home.html', context)


def CoursePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    course = Course.objects.filter(course_name__icontains=q)
    return render(request, 'school/course.html', {'course': course})


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    # rooms = user.room_set.all()
    # room_messages = user.message_set.all()
    # topics = Topic.objects.all()
    # context = {'user': user, 'rooms': rooms,
    #            'room_messages': room_messages, 'topics': topics}
    return render(request, 'school/profile.html')


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializers


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializers


def createSchool(request):
    form = SchoolForm()
    if request.method == 'DELETE':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Your form is wrong")
