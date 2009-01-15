#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Stock Inventory for many locations',
    'version': '0.0.1',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': '''Stock Inventory for many locations
    ''',
    'depends': [
        'ir',
        'stock',
        'stock_report',
        'company',
        'product',
    ],
    'xml': [
        'inventory.xml',
    ],
    'translation': [
    ],
}
