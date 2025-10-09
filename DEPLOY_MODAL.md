# 🚀 Guia de Deploy no Modal.com

Este guia explica como fazer o deploy do projeto CoPlexi no Modal.com.

## 📋 Pré-requisitos

1. Conta no [Modal.com](https://modal.com)
2. Token de autenticação do Modal
3. Modelo treinado localmente (pasta `models_data/`)

---

## 🔧 Passo a Passo

### 1. Instalar o Modal CLI

Se ainda não instalou, rode:

```bash
source .venv/bin/activate
pip install modal
```

### 2. Autenticar no Modal

Execute o comando de autenticação e siga as instruções no navegador:

```bash
modal setup
```

ou

```bash
modal token new
```

Isso abrirá uma página no navegador para você fazer login e autorizar o CLI.

### 3. Verificar se o modelo está treinado

Certifique-se de que a pasta `models_data/` existe e contém os arquivos:

- `w2v_model.model`
- `classifier.pkl`

Se não existir, treine o modelo primeiro:

```bash
PYTHONPATH=.venv/lib/python3.12/site-packages:/usr/lib/python3.12 /usr/bin/python3 src/pipeline.py
```

### 4. Fazer o Deploy

Execute o seguinte comando para fazer o deploy:

```bash
modal deploy app.py
```

Este comando irá:

- Criar a imagem Docker com todas as dependências
- Fazer upload dos arquivos locais (src/, models_data/)
- Registrar a função no Modal

### 5. Testar a Função Deployada

Após o deploy, você pode testar a função de duas formas:

#### a) Via linha de comando:

```bash
modal run app.py
```

Isso executará a função `main()` definida no `app.py` com transações de teste.

#### b) Via código Python:

```python
import modal

app = modal.App.lookup("coplexi")
predict_fn = modal.Function.lookup("coplexi", "predict_on_modal")

transactions = [
    {"description": "Deposit from bank"},
    {"description": "Purchase at store"},
    {"description": "Transfer to account"}
]

result = predict_fn.remote(transactions)
print(result)
```

---

## 📊 Monitoramento

Você pode monitorar suas funções no painel do Modal:

1. Acesse: https://modal.com/apps
2. Encontre seu app "coplexi"
3. Visualize logs, métricas e invocações

---

## 🔄 Atualizar o Deploy

Para atualizar o código após modificações:

```bash
modal deploy app.py
```

---

## 💰 Custos

Modal oferece:

- **$30 de créditos gratuitos por mês** para novos usuários
- Pricing baseado em uso (CPU/GPU time)
- Sem custos quando a função não está rodando

---

## 🆘 Troubleshooting

### Erro: "Models not found"

- Certifique-se de que a pasta `models_data/` existe localmente
- Treine o modelo novamente se necessário

### Erro de autenticação

- Execute `modal token new` novamente
- Verifique se você está logado no navegador

### Dependências faltando

- Verifique o `requirements.txt`
- Certifique-se de que `modal` está listado

---

## 📝 Notas Importantes

1. **Arquivos locais**: O Modal faz upload dos diretórios `src/` e `models_data/` automaticamente via `image.add_local_dir()` (Modal 1.0+ API)

2. **Volumes**: Criamos um volume persistente `coplexi-models` para armazenar modelos (caso queira persistir entre deploys)

3. **Cold starts**: A primeira invocação pode demorar mais (1-2 min) enquanto a imagem é construída

4. **Logs**: Use `modal app logs coplexi` para ver logs em tempo real

---

## 🔗 Links Úteis

- [Documentação do Modal](https://modal.com/docs)
- [Exemplos Modal](https://modal.com/docs/examples)
- [Modal Discord](https://discord.gg/modal)
