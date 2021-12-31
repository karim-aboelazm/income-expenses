from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header="Income Expenses Admin"
admin.site.site_title="Income Expenses Admin"
admin.site.index_title="Income Expenses Administration"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('income.urls',namespace='income')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

