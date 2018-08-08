import django_tables2 as tables
from django_tables2.utils import A

from jba_core.models import Person, Role, Key, Controller
from jba_ui.common.view_fields import ID


class PersonTable(tables.Table):
    id = tables.LinkColumn('ui:person details', kwargs={ID: A(ID)})

    class Meta:
        model = Person


class RoleTable(tables.Table):
    id = tables.LinkColumn('ui:role details', kwargs={ID: A(ID)})

    class Meta:
        model = Role


class KeyTable(tables.Table):
    id = tables.LinkColumn('ui:key details', kwargs={ID: A(ID)})

    class Meta:
        model = Key


class ControllerTable(tables.Table):
    id = tables.LinkColumn('ui:controller details', kwargs={ID: A(ID)})

    class Meta:
        model = Controller
