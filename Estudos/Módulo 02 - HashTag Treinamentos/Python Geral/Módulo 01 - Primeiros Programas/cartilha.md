# Cartilha para Consulta - 1ºs Códigos em Python

Essa cartilha é para revisão e consulta dor primeiros códigos que aprendemos. Na prática você vai acabar naturalmente decorando esses códigos a medida que formos usando mais no curso, mas essa cartilha pode te ajudar sempre que precisar.

### print(texto) -> Para "imprimir" (exibir) um texto ou uma variável

```python
print('O faturamento da loja foi de R$1.000')
```

### Textos (strings) são sempre entre aspas

'lira@gmail.com' -> é uma string 

lira@gmail.com -> vai dar erro porque o Python acha que isso é uma variável (vamos ver como funcionam mais a frente)

# Operações Mateméticas no Python:

1. Adição -> +
2. Subtração -> -
3. Divisão -> /
4. Multiplicação -> *
5. Mod (resto da divisão) -> %


### Adição
```python
print(3 + 5)
```
### Subtração
```python
print(5 - 3)
```
### Divisão
```python
print(5 / 3)
```
### Multiplicação
```python
print(5 * 3)
```
### Mod (resto da divisão de 5 por 3)
```python
print(5 % 3)
```
# Operações Básicas com String

1. Concatenar -> +
2. Verificar se um texto está contido dentro do outro -> in

### Concatenar
```python
print('O faturamento da loja foi ' + '1000')
```
### Verificar se um texto está dentro do outro
```python
print('@' in 'lira@gmail.com')
```
### Variável
```python
variavel = valor

faturamento = 1500
custo = 800
lucro = faturamento - custo 
print(faturamento)
print(lucro)
```
### Pegar informações do Usuário
```python
variavel = input('Texto para o Usuário')
```

### Para cadastrar um cliente
```python
cpf = input('Digite seu cpf (apenas números, sem pontos e traços)')
print('O cpf do cliente é ' + cpf)
```

# Misturando Tipos de Váriaveis
```python
faturamento = 2000
custo = 500
lucro = faturamento - custo

print('O faturamento da loja foi ' + str(faturamento) + '.O custo da loja foi ' + str(custo) + '.Assim, o lucro da loja foi de ' + str(lucro))
```

# Método format
Serve para formatar os prints sem precisar converter para String igual no exemplo acima.
```python
faturamento = 2000
custo = 500
lucro = faturamento - custo

print('O faturamento da loja foi {}. O custo da loja foi {}. Assim, o lucro da loja foi {}'.format(faturamento, custo, lucro))
```
# Condições no Python -> If

## Estrutura:

### Uso mais simples:

if condição:
    o que fazer caso a condição seja verdadeira

### Exemplo Real (informações 100% hipotéticas e inventadas):

Digamos que você trabalha na Amazon (que tem centenas de milhares, se não milhões de produtos) e está analisando o resultado de vendas dos produtos.

Você precisa criar um programa que vai analisar o resultado de vendas dos produtos da Amazon em um mês. Para simplificar vamos pensar em um único produto: um Iphone.

Meta de Vendas do Iphone = 50.000 unidades<br>
Quantidade vendida no Mês = 65.300 unidades

O seu programa deve avisar (usaremos o print por enquanto) caso o produto tenha batido a meta do mês. Então devemos fazer:<br>
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, o seu programa não deve fazer nada
```python
meta = 50000
qtde_vendida = 65300

if qtde_vendida > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendida))

```
### Tratando a condição falsa:
Quando usamos o if, nem sempre queremos apenas analisar o caso verdadeiro, em boa parte das vezes queremos fazer alguma coisa caso a condição seja verdadeira e fazer outra coisa caso a condição seja falsa.

Nesse caso usaremos:
```python
if condição:
    o que eu quero fazer caso a condição seja verdadeira
else:
    o que eu quero fazer caso a condição seja falsa
```

Voltando ao nosso Exemplo Real da Amazon e do Iphone, agora nossa programa deve avisar nos 2 casos:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, devemos exibir a mensagem: "Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades"
```python
meta = 50000
qtde_vendida = 15000

if qtde_vendida > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendida))
else:
    print('Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades'.format(qtde_vendida, meta))
```
