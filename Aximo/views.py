from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    context={
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>'
    }
    return render(request, "home/index7.html", context)

def index7(request):
    portfolios = Portfolio.objects.all()[:6]
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/bricolage-grotesque/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#F8FCDD]',
        'header':'false',
        'footer':'false',
        'portfolios': portfolios
    }
    return render(request, "home/index7.html", context)

# List all portfolio items
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, "pages/projects/portfolio1.html", {'portfolios': portfolios})

# View portfolio detail page
def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    gallery_images = portfolio.gallery_images.all()
    return render(request, "pages/projects/portfolioDetails.html", {'portfolio': portfolio, 'gallery_images': gallery_images})

def index2(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/clash-grotesk/style.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass': 'bg-[#F6F5EF]',
        'header': 'false',
        'footer': 'false'
    }
    return render(request, "home/index2.html", context)

def index3(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/familjen-grotesk/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass': 'bg-[#FEFCFB]',
        'header': '',
        'footer': 'false'
    }
    return render(request, "home/index3.html", context)

def index4(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/arimo/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/offcanvas-menu.js"></script>',
        'bodyClass':'bg-[#FFF7EA]',
        'header':'false',
        'footer':'false'
    }
    return render(request, "home/index4.html", context)

def index5(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/libre-baskerville/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#FFFCF2]',
        'header':'false',
        'footer':'false'
    }
    return render(request, "home/index5.html", context)

def index6(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/playfair-display/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-white',
        'header':'false',
        'footer':'false'
    }
    return render(request, "home/index6.html", context)

def index8(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/outfit/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#FCF9F0]',
        'header':'false',
        'footer':'false'
    }
    return render(request, "home/index8.html", context)

def index9(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/epilogue/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#FEF6E0]',
        'header':'false',
        'footer':'false'
    }
    return render(request, "home/index9.html", context)

def create_checkout_session(request, package_id):
    # Define packages manually
    packages = {
        "starter": {"name": "Starter Package", "price": 90000},  # Price in cents
        "growth": {"name": "Growth Package", "price": 200000},
        "premium": {"name": "Premium Package", "price": 400000},
    }

    package = packages.get(package_id)

    if not package:
        return JsonResponse({"error": "Invalid package selected"}, status=400)

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": package["name"]},
                        "unit_amount": package["price"],
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return JsonResponse({"id": session.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

def payment_success(request):
    return render(request, "payments/success.html", {"message": "Payment Successful!"})


def payment_cancel(request):
    return render(request, "payments/cancel.html", {"message": "Payment Cancelled."})