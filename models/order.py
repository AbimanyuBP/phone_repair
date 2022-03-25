from odoo import api, fields, models


class Order(models.Model):
    _name = 'pr.order'
    _description = 'New Description'

    name = fields.Char(string='Name')
