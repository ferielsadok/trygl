
# from django.urls import path
# from rest_framework_nested import routers
# from . import views
# from .views import LawyerAdminDashboardViewSet, create_appointment,appointments_for_lawyer,appointments_for_client,reviews_for_lawyer,average_rating_for_lawyer
# from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

# router = routers.DefaultRouter()
# router.register(r'lawyers', views.LawyerProfileViewSet , basename='lawyer-profile')
# router.register(r'clients', views.ClientProfileViewSet, basename='client-profile')
# router.register(r'dashboard', views.LawyerAdminDashboardViewSet , basename='lawyer-admin-dashboard')

# lawyers_router = routers.NestedSimpleRouter(router, r'lawyers', lookup='lawyer')
# lawyers_router.register(r'images', views.LawyerImageViewSet, basename='lawyer-images')
# lawyers_router.register(r'documents', views.LawyerDocumentViewSet, basename='lawyer-documents')

# lawyers_dashbord = routers.NestedSimpleRouter(router, r'dashboard', lookup='lawyer')




# urlpatterns = router.urls + lawyers_router.urls + lawyers_dashbord.urls + [
#     path('lawyer-profile-search/', views.lawyer_profile_search),
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
#     path('appointments/create/', create_appointment, name='create_appointment'),
#     path('appointments/lawyer/', appointments_for_lawyer, name='appointments_for_lawyer'),
#     path('appointments/client/', appointments_for_client, name='appointments_for_client'),
#     path('lawyers/<int:lawyer_id>/reviews/', views.create_review, name='create_review'),
#     path('lawyer/<int:lawyer_id>/reviews/', reviews_for_lawyer, name='reviews_for_lawyer'),
#     path('lawyer/<int:lawyer_id>/average-rating/', average_rating_for_lawyer, name='average_rating_for_lawyer'),
#     path('auth/', include('dj_rest_auth.urls')),
    
# ]
from django.urls import path
from rest_framework_nested import routers
from . import views
from .views import LawyerAdminDashboardViewSet, create_appointment, appointments_for_lawyer, appointments_for_client, \
    reviews_for_lawyer, average_rating_for_lawyer
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# Import the necessary Swagger modules
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'lawyers', views.LawyerProfileViewSet, basename='lawyer-profile')
router.register(r'clients', views.ClientProfileViewSet, basename='client-profile')
router.register(r'dashboard', views.LawyerAdminDashboardViewSet, basename='lawyer-admin-dashboard')

lawyers_router = routers.NestedSimpleRouter(router, r'lawyers', lookup='lawyer')
lawyers_router.register(r'images', views.LawyerImageViewSet, basename='lawyer-images')
lawyers_router.register(r'documents', views.LawyerDocumentViewSet, basename='lawyer-documents')

lawyers_dashbord = routers.NestedSimpleRouter(router, r'dashboard', lookup='lawyer')

urlpatterns = [
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls + lawyers_router.urls + lawyers_dashbord.urls + [
    path('lawyer-profile-search/', views.lawyer_profile_search),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('appointments/create/', create_appointment, name='create_appointment'),
    path('appointments/lawyer/', appointments_for_lawyer, name='appointments_for_lawyer'),
    path('appointments/client/', appointments_for_client, name='appointments_for_client'),
    path('lawyers/<int:lawyer_id>/reviews/', views.create_review, name='create_review'),
    path('lawyer/<int:lawyer_id>/reviews/', reviews_for_lawyer, name='reviews_for_lawyer'),
    path('lawyer/<int:lawyer_id>/average-rating/', average_rating_for_lawyer, name='average_rating_for_lawyer'),
    path('auth/', include('dj_rest_auth.urls')),
]



