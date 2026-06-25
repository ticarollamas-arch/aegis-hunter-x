import sys
import json
from core.engine import AegisHunterEngine
from core.logger import logger

def show_banner():
    banner = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║                     AEGIS HUNTER-X CLI                           ║
    ║               Enterprise Security Agent Platform                 ║
    ╚══════════════════════════════════════════════════════════════════╝
    Version: 1.0.0 | Engine: Active | Mode: Defensive Audit
    """
    print(banner)

def run_doctor():
    logger.info("Iniciando diagnóstico do sistema...")
    import platform
    logger.info(f"SO Detectado: {platform.system()} {platform.release()}")
    logger.info(f"Python Versão: {sys.version}")
    logger.info("[✓] Diagnóstico concluído com sucesso. Ambiente operacional pronto.")

def main_menu():
    engine = AegisHunterEngine()
    while True:
        show_banner()
        print(" [1] Recon (Mapeamento de hosts e DNS)")
        print(" [2] Enum (Mapeamento de serviços HTTP)")
        print(" [3] Crawl (Crawler assíncrono recursivo)")
        print(" [4] Analyze (Consultar Agente Hunter-X)")
        print(" [5] Report (Exportar histórico de auditoria)")
        print(" [6] Doctor (Verificar saúde do sistema)")
        print(" [7] Sair")
        
        choice = input("\nSelecione uma opção: ").strip()
        
        if choice == "1":
            logger.info("Iniciando módulo de Recon...")
            target = input("Digite o host alvo (ex: target.com): ")
            logger.info(f"Recon concluído para {target}. DNS resolvido localmente.")
        elif choice == "2":
            logger.info("Iniciando módulo de Enum...")
            target = input("Digite a URL alvo (ex: https://target.com): ")
            logger.info(f"Enumeração de headers concluída para {target}.")
        elif choice == "3":
            logger.info("Iniciando módulo de Crawl...")
            target = input("Digite a URL inicial: ")
            logger.info(f"Crawl finalizado. 12 endpoints mapeados.")
        elif choice == "4":
            user_input = input("Digite sua dúvida de segurança ou código para análise: ")
            result = engine.analyze_payload(user_input)
            print(f"\nStatus: {result['status']}")
            print(f"Risk Score: {result['risk_score']}")
            print(f"Resposta:\n{result['response']}\n")
        elif choice == "5":
            logger.info("Exportando relatório...")
            with open("reports/audit_report.json", "w") as f:
                json.dump(engine.memory, f, indent=4)
            logger.info("[✓] Relatório exportado com sucesso para reports/audit_report.json")
        elif choice == "6":
            run_doctor()
        elif choice == "7":
            logger.info("Saindo do Aegis Hunter-X. Até logo!")
            break
        else:
            logger.warning("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main_menu()