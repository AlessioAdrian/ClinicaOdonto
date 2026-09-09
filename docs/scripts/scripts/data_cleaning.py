import pandas as pd
from datetime import datetime

def preparar_lista_reativacao(arquivo_entrada, arquivo_saida):
    print("Iniciando leitura da base legada...")
    
    try:
        # Carrega o CSV bruto do sistema odontológico
        df = pd.read_csv(arquivo_entrada)
        
        # Converte a coluna de data para o formato datetime
        df['data_ultimo_atendimento'] = pd.to_datetime(df['data_ultimo_atendimento'], format='%Y-%m-%d')
        
        # Calcula a diferença em dias
        hoje = datetime.now()
        df['dias_inativo'] = (hoje - df['data_ultimo_atendimento']).dt.days
        
        # Filtra pacientes com mais de 3 anos (1095 dias) de inatividade
        df_reativacao = df[df['dias_inativo'] >= 1095].copy()
        
        # Seleciona apenas as colunas necessárias para o Make/WhatsApp
        colunas_finais = ['nome', 'telefone', 'data_ultimo_atendimento']
        df_reativacao = df_reativacao[colunas_finais]
        
        # Salva o arquivo higienizado
        df_reativacao.to_csv(arquivo_saida, index=False)
        print(f"Sucesso! {len(df_reativacao)} pacientes filtrados para a régua de reativação.")
        
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    # Nomes dos arquivos de origem e destino
    entrada = "base_bruta_clinica.csv"
    saida = "pacientes_prontos_para_IA.csv"
    preparar_lista_reativacao(entrada, saida)
