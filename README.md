📦 ConsultarCEP — Consulta de Endereço via CEP (Python)

Projeto criado em Python para consultar informações de endereço usando a API pública ViaCEP.
Simples, direto e perfeito para quem está aprendendo consumo de APIs no back-end.

🔧 Tecnologias utilizadas

Python 3

Requests (biblioteca)

ViaCEP API

🚀 Funcionalidades

✔️ Validação automática do CEP

✔️ Limpeza (remove hífen automaticamente)

✔️ Consulta via API

✔️ Exibe rua, bairro, cidade e estado

✔️ Histórico de CEPs pesquisados

✔️ Tratamento completo de erros

📁 Estrutura do projeto
```
ConsultarCEP/
│
├── consultaCEP.py   # Código principal
└── README.md        # Documentação
```

▶️ Como executar

Instale a biblioteca necessária:

```pip install requests```


Execute o arquivo:

```python consultaCEP.py```


## 🖥️ Exemplo de uso

```bash
Digite um CEP (ou 'sair' para encerrar): 02998260

Endereço encontrado:
Rua: Rua Henrique Salvatori
Bairro: Conjunto City Jaraguá
Cidade: São Paulo
Estado: SP

Digite um CEP (ou 'sair' para encerrar): sair

Histórico de CEPs consultados:
- 02998260
```



🔮 Melhorias futuras

📝 Salvar histórico em TXT

🌐 Criar API com Flask/FastAPI

🖼️ Criar interface gráfica (Tkinter)

🧪 Adicionar testes unitários

📜 Licença

Livre para estudo e modificações.
