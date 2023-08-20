from django.urls import path
from .views import views, views_resource_cat, views_need_cat, views_resource, views_nat_struct_cat

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('settings-hub/', views.settings_hub, name='settings_hub'),
    path('delete-game-mode/', views.delete_game_mode, name='delete_game_mode'),
    path('modify-game-mode/<int:game_mode_id>/', views.modify_game_mode, name='modify_game_mode'),
    path('need-category/', views_need_cat.NeedCatListView.as_view(), name='need_cat_list'),
    path('need-category/create/', views_need_cat.NeedCatCreateView.as_view(), name='need_cat_create'),
    path('need-category/<int:pk>/update/', views_need_cat.NeedCatUpdateView.as_view(), name='need_cat_update'),
    path('need-category/<int:pk>/delete/', views_need_cat.NeedCatDeleteView.as_view(), name='need_cat_delete'),
    path('resource-category/', views_resource_cat.ResourceCatListView.as_view(), name='resource_cat_list'),
    path('resource-category/create/', views_resource_cat.ResourceCatCreateView.as_view(), name='resource_cat_create'),
    path('resource-category/<int:pk>/update/', views_resource_cat.ResourceCatUpdateView.as_view(), name='resource_cat_update'),
    path('resource-category/<int:pk>/delete/', views_resource_cat.ResourceCatDeleteView.as_view(), name='resource_cat_delete'),
    path('natural-structure-category/', views_nat_struct_cat.NatStructCatListView.as_view(), name='nat_struct_cat_list'),
    path('natural-structure-category/create/', views_nat_struct_cat.NatStructCatCreateView.as_view(), name='nat_struct_cat_create'),
    path('natural-structure-category/<int:pk>/update/', views_nat_struct_cat.NatStructCatUpdateView.as_view(), name='nat_struct_cat_update'),
    path('natural-structure-category/<int:pk>/delete/', views_nat_struct_cat.NatStructCatDeleteView.as_view(), name='nat_struct_cat_delete'),
    path('resource/', views_resource.ResourceListView.as_view(), name='resource_list'),
    path('resource/create/', views_resource.ResourceCreateView.as_view(), name='resource_create'),
    path('resource/<int:pk>/update/', views_resource.ResourceUpdateView.as_view(), name='resource_update'),
    path('resource/<int:pk>/delete/', views_resource.ResourceDeleteView.as_view(), name='resource_delete'),
]
