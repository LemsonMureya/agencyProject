from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactLead
from django.conf import settings

def login(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'bodyClass':'bg-colorIvory',
        'header':'false',
        'footer':'false',
    }
    return render(request, "pages/authentication/login.html", context)

def resetPassword(request):
    context = {
    'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
     'bodyClass':'bg-colorIvory',
     'header':'false',
     'footer':'false'
    }
    return render(request, "pages/authentication/resetPassword.html", context)

def signup(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'bodyClass':'bg-colorIvory',
        'header':'false',
        'footer':'false',
    }
    return render(request, "pages/authentication/signUp.html", context)

def portfolio1(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Our Portfolio',
        'subTitle' : 'Portfolio',
    }
    return render(request, "pages/projects/portfolio1.html", context)

def portfolio2(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Our Portfolio',
        'subTitle' : 'Portfolio',
    }
    return render(request, "pages/projects/portfolio2.html", context)

def portfolioDetails(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Product Design',
        'subTitle' : 'Portfolio Single'
    }
    return render(request, "pages/projects/portfolioDetails.html", context)

def service(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Our Services',
        'subTitle':'Our Services',
    }
    return render(request, "pages/services/service.html", context)

def serviceDetails(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'UI/UX Design',
        'subTitle':'Service Details',
    }
    return render(request, "pages/services/serviceDetails.html", context)

def team(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Our Team',
        'subTitle':'Team',
    }
    return render(request, "pages/team/team.html", context)

def teamDetails(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Team Details',
        'subTitle':'Team Details',
    }
    return render(request, "pages/team/teamDetails.html", context)

def error(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'404',
        'subTitle':'404',
    }
    return render(request, "pages/utility/error.html", context)

def comingsoon(request):
    context = {
        'css':' <link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css" />',
        'script':' <script src="/static/js/vendors/countdown.js"></script>',
        'bodyClass':'bg-colorIvory',
        'header':'false',
        'footer':'false',
    }
    return render(request, "pages/utility/comingsoon.html", context)

def faq(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'FAQs',
        'subTitle':'FAQs',
    }
    return render(request, "pages/faq.html", context)

def pricing(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Pricing Plans',
        'subTitle':'Pricing Plans',
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, "pages/pricing.html", context)

def testimonial(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'title':'Testimonial',
        'subTitle':'Testimonial',
    }
    return render(request, "pages/testimonial.html", context)

def about(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        # 'script':'<script src="/static/js/vendors/counterup.js" type="module"></script>',
        'title':'About Us',
        'subTitle':'About Us',
    }
    return render(request, "pages/about.html", context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('contact-name')
        email = request.POST.get('contact-email')
        phone_number = request.POST.get('contact-phone', '')  # Default to an empty string if not provided
        message = request.POST.get('contact-message')

        if name and email and message: 
            # Save data to the database
            ContactLead.objects.create(
                name=name,
                email=email,
                phone_number=phone_number if phone_number else None,  # Handle empty phone numbers
                message=message
            )
            messages.success(request, "Thank you for contacting us. We'll get back to you soon!")
            return redirect('contact')  # Redirect back to contact page

        else:
            messages.error(request, "Name, Email, and Message are required. Please fill the form completely.")

    context = {
        'css': '<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script': '<script src="/static/js/vendors/menu.js"></script>',
        'title': 'Contact Us',
        'subTitle': 'Contact Us',
    }
    return render(request, "pages/contact.html", context)
