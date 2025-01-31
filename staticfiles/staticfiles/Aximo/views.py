from django.shortcuts import render

def index(request):
    context={
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>'
    }
    return render(request, "home/index.html", context)

def index7(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/bricolage-grotesque/stylesheet.css"/>',
        'script':'<script src="/static/js/vendors/menu.js"></script>',
        'bodyClass':'bg-[#F8FCDD]',
        'header':'false',
        'footer':'false'
    }
    return render(request, "home/index7.html", context)

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
