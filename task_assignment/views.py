from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from task_assignment.forms import ContributorForm, TaskForm
from task_assignment.models import Contributor, Task, Attendance
from django.utils import timezone
# Create your views here.

def add_contributor(request):
    if request.method == 'POST':
        form = ContributorForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContributorForm()
    else:
        form = ContributorForm()
    return render(request, 'add_contributor.html', {'form': form}) 


def contributor_list(request):
    contributors = Contributor.objects.all().values('id', 'name', 'email')
    return JsonResponse(list(contributors), safe=False)

def display_contributors(request):
    today = timezone.now().date()
    if request.method == 'POST':
        # Get all selected contributor IDs
        selected_ids = [
            int(value) for name, value in request.POST.items()
            if name.startswith('contributor_') and value.isdigit()
        ]
        
        # Create attendance records for selected contributors
        for contributor_id in selected_ids:
            Attendance.objects.create(
                contributor_id=contributor_id,
                date=today,
                status='Present'
            )
        return redirect('contributor_list')

    contributors = Contributor.objects.all()
    context = {
        'contributors': contributors,
        'date': today
    }
    return render(request, 'contributor_list.html', context)


def mark_attendance(request):
    contributors = Contributor.objects.all()
    date =timezone.now().date()
    if request.method == 'POST':
        for contributor in contributors:
            status= f'status_{contributor.id}' in request.POST and request.POST[f'status_{contributor.id}']
            status = 'Present' if status else 'Absent'
            Attendance.objects.update_or_create(
                contributor=contributor,
                date=date,
                defaults={'status': status}
            )
        return redirect('attendance_list')
    
    return render(request, 'mark_attendance.html', {'contributors': contributors, 'date': date})

    
