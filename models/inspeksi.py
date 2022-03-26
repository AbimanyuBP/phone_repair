from odoo import api, fields, models


class Inspeksi(models.Model):
    _name = 'pr.inspeksi'
    _description = 'New Description'

    id_inspeksi = fields.Char(string='ID inspeksi')
    order_id = fields.Many2one(comodel_name='pr.order', string='No order')
    teknisi_id = fields.Many2one(comodel_name='res.partner', string='Teknisi')
    keluhan = fields.Text(string='Keluhan')
    diagnosa = fields.Text(string='Diagnosa')
    status_ins = fields.Selection(string='Status', selection=[('proses', 'Proses'), ('diagnosed', 'Diagnosed'),], default='proses')

    @api.model
    def create(self, vals):
        record = super(Inspeksi, self).create(vals)
        if record.keluhan:
            self.env['pr.order'].search([('id','=',record.order_id.id)]).write({'progress':'inspeksi'})
            return record


    
    
    
    
    
