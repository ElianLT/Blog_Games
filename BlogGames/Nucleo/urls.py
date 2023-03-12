from django.urls import path
from .views import home, post, category, author, dates

urlpatterns = [
    # Pagina inicio
    path('', home, name='home'),

    # Pagina filtrado de categorias
    path('category/<int:category_id>', category, name='category'),

    # Pagina filtrado de autor
    path('author/<int:author_id>', author, name='author'),

    # Pagina filtrado por fecha
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    path('post/<int:post_id>', post, name='post'),
]