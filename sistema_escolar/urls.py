"""sistema_escolar URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('csdesenvolvimento240187/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('funcionarios', include('apps.funcionarios.urls')),
    path('professores', include('apps.professores.urls')),
    path('materias', include('apps.materias.urls')),
    path('alunos', include('apps.alunos.urls')),
    path('turmas', include('apps.turmas.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
