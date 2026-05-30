# =============================================================================
# --- INÍCIO DO ARQUIVO: test_notas.py ---
# =============================================================================
import unittest

# Importação das funções do módulo principal
from gerenciador_notas import calcular_media, verificar_aprovacao

class TestMotorAcademico(unittest.TestCase):
    """
    Suíte de testes de unidade para validação do núcleo operacional de notas.
    Garante a integridade matemática e o cumprimento das regras institucionais.
    """

    def test_condicoes_normais_aprovacao_reprovacao(self):
        """
        Valida o comportamento padrão do sistema para médias normais limpas.
        """
        # Teste de Aprovação
        notas_aprovacao = [8.0, 7.5, 8.5]
        media_aprovacao = calcular_media(notas_aprovacao)
        self.assertEqual(media_aprovacao, 8.0, "Erro: A média de [8.0, 7.5, 8.5] deve ser 8.0")
        self.assertEqual(
            verificar_aprovacao(media_aprovacao), 
            "Aprovado", 
            "Erro: Média 8.0 com corte padrão (7.0) deve retornar 'Aprovado'"
        )

        # Teste de Reprovação
        notas_reprovacao = [5.0, 6.0, 5.5]
        media_reprovacao = calcular_media(notas_reprovacao)
        self.assertEqual(media_reprovacao, 5.5, "Erro: A média de [5.0, 6.0, 5.5] deve ser 5.5")
        self.assertEqual(
            verificar_aprovacao(media_reprovacao), 
            "Reprovado", 
            "Erro: Média 5.5 com corte padrão (7.0) deve retornar 'Reprovado'"
        )

    def test_caso_extremo_lista_vazia(self):
        """
        Valida a resiliência do sistema (edge case) ao receber uma lista vazia,
        garantindo a prevenção do ZeroDivisionError.
        """
        notas_vazias = []
        media_vazia = calcular_media(notas_vazias)
        
        self.assertEqual(media_vazia, 0.0, "Erro Crítico: Lista vazia não retornou média 0.0")
        self.assertEqual(
            verificar_aprovacao(media_vazia), 
            "Reprovado", 
            "Erro Lógico: Aluno sem notas (média 0.0) deve ser 'Reprovado'"
        )

    def test_limitador_corte_zero(self):
        """
        Valida a estabilidade da função ao injetar o valor absoluto 0 (zero) 
        como média mínima de corte.
        """
        media_aluno = 0.0
        media_corte_zero = 0.0
        
        resultado_limite = verificar_aprovacao(media_aluno, media_minima=media_corte_zero)
        self.assertEqual(
            resultado_limite, 
            "Aprovado", 
            "Erro Lógico: Com corte absoluto em 0.0, a nota 0.0 deve resultar em 'Aprovado'"
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)

# =============================================================================
# --- FIM DO ARQUIVO: test_notas.py ---
# =============================================================================