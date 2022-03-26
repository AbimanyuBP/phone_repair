from odoo import api, fields, models


class Repair(models.Model):
    _name = 'pr.repair'
    _description = 'New Description'

    name = fields.Char(string='ID Repair')
    quotation_id = fields.Many2one(comodel_name='pr.quotation', string='No Quotation', domain=[('status_quo', '=', 'diterima')], required=True)
    teknisi_id = fields.Many2one(comodel_name='res.partner', string='Teknisi', domain=[('is_teknisi', '=', True)])
    diagnosa = fields.Text(compute='_compute_diagnosa', string='Diagnosa')
    status_rep = fields.Selection(string='Status', selection=[('perbaikan', 'Perbaikan'), ('selesai', 'Selesai'),], default='perbaikan')
    
    @api.depends('quotation_id')
    def _compute_diagnosa(self):
        for record in self:
            record.diagnosa = self.env['pr.inspeksi'].search([('id', '=', record.quotation_id.ins_detail_id.id)]).mapped('diagnosa')
    
    @api.onchange('status_rep')
    def onchange_status_quo(self):
        if self.status_rep == 'selesai':
            self.env['pr.order'].search([('id','=',self.quotation_id.ins_detail_id.order_id.id)]).write({'progress':'selesai'})
    
