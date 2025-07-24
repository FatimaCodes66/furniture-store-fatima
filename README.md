#   Furnish-Zone – E-commerce Furniture Store (Django + MongoDB)

A student project developed using Django and MongoDB Atlas.  
This furniture store app allows users to browse, search, filter, and purchase furniture online.  
Includes cart functionality, category filters, and admin controls.

##   Project Demo Video
[Watch Demo on Google Drive](https://drive.google.com/file/d/1ZlkDs420UxZ-xbbkrb1O004vJ6JXjC-3/view?usp=sharing)


##   Features

###    Admin Panel
- Add, update, and delete furniture products.
- Manage user messages and orders.

###   User Functionality
- Register and login/logout.
- Browse all furniture products.
- Search by keyword (e.g., sofa, bed).
- Filter by category (e.g., Office, Bedroom).
- View product details.
- Add products to cart.
- Checkout placeholder available.
- Contact form to message admin.
- View image gallery.


##   Technologies Used

- **Backend**: Django 5.0.3
- **Database**: MongoDB Atlas (via Djongo)
- **Frontend**: HTML, CSS, Bootstrap, Django Templates
- **Others**: Django Admin, Humanize Filters



##    How to Run the Project Locally

###   Prerequisites
- Python 3.12 installed
- Internet connection to access MongoDB Atlas
- Git (optional)

###   Installation Steps

1. **Clone or Download the Project**:

git clone https://github.com/FatimaCodes66/furniture-store-fatima.git
cd furniture-store-fatima

2. **Install Required Packages**:
python -m pip install -r requirements.txt

3. **Run Migrations**:
py manage.py makemigrations
py manage.py migrate

4. **Run the Server**:
py manage.py runserver

5. Open your browser and go to:
http://127.0.0.1:8000/


