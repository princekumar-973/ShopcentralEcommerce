# ShopCentral E-Commerce

## 🛒 Overview

ShopCentral is a full-stack e-commerce web application developed using Django that provides a seamless online shopping experience. The platform enables users to browse products, search and filter items, manage wishlists and shopping carts, and place orders through multiple payment methods.

The application is built with a modular architecture, responsive user interface, secure authentication system, and efficient product and order management features.

## 🌟 Key Highlights
- Full-Stack E-Commerce Platform
- User Authentication & Profile Management
- Product Catalog with Categories
- Advanced Search & Filtering
- Wishlist Functionality
- Session-Based Shopping Cart
- Product Variations (Size & Color)
- Multiple Payment Options
- Order Tracking & Management
- Responsive and Modern UI
- Django Admin Integration

## 🏗️ Project Architecture

The project is organized into three Django applications:

### 1. ecommerce (Main Project App)
Responsible for the overall project configuration.

**Features:**
- Global project settings
- Database configuration
- Static and media file handling
- Root URL routing
- Application integration

### 2. store (Core E-Commerce App)
Handles all shopping-related functionality.

**Features:**
- Product Management
- Category Management
- Product Variations
- Product Image Gallery
- Wishlist Management
- Shopping Cart Operations
- Order Processing
- Payment Method Handling
- Order Status Tracking

**Supported Payment Methods:**
- UPI / Google Pay
- Credit Card
- Debit Card
- Net Banking
- Cash on Delivery

### 3. accounts (User Management App)
Manages user authentication and profile information.

**Features:**
- User Registration
- User Login & Logout
- Profile Management
- Address Management
- Phone Number Storage
- Profile Avatar Upload
- Order History Tracking

## ✨ Features

**Product Browsing**
Users can:
- Browse products by category
- View detailed product information
- Explore multiple product images
- Check available sizes and stock

**Smart Search & Filtering**
- Product search functionality
- Category-based filtering
- Price range filtering
- Sorting options for better product discovery

**Shopping Cart**
- Add products to cart
- Update quantities
- Remove products
- Calculate total price dynamically

**Wishlist**
- Save favorite products
- Access wishlist anytime
- Move items from wishlist to cart

**Order Management**
- Place orders securely
- Select preferred payment method
- Track order status
- View previous orders

**User Profiles**
- Manage personal information
- Save shipping addresses
- Upload profile pictures
- Track purchase history

## 🛠️ Technology Stack

**Backend**
- Python
- Django

**Frontend**
- HTML5
- CSS3
- JavaScript

**Database**
- SQLite3

**Authentication**
- Django Authentication System

**Media Storage**
- Local Media Storage

**Development Tools**
- Git
- GitHub
- VS Code

## 📂 Project Structure

```text
ShopcentralEcommerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── media/
│   ├── avatars/
│   └── products/
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── accounts/
│   ├── registration/
│   ├── store/
│   └── base.html
├── db.sqlite3
├── seed_gallery.py
├── seed_jeans.py
└── manage.py
```

## 📸 Screenshots

*Add screenshots of the application here.*

- Home Page
- Product Listing
- Product Details
- Shopping Cart
- User Dashboard

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- pip
- Git

### Clone the Repository
```bash
git clone <repository-url>
cd ShopcentralEcommerce
```

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```
**Linux/Mac:**
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Run Development Server
```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/

## 👨‍💻 Database Schema Overview

**Product**
- Stores product information.
- *Fields:* `name`, `slug`, `description`, `price`, `original_price`, `stock`, `available`, `category`

**ProductSize**
- Stores size-specific stock information.
- *Fields:* `product`, `size`, `stock`

**ProductImage**
- Stores multiple images for products.
- *Fields:* `product`, `image`, `color_name`, `color_hex`

**Wishlist**
- Stores user wishlist items.
- *Fields:* `user`, `product`

**Order**
- Stores customer orders.
- *Fields:* `user`, `total_amount`, `payment_method`, `status`, `shipping_address`

**OrderItem**
- Stores products associated with an order.
- *Fields:* `order`, `product`, `quantity`, `price`

**Profile**
- Stores additional user information.
- *Fields:* `user`, `phone`, `address`, `city`, `pincode`, `avatar`

## 🔮 Future Enhancements
- Razorpay Integration
- Stripe Payment Gateway
- Product Reviews & Ratings
- Email Notifications
- Product Recommendations
- Coupon & Discount System
- Admin Analytics Dashboard
- Inventory Alerts
- PostgreSQL Migration
- Docker Deployment
- Cloud Hosting

## 🎯 Learning Outcomes
Through this project, I gained practical experience in:
- Django Framework Development
- Database Design & ORM
- User Authentication & Authorization
- Session Management
- E-Commerce Workflow Implementation
- CRUD Operations
- File & Media Handling
- Responsive UI Design
- Git & GitHub Version Control

## 👤 Author

**Prince Kumar**  
B.Tech Computer Science Student

**Skills:**  
Python | Django | SQL | HTML | CSS | JavaScript

**GitHub:** [Add Your GitHub Profile Link](#)  
**LinkedIn:** [Add Your LinkedIn Profile Link](#)
