# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_cours(models.Model):
    _name = 'iut.cours'
    name = fields.Char(string='nom')