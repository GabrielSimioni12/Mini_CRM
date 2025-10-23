import json, csv
from pathlib import Path
from models import Lead

class LeadRepository:
    def __init__(self):
        self.data_dir = Path(__file__).resolve().parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self):
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        self.db_path.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

    # CRUD
    def add_lead(self, lead: Lead):
        leads = self._load()
        leads.append(lead.to_dict())
        self._save(leads)

    def list_leads(self):
        return [Lead(**l) for l in self._load()]

    def search(self, query):
        query = query.lower()
        results = []
        for l in self._load():
            blob = f"{l['name']} {l['company']} {l['email']}".lower()
            if query in blob:
                results.append(Lead(**l))
        return results

    def export_csv(self, path=None):
        path = Path(path) if path else (self.data_dir / "leads.csv")
        leads = self._load()
        try:
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["name", "company", "email", "stage", "created"])
                w.writeheader()
                for row in leads:
                    w.writerow(row)
            return path
        except PermissionError:
            return None
