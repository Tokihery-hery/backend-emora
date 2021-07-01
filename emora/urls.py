from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>', views.UsersDetail.as_view()),
    path('products/', views.ProductsList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('users/<int:owner_id>/products/', views.ProductsListByUser.as_view()),
    path('users/<int:owner_id>/products/<int:pk>', views.ProductDetailByUser.as_view()),
    path('users/<int:owner_id>/sale/', views.CreateSaleOrder.as_view()),
    path('users/<int:owner_id>/sale/<int:pk>', views.SaleOrderDetail.as_view()),
    path('users/<int:owner_id>/purchase/', views.CreatePurchase.as_view()),
    path('users/<int:owner_id>/purchase/<int:pk>', views.PurchaseDetail.as_view()),
    path('list_user/<int:pk>', views.getListUsers, name="users-list")
    # get_list_users
]