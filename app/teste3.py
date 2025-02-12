from datetime import datetime

# Funções de Banco de Dados Simuladas
# Vamos simular a estrutura de dados com um dicionário para representar as vagas e os pagamentos
vagas = {
    1: {"status": "Disponível", "veiculo": None},
    2: {"status": "Disponível", "veiculo": None},
    3: {"status": "Disponível", "veiculo": None},
    4: {"status": "Disponível", "veiculo": None},
    5: {"status": "Disponível", "veiculo": None}
}

# Função para registrar o pagamento
def registrar_pagamento(veiculo, forma_pagamento, valor):
    print(f"Pagamento do veículo {veiculo} registrado!")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Valor pago: R${valor:.2f}")

# Função para calcular o valor com base no tipo de veículo
def calcular_tarifa(tipo_veiculo):
    if tipo_veiculo == "Grande Porte":
        return 50.00  # Tarifa para veículos grandes
    elif tipo_veiculo == "Pequeno":
        return 20.00  # Tarifa para veículos pequenos
    else:
        return 30.00  # Tarifa padrão para outros veículos

# Função para calcular o tempo de permanência do veículo
def calcular_tempo_permanencia(entrada, saida):
    tempo_permanencia = saida - entrada
    return tempo_permanencia

# Função para alterar o status da vaga
def alterar_status_vaga(vaga_id, novo_status):
    vagas[vaga_id]["status"] = novo_status
    print(f"Vaga {vaga_id} agora está {novo_status}")

# Função para ocupar a vaga
def ocupar_vaga(vaga_id, veiculo, tipo_veiculo, entrada):
    if vagas[vaga_id]["status"] == "Disponível":
        vagas[vaga_id]["veiculo"] = veiculo
        vagas[vaga_id]["status"] = "Ocupada"
        tarifa = calcular_tarifa(tipo_veiculo)
        print(f"Vaga {vaga_id} ocupada por {veiculo}. Tarifa: R${tarifa:.2f}")
        return entrada, tarifa
    else:
        print(f"Vaga {vaga_id} já está ocupada!")
        return None, None

# Função para liberar a vaga
def liberar_vaga(vaga_id, saida):
    veiculo = vagas[vaga_id]["veiculo"]
    if veiculo:
        tempo = calcular_tempo_permanencia(vagas[vaga_id]["entrada"], saida)
        print(f"Veículo {veiculo} ficou {tempo} horas no estacionamento.")
        vagas[vaga_id]["veiculo"] = None
        vagas[vaga_id]["status"] = "Disponível"
        print(f"Vaga {vaga_id} liberada.")
    else:
        print(f"Vaga {vaga_id} já está livre.")

# Função para listar as vagas
def listar_vagas():
    for vaga_id, vaga in vagas.items():
        print(f"Vaga {vaga_id}: {vaga['status']} - Veículo: {vaga['veiculo']}")

# Testando as funções
def main():
    # Exemplo de ocupação e liberação de vagas
    print("#### Ocupando Vagas ####")
    entrada1 = datetime(2025, 2, 12, 10, 30)
    entrada2 = datetime(2025, 2, 12, 11, 00)
    entrada3 = datetime(2025, 2, 12, 12, 00)
    
    # Veículos que irão ocupar as vagas
    ocupar_vaga(1, "ABC-1234", "Pequeno", entrada1)
    ocupar_vaga(2, "XYZ-5678", "Grande Porte", entrada2)
    ocupar_vaga(3, "LMN-1234", "Pequeno", entrada3)
    
    # Listar vagas após ocupação
    listar_vagas()
    
    # Exemplo de pagamento
    registrar_pagamento("ABC-1234", "Cartão de Débito", 20.00)
    
    # Exemplo de liberação de vaga
    saida1 = datetime(2025, 2, 12, 14, 30)
    saida2 = datetime(2025, 2, 12, 13, 00)
    
    liberar_vaga(1, saida1)
    liberar_vaga(2, saida2)
    
    # Listar vagas após liberação
    listar_vagas()

# Executar a função principal
if __name__ == "__main__":
    main()
