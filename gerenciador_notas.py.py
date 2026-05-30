# =============================================================================
# --- INÍCIO DO ARQUIVO: gerenciador_notas.py ---
# =============================================================================
"""
Módulo Principal do Sistema de Gerenciamento Acadêmico.
Responsável pelo motor lógico de cálculos, regras institucionais
e interface de apresentação de relatórios.
"""

from typing import Optional, List

def calcular_media(notas: Optional[List[float]]) -> float:
    """
    Calcula a média aritmética simples de uma lista de avaliações.

    Esta função recebe um conjunto numérico (notas) e processa o 
    resultado algébrico. Implementa proteção contra divisão por zero, 
    assegurando a estabilidade do sistema caso um estudante ainda 
    não possua notas cadastradas.

    Args:
        notas (Optional[List[float]]): Uma lista contendo as notas do estudante. 
                                       Espera-se que contenha valores numéricos.
                                       Caso seja None ou vazia, será tratado.

    Returns:
        float: O valor da média calculada, arredondado para uma casa decimal.
               Retorna 0.0 se a lista 'notas' estiver vazia ou for None.
    """
    if not notas:
        return 0.0
        
    media_calculada = sum(notas) / len(notas)
    return round(media_calculada, 1)


def verificar_aprovacao(media: float, media_minima: float = 7.0) -> str:
    """
    Determina a situação acadêmica do estudante com base em sua média.

    Compara a média final obtida pelo estudante com a nota de corte 
    estabelecida pela instituição. A função atua de forma determinística 
    e flexível.

    Args:
        media (float): A nota média final calculada para o estudante.
        media_minima (float, optional): A nota de corte exigida pela instituição 
                                        para a aprovação. O valor padrão é 7.0.

    Returns:
        str: 'Aprovado' caso a média do estudante seja maior ou igual 
             à média mínima; 'Reprovado' caso contrário.
    """
    if media >= media_minima:
        return "Aprovado"
    return "Reprovado"


def gerar_relatorio(alunos: list[dict], media_minima: float = 7.0) -> None:
    """
    Gera e exibe no terminal um relatório acadêmico formatado.

    Processa as notas para obter a média de forma otimizada, ordena os 
    estudantes por desempenho, determina a situação e apresenta os dados 
    em formato tabular. Também gera estatísticas gerais da turma.

    Args:
        alunos (list[dict]): Lista de dicionários contendo os dados dos estudantes.
        media_minima (float): Média mínima exigida para aprovação (padrão 7.0).
    """
    print("\n" + "=" * 65)
    print(f"{'RELATÓRIO ACADÊMICO DE DESEMPENHO':^65}")
    print("=" * 65)
    print(f"{'NOME DO ESTUDANTE':<30} | {'MÉDIA':<7} | {'SITUAÇÃO'}")
    print("-" * 65)

    if not alunos:
        print("Nenhum estudante cadastrado no sistema no momento.")
        print("=" * 65 + "\n")
        return

    # Pré-cálculo de dados ($O(n)$ otimizado)
    dados_processados = []
    for estudante in alunos:
        nome = estudante.get("nome", "Nome não informado")
        notas = estudante.get("notas", [])
        media = calcular_media(notas)
        dados_processados.append((nome, media, notas))

    # Ordenação por média (ranking decrescente)
    alunos_ordenados = sorted(dados_processados, key=lambda x: x[1], reverse=True)

    # Exibição tabular
    for nome, media, notas in alunos_ordenados:
        situacao = verificar_aprovacao(media, media_minima)
        print(f"{nome:<30} | {media:<7.1f} | {situacao}")
        
    # Estatísticas gerais
    print("-" * 65)
    media_turma = sum(media for _, media, _ in alunos_ordenados) / len(alunos_ordenados)
    maior_desempenho = alunos_ordenados[0]
    menor_desempenho = alunos_ordenados[-1]

    print(f"Média geral da turma: {media_turma:.2f}")
    print(f"Maior média: {maior_desempenho[0]} ({maior_desempenho[1]:.2f})")
    print(f"Menor média: {menor_desempenho[0]} ({menor_desempenho[1]:.2f})")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    # População do banco de dados em memória para execução de demonstração
    escola_db = [
        {"nome": "Ana Silva", "notas": [8.0, 9.5, 8.5]},
        {"nome": "Carlos Sousa", "notas": [5.0, 4.5, 6.0]},
        {"nome": "Beatriz Lemos", "notas": [7.0, 7.0, 7.0]},
        {"nome": "Estudante Novo", "notas": []}  # Teste de robustez visual
    ]
    
    # Chamada do componente de visão
    gerar_relatorio(escola_db)

# =============================================================================
# --- FIM DO ARQUIVO: gerenciador_notas.py ---
# =============================================================================