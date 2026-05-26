import os
import django
import sys

# Add the project root to sys.path to allow importing settings
sys.path.append('c:/Users/Admin/Desktop/Ecommerce/ecommerce')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product, ProductImage, Category

def seed():
    # Nike Running Shoe
    try:
        nike = Product.objects.get(slug='nike-running-shoe')
        ProductImage.objects.get_or_create(product=nike, image='products/gallery/nike_orange_side.png', color_name='Orange', color_hex='#ff5722')
        ProductImage.objects.get_or_create(product=nike, image='products/gallery/nike_orange_top.png', color_name='Orange', color_hex='#ff5722')
        print("Updated Nike gallery.")
    except Product.DoesNotExist:
        print("Nike product not found.")

    # Samsung Galaxy S25 Ultra
    try:
        samsung = Product.objects.get(slug='the-samsung-galaxy-s25-ultra')
        ProductImage.objects.get_or_create(product=samsung, image='products/gallery/samsung_s25_back.png', color_name='Titanium', color_hex='#4a4a4a')
        ProductImage.objects.get_or_create(product=samsung, image='products/gallery/samsung_s25_angle.png', color_name='Titanium', color_hex='#4a4a4a')
        print("Updated Samsung gallery.")
    except Product.DoesNotExist:
        print("Samsung product not found.")

    # Add more products
    try:
        cat_elec, _ = Category.objects.get_or_create(name='Electronics', slug='electronics')
        
        # Sony WH-1000XM5
        sony, created = Product.objects.get_or_create(
            slug='sony-wh-1000xm5',
            defaults={
                'category': cat_elec,
                'name': 'Sony WH-1000XM5 Noise Canceling Headphones',
                'description': 'Industry-leading noise cancellation, exceptional sound quality, and crystal-clear hands-free calling. Up to 30-hour battery life with quick charging.',
                'price': 29990.00,
                'stock': 12,
                'available': True,
                'image': 'products/sony_headphones.png'
            }
        )
        if created:
            print("Created Sony Headphones.")
            
        # Apple Watch Ultra 2
        apple, created = Product.objects.get_or_create(
            slug='apple-watch-ultra-2',
            defaults={
                'category': cat_elec,
                'name': 'Apple Watch Ultra 2',
                'description': 'The most rugged and capable Apple Watch ever. Built for the outdoors, with a titanium case, dual-frequency GPS, and up to 36 hours of battery life.',
                'price': 89900.00,
                'stock': 8,
                'available': True,
                'image': 'products/apple_watch.png'
            }
        )
        if created:
            print("Created Apple Watch.")
            
    except Exception as e:
        print(f"Error seeding products: {e}")

if __name__ == '__main__':
    seed()
