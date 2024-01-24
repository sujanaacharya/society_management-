# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SocietyMember, Event, Announcement,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# @login_required
@login_required
def user_dashboard(request):
    user = request.user
    activity_type = request.GET.get('activity', 'general')  # Get the activity type from the URL parameter, default to 'general'

    if activity_type == 'my':
        show_my_activities = True
        user_events = Event.objects.filter(created_by__user=user)
        user_announcements = Announcement.objects.filter(posted_by__user=user)
        user_comments = Comment.objects.filter(posted_by__user=user)
    else:
        show_my_activities = False
        user_events = Announcement.objects.all()
        user_announcements = Announcement.objects.all()
        user_comments = Comment.objects.all()

    general_announcements = Announcement.objects.all()
    general_events = Event.objects.all()
    all_announcement_comments = Comment.objects.filter(related_announcement__in=general_announcements)

    pending_approval_requests = None
    if user.is_superuser:
        pending_approval_requests = SocietyMember.objects.filter(is_approved=False)

    return render(request, 'user_dashboard.html', {
        'user_events': user_events,
        'user_announcements': user_announcements,
        'user_comments': user_comments,
        'general_announcements': general_announcements,
        'general_events': general_events,
        'all_announcement_comments': all_announcement_comments,
        'pending_approval_requests': pending_approval_requests,
        'show_my_activities': show_my_activities,
    })



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create a SocietyMember instance associated with the user
            SocietyMember.objects.create(
                user=user,
                full_name=request.POST['full_name'],
                contact_number=request.POST['contact_number'],
                email=request.POST['email']
            )

            # Log the user in
            login(request, user)
            
            # Redirect to the user dashboard
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})





def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
@user_passes_test(lambda user: user.is_superuser)
def approve_user(request, member_id):
    if request.method == 'POST':
        member = SocietyMember.objects.get(pk=member_id)
        member.is_approved = True
        member.save()
        return redirect('user_dashboard')  # Redirect back to user_dashboard after approval
    else:
        member = SocietyMember.objects.get(pk=member_id)
        return render(request, 'approve_user.html', {'member': member})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')




# Views only admin can perform
@user_passes_test(lambda user: user.is_superuser)
def approve_member(request, member_id):
    if request.method == 'POST':
        member = SocietyMember.objects.get(pk=member_id)
        member.is_approved = True
        member.save()
        return redirect('admin_dashboard')  # Redirect to admin dashboard or any other page
    else:
        member = SocietyMember.objects.get(pk=member_id)
        return render(request, 'approve_member.html', {'member': member})

@user_passes_test(lambda user: user.is_superuser)
def create_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        event_date = request.POST['event_date']
        event_time = request.POST['event_time']
        created_by = SocietyMember.objects.get(user=request.user)
        event = Event.objects.create(
            title=title,
            description=description,
            event_date=event_date,
            event_time=event_time,
            created_by=created_by
        )
        return redirect('view_events')
    else:
        return render(request, 'create_event.html')

# Views authenticated users can perform
@login_required
def post_announcement(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        posted_by = SocietyMember.objects.get(user=request.user)
        
        announcement = Announcement.objects.create(
            title=title,
            content=content,
            posted_by=posted_by
        )

        return redirect('user_dashboard')  # Redirect back to user_dashboard after posting the announcement

    return redirect('user_dashboard')  # Redirect to user_dashboard even if it's a GET request

@login_required
def view_approved_announcements(request):
    approved_announcements = Announcement.objects.filter(is_approved=True)
    return render(request, 'view_approved_announcements.html', {'announcements': approved_announcements})

@login_required
def view_events(request):
    events = Event.objects.all()
    return render(request, 'view_events.html', {'events': events})




@login_required
def post_comment(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    if request.method == 'POST':
        text = request.POST['text']
        posted_by = SocietyMember.objects.get(user=request.user)

        comment = Comment.objects.create(
            text=text,
            posted_by=posted_by,
            related_announcement=announcement
        )


    # Get all the required data to pass to the user_dashboard.html template
    user_events = Event.objects.filter(created_by__user=request.user)
    user_announcements = Announcement.objects.filter(posted_by__user=request.user)
    user_comments = Comment.objects.filter(posted_by__user=request.user)
    general_announcements = Announcement.objects.all()
    general_events = Event.objects.all()
    all_announcement_comments = Comment.objects.filter(related_announcement__in=general_announcements)

    pending_approval_requests = None
    if request.user.is_superuser:
        pending_approval_requests = SocietyMember.objects.filter(is_approved=False)

    return render(request, 'user_dashboard.html', {
        'user_events': user_events,
        'user_announcements': user_announcements,
        'user_comments': user_comments,
        'general_announcements': general_announcements,
        'general_events': general_events,
        'all_announcement_comments': all_announcement_comments,
        'pending_approval_requests': pending_approval_requests,
        'show_my_activities': True,  # Assuming that the user should see their activities after posting a comment
    })
# General views accessible to all users
def home(request):
    return render(request, 'home.html')  # Render  homepage template

def about(request):
    return render(request, 'about.html')  

def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request, 'help.html')