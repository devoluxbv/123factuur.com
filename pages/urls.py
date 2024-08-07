from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('test/', TemplateView.as_view(template_name='./askAndQuestionPageSection/oneQuestion.html'),
         name='oneQuestion'),
]
