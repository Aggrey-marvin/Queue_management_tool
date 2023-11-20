{
    'name': 'Custom QMS',

    'summary': """
        Customization of the queue management system. 
    """,

    'description': """
        This is a customization of a queue management module.
    """,

    'author': 'Pearl Tech',
    'website': '',
    'category': '',
    'license': 'AGPL-3',
    'version': '0.1',
    
    'depends': [
      'customer_queue'
    ],
    
    'data': [
        # Security
        # 'security/ir.model.access.csv',
        'security/queue_security.xml',
        'security/queue_record_rules.xml',

        # Data
        

        # wizards
        

        # Views
        # 'views/counter_views.xml',

        # Reports

    ]
}
