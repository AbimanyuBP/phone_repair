from odoo import api, fields, models


class Parts(models.Model):
    _name = 'pr.parts'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    merek = fields.Char(string='Merek')
    tipe = fields.Selection(string='Tipe', selection=[('oem', 'OEM'), ('donor', 'Donor'),])
    stok = fields.Integer(string='Stok')
    harga = fields.Integer(string='Harga')
    
    
    
    
