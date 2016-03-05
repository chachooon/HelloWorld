
from django.conf.urls import url
from django.contrib import admin

from blog import views as blog_views


urlpatterns = [
    url(r'^$', blog_views.list_posts),
    url(r'^post/create/$', blog_views.create_post, name='create_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', blog_views.edit_post, name='edit_post'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', blog_views.delete_post, name='delete_post'), 
    url(r'^post/(?P<pk>[0-9]+)/$', blog_views.view_post, name='view_post'),
    #[]+한자리이상의 숫자 정규표현식 ?P<>키워드인자값
    url(r'^admin/', admin.site.urls),
]
