# -*- coding: utf-8 -*-
# Copyright 2014-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# Copyright 2016 Sodexis (http://sodexis.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Rental Surfrio',
    'version': '10.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'summary': 'Administração de aluguel de pranchas da surfrio',
    'author': 'Luciano Veras',
    'website': 'https://github.com/lveras',
    'depends': ['l10n_br_sale_rental', ],
    'data': [
        'views/menu_sale_rental_surfrio.xml',
    ],
    'demo': ['demo/rental_demo.xml'],
    'installable': True,
    'auto_install': False,
}
