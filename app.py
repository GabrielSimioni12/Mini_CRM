from models import Lead
from repo import LeadRepository

class CRMApp:
    def __init__(self):
        self.repo = LeadRepository()

    def add_lead_flow(self):
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()

        if not name or not email or "@" not in email:
            print("❌ Nome e e-mail válidos são obrigatórios.")
            return

        lead = Lead(name, company, email)
        self.repo.add_lead(lead)
        print("✔ Lead adicionado!")

    def list_flow(self):
        leads = self.repo.list_leads()
        if not leads:
            print("Nenhum lead ainda.")
            return

        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in enumerate(leads):
            print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

    def search_flow(self):
        q = input("Buscar por: ").strip()
        if not q:
            print("Consulta vazia.")
            return

        results = self.repo.search(q)
        if not results:
            print("Nada encontrado.")
            return

        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, l in enumerate(results):
            print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

    def export_flow(self):
        path = self.repo.export_csv()
        if path:
            print(f"✔ Exportado para: {path}")
        else:
            print("❌ Não consegui exportar o CSV. Feche o arquivo se estiver aberto.")

    def run(self):
        while True:
            self.print_menu()
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_lead_flow()
            elif op == "2":
                self.list_flow()
            elif op == "3":
                self.search_flow()
            elif op == "4":
                self.export_flow()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def print_menu():
        print("\nMini CRM de Leads — Versão OO")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar lead")
        print("[4] Exportar CSV")
        print("[0] Sair")
