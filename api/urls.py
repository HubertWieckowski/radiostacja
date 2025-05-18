from django.urls import path
from .views import home, hit_detail, create_hit, edit_hit, delete_hit, HitListCreateView, HitDetailView

urlpatterns = [
    path('', home, name='home'),
    path('hits/new/', create_hit, name='create-hit'),  # Strona dodawania hitu (UI)
    path('hits/<slug:title_url>/', hit_detail, name='hit-detail'),
    path('hits/edit/<slug:title_url>/', edit_hit, name='edit-hit'),
    path('hits/delete/<slug:title_url>/', delete_hit, name='delete-hit'),

    path('api/v1/hits/', HitListCreateView.as_view(), name='hit-list-create'),  # API dla listy hitów
    path('api/v1/hits/<slug:title_url>/', HitDetailView.as_view(), name='hit-detail-api'),  # API dla pojedynczego hitu
]
