from django import forms

from utilities.forms import BootstrapMixin, StaticSelect2Multiple

OBJ_TYPE_CHOICES = (
    ('', 'All Objects'),
    ('Circuits', (
        ('provider', 'Providers'),
        ('circuit', 'Circuits'),
    )),
    ('DCIM', (
        ('site', 'Sites'),
        ('rack', 'Racks'),
        ('rackgroup', 'Rack Groups'),
        ('devicetype', 'Device types'),
        ('device', 'Devices'),
        ('virtualchassis', 'Virtual Chassis'),
        ('cable', 'Cables'),
        ('powerfeed', 'Power Feeds'),
        ('inventoryitem', 'Inventory Items'),
    )),
    ('IPAM', (
        ('vrf', 'VRFs'),
        ('aggregate', 'Aggregates'),
        ('prefix', 'Prefixes'),
        ('ipaddress', 'IP addresses'),
        ('vlan', 'VLANs'),
    )),
    ('Secrets', (
        ('secret', 'Secrets'),
    )),
    ('Tenancy', (
        ('tenant', 'Tenants'),
    )),
    ('Virtualization', (
        ('cluster', 'Clusters'),
        ('virtualmachine', 'Virtual machines'),
    )),
)


class SearchForm(BootstrapMixin, forms.Form):
    q = forms.CharField(
        label='Search'
    )
    obj_type = forms.MultipleChoiceField(
        widget=StaticSelect2Multiple(attrs={'data-placeholder': 'All Objects'}),
        choices=OBJ_TYPE_CHOICES, required=False, label='Type'
    )
