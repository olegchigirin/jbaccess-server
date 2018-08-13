import django_tables2 as tables
from django_tables2.utils import A

from jba_core.models import Person, Role, Key, Controller, Door, Place, PersonACLEntry, RoleACLEntry
from jba_ui.common.const import ID


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


class DoorTable(tables.Table):
    id = tables.LinkColumn('ui:door details', kwargs={ID: A(ID)})

    class Meta:
        model = Door


class PlaceTable(tables.Table):
    id = tables.LinkColumn('ui:place details', kwargs={ID: A(ID)})

    class Meta:
        model = Place


class BooleanColumn(tables.BooleanColumn):

    def _get_bool_value(self, record, value, bound_column):
        if value == 1:
            value = True
        else:
            value = False
        return value


class PersonACLEntryTable(tables.Table):
    place = tables.LinkColumn('ui:place details', kwargs={ID: A('place.id')})
    type = BooleanColumn(yesno='Allow,Deny')

    class Meta:
        model = PersonACLEntry
        fields = ['place', 'type']


class RoleACLEntryTable(tables.Table):
    place = tables.LinkColumn('ui:place details', kwargs={ID: A('place.id')})
    type = BooleanColumn(yesno='Allow,Deny')

    class Meta:
        model = RoleACLEntry
        fields = ['place', 'type']
