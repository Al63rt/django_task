from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BugReport, FeatureRequest
from django.shortcuts import render


#Function_Based_Views

def index(request):
    return render(request, 'quality_control/index.html')

# def bugs_list(request):
#     bugs = BugReport.objects.all()
#     return render(request, 'quality_control/bugs_list.html', {'bugs': bugs})

# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     return render(request, 'quality_control/bug_detail.html', {'bug': bug})

# def features_list(request):
#     features = FeatureRequest.objects.all()
#     return render(request, 'quality_control/features_list.html', {'features': features})

# def feature_detail(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, id=feature_id)
#     return render(request, 'quality_control/feature_detail.html', {'feature': feature})

#Class_Based_Views

class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'
    context_object_name = 'bugs'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

class FeaturesListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'
    context_object_name = 'features'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'