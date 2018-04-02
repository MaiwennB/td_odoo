# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_classe(models.Model):
    _name = 'iut.classe'
    name = fields.Char(string='nom classe')
    #level 
    student_nb = fields.Char(string='nombre d\'éleves')
    # professeur_id = fields.One2many('iut.professeur', string='professeur')    
    # eleve_id = fields.One2many('iut.eleve', string='eleve')    
