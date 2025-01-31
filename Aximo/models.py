from django.db import models


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=255, blank=True) 
    image = models.ImageField(upload_to='portfolio_images/')
    video = models.FileField(upload_to='portfolio_videos/', blank=True, null=True) 
    client_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)  # Example: '6 months'
    cost = models.CharField(max_length=100)  # Example: '$20,000'
    description = models.TextField()
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, related_name='portfolios')

    def __str__(self):
        return self.client_name

class PortfolioGallery(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_gallery/')

    def __str__(self):
        return f"Gallery image for {self.portfolio.title}"
    
class ContactLead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class PricingPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_in_cents = models.IntegerField()
    features = models.TextField()

    def __str__(self):
        return self.name