from datetime import date

class Lead:
    def __init__(self, name, company, email, stage="novo", created=None):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = created or date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

    def __str__(self):
        return f"{self.name} ({self.company}) - {self.email}"

# Exemplo opcional de herança e polimorfismo
class QualifiedLead(Lead):
    def __init__(self, name, company, email, score, stage="qualificado", created=None):
        super().__init__(name, company, email, stage, created)
        self.score = score

    def to_dict(self):
        data = super().to_dict()
        data["score"] = self.score
        return data
