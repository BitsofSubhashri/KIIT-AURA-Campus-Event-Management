from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Registration
from django.contrib.auth.models import User
from .models import Feedback


def home(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/home.html', {'events': events})


@login_required
def history(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/history.html', {'registrations': registrations})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def register_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll = request.POST.get('roll_number')
        phone = request.POST.get('phone')

        # SAVE ONLY ONCE (FIXED)
        Registration.objects.create(
            user=request.user,
            event=event,
            name=name,
            email=email,
            roll_number=roll,
            phone=phone
        )

        messages.success(request, "Registration successful 🎉")

        return redirect('home')

    return render(request, 'events/register.html', {'event': event})

@login_required
def contact(request):
    return render(request, 'events/contact.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'registration/signup.html')

@login_required
def feedback(request):
    if request.method == "POST":
        rating = request.POST.get('rating')

        Feedback.objects.create(
            user=request.user,
            rating=rating
        )

        messages.success(request, "Thanks for your feedback ⭐")
        return redirect('home')

    return render(request, 'events/feedback.html')