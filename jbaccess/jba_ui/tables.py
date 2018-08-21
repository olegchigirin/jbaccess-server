import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_tables2.utils import A

from jba_core.models import Person, Role, Key, Controller, Door, Place, PersonACLEntry, RoleACLEntry, \
    SimpleRecurringPattern
from jba_ui.common.column import TypeColumn
from jba_ui.common.const import ID
from jba_ui.common.utils import drop_squared_brackets, replace_days_of_week_for_names, replace_months_for_names


class PersonHomePageTable(tables.Table):
    person = tables.LinkColumn('ui:person details', kwargs={ID: A('person.id')})
    keys = tables.Column()
    roles = tables.Column()

    def render_keys(self, value):
        result = []
        for v in value:
            result.append('<a href="{}">{}</a>'.format(reverse('ui:key details', kwargs={ID: v.id}), v.name))
        if result:
            return mark_safe(' '.join(result))
        else:
            return 'Person has no key'

    def render_roles(self, value):
        result = []
        for v in value:
            result.append('<a href="{}">{}</a>'.format(reverse('ui:role details', kwargs={ID: v.id}), v.name))
        if result:
            return mark_safe(' '.join(result))
        else:
            return 'Person has no role yes'


class PersonTable(tables.Table):
    name = tables.LinkColumn('ui:person details', kwargs={ID: A(ID)})

    class Meta:
        model = Person


class RoleTable(tables.Table):
    name = tables.LinkColumn('ui:role details', kwargs={ID: A(ID)})

    class Meta:
        model = Role


class KeyTable(tables.Table):
    name = tables.LinkColumn('ui:key details', kwargs={ID: A(ID)})

    class Meta:
        model = Key


class ControllerTable(tables.Table):
    name = tables.LinkColumn('ui:controller details', kwargs={ID: A(ID)})

    class Meta:
        model = Controller


class DoorTable(tables.Table):
    name = tables.LinkColumn('ui:door details', kwargs={ID: A(ID)})

    class Meta:
        model = Door


class PlaceTable(tables.Table):
    name = tables.LinkColumn('ui:place details', kwargs={ID: A(ID)})

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
    class Meta:
        model = SimpleRecurringPattern
        fields = ['from_time', 'until_time', 'days_of_week', 'days_of_month', 'months']
        row_attrs = {
            'onclick': lambda record: reverse('ui:acl pattern details', kwargs={ID: record.id})
        }

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

    class Meta:
        fields = ['key', 'door', 'pattern', 'type']

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
