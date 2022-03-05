<!-- @format -->

<h1 align="center">
  Entrega - Leads
</h1>

<p align = "center">
Esta é uma API hospedada no Heroku onde é possível realizar requisições seguindo os parâmetros abaixo.
</p>

<p align="center">
  <a href="#endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

## **Endpoints**

A API tem um total de 4 endpoints, aplicação capaz de realizar um CRUD completo.
Lead: São pessoas que podem estar interessadas em algum tipo de
produto ou serviço. Esses possíveis futuros clientes podem ser coletados através de preenchimento de formulários ou cliques em
páginas da internet, os dados geralmente são utilizados em campanhas publicitárias.<br/>
O JSON para utilizar no Insomnia é este aqui ->
[Arquivo](Insomnia_2022-03-05.json)

Para importar o JSON no Insomnia é só clicar na palavra "Insomnia" no canto superior esquerdo. Nesse dropdown é só clicar em "Import / Export > Import Data > From Url" e colocar o link acima :v:

O url base da API é https://leads-maria.herokuapp.com/

## Nenhuma das rotas precisam de autenticação

<h2 align ='center'> Registra um novo Lead </h2>

`POST /leads - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /leads - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "(41)90000-0000",
  "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
  "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
  "visits": 1
}
```

<h2 align ='center'> Possíveis erros </h2>

E-mail e telefone único:

`POST /leads - `
` FORMATO DA RESPOSTA - STATUS 409`

```json
{
  "msg": "Email or phone already exists"
}
```

Telefone obrigatoriamente no formato (xx)xxxxx-xxxx:

`POST /leads - `
` FORMATO DA RESPOSTA - STATUS 409`

```json
"msg: Phone must be in the format (xx)xxxxx-xxxx"
```

Corpo da requisição obrigatoriamente apenas com name, email e phone:

`POST /leads - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "wrong fields"
}
```

Corpo da requisição sendo todos os campos do tipo string:

`POST /leads - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "fields must be strings"
}
```

<h2 align ='center'> Lista todos os LEADS por ordem de visitas, do maior para o menor. </h2>

`GET /leads - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 3,
    "name": "maria",
    "email": "john1@email.com",
    "phone": "(92)99380-4205",
    "creation_date": "Sun, 03 Apr 2022 13:44:00 GMT",
    "last_visit": "Sun, 03 Apr 2022 13:44:00 GMT",
    "visits": 1
  },
  {
    "id": 5,
    "name": "maria",
    "email": "maria@gmail.com",
    "phone": "(92)99380-4206",
    "creation_date": "Sun, 03 Apr 2022 13:45:00 GMT",
    "last_visit": "Sun, 03 Apr 2022 13:45:00 GMT",
    "visits": 1
  },
  {
    "id": 9,
    "name": "maria",
    "email": "maria1@gmail.com",
    "phone": "(92)99380-4207",
    "creation_date": "Sun, 03 Apr 2022 14:16:00 GMT",
    "last_visit": "Sun, 03 Apr 2022 14:16:00 GMT",
    "visits": 1
  }
]
```

<h2 align = "center"> Atualizar apenas o valor de visits e last_visit.</h2>

`PATCH /leads- FORMATO DA REQUISIÇÃO`

```json
{
  "email": "john@email.com"
}
```

<h2 align ='center'> Possíveis erros: </h2>
```

Corpo da requisição obrigatoriamente apenas com email:

`PATCH /leads - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "request must be passsed only email"
}
```

Deve ser uma string:

`PATCH /leads - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "field must be string"
}
```

Caso o e-mail não seja encontrado:

`PATCH /leads - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "No data found"
}
```

Caso dê tudo certo, a resposta será assim:

`PATCH /leads - FORMATO DA RESPOSTA - STATUS 204`

```json
No body returned for response
```

<h2 align = "center"> Deletar um Lead específico.</h2>

`DELETE /leads- FORMATO DA REQUISIÇÃO`

```json
{
  "email": "john@email.com"
}
```

<h2 align ='center'> Possíveis erros: </h2>

Corpo da requisição obrigatoriamente apenas com email:

`DELETE /leads -`
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "request must be passsed only email"
}
```

Deve ser uma string:

`DELETE /leads -`
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "field must be string"
}
```

Caso o e-mail não seja encontrado:

`DELETE /leads -`
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "msg": "No data found"
}
```

Caso dê tudo certo, a resposta será assim:

`DELETE /leads - FORMATO DA RESPOSTA - STATUS 204`

```json
No body returned for response
```

---

Feito com ♥ by maria-baia :wave:
