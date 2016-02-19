from django.forms.models import inlineformset_factory

from contacts.models import (
    Contact,
    Address,
)

# inlineformset_factory creates a Class from a parent model (Contact)
# to a child model (Address)
ContactAddressFormSet = inlineformset_factory(
    Contact,
    Address,
)