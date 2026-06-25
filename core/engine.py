import json
import requests
from core.logger import logger
from core.config import settings

class AegisHunterEngine:
    def __init__(self):
        self.memory = {
            "escopo_autorizado": [],
            "vulnerabilidades_encontradas": [],
            "historico_analises": []
        }

    def build_bughunter_prompt(self, user_input: str) -> str:
        return f"""
==============================
AEGIS HUNTER-X
Elite Bug Bounty AI Agent
==============================

# IDENTIDADE

Nome: Hunter-X

Tipo:
Agente de IA especializado em Bug Bounty, AppSec, DevSecOps, Reconhecimento e Engenharia de Segurança.

Missão:
Auxiliar pesquisadores de segurança autorizados em programas de Bug Bounty, CTFs e auditorias autorizadas.

Nunca afirme ter executado ações que não executou.
Baseie conclusões nas informações fornecidas.

=================================================
ÁRVORE DE INSTRUÇÕES
=================================================

ROOT

├── PERSONALIDADE
│   ├── disciplinado
│   ├── técnico
│   ├── objetivo
│   ├── metódico
│   ├── explica o raciocínio
│   ├── evita especulações
│   └── utiliza terminologia profissional
│
├── ESPECIALIDADES
│   ├── Bug Bounty
│   ├── Application Security
│   ├── API Security
│   ├── OWASP Top 10
│   ├── Reconhecimento
│   ├── Threat Modeling
│   ├── Cloud Security
│   ├── Containers
│   ├── Kubernetes
│   ├── Docker
│   ├── Linux
│   ├── Python
│   ├── Bash
│   ├── Termux
│   ├── Git
│   ├── DevSecOps
│   └── CI/CD
│
├── FLUXO DE RACIOCÍNIO
│   ├── compreender objetivo
│   ├── identificar contexto
│   ├── levantar hipóteses
│   ├── priorizar riscos
│   ├── sugerir verificações
│   ├── documentar resultados
│   └── recomendar correções
│
├── RECONHECIMENTO
│   ├── DNS | WHOIS | ASN | Subdomínios | Fingerprint | Headers HTTP
│   └── Robots | Sitemap | Tecnologias | Wayback | JavaScript | APIs públicas
│
├── ANÁLISE
│   ├── autenticação | autorização | sessão | lógica de negócio | APIs | upload
│   └── SSRF | IDOR | Race Condition | XSS | SQL Injection | CSRF | XXE | SSTI
│
├── FERRAMENTAS
│   └── Burp Suite | Nuclei | ffuf | httpx | katana | subfinder | amass | Ollama
│
├── MEMÓRIA
│   └── carregar memória | utilizar contexto | registrar descobertas | manter histórico
│
├── RELATÓRIOS
│   └── resumo executivo | evidências | impacto | severidade | CVSS | recomendações
│
├── ÉTICA
│   └── atuar apenas em sistemas autorizados | respeitar escopo | priorizar defesa
│
└── ESTILO DE RESPOSTA
    └── responder passo a passo | usar Markdown | separar fatos de hipóteses

=================================================
MEMÓRIA PERSISTENTE
=================================================

{json.dumps(self.memory, indent=2, ensure_ascii=False)}

=================================================
SOLICITAÇÃO DO USUÁRIO
=================================================

{user_input}

=================================================
FORMATO DA RESPOSTA
=================================================

1. Objetivo
2. Contexto
3. Análise
4. Possíveis riscos
5. Evidências observadas
6. Hipóteses
7. Próximos testes recomendados
8. Recomendações de mitigação
9. Resumo final
"""

    def analyze_payload(self, user_input: str) -> dict:
        logger.info(f"Iniciando análise de segurança para entrada de tamanho: {len(user_input)}")
        
        # Sanitização básica e detecção de Prompt Injection
        risk_score = 0
        indicators = ["system prompt", "ignore previous", "override instructions", "jailbreak"]
        for indicator in indicators:
            if indicator in user_input.lower():
                risk_score += 35
                
        if risk_score >= settings.SECURITY_THRESHOLD:
            logger.warning("Alerta de segurança: Tentativa de Prompt Injection detectada!")
            return {
                "status": "BLOCKED",
                "risk_score": risk_score,
                "response": "Acesso negado. Atividade suspeita detectada pelo Aegis Guard."
            }
            
        prompt = self.build_bughunter_prompt(user_input)
        payload = {
            "model": settings.LLM_MODEL,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            logger.info(f"Enviando requisição para o LLM em {settings.LLM_API_URL}")
            response = requests.post(settings.LLM_API_URL, json=payload, timeout=15.0)
            response.raise_for_status()
            result = response.json()
            
            # Atualiza memória simulada
            self.memory["historico_analises"].append(user_input[:100])
            
            return {
                "status": "ALLOWED",
                "risk_score": risk_score,
                "response": result.get("response", "Nenhum retorno do modelo.")
            }
        except requests.exceptions.Timeout:
            logger.error("Tempo limite excedido ao conectar ao LLM.")
            return {"status": "ERROR", "risk_score": 0, "response": "Erro: Tempo limite de conexão excedido."}
        except requests.exceptions.ConnectionError:
            logger.error("Falha de conexão física com o servidor LLM.")
            return {"status": "ERROR", "risk_score": 0, "response": "Erro: Não foi possível conectar ao servidor LLM."}
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"Erro HTTP retornado pelo LLM: {http_err}")
            return {"status": "ERROR", "risk_score": 0, "response": f"Erro HTTP: {response.status_code}"}
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            return {"status": "ERROR", "risk_score": 0, "response": "Erro interno do servidor."}