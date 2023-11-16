# Query simples

Para acessar uma tabela de maneira simples basta usar o comando:
```
select * from NOME_DA_TABELA
```
Agora, caso a tabela tenha bastante informação pode-se usar um limitador:
```
select * from orders
limit 10
```
Ainda se pode acessar colunas especificas de certa tabela e criar uma uma nova coluna (temporaria, mas pode ser salvado) para acessar um tipo de dado
```
select product_name,
  unit_price,
  units_in_stock
  units_in_stock * unit_price as total_revenue -- Criando uma nova coluna temporaria
from products
```
Pode-se, também, filtrar os dados:
```
select * from employees
where city = 'London'
```
ou 
```
select * from employees
where hire_date >= '1993-01-01'
```
ou 
```
select * from employees
where first_name like 'M%'
```

# Funções agragadas

Dentro de funções agragadas pordemos destacar estes tipos
+ Contagem
+ Soma
+ Media
+ Máximo
+ Mínimo

**Soma**
Soma os valores que estão em uma lista
```
select sum(quantity) as total_unit_sold from order details
```
Além da soma pode-se separar esta soma por um agrupamento 
```
select product_id, sum(quantity) as total_unitys_sold -- Separando dois grupos
from order_details
group by product_id -- Criando o grupo
order by total_units_sold desc -- Organizando o grupo
```
**Contagem**

Agora, com essa mesma estrutura podemos fazer uma analise mensal
```
select date_trunc('month', order_date) as order_month, count(order_id) -- Organiza as informacoes pelo mes com date_trunc
from orders
group by order_month
order by order_month
```
Outra forma de procurar os produtos
```
select product_id, sum(quantity) as total_unitys_sold -- Separando dois grupos
from order_details
group by product_id -- Criando o grupo
having sum(quantity) <= 1000 -- Procurando os valores que sao maiores ao igual a mil
```

# Joins
Dependendo de como o banco de dados foi montando é interssante de se juntar tabelas diferentes para ter uma visualização mais ampla de como tudo funciona. 
Para isso podemos ter as seguintes relações
+ Inner join (A intercessão com B)
+ Right Join (A intercessão com B E A)
+ Left Join (A intercessão com B E B)
+ Full Join (A E B)

```
Select
  product_name,
  quantity_per_unit,
  unit_price,
  category_name,
  description
from products
inner join categories on
categories.category_id = products.category_id
```
Neste código 'categories' e 'products' são tables diferentes mas possuem 'category_id' em ambas. Para isso foi mostrado as características do produto de 'products' com o que possui em comum em 'category_id'

# Queries complexas

Para compreender melhor este tópico é fundamental trabalhar com um exemplo

**Exemplo:** Como encontrar os pedidos que possuem uma quantidade maior do que a quanitade media de pedidos

```
select *
from order_details
where quantity <
  (
  select avg(quantity)
  from order_details
  )
```
Outra forma de trabalhar é utilizando o CTE (como se fosse uma função)

```
with avarage as (
  select avg(quantity) as avarage_quantity
  from order_details
)
select *
from order_details, avarage
where quantity > avarage.avarage_quantity
```

































