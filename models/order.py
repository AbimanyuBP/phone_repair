from odoo import api, fields, models


class Order(models.Model):
    _name = 'pr.order'
    _description = 'isi order pelanggan'

    id_order = fields.Char(string='Order ID')
    seri = fields.Char(string='Seri HP')
    pelanggan = fields.Char(string='Pelanggan')
    progress = fields.Selection(string='Progress', selection=[
        ('baru', 'Baru'), 
        ('inspeksi', 'Inspeksi'), 
        ('quotation', 'Quotation'), 
        ('ditolak', 'Ditolak'), 
        ('repair', 'Repair'),
        ('selesai', 'Selesai'),], 
        default='baru')
    
    
    
    
    
