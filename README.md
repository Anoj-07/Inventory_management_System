# Inventory Management System

Welcome to the **Inventory Management System** project!  
This Django RESTful API helps you efficiently manage products, departments, vendors, purchases, ratings, groups, and more for any business or organization.

> **Project by Anoj-07 | Mindrisers Projects**

---

## 🚀 Features

- Product, Vendor, Department, and Customer management
- Ratings, Purchases, and Sales tracking
- Authentication (Register/Login)
- AI-powered product description generation
- Insights: Best selling, most purchased, and top-rated products
- User Groups management for role-based access or categorization

---

## 🛠️ Technology Stack

- **Backend:** Python (Django, Django REST Framework)
- **Database:** SQLite (default, configurable)
- **Auth:** Token-based authentication

---

## 📚 API Endpoints

### Authentication

| Endpoint     | Method | Description      |
|--------------|--------|-----------------|
| `/register/` | POST   | Register user   |
| `/login/`    | POST   | User login      |

### Product Types

| Endpoint                      | Method              | Description           |
|-------------------------------|---------------------|-----------------------|
| `/product/types/`             | GET, POST           | List & Add types      |
| `/product/types/<int:pk>/`    | GET, PUT, DELETE    | Retrieve, Update, Delete type |

### Departments

| Endpoint                          | Method                     | Description                |
|------------------------------------|----------------------------|----------------------------|
| `/department/types/`               | GET, POST                  | List & Add department types|
| `/department/types/<int:pk>`       | GET, PUT, DELETE, PATCH    | Retrieve, Update, Delete, Partial Update |

### Vendors

| Endpoint                  | Method                     | Description                |
|---------------------------|----------------------------|----------------------------|
| `/vendor/`                | GET, POST                  | List & Add vendors         |
| `/vendor/<int:pk>/`       | GET, PUT, DELETE, PATCH    | Retrieve, Update, Delete, Partial Update |

### Products

| Endpoint                        | Method                     | Description                         |
|----------------------------------|----------------------------|-------------------------------------|
| `/product/`                     | GET, POST                  | List & Add products                 |
| `/product/<int:pk>/`            | GET, PUT, DELETE, PATCH    | Retrieve, Update, Delete, Partial Update |
| `/best/selling/product/`        | GET                        | Get best selling product            |
| `/most/purchased/products/`     | GET                        | Get most purchased products         |
| `/top/rated/products/`          | GET                        | Get top rated products              |
| `/generate-ai/`                 | POST                       | Generate product description with AI|

### Sales & Purchases

| Endpoint                  | Method                     | Description                         |
|---------------------------|----------------------------|-------------------------------------|
| `/sell/`                  | GET, POST                  | List & Record sales                 |
| `/sell/<int:pk>/`         | GET, PUT, DELETE, PATCH    | Retrieve, Update, Delete, Partial Update |
| `/purchase/`              | GET, POST                  | List & Record purchases             |
| `/purchase/<int:pk>/`     | GET, PUT, DELETE, PATCH    | Retrieve, Update, Delete, Partial Update |

### Ratings

| Endpoint                  | Method                     | Description                         |
|---------------------------|----------------------------|-------------------------------------|
| `/rating/`                | GET, POST                  | List & Add ratings                  |
| `/rating/<int:pk>/`       | GET, PUT, DELETE, PATCH    | Retrieve, Update, Delete, Partial Update |

### Groups

| Endpoint     | Method | Description        |
|--------------|--------|-------------------|
| `/groups/`   | GET    | List all groups   |

---

## ⚡ Quickstart

1. **Clone the repo**
   ```bash
   git clone https://github.com/Anoj-07/Inventory_management_System.git
   cd Inventory_management_System
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run migrations**
   ```bash
   python manage.py migrate
   ```
4. **Start the server**
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication

- All API endpoints require Token Authentication.  
- Obtain your token through the `/login/` endpoint after registering.

---

## 📖 Documentation & Notes

- All endpoints follow REST principles.
- Example requests and serializers are available in `/base/views.py` and `/base/serializers.py`.
- The AI-powered endpoint `/generate-ai/` can auto-generate product descriptions if not provided.
- Product analytics endpoints include `/best/selling/product/`, `/most/purchased/products/`, and `/top/rated/products/`.
- All main resources (Product, Vendor, Department, etc.) support standard CRUD operations.
- The `/groups/` endpoint allows listing all available user groups.
- Responses are JSON-formatted and use standard HTTP status codes.
- The project uses Django REST Framework's permission and authentication classes by default.

---

## 👤 Author

**Anoj-07**  
_Mindrisers Projects_

---

## 🌟 Contributing

Feel free to fork this repository and submit pull requests!  
For issues or feature requests, please open a [GitHub Issue](https://github.com/Anoj-07/Inventory_management_System/issues).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
