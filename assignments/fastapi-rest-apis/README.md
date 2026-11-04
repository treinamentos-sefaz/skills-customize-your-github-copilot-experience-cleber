# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST funcional usando o framework FastAPI, aprendendo os conceitos fundamentais de criação de endpoints, validação de dados e boas práticas de design de APIs.

## 📝 Tarefas

### 🛠️ Tarefa 1: Criar seu Primeiro Endpoint

#### Descrição
Nesta tarefa você vai criar uma API FastAPI básica com um simples endpoint GET que retorna dados estáticos. Você aprenderá como inicializar uma aplicação FastAPI e como criar seu primeiro endpoint.

#### Requisitos
O programa concluído deve:

- Importar e inicializar a aplicação FastAPI
- Criar um endpoint GET na rota `/` que retorna uma mensagem de boas-vindas em JSON
- Incluir um endpoint GET `/items/{item_id}` que retorna informações sobre um item baseado no ID passado na URL
- Executar o servidor usando `uvicorn` (você pode testar rodando `uvicorn main:app --reload`)

#### Dicas
- Use `@app.get()` como decorator para definir endpoints GET
- Parâmetros de caminho (path parameters) são definidos usando chaves: `{item_id}`
- FastAPI automaticamente converte respostas para JSON


### 🛠️ Tarefa 2: Adicionar Validação e Modelos de Dados

#### Descrição
Agora você vai expandir sua API adicionando requisições POST, criando modelos de dados validados com Pydantic, e aprendendo como validar automaticamente as entradas do usuário.

#### Requisitos
O programa concluído deve:

- Criar um modelo Pydantic `Item` com campos: `name` (string), `description` (string opcional), `price` (float positivo) e `tax` (float opcional)
- Implementar um endpoint POST `/items/` que recebe um objeto Item no corpo da requisição
- Armazenar temporariamente os itens criados em uma lista na memória
- Criar um endpoint GET `/items/` que retorna a lista de todos os itens criados
- Validação automática: se alguém enviar um price negativo, a API deve rejeitar com erro apropriado

#### Dicas
- Importe `BaseModel` de `pydantic` para definir seus modelos
- Use `@app.post()` para criar endpoints que recebem dados
- Use `Optional[]` do módulo `typing` para campos opcionais
- Use `Field()` do Pydantic para adicionar validações (ex: `price: float = Field(..., gt=0)`)


### 🛠️ Tarefa 3: Implementar CRUD Completo com Status Codes

#### Descrição
Aqui você vai criar uma API completa de CRUD (Create, Read, Update, Delete) para gerenciar items, implementando todas as operações HTTP padrão e retornando os status codes apropriados.

#### Requisitos
O programa concluído deve:

- Manter um armazenamento em memória com IDs auto-incrementais para cada item criado
- Endpoint POST `/items/` que retorna status code 201 (Created) com o item criado incluindo seu ID
- Endpoint GET `/items/{item_id}` que retorna um item específico ou status 404 se não encontrado
- Endpoint PUT `/items/{item_id}` que atualiza um item existente, ou retorna 404 se não encontrado
- Endpoint DELETE `/items/{item_id}` que remove um item ou retorna 404 se não encontrado
- Implementar tratamento de erros apropriado com mensagens descritivas usando `HTTPException`

#### Dicas
- Use um dicionário para armazenar items com seus IDs como chaves
- Importe `HTTPException` e `status` de `fastapi`
- Use `status.HTTP_201_CREATED` para POST bem-sucedido
- Use `@app.put()` e `@app.delete()` para implementar as outras operações
- Retorne status 404 quando o recurso não for encontrado
