# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2016-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

import logging

_logger = logging.getLogger(__name__)

class WebsiteSale(WebsiteSale):

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        vals = super(WebsiteSale, self).shop(page=page, category=category, search=search, ppg=ppg, **post)
        customer_group = request.env.user.customer_grp_id
        if customer_group:
            if customer_group.product_visible == 'all':
                return vals
            else:
                cat_ids = []
                for cat_obj in customer_group.product_cat_ids:
                    cat_ids.append(cat_obj.id)
                category_obj = request.env['product.public.category']
                categs = category_obj.search([('parent_id', 'not in', cat_ids), ('id', 'in', cat_ids)])
                vals.qcontext['categories'] = categs
        return vals