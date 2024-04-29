from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #Function Based Views
    # path('', views.index, name='index'),
    # path('bugs/', views.bugs_list, name='bugs_list'),
    # path('bugs/<int:bug_id>', views.bug_detail, name='bug_detail'),
    # path('bugs/add/', views.add_bug_report, name='add_bug_report'),
    # path('bugs/<int:bug_id>/update/', views.update_bug_report, name='update_bug_report'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bug_report, name='delete_bug_report'),
    # path('features/', views.features_list, name='features_list'),
    # path('features/<int:feature_id>', views.feature_detail, name='feature_detail'),
    # path('features/add/', views.add_feature_request, name='add_feature_request'),
    # path('features/<int:feature_id>/update/', views.update_feature_request, name='update_feature_request'),
    # path('features/<int:feature_id>/delete/', views.delete_feature_request, name='delete_feature_request'),

    #Class Based Views
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('bugs/add/', views.BugCreateView.as_view(), name='add_bug_report'),
    path('bugs/<int:bug_id>', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug_report'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug_report'),
    path('features/', views.FeaturesListView.as_view(), name='features_list'),
    path('features/add/', views.FeatureCreateView.as_view(), name='add_feature_request'),
    path('features/<int:feature_id>', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature_request'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature_request'),
]