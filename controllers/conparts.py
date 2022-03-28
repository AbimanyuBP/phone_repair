from odoo import http, fields, models
from odoo.http import request
import json


class PartsCon(http.Controller):
    @http.route(['/parts','/parts/<int:idnya>'], auth='public', method=['GET'], csrf=True)
    def getAllParts(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            part = request.env['pr.parts'].search([])
            for k in part:
                value.append({"id":k.id,
                            "name":k.name,
                            "merek":k.merek,
                            "tipe":k.tipe,
                            "stok":k.stok,
                            "harga":k.harga})
            return json.dumps(value)
        else:
            partsid = request.env['pr.parts'].search([('id', '=', idnya)])
            for k in partsid:
                value.append({"id":k.id,
                            "name":k.name,
                            "merek":k.merek,
                            "tipe":k.tipe,
                            "stok":k.stok,
                            "harga":k.harga})
            return json.dumps(value)

    @http.route('/createparts', auth='user', type='json', method=['POST'])
    def createParts(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals = {
                    'name': kw['name'],
                    'merek': kw['merek'],
                    'tipe': kw['tipe'],
                    'stok': kw['stok'],
                    'harga': kw['harga'],
                }   
                partsbaru = request.env['pr.parts'].create(vals)
                args = {'succeed': True, "ID": partsbaru.id}
                return args
