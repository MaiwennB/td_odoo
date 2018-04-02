# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_professeur(models.Model):
    _name = 'iut.professeur'

    name = fields.Char(string='nom')
    surname = fields.Char(string='prénom')
    # classe_id = fields.One2many('iut.classe', string='classe')    

