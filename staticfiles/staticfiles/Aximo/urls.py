"""
URL configuration for Aximo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from Aximo import views
from Aximo import pages
from Aximo import blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

# Views routes
    path('', views.index),
    path('index7', views.index7, name='index7'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('index4', views.index4, name='index4'),
    path('index5', views.index5, name='index5'),
    path('index6', views.index6, name='index6'),
    # path('index7', views.index7, name='index7'),
    path('index8', views.index8, name='index8'),
    path('index9', views.index9, name='index9'),


# Pages routes
    path('authentication/login', pages.login, name='login'),
    path('authentication/reset-password', pages.resetPassword, name='resetPassword'),
    path('authentication/signup', pages.signup, name='signup'),
    path('projects/portfolio1', pages.portfolio1, name='portfolio1'),
    path('projects/portfolio2', pages.portfolio2, name='portfolio2'),
    path('projects/portfolio-details', pages.portfolioDetails, name='portfolioDetails'),
    path('services/service', pages.service, name='service'),
    path('services/service-details', pages.serviceDetails, name='serviceDetails'),
    path('team/team', pages.team, name='team'),
    path('team/team-details', pages.teamDetails, name='teamDetails'),
    path('utility/error', pages.error, name='error'),
    path('utility/comingsoon', pages.comingsoon, name='comingsoon'),
    path('pages/faq', pages.faq, name='faq'),
    path('pages/pricing', pages.pricing, name='pricing'),
    path('pages/testimonial', pages.testimonial, name='testimonial'),
    path('pages/about', pages.about, name='about'),
    path('pages/contact', pages.contact, name='contact'),

# Blog routes

    path('blog1', blog.blog1, name='blog1'),
    path('blog2', blog.blog2, name='blog2'),
    path('blog3', blog.blog3, name='blog3'),
    path('blog4', blog.blog4, name='blog4'),
    path('blog-details', blog.blogDetails, name='blogDetails')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

