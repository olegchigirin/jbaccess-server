import django_tables2 as tables
from django_tables2.utils import A

from jba_core.models import Person, Role, Key, Controller, Door, Place, PersonACLEntry, RoleACLEntry, \
    SimpleRecurringPattern
from jba_ui.common.column import TypeColumn
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


class PersonACLEntryTable(tables.Table):
    place = tables.LinkColumn('ui:place details', kwargs={ID: A('place.id')})
    type = TypeColumn(yesno='Allow,Deny')
    id = tables.LinkColumn('ui:acl pattern list', kwargs={ID: A('id')})

    class Meta:
        model = PersonACLEntry
        fields = ['id', 'place', 'type']


class RoleACLEntryTable(tables.Table):
    place = tables.LinkColumn('ui:place details', kwargs={ID: A('place.id')})
    type = TypeColumn(yesno='Allow,Deny')
    id = tables.LinkColumn('ui:acl pattern list', kwargs={ID: A('id')})

    class Meta:
        model = RoleACLEntry
        fields = ['id', 'place', 'type']


class ACLPattern(tables.Table):
    id = tables.LinkColumn('ui:acl pattern details', kwargs={ID: A('id')})

    class Meta:
        model = SimpleRecurringPattern
        fields = ['id', 'from_time', 'until_time', 'days_of_week', 'days_of_month', 'months']

    def render_days_of_week(self, value: str):
        value = self._drop_squared_brackets(value)
        return self._replace_days_of_week_for_names(value)

    def render_days_of_month(self, value: str):
        return self._drop_squared_brackets(value)

    def render_months(self, value: str):
        value = self._drop_squared_brackets(value)
        return self._replace_months_for_names(value)

    @staticmethod
    def _drop_squared_brackets(value: str):
        return value.replace('[', '').replace(']', '')

    @staticmethod
    def _replace_days_of_week_for_names(value):
        days_of_week = (
            ('1', 'Sun'),
            ('2', 'Mon'),
            ('3', 'Tue'),
            ('4', 'Wed'),
            ('5', 'Thu'),
            ('6', 'Fri'),
            ('7', 'Sat'),
        )
        for number, day in days_of_week:
            value = value.replace(number, day)
        return value

    def _replace_months_for_names(self, value):
        months = (
            ('1', 'Jan'),
            ('2', 'Feb'),
            ('3', 'Mar'),
            ('4', 'Apr'),
            ('5', 'May'),
            ('6', 'Jun'),
            ('7', 'Jul'),
            ('8', 'Aug'),
            ('9', 'Sep'),
            ('10', 'Oct'),
            ('11', 'Nov'),
            ('12', 'Dec')
        )
        for number, month in months:
            value = value.replace(number, month)
        return value
