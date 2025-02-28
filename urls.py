
from django.contrib import admin
from django.urls import include, path
from accounts import views as accounts_views  # ویوهای اپلیکیشن اکانت
from hotels import views as hotels_views     # ویوهای اپلیکیشن هتل
from django.conf import settings
from django.conf .urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
       
    path('admin/', admin.site.urls),  
    path('accounts/', include('accounts.urls')),  # مسیرهای مربوط به اپلیکیشن اکانت
    path('hotels/', include('hotels.urls')),      # مسیرهای مربوط به اپلیکیشن هتل
    path('', hotels_views.home, name='home'),  # حالا صفحه اصلی لیست هتل‌ها رو نشون 
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






if settings.DEBUG:
       urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



       urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)