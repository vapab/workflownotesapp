"""
from django.urls import path
from notes import views as notes_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', notes_views.index, name='home'),
    path('', notes_views.index.as_view(), name='home'),
    path('api/notes/', notes_views.note_list),
    path('api/notes/<int:pk>/', notes_views.note_detail),
    path('api/notes/published/', notes_views.note_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""

#from django.urls import path
#from . import views
#from django.conf.urls.static import static
#from django.conf import settings
from django.urls import path
from notes import views as notes_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', notes_views.index, name='home'),
    path('', notes_views.index.as_view(), name='home'),
    path('api/notes/', notes_views.note_list),
    path('api/notes/<int:pk>/', notes_views.note_detail),
    path('api/notes/published/', notes_views.note_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    #path('', notes_views.LoginView.as_view(), name='login'),
    #path('create-note/', notes_views.CreateNote.as_view(), name='create_note'),
    #path('edit-note/', notes_views.EditNote.as_view(), name='edit_note'),