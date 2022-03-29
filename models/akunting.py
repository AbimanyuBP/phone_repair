from odoo import api, fields, models


class Akunting(models.Model):
    _name = 'pr.akunting'
    _description = 'New Description'
    _order = 'id asc'

    name = fields.Char(string='ID quotation')
    id_ak = fields.Char(string='Kode akunting')
    order_id = fields.Many2one(comodel_name='pr.order', string='Order No')
    date = fields.Datetime(string='Date', default=fields.Datetime.now())
    debet = fields.Integer(string='debet')
    kredit = fields.Integer(string='kredit')
    saldo = fields.Float(compute='_compute_saldo', string='saldo')
    
    @api.depends('debet', 'kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id', '<', record.id)], limit=1, order='date desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debet
    
    
    
