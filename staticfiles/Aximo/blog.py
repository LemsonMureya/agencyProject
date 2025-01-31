from django.shortcuts import render

def blog1(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render(request, "blog/blog1.html", context)
    
def blog2(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render(request, "blog/blog2.html", context)
    
def blog3(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render(request, "blog/blog3.html", context)
    
def blog4(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'title': 'Our Blog',
        'subTitle': 'Blog',
    }
    return render(request, "blog/blog4.html", context)
    
def blogDetails(request):
    context = {
        'css':'<link rel="stylesheet" href="/static/fonts/webfonts/syne/stylesheet.css"/>',
        'breadcrumb' : 'false'
    }
    return render(request, "blog/blogDetails.html", context)
    