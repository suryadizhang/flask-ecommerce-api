# Flask E-commerce API

A modular Flask REST API for e-commerce operations with user management, product catalog, and order processing.

## 🚀 Features

- **User Management**: CRUD operations for users with email validation
- **Product Catalog**: Complete product management system
- **Order Processing**: Order creation and product-order relationship management
- **Data Validation**: Comprehensive input validation using Marshmallow schemas
- **Modular Architecture**: Clean, maintainable code structure

## 🏗️ Project Structure

```
flask-ecommerce-api/
├── app/
│   ├── __init__.py          # App factory
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   ├── schemas/             # Data validation schemas
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   └── order_schema.py
│   ├── routes/              # API endpoints
│   │   ├── __init__.py
│   │   ├── user_routes.py
│   │   ├── product_routes.py
│   │   └── order_routes.py
│   └── utils/               # Utility functions
├── config.py                # Configuration settings
├── run.py                   # Application runner
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- MySQL 8.0+
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/suryadizhang/flask-ecommerce-api.git
   cd flask-ecommerce-api
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
   - Create MySQL database: `CREATE DATABASE ecommerce_api;`
   - Update database credentials in `config.py`

5. **Run the application:**
   ```bash
   python run.py
   ```

The API will be available at `http://localhost:5000`

## 📋 API Endpoints

### Users
- `POST /users` - Create a new user
- `GET /users` - Get all users
- `GET /users/{id}` - Get user by ID
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Products
- `POST /products` - Create a new product
- `GET /products` - Get all products
- `GET /products/{id}` - Get product by ID
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product

### Orders
- `POST /orders` - Create a new order
- `GET /orders` - Get all orders
- `GET /orders/{id}` - Get order by ID
- `PUT /orders/{order_id}/add_product/{product_id}` - Add product to order
- `DELETE /orders/{order_id}/remove_product/{product_id}` - Remove product from order
- `GET /orders/user/{user_id}` - Get orders by user
- `GET /orders/{order_id}/products` - Get products in order
- `DELETE /orders/{id}` - Delete order

## 🧪 Testing

### Sample API Calls

**Create a user:**
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "address": "123 Main St"
  }'
```

**Create a product:**
```bash
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Laptop",
    "price": 999.99
  }'
```

**Create an order:**
```bash
curl -X POST http://localhost:5000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "order_date": "2024-01-15"
  }'
```

## 🛡️ Data Validation

The API includes comprehensive validation:
- **Email validation**: Ensures proper email format
- **Required fields**: Validates all required fields are present
- **Data types**: Ensures correct data types for all fields
- **Business rules**: Validates business logic (e.g., positive prices)

## 🏛️ Database Schema

The application uses three main entities:
- **Users**: Store customer information
- **Products**: Store product catalog
- **Orders**: Store order information with many-to-many relationship to products

## 🔧 Configuration

Update `config.py` with your database credentials:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/ecommerce_api'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Surya**
- GitHub: [@suryadizhang](https://github.com/suryadizhang)
- Email: suryadizhang86@gmail.com

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy for excellent ORM capabilities
- Marshmallow for data validation
- Coding Temple for the learning opportunity
