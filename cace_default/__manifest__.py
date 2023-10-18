# -----------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'cace',
    'version': '11.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customization for CACE',
    "development_status": "Beta",  # "Alpha|Beta|Production/Stable|Mature"
    'author': 'CACE Software',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',
        'stock',

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ce',

        # utilitarios adicionales
        #'backend_theme_v11',
        

        # requerido por la restriccion de menuitems
        #'mail', 'calendar', 'contacts', 'mrp', 'sale', 'purchase', 'stock',
        #'account', 'hr', 'base'
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'config': [
    ],

    'env-ver': '2',
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    'git-repos': [
        'https://github.com/pabarrientos/cl-cace.git',
        'https://github.com/jobiols/odoo-addons.git',
        #'https://github.com/jobiols/rafi16jan-backend-theme.git',
        'https://github.com/Openworx/backend_theme.git',
        'https://github.com/jobiols/odoo-jeo-ce.git',
	    'https://github.com/soroushCoder/theme_soroush_first.git',
	    'https://github.com/odoo/design-themes.git',
	    'https://github.com/muk-it/muk_website.git',

        'https://github.com/ingadhoc/odoo-argentina.git ingadhoc-odoo-argentina',
        'https://github.com/ingadhoc/argentina-sale.git ingadhoc-argentina-sale',
        'https://github.com/ingadhoc/account-analytic.git ingadhoc-account-analytic',
        'https://github.com/ingadhoc/account-financial-tools.git ingadhoc-account-financial-tools',
        'https://github.com/ingadhoc/account-payment.git ingadhoc-account-payment',
        'https://github.com/ingadhoc/website.git ingadhoc-website',
        'https://github.com/ingadhoc/miscellaneous.git ingadhoc-miscellaneous',
        'https://github.com/ingadhoc/argentina-reporting.git ingadhoc-argentina-reporting',
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale',
        'https://github.com/ingadhoc/reporting-engine.git ingadhoc-reporting-engine',
        'https://github.com/ingadhoc/aeroo_reports.git ingadhoc-aeroo_reports',
        'https://github.com/ingadhoc/sale.git ingadhoc-sale',
        'https://github.com/ingadhoc/odoo-support.git ingadhoc-odoo-support',
        'https://github.com/ingadhoc/patches.git ingadhoc-patches',
        'https://github.com/ingadhoc/product.git ingadhoc-product',
        'https://github.com/ingadhoc/partner.git ingadhoc-partner',
        'https://github.com/ingadhoc/project.git ingadhoc-project',
        'https://github.com/ingadhoc/account-invoicing.git ingadhoc-account-invoicing',
        'https://github.com/ingadhoc/sale.git ingadhoc-sale',
        'https://github.com/ingadhoc/stock.git ingadhoc-stock',
	    'https://github.com/ingadhoc/purchase.git ingadhoc-purchase',
        'https://github.com/ingadhoc/hr.git ingadhoc-hr',
        'https://github.com/ingadhoc/multi-company.git ingadhoc-multi-company',

        'https://github.com/oca/partner-contact.git oca-partner-contact',
        'https://github.com/oca/web.git oca-web',
        'https://github.com/oca/server-tools.git oca-server-tools',
        'https://github.com/oca/social.git oca-social',
        'https://github.com/oca/server-brand.git oca-server-brand',
        'https://github.com/oca/server-ux.git oca-server-ux',
        'https://github.com/oca/project.git oca-project',
        'https://github.com/oca/queue.git oca-queue',
	    'https://github.com/oca/sale-workflow.git oca-sale-workflow',
	    'https://github.com/OCA/e-commerce.git oca-e-commerce',
	    'https://github.com/OCA/website.git oca-website',
        'https://github.com/OCA/website-cms.git oca-website-cms',
	    'https://github.com/OCA/product-attribute.git oca-product-attribute',
        'https://github.com/OCA/knowledge.git oca-knowledge',
        'https://github.com/OCA/maintenance.git oca-maintenance',
        'https://github.com/OCA/management-system.git oca-management-system',
        'https://github.com/OCA/purchase-workflow.git oca-purchase-workflow',
        'https://github.com/OCA/report-print-send.git oca-report-print-send',
        'https://github.com/OCA/stock-logistics-warehouse.git oca-stock-logistics-warehouse',
        'https://github.com/OCA/account-analytic.git oca-account-analytic',
        'https://github.com/OCA/account-closing.git oca-account-closing',
        'https://github.com/OCA/bank-payment.git oca-bank-payment',
        'https://github.com/OCA/currency.git',
        'https://github.com/OCA/hr.git oca-hr',
        'https://github.com/OCA/hr-timesheet.git oca-hr-timesheet',
        'https://github.com/OCA/server-auth.git oca-server-auth',
        'https://github.com/OCA/server-backend.git oca-server-backend',

        #OpenHRMS
        'https://github.com/CybroOdoo/OpenHRMS.git openhrms',
    ],

    'docker-images': [
        'odoo pabarrientos/odoo11:0.1.1',
        'postgres postgres:11.1-alpine',
        'nginx nginx',
        'aeroo adhoc/aeroo-docs'
    ]

}
