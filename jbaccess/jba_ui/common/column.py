import django_tables2 as tables


class TypeColumn(tables.BooleanColumn):

    def _get_bool_value(self, record, value, bound_column):
        if value == 1:
            value = True
        else:
            value = False
        return value