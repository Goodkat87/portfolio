from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name=''),
    path('back', views.back, name='back'),
    path('back/<int:id>/destroy/testimonials', views.delete_testimonials, name='destroy_testimonial'),
    path('add_testimonials/', views.add_testimonials, name='add_testimonials'),
    path('add_services/', views.add_services, name='add_services'),
    path('back/<int:id>/destroy/services', views.delete_services, name='destroy_services'),
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
    path('back/<int:id>/destroy/portfolio', views.delete_portfolio, name='destroy_portfolio'),
    path('add_skills/', views.add_skills, name='add_skills'),
    path('back/<int:id>/destroy/skills', views.delete_skills, name='destroy_skills'),
    path('update_about/<int:id>',views.update_about,name="update_about"),
    path('update_contact/<int:id>',views.update_contact,name="update_contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
