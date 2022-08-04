# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Ecommerce Snippets",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Website",
    "summary": """
Ecommerce Snippets, Ecommerce Slider Snippet Module,
Stylish Ecommerce Snippets, Product Grid Block,Products Blocks,
Goods Snippet App, E-commerce Snipet, Ecommerce Box Application,
Product Content Box, Effective Ecommerece Snippet Odoo
""",
    "description": """
This module provides a 50 different and stylish snippet
for display products on the shop page. This snippet is clean,
responsive, animated, professional, effective and efficient.
Easy to set products in the snippet as category wise. Also,
you can set product description, add to cart
and add to wish buttons, sale price.
Ecommerce Snippet Odoo, E-commerce Blocks Odoo
Ecommerce Snippets, Ecommerce Slider Snippet Module,
Stylish Ecommerce Snippets, Product Grid Block,Products Blocks,
Goods Snippet, Ecommerce Snipet, Ecommerce Box,
Product Content Box, Effective E-commerece Snippet,
Top Selling Product Snnipet, New Arrival Product Snippet,
Featured Snnipet, Alternative Product Snnipet Odoo.
Ecommerce Snippets, Ecommerce Slider Snippet Module,
Stylish Ecommerce Snippets, Product Grid Block,
Products Blocks, Goods Snippet App, E-commerce Snipet,
Ecommerce Box Application, Product Content Box,
Effective Ecommerece Snippet, Top Selling Product Snnipet,
New Arrival Product Snippet, Featured Snippet,
Alternative Product Snnipet Odoo.
""",
    "version": "15.0.3",
    "depends": [
        "website_sale_wishlist",
        "sh_snippet_adv",
    ],
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/filter.xml",
        "views/product_s_item.xml",
        "views/product_s.xml",
        "views/snippet_option.xml",
        "views/snippet_panel.xml",
    ],
    'assets': {
         'web.assets_frontend': [
            'sh_ecommerce_snippet/static/src/scss/sh_ecom_s.scss',
            'sh_ecommerce_snippet/static/src/js/s_product.js',
            
        ],
     },
    "images": ["static/description/background.png", ],
    "license": "OPL-1",
    "live_test_url":
    "https://www.youtube.com/watch?v=mNu-lwXBtZg&feature=youtu.be",
    "auto_install": False,
    "installable": True,
    "price": 50,
    "currency": "EUR"
}
