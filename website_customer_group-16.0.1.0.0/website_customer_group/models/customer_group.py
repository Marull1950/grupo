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

from odoo import models, fields, api, _

visible_product = [('all', 'All'), ('custom', 'Product Belonging to Following Category Only')]

class CustomerGroup(models.Model):
    _name = "customer.group"
    _description = "groups for customers"

    name = fields.Char(string="Group Name", translate=True)
    show_customers = fields.Boolean(string="Show Customers")
    product_visible = fields.Selection(visible_product, string="Visible Product For This Customer Group", default="all")
    product_cat_ids = fields.Many2many(comodel_name='product.public.category', relation='product_user_rel', column1='product_cat', column2='user_cat', string="Product Category")
    group_pricelist_id = fields.Many2one(comodel_name='product.pricelist', string="Group Pricelist")
    customer_ids = fields.One2many(comodel_name='res.users', inverse_name='customer_grp_id', String="Customers in the Group")

    # @api.multi
    def toggle_show_hide(self):
        self.show_customers = not self.show_customers
