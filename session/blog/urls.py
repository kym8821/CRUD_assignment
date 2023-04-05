from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>', views.detail, name='detail'),
    path('blog/new', views.new, name='new'),
    path('blog/create', views.create, name='create'),
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    # edit은 특정 id에 해당하는 페이지를 편집하므로 url에 id를 껴준다.
    path('blog/update/<int:blog_id>', views.update, name='update'),
    # update는 특정 id에 해당하는 페이지를 업데이트 하므로 url에 id를 껴준다.
    path('blog/delete/<int:blog_id>', views.delete, name='delete'),
    path('blog/search', views.search, name='search'),
]
