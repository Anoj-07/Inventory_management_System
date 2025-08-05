# Inventory Management System

Welcome to the **Inventory Management System** project!  
This Django RESTful API helps you efficiently manage products, departments, vendors, purchases, ratings, and more for any business or organization.

> **Project by Anoj-07 | Mindrisers Projects**

---

## 🚀 Features

- Product, Vendor, Department, and Customer management
- Ratings, Purchases, and Sales tracking
- Authentication (Register/Login)
- AI-powered product description generation
- Insights: Best selling, most purchased, and top-rated products

---

## 🛠️ Technology Stack

- **Backend:** Python (Django, Django REST Framework)
- **Database:** SQLite (default, configurable)
- **Auth:** Token-based authentication

---

## 📚 API Endpoints

**Authentication**

| Endpoint         | Method | Description      |
|------------------|--------|-----------------|
| `/register/`     | POST   | Register user   |
| `/login/`        | POST   | User login      |

**Product Types**

| Endpoint                       | Method     | Description           |
|--------------------------------|------------|-----------------------|
| `/product/types/`              | GET, POST  | List & Add types      |
| `/product/types/<int:pk>/`     | GET, PUT, DELETE | Retrieve, Update, Delete type |

**Departments**

| Endpoint                         | Method     | Description                |
|-----------------------------------|------------|----------------------------|
| `/department/types/`              | GET, POST  | List & Add department types|
| `/department/types/<int:pk>`      | GET, PUT, DELETE, PATCH | Retrieve, Update, Delete, Partial Update |

**Vendors**

| Endpoint                 | Method     | Description                |
|--------------------------|------------|----------------------------|
| `/vendor/`               | GET, POST  | List & Add vendors         |
| `/vendor/<int:pk>/`      | GET, PUT, DELETE, PATCH | Retrieve, Update, Delete, Partial Update |

**Products**

| Endpoint                      | Method     | Description                         |
|-------------------------------|------------|-------------------------------------|
| `/product/`                   | GET, POST  | List & Add products                 |
| `/product/<int:pk>/`          | GET, PUT, DELETE, PATCH | Retrieve, Update, Delete, Partial Update |
| `/best/selling/product/`      | GET        | Get best selling product            |
| `/most/purchased/products/`   | GET        | Get most purchased products         |
| `/top/rated/products/`        | GET        | Get top rated products              |
| `/generate-ai/`               | POST       | Generate product description with AI|

**Sales & Purchases**

| Endpoint                  | Method     | Description                         |
|---------------------------|------------|-------------------------------------|
| `/sell/`                  | GET, POST  | List & Record sales                 |
| `/sell/<int:pk>/`         | GET, PUT, DELETE, PATCH | Retrieve, Update, Delete, Partial Update |
| `/purchase/`              | GET, POST  | List & Record purchases             |
| `/purchase/<int:pk>/`     | GET, PUT, DELETE, PATCH | Retrieve, Update, Delete, Partial Update |

**Ratings**

| Endpoint                  | Method     | Description                         |
|---------------------------|------------|-------------------------------------|
| `/rating/`                | GET, POST  | List & Add ratings                  |
| `/rating/<int:pk>/`       | GET, PUT, DELETE, PATCH | Retrieve, Update, Delete, Partial Update |

---

## ⚡ Quickstart

1. **Clone the repo**
   ```
   git clone https://github.com/Anoj-07/Inventory_management_System.git
   cd Inventory_management_System
   ```
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Run migrations**
   ```
   python manage.py migrate
   ```
4. **Start the server**
   ```
   python manage.py runserver
   ```

---

## 🔐 Authentication

- All API endpoints require Token Authentication.  
- Obtain your token through the `/login/` endpoint after registering.

---

## 📖 Documentation

- All endpoints follow REST principles.
- Example requests available in `/base/views.py` and `/base/serializers.py`.

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

Open-source under the [MIT License](LICENSE).

