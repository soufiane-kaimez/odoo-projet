{
    "name": "Gestion des Autorisations",
    "version": "1.0",
    "summary": "Demandes simples d'autorisation",
    "category": "Tools",
    "author": "Vous",
    "depends": ["base"],
    "data": [
        "security/security.xml",          # <--- THIS MUST BE FIRST
        "security/ir.model.access.csv",   # <--- THIS MUST BE SECOND
        "views/autorisation_views.xml",
    ],
    "installable": True,
    "application": True,
}