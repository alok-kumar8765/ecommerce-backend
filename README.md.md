# 🛒 E-Commerce Backend System

An enterprise-grade, lightweight E-Commerce Backend REST API built with **Python**, **FastAPI**, and **SQL** architecture concepts. Designed to handle core e-commerce workflows like product management, user profiles, shopping carts, order creation, and payment tracking.

---


[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![DeepFace](https://img.shields.io/badge/DeepFace-0.0.80%2B-red.svg?style=for-the-badge&logo=tensorflow&logoColor=white)](https://github.com/serengil/deepface)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 🚀 Key Features

* **Product Management (CRUD):** Add, view, and manage store inventories.
* **User & Order Management:** Handle customer profiles and track order lifecycles.
* **Shopping Cart Functionality:** Manage items added to customer carts prior to checkout.
* **Payment Status Tracking:** Track order payment states (`Pending`, `Completed`, `Failed`).
* **Interactive API Documentation:** Automatically generated Swagger UI & Redoc endpoints for live testing.

---

## 🛠️ Tech Stack

* **Core Language:** Python 3.9+
* **Framework:** FastAPI
* **Data Validation:** Pydantic v2
* **Server:** Uvicorn (ASGI)
* **Database Integration (Planned):** MySQL / SQLAlchemy

---

## 📂 Project Structure

```text
ecommerce_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── products.py
│   │   ├── users.py
│   │   ├── orders.py
│   │   ├── cart.py
│   │   └── payments.py
│   └── models/
│       ├── __init__.py
│       └── database.py
│
└── requirements.txt
```

---

## ⚙️ Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/alok-kumar8765/ecommerce-backend.git
cd ecommerce_backend
```

### 2. Create and Activate a Virtual Environment
* **Windows:**
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 4. Run the Application
Start the development server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

---

## 📖 Interactive API Testing (Swagger UI)

Once the server is running, open your browser and navigate to:
* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Alternative:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can interact directly with endpoints like `POST /products/`, `GET /users/`, and `POST /cart/` right from your browser.

---

## 💡 Future Improvements
* [ ] Integrate MySQL database via SQLAlchemy ORM.
* [ ] Implement JWT-based User Authentication and Authorization.
* [ ] Add unit testing using `pytest`.

---


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project Repository.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git checkout -b feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📜 License & Acknowledgments

This project is open-source and released under the **MIT License**.

**Special Thanks to:**
- [DeepFace Library](https://github.com/serengil/deepface) by Sefik Ilkin Serengil.
- [Streamlit Framework](https://streamlit.io/) for seamless Python web app deployments.
- [OpenCV Community](https://opencv.org/) for real-time computer vision utilities.