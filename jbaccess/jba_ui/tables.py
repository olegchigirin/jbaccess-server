import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_tables2.utils import A

from jba_core.models import Person, Role, Key, Controller, Door, Place, PersonACLEntry, RoleACLEntry, \
    SimpleRecurringPattern
from jba_ui.common.column import TypeColumn
from jba_ui.common.const import ID
from jba_ui.common.utils import drop_squared_brackets, replace_days_of_week_for_names, replace_months_for_names


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
        value = drop_squared_brackets(value)
        return replace_days_of_week_for_names(value)

    def render_days_of_month(self, value: str):
        return drop_squared_brackets(value)

    def render_months(self, value: str):
        value = drop_squared_brackets(value)
        return replace_months_for_names(value)


class ControllerResolveTable(tables.Table):
    type = TypeColumn(yesno='Allow,Deny')
    key = tables.LinkColumn('ui:key details', kwargs={ID: A('key.id')})
    door = tables.LinkColumn('ui:door details', kwargs={ID: A('door.id')})
    pattern = tables.Column()

    def render_pattern(self, value: SimpleRecurringPattern):
        return mark_safe("""
        <a href="%s">Pattern</a>: from %s until %s</br> 
        days of week: %s </br> 
        days: %s </br> 
        months: %s
        """ % (
            reverse('ui:acl pattern details', kwargs={ID: value.id}),
            value.from_time,
            value.until_time,
            replace_days_of_week_for_names(drop_squared_brackets(value.days_of_week)),
            drop_squared_brackets(value.days_of_month),
            replace_months_for_names(drop_squared_brackets(value.months))
        ))
