"""project_ideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from core import views as core_view

urlpatterns = [
                  path('', core_view.IdeaListView.as_view(), name='home'),
                  path('register/', views.RegisterView.as_view(), name='register'),
                  path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
                  path('admin/', admin.site.urls),
                  path('comments/', include('django_comments.urls')),
                  path('oauth/', include('social_django.urls', namespace='social')),

                  path('idea/', core_view.IdeaListView.as_view(), name='ideas'),
                  path('idea/create', core_view.IdeaCreate.as_view(), name='idea_add'),
                  path('idea/<int:pk>/', core_view.IdeaDetailView.as_view(), name='idea_details'),
                  path('idea/<int:pk>/update', core_view.IdeaUpdate.as_view(), name='idea_update'),
                  path('idea/<int:pk>/delete', core_view.IdeaDelete.as_view(), name='idea_delete'),
                  path('share/idea', core_view.share_via_email, name='share_via'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
