from odoo import api, fields, models


class Teknisi(models.Model):
    _inherit = 'res.partner'

    is_teknisi = fields.Boolean(string='Teknisi')

    
    
