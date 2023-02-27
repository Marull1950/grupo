# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
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
{
  "name"                 :  "Website Customer Groups",
  "summary"              :  """Manage Website Product Category List of Product, According To Customer Group""",
  "category"             :  "Website",
  "version"              :  "1.0.0",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-Website-Customer-Group.html",
  "description"          :  """http://webkul.com/blog/website-customer-group/""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=website_customer_group",
  "depends"              :  [
                             'sale_stock',
                             'sale_management',
                             'website_sale',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'views/res_users_view.xml',
                             'views/customer_group_view.xml',
                             'data/customer_group_data.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "price"                :  39,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}