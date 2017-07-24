from rest_framework.permissions import *


class JbAccessPermission(IsAuthenticatedOrReadOnly):
    pass
