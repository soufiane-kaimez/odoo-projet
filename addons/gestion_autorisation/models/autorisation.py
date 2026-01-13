from odoo import models, fields

class Autorisation(models.Model):
    _name = "gestion.autorisation"
    _description = "Demande d'autorisation"

    name = fields.Char(string="Titre de la demande", required=True)
    description = fields.Text(string="Description simple")
    
    # Optional: Useful for authorizations
    date_demande = fields.Date(string="Date de la demande", default=fields.Date.today)
    state = fields.Selection([
        ("brouillon", "Brouillon"),
        ("valide", "Validée"),
        ("refuse", "Refusée"),
    ], string="État", default="brouillon")