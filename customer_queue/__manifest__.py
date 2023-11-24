# -*- coding: utf-8 -*-
#############################################################################
#
#    Hundred Solutions
#
#    Copyright (C) 2023-TODAY Hundred Solutions(<https://www.hundredsolutions.com/>)
#    Author: Arjun Baidya (arjun.b@hundredsolutions.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Customer Queue',
    'version': '16.0.1.0.0',
    'summary': """Manage your customer by smart app""",
    'author': "Hundred Solutions",
    'maintainer': 'Hundred Solutions',
    'company': "Hundred Solutions",
    'website': 'https://www.hundredsolutions.com/',
    'category': 'Industries',
    'description': """
    Helps You To manage customer support.
    """,
    'depends': [
        'base',
        'hr',
        'contacts',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',
        'data/demo_data.xml',

        # Backend
        'views/backend/token_create.xml',
        'views/backend/counter_create.xml',
        'views/backend/token_screen.xml',
        'views/backend/menu.xml',
        
        # Frontend
        'views/frontend/web_view.xml',
        'views/frontend/customer_web_token.xml',

        'wizard/services.xml',
        # 'wizard/token_screen.xml',
        'data/cron.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            
        ],
    },

    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
