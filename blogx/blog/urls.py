from django.urls import include, path
from . import views

app_name = 'blog'
urlpatterns = [
    path(
        '',
        views.PostListView.as_view(),
        name="post_list",
        ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name="post_detail",
        ),
    path(
        '<int:post_id>/share/',
        views.post_share,
        name="post_share",
        ),
    path(
        r'comments/', include('django_comments_xtd.urls'),
        ),
    ]
