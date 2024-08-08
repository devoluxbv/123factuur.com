from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('test/', TemplateView.as_view(template_name='./test.html'),
         name='test'),
    # path('news-list/', TemplateView.as_view(template_name='./news/news_list.html'),
    #      name='news-list'),
    path('', TemplateView.as_view(template_name='./home.html'),
         name='home'),
]
