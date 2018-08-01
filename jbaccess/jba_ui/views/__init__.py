from .ServiceViews import LoginView, LogoutView, HomeView, LogoutConfirmView, DetailRedirectView
from .PersonnelViews import PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView
from .KeyViews import KeyListView, KeyCreateView, KeyDetailView, KeyUpdateView, KeyDeleteView, KeyAttachedToPersonView, \
    AttachKeyToPersonView
from .RoleViews import RoleListView, RoleCreateView, RoleDetailView, RoleUpdateView, RoleDeleteView, \
    AttachRoleToPersonView, AttachedRolesToPersonView, DetachRoleFromPersonView
from .ControllerViews import ControllerListView, ControllerDetailsView, ControllerCreateView, ControllerUpdateView, \
    ControllerDeleteView
from .DoorViews import DoorDetailsView, DoorListView, DoorCreateView, DoorUpdateView, DoorDeleteView
from .PlacesViews import PlaceDetailsView, PlaceListView, PlaceCreateView, PlaceDeleteView, PlaceUpdateView
