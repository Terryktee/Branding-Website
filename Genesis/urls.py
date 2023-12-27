from django.urls import path
from .views import ProductIndexView , ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name="Genesis"

urlpatterns = [
    path('',ProductIndexView.as_view(),name='index'),
    path('<int:pk>/',ProductDetailView.as_view(), name = 'product_view'),  
]
# Add the following line at the end of the file
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
