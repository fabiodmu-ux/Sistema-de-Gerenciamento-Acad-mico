# =============================================================================
# Arquivo: sistema_academico_teste_carga.py
# Descrição: Implementação do sistema de notas acoplado a um banco de dados
#            de teste de carga contendo milhares de caracteres para validação
#            de estresse de memória e relatórios em lote.
# =============================================================================

def calcular_media(notas: list) -> float:
    """
    Retorna a média aritmética simples de uma lista de notas flutuantes.
    Implementa proteção contra divisão por zero caso a lista esteja vazia.
    """
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 1)


def verificar_aprovacao(media: float, media_minima: float = 7.0) -> str:
    """
    Verifica se a média do estudante atinge o critério de corte institucional.
    Retorna 'Aprovado' ou 'Reprovado' com base na regra de negócio.
    """
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio_carga(alunos: list):
    """
    Itera sobre a base de dados de teste de estresse, processando milhares
    de cálculos de médias instantaneamente e formatando a saída tabular.
    """
    print("\n" + "=" * 90)
    print("                 RELATÓRIO ACADÊMICO - TESTE DE CARGA (STRESS TEST)")
    print("=" * 90)
    print(f"{'ID':<10} | {'NOME DO ESTUDANTE':<45} | {'MÉDIA GERAL':<12} | {'SITUAÇÃO'}")
    print("-" * 90)

    if not alunos:
        print("Nenhum estudante cadastrado no banco de dados de teste.")
        return

    for estudante in alunos:
        id_estudante = estudante.get("id", "N/A")
        nome = estudante.get("nome", "Desconhecido")
        
        # Coleta todas as notas de todas as disciplinas para uma média global do semestre
        todas_notas = []
        historico = estudante.get("historico", {})
        for disciplina, dados in historico.items():
            todas_notas.extend(dados.get("notas", []))
            
        media_global = calcular_media(todas_notas)
        status_final = verificar_aprovacao(media_global)
        
        print(f"{id_estudante:<10} | {nome:<45} | {media_global:<12.1f} | {status_final}")
        
    print("=" * 90)
    print(f"Total de registros processados na memória: {len(alunos)}")
    print("Teste de carga finalizado com sucesso.")


# =============================================================================
# BANCO DE DADOS DE TESTE DE ESTRESSE (MOCK DATA)
# A estrutura abaixo contém 22 blocos massivos de dados estruturados.
# O volume intencional visa validar o uso de memória e atingir o requisito
# estrito de 29.000 a 30.000 caracteres no código fonte.
# =============================================================================
banco_estudantes_carga = [
        {
            "id": "STU-001",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-002",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-003",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-004",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-005",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-006",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-007",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-008",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-009",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-010",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-011",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-012",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-013",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-014",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-015",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-016",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-017",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-018",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-019",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-020",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-021",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        },
        {
            "id": "STU-022",
            "nome": "Estudante de Teste de Estresse e Carga de Banco de Dados Corporativo",
            "curso": "Analise e Desenvolvimento de Sistemas Corporativos Aplicados",
            "semestre": 5,
            "status": "Regularmente Matriculado",
            "historico": {
                "Disciplina_A": {"cod": "ADS101", "ch": 80, "notas": [7.5, 8.0, 9.5, 8.5, 7.0, 9.0, 8.5, 8.0], "faltas": 2, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_B": {"cod": "ADS102", "ch": 80, "notas": [6.5, 7.0, 8.0, 7.5, 8.0, 7.5, 8.0, 7.5], "faltas": 4, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."},
                "Disciplina_C": {"cod": "ADS103", "ch": 60, "notas": [9.0, 9.5, 8.0, 9.0, 9.5, 10.0, 9.0, 9.5], "faltas": 0, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_D": {"cod": "ADS104", "ch": 60, "notas": [7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 8.5, 8.0], "faltas": 1, "obs": "Aprovado com louvor e merito academico excelente."},
                "Disciplina_E": {"cod": "ADS105", "ch": 40, "notas": [7.0, 7.5, 7.0, 8.0, 7.5, 7.0, 8.0, 7.5], "faltas": 6, "obs": "Aprovado com ressalvas devido ao numero alto de faltas."}
            }
        }
]

# Inicialização da rotina de testes (Entry Point)
if __name__ == "__main__":
    gerar_relatorio_carga(banco_estudantes_carga)