from django.urls import path
from .views import ArticleList

urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<slug:slug>/', article_details),
    path('articles/', ArticleList.as_view())
]