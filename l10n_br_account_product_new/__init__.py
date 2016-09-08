# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from . import models


def post_init(cr, registry):
    """Import CSV data as it is faster than xml and because we can't use
    noupdate anymore with csv"""
    from odoo.tools import convert_file
    filename = 'data/l10n_br_account_product.cfop.csv'
    convert_file(cr, 'l10n_br_account_product', filename, None, mode='init',
                 noupdate=True, kind='init', report=None)
