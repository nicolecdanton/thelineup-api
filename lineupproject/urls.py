from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from lineupapi.views import InstrumentView, VenueView, ProfileView, UserViewSet,GigView, GigSlotView, InviteView

router = DefaultRouter(trailing_slash=False)
router.register(r'instruments', InstrumentView, 'instrument')
router.register(r'venues', VenueView, 'venue')
router.register(r'profiles', ProfileView, 'profile')
router.register(r'gigs', GigView, 'gig')
router.register(r'gigslots', GigSlotView, 'gigslot')
router.register(r'invites', InviteView, 'invite')

urlpatterns = [
    path('', include(router.urls)),
    path('login', UserViewSet.as_view({'post': 'user_login'}), name='login'),
    path('register', UserViewSet.as_view({'post': 'register_account'}), name='register'),
]