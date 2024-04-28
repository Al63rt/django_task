from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новое'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершено'),
    ]
    PRIORITY_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bug_report',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bug_report',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_request',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_request',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Review',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
