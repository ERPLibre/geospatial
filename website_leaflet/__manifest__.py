# Copyright (C) 2020, SantéLibre
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Leaflet',
    'summary': 'Leaflet Integration in website',
    'version': '12.0.1.0.0',
    'author': 'SantéLibre',
    'license': 'AGPL-3',
    'category': 'Extra Tools',

    # any module necessary for this one to work correctly
    'depends': ['website', 'base_goengine'],

    # always loaded
    'data': [
    ],
    'installable': True,
    'application': True,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
