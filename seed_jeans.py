import os
import django
import sys

# Add the project root to sys.path to allow importing settings
sys.path.append('c:/Users/Admin/Desktop/Ecommerce/ecommerce')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product, ProductImage, Category, ProductSize

def seed():
    try:
        clothing, _ = Category.objects.get_or_create(name='Clothing', slug='clothing')
        
        # Slim Fit Denim Jeans
        jeans, created = Product.objects.get_or_create(
            slug='slim-fit-denim-jeans',
            defaults={
                'category': clothing,
                'name': 'Slim Fit Denim Jeans',
                'description': 'Trendy denim with modern style and all-day comfort. Slim fit design, soft stretchable fabric, and strong stitching — ideal for daily wear and long-lasting use.',
                'price': 999.00,
                'original_price': 1499.00,
                'stock': 50,
                'available': True,
                'image': 'products/denim_jeans.png',
                'has_sizes': True
            }
        )
        
        # Add gallery image
        ProductImage.objects.get_or_create(product=jeans, image='products/gallery/denim_jeans_back.png', color_name='Blue', color_hex='#5c72a8')
        
        # Add sizes
        for size_val in ['28', '30', '32', '34', '36']:
            ProductSize.objects.get_or_create(product=jeans, size=size_val, defaults={'stock': 10})
            
        print("Seeded Denim Jeans.")
            
    except Exception as e:
        print(f"Error seeding: {e}")

if __name__ == '__main__':
    seed()
