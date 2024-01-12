from django.urls import path
from .views import BlogListCreateView, BlogRetrieveUpdateView

urlpatterns = [
    path("blogs/", BlogListCreateView.as_view(), name="blog-list-create"),
    path(
        "blogs/<int:pk>/", BlogRetrieveUpdateView.as_view(), name="blog-retrieve-update"
    ),
]
