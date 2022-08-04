# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Banner Snippet",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Website",
    "summary": " Banner Snippets Module, Stylish Banner Snippets App, Website Banner Snippet, Banner Snipet, Banner Box, Banner Content Box, Product Offer Banner Snippet Odoo",
    "description": """Do you want "Banner Snippets" for your webpage? Do you want different types of banners? So you are the right place. We provide 25 different snippet styles of the banner. This module useful to make your webpage beautiful with different banner snippets. This snippet is clean, responsive, animated, professional, effective & efficient. This snippet is great for the highlight product offers with a banner on your webpage. You can use this snippet without any technical skills. Here you get a stylish, flexible, attractive, beautiful & modern banners for your webpage.""",
    "version": "15.0.2",
    "depends": ["base", "website", "sh_snippet_adv"],
    "application": True,
    "data": [
        "views/snippets.xml",
        "views/snippet_panel.xml",
    ],
      'assets': {
         'web.assets_frontend': [
            'sh_banner_snippet/static/src/scss/snippet.scss',
            
        ],
     },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/PmIjSPtaUAc",
    "auto_install": False,
    "installable": True,
    "license": "OPL-1",
    "price": "35",
    "currency": "EUR"
}
