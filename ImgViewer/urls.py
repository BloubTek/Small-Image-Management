from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('picture/<int:id_picture>', views.ViewPicture, name='aff_pict'),
    path('upload', views.model_form_upload, name='upload'),
    path('list', views.listing, name='listing'),
    path('keep', views.keepPicture),
    path('reject', views.rejectPicture),
    path('prev', views.prevPic),
    path('next', views.nextPic),
    path('', views.home),
    path('/home', views.home),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
