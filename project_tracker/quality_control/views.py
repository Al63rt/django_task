from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BugReport, FeatureRequest

#FBV-------------------------------------------------
# def index(request):
#     bug_list_url = reverse('quality_control:bug_list')
#     feature_list_url = reverse('quality_control:feature_list')
#     html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = f"<h1>Список отчетов об ошибках</h1><ul>"
#     for bug in bugs:
#         bugs_html += f"<li><a href='{bug.id}'>{bug.title} (статус: {bug.status})</a></li>"
#     bugs_html += "</ul>"
#     return HttpResponse(bugs_html)

# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     bug_html = f"<h1>Детали бага {bug.title} (ID: {bug_id})</h1><p>Описание: {bug.description}</p>"
#     bug_html += f"<p>Статус: {bug.status}</p><p>Приоритет: {bug.priority}</p>"
#     bug_html += f"<p>Проект: {bug.project}</p><p>Задание: {bug.task}</p>"
#     return HttpResponse(bug_html)    

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     features_html = "<h1>Список запросов на улучшение</h1><ul>"
#     for feature in features:
#         features_html += f"<li><a href='{feature.id}'>{feature.title} (статус: {feature.status})</a></li>"
#     features_html += "</ul>"
#     return HttpResponse(features_html)

# def feature_id_detail(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, id=feature_id)
#     feature_html = f"<h1>Детали улучшения {feature.title} (ID: {feature_id})</h1><p>Описание: {feature.description}</p>"
#     feature_html += f"<p>Статус: {feature.status}</p><p>Приоритет: {feature.priority}</p>"
#     feature_html += f"<p>Проект: {feature.project}</p><p>Задание: {feature.task}</p>"
#     return HttpResponse(feature_html)  

#CBV-------------------------------------------------
class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)

class BugListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
        for bug in bugs:
            bugs_html += f"<li><a href='{bug.id}'>{bug.title} (статус: {bug.status})</a></li>"
        bugs_html += "</ul>"
        return HttpResponse(bugs_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        bug_html = f"<h1>Детали бага {bug.title} (ID: {bug.id})</h1><p>Описание: {bug.description}</p>"
        bug_html += f"<p>Статус: {bug.status}</p><p>Приоритет: {bug.priority}</p>"
        bug_html += f"<p>Проект: {bug.project}</p><p>Задание: {bug.task}</p>"
        return HttpResponse(bug_html)

class FeatureListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список запросов на улучшение</h1><ul>'
        for feature in features:
            features_html += f"<li><a href='{feature.id}'>{feature.title} (статус: {feature.status})</a></li>"
        features_html += "</ul>"
        return HttpResponse(features_html)
        
class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        feature_html = f"<h1>Детали запроса на улучшение {feature.title} (ID: {feature.id})</h1><p>Описание: {feature.description}</p>"
        feature_html += f"<p>Статус: {feature.status}</p><p>Приоритет: {feature.priority}</p>"
        feature_html += f"<p>Проект: {feature.project}</p><p>Задание: {feature.task}</p>"
        return HttpResponse(feature_html)
