from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from jobs.models import Category
from .forms import CategoryForm, JobForm, ApplicationForm
from .models import Category, Job, Application
from . import utils
from django.utils.text import slugify
from uuid import uuid4
from django.contrib.auth.decorators import login_required


class Homepage(TemplateView):
    ctx = {}
    template_name = 'jobs/homepage.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        data['opennings'] = Job.objects.all()
        return data


@user_passes_test(utils.is_superadmin)
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:homepage')  # Replace with the name of the URL for your category list or success page
    else:
        form = CategoryForm()
    
    return render(request, 'jobs/create_cateory.html', {'form': form})



@user_passes_test(utils.is_superadmin)
def job_add_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job created')
            return redirect('jobs:homepage')  # Replace with the name of the URL for your category list or success page
        else:
            messages.error(request, str(form.errors))
    else:
        form = JobForm()
    
    return render(request, 'jobs/add_job.html', {'form': form})


def view_job_detail(request, pk):
    job = get_object_or_404(Job, id=pk)
    applications = job.application_set.all()
    return render(request, 'jobs/job_detail.html', {'job': job, 'applications': applications})


@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, id=pk)

    if request.method == 'POST':
        # Create a form instance with the POST data and current user
        print(request.POST)
        form = ApplicationForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            # If the form is valid, save the application and redirect to a success page
            form.save()
            messages.success(request, 'Applied Successfully')
            return redirect('jobs:homepage')  # Redirect to the job list or another page after successful application
        else:
            # If the form is not valid, just render it again with errors
            return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})
    else:
        # If the request is GET, just render the form
        form = ApplicationForm(user=request.user)
        return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})