# Lesson

## Data types

Para descobrir qual é o melhor data type para o seu caso é necessário conferir na documentação do postgreesql

> obs: Normalmente para espaços de texto é intressante, para a própria segurança do banco de dados. Limitar o espaço de texto

## Modelagem de entidades

Uma ótima ferramenta para construir diagramas de entendidades é o VisualParadigm

Para construir uma entidade é necessário
+ Nome da entidade
+ Atributos
+ Tipos de atributos
+ Chave primaria

## Modelagem de relacionamento

Para relacionar as entidades é necessário cirar uma chave estrangeira e estipular o tipo de relacionamento. São eles:
+ 1 - 1 ( uma entidade para uma entidade )
+ 1 - n ( uma enteidade para n entidades )
+ n - n ( n entidades para n entidades )

## Normalização de dados

**Primeira forma normal**

+ Cada atributo deve possuir um único valor correspondente

**Segunda forma normal**

+ Cada elemento deve se atribuir a uma única chave primaria

> obs: Há outras regras para a normalização. Por enquanto basta estas duas.

## Inserindo tabelas no banco

Para criar uma tabela é importante ter uma esquema já montado. Depois basta usar o esquema de comandos:

```
# Exemplo de Entidade

create table professores(
    id_professor integer,
    celular varchar(14),
    nome varchar(40),
    id_disciplina integer,
    primary key (id_professor),
    foreign key (id_disciplina)
    references disciplinas(id_disciplina)
)
```

## Para inserir dados ao banco

Fazendo o processo manualmente:
```
# Adicionando valores para professores

insert into professores values
(1, 123456789, 'Tiago da Silva', 1),
(2, 987654321, 'Lucas Monteiro', 2)
```

Fazendo por arquivo .csv

```
copy professores(id_professor, celular, nome, id_disciplina)
from 'local_do_arquivo'
delimiter ',' # O separador das informações
csv header # Exclui a primeira linha do .csv
```

## Para atualizar e remover dados

Para atualizar

```
update professores set nome = 'Thiago da Silva'
where id_professor = 1
```

Para remover

```
delete from professores
where id_professor = 2
```

## Permissionamento e Views

Na hora de criar um banco de dados é necessário proteger certos dados sensíveis para se conter à **LGPD**. Um jeito interessante de resolver isso é com as views:

```
create view professor_com_sigilo as
(
    select
        celular
    from professores
)
```

## Indices

É uma forma de agilizar o processo de buscas em base de dados maiores. É importante ressaltar que adiocionar indicies em tabelas que estão em contate estado de update não é interessante adicionar um indice.