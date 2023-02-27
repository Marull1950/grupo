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

from odoo import api, models, fields, tools, _
from odoo.http import request

import logging

_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = 'website'

    # @api.multi
    def sale_product_domain(self):
        vals = super(Website, self).sale_product_domain()
        customer_group = self.env.user.customer_grp_id
        if customer_group:
            if customer_group.product_visible == 'all':
                return vals
            else:
                cat_ids = []
                operator = 'child_of' if customer_group.product_cat_ids else 'in'
                for cat_obj in customer_group.product_cat_ids:
                    cat_ids.append(cat_obj.id)
                vals+=[('public_categ_ids', operator, cat_ids)]
        return vals

    def get_current_pricelist(self):
        pricelist, uid = False, self.env.context.get('uid')
        customer_group = self.env['res.users'].sudo().browse(uid).customer_grp_id if uid else request.website.user_id.sudo().customer_grp_id
        if customer_group and customer_group.group_pricelist_id:
            pricelist = customer_group.group_pricelist_id
            request.session['website_sale_current_pl'] = pricelist.id
        else:
            pricelist = super(Website, self).get_current_pricelist()
        return pricelist

    def get_pricelist_available(self, show_visible=False):
        aval_pricelist, customer_group = False, self.env.user.customer_grp_id
        if customer_group and customer_group.group_pricelist_id:
            aval_pricelist = customer_group.group_pricelist_id
        else:
            aval_pricelist = super(Website, self).get_pricelist_available(show_visible)
        return aval_pricelist
