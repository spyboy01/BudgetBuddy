from django.urls import path
from tracker.views import index, deleteTransaction, registration, login_page, logout_page

urlpatterns = [
    path('', index, name="index"),  # Home page
    path('registration/', registration, name="registration"),  # User registration
    path('login/', login_page, name="login_page"),  # User login
    path('logout/', logout_page, name="logout_page"),  # User logout
    path('delete-transaction/<uuid:uuid>/', deleteTransaction, name="deleteTransaction")  # Delete a transaction
]
