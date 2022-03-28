from odoo import api, fields, models


class Akunting(models.Model):
    _name = 'pr.akunting'
    _description = 'New Description'
    _order = 'id asc'

    name = fields.Char(string='Name')
    id_ak = fields.Char(string='Kode akunting')
    tanggal = fields.Date('tanggal')
    debet = fields.Integer(string='debet')
    kredit = fields.Integer(string='kredit')
    saldo = fields.Integer(compute='_compute_saldo', string='saldo')
    
    @api.depends('debet', 'kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id', '<', record.id)], limit=1, order='date desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debet
    
    
    
