from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BugReport, FeatureRequest
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BugReportForm, FeatureRequestForm
from django.urls import reverse_lazy


#Function_Based_Views

def index(request):
    return render(request, 'quality_control/index.html')

def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs': bugs})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def update_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'bug': bug})

def delete_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs_list')

def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features': features})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def update_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_request_update.html', {'form': form, 'feature': feature})

def delete_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:features_list')

#Class_Based_Views

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'
    context_object_name = 'bugs'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_list')
    context_object_name = 'bug'

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_report_update.html'
    success_url = reverse_lazy('quality_control:bugs_list')
    context_object_name = 'bug'

class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_report_confirm_delete.html'
    success_url = reverse_lazy('quality_control:bugs_list')
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

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features_list')
    context_object_name = 'feature'

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_list')
    context_object_name = 'feature'

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_request_confirm_delete.html'
    success_url = reverse_lazy('quality_control:features_list')
    context_object_name = 'feature'