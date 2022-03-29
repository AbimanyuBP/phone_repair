from odoo import api, fields, models


class Quotation(models.Model):
    _name = 'pr.quotation'
    _description = 'New Description'

    id_quo = fields.Char(string='ID quotation')
    partsdetail_ids = fields.One2many(comodel_name='pr.partsdetail', inverse_name='quotation_id', string='Parts Detail')
    ins_detail_id = fields.Many2one(comodel_name='pr.inspeksi', string='No Inspeksi', domain=[('status_ins', '=', 'diagnosed')])
    status_quo = fields.Selection(string='Status', selection=[('diterima', 'Diterima'), ('ditolak', 'Ditolak'), ('waiting', 'Waiting')], default='waiting')
    har_inspeksi = fields.Integer(string='Harga Inspeksi', readonly=True, default=45000)
    har_parts = fields.Char(compute='_compute_har_parts', string='Total harga parts ', store=True)
    tot_harga = fields.Integer(compute='_compute_tot_harga', string='Total akhir', store=True)
    
    @api.depends('partsdetail_ids')
    def _compute_har_parts(self):
        for record in self:
            k = sum(self.env['pr.partsdetail'].search([('parts_id', '=', record.id)]).mapped('total'))
            record.har_parts = k
    
    @api.depends('partsdetail_ids', 'har_inspeksi')
    def _compute_tot_harga(self):
        for record in self:
            a = sum(self.env['pr.partsdetail'].search([('parts_id', '=', record.id)]).mapped('total'))
            record.tot_harga = a + record.har_inspeksi
    
    
    @api.model
    def create(self, vals):
        record = super(Quotation, self).create(vals)
        if record.status_quo:
            self.env['pr.order'].search([('id','=',record.ins_detail_id.order_id.id)]).write({'progress':'quotation'})
            self.env['pr.akunting'].create({'kredit': record.har_inspeksi, 'name': record.id_quo})
            return record

    @api.onchange('status_quo')
    def onchange_status_quo(self):
        if self.status_quo == 'diterima':
            self.env['pr.order'].search([('id','=',self.ins_detail_id.order_id.id)]).write({'progress':'repair'})
        elif self.status_quo == 'ditolak':
            self.env['pr.order'].search([('id','=',self.ins_detail_id.order_id.id)]).write({'progress':'ditolak'})


class PartsDetail(models.Model):
    _name = 'pr.partsdetail'
    _description = 'New Description'

    name = fields.Char(string='Name')
    quotation_id = fields.Many2one(comodel_name='pr.quotation', string='Quotation')
    parts_id = fields.Many2one(comodel_name='pr.parts', string='Parts')
    qty = fields.Integer(string='Kuantitas')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    total = fields.Integer(compute='_compute_total', string='total')
    
    @api.depends('parts_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.parts_id.harga
    
    @api.depends('parts_id', 'qty')
    def _compute_total(self):
        for record in self:
            record.total = record.parts_id.harga * record.qty
    

    
    
