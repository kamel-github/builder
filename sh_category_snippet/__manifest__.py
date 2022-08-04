# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

{
    "name": "Category Snippets",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Website",
    "summary": """
Category Snippets, Category Slider Snippet Module,
Stylish Category Snippets, Categories Blocks App,
Category Snipet Application, Category Box, Category Content Box,
Featured Snippet, Alternative Category Snnipet,
Multiple Category Snippets Odoo
""",
    "description": """
Do you want to show a beautiful category on-page?
This module useful to make your
webpage beautiful with different category snippets.
you can use this snippet without any technical skill.
you can easily add links to change images.
if you want to see how it will work
then please check out the below video.
This module provides a 20+ different and stylish snippet
for display products on the shop page with image,
description & product count feature.
This snippet is clean, responsive, animated,
professional, effective and efficient.
""",
    "version": "15.0.1",
    "depends": [
        "website_sale",
        "sh_snippet_adv",
    ],
    "application": True,
    "data": [
        "views/public_category_view.xml",
        "views/category_s_item.xml",
        "views/category_s.xml",
        "views/snippet_panel.xml",
        "views/snippet_option.xml",
    ],
    'assets': {
         'web.assets_frontend': [
            'sh_category_snippet/static/src/scss/snippet.scss',
            'sh_category_snippet/static/src/js/s_category.js',
            
        ],
     },
    "images": ["static/description/background.png"],
    "live_test_url": "https://youtu.be/qCBAT3OtVf0",
    "auto_install": False,
    "installable": True,
    "price": 35,
    "currency": "EUR",
    "license": "OPL-1"
}
