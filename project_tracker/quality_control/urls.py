from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #FBV
    # path('', views.index, name='index'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('bugs/<int:bug_id>', views.bug_detail, name='bug_detail'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('features/<int:feature_id>', views.feature_id_detail, name='feature_id_detail'),

    #CBV
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugListView.as_view(), name='bug_list'),
    path('bugs/<int:bug_id>', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('features/<int:feature_id>', views.FeatureDetailView.as_view(), name='feature_id_detail'),
]