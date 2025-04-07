from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils import translation
from django.shortcuts import redirect

from exsam2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exsam2.urls')),
    path('users/', include('users.urls')),
    path('change-language/<str:lang_code>/', views.change_language, name='change_language'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# views.py

def change_language(request, lang_code):
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))
