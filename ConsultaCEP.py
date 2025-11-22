# Importa a biblioteca requests para fazer requisições HTTP
import requests as req

# Função para ler o CEP do usuário
def ler_cep(mensagem):
    """
    Solicita ao usuário que digite um CEP.
    Remove espaços em branco no início e fim.
    Retorna o CEP como string.
    """
    try:
        cep = input(mensagem).strip()
        return cep
    except:
        print("Erro ao ler o CEP.")
        return ""

# Função para buscar os dados do CEP usando a API ViaCEP
def buscar_cep(cep):
    """
    Faz uma requisição à API ViaCEP para obter informações do CEP.
    Retorna um dicionário com logradouro, bairro, cidade e estado.
    Retorna None se o CEP não for encontrado ou ocorrer um erro.
    """
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = req.get(url)

        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            dados = resposta.json()

            # Verifica se a API retornou erro
            if "erro" in dados:
                return None

            # Retorna as informações do endereço em um dicionário
            return {
                "logradouro": dados["logradouro"],
                "bairro": dados["bairro"],
                "cidade": dados["localidade"],
                "estado": dados["uf"]
            }
        else:
            return None

    except Exception as erro:
        print("Erro ao acessar a API:", erro)
        return None

# Lista para armazenar o histórico de CEPs consultados
historico = []

# Loop principal do programa
while True:
    # Solicita o CEP ao usuário
    cep = ler_cep("Digite um CEP (ou 'sair' para encerrar): ")

    # Condição para encerrar o programa
    if cep.lower() == "sair":
        print("Finalizando...")
        break

    # Remove hífen do CEP e valida se tem exatamente 8 números
    cep = cep.replace("-", "")
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido! Digite exatamente 8 números.")
        continue  # Volta ao início do loop para pedir o CEP novamente

    # Busca os dados do CEP
    resultado = buscar_cep(cep)

    # Exibe os resultados encontrados ou mensagem de erro
    if resultado:
        print("\nEndereço encontrado:")
        print(f"Rua: {resultado['logradouro']}")
        print(f"Bairro: {resultado['bairro']}")
        print(f"Cidade: {resultado['cidade']}")
        print(f"Estado: {resultado['estado']}")

        # Adiciona o CEP ao histórico
        historico.append(cep)
    else:
        print("Não foi possível encontrar o endereço.")

# Exibe o histórico de CEPs consultados, se houver
if historico:
    print("\nHistórico de CEPs consultados:")
    for c in historico:
        print("-", c)
