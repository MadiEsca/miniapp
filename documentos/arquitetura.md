# Arquitetura

Aqui irei colocar algumas informações sobre as decisões que vou tomar sobre o desenvolvimento desse projeto. Essa é apenas uma anotação para minha consulta pessoal futura, se você por acaso não for eu, vale o aviso de que isso não segue nenhum padrão de organização além da forma que meu raciocínio funciona.

## Informações sobre o sistema
O backend será feito utilizando python
O frontend será feito utilizando react
O banco de dados será o postgreSQL
Toda a infraestrutura será montadada dentro de um container docker
Vou utilizar alguns outros sistemas como base da contrução desse SGE simplificado
Será um sistema para uma escola no estilo do SESI/SENAI, onde o ensino médio é integrado com o ensino técnico profissional

## Definições
- Qual a diferença entre TURMA x DISCIPLINA
    Estou considerando uma escola de ensino médio integrada com o ensino técnico, dessa forma um único aluno pode estar matriculado em diferentes turmas, como por exemplo, uma única **turma do ensino médio** (tem várias **disciplinas**) e uma turma do ensino técnico.
- Turma
    Um aluno poderá estar matriculado em APENAS UMA TURMA DO ENSINO MÉDIO e a uma ou mais turmas do ensino técnico. Dessa forma, uma turma contém mais de uma disciplina, da mesma forma que acontece no mundo real.
- Disciplina
    Um aluno poderá estar matriculado A UMA OU MAIS DISCIPLINAS, dado que uma turma contém diversas disciplinas.


## Telas

0. Tela de login
    - Assim que o usuário entrar no sistema, irá aparecer essa tela de login, que será por onde iremos identificar o tipo de usuário que está tentando ver as informações do sistema, podendo ser de um dos 5 tipos:
        - Aluno -> Só terá acesso à informações referentes ao seu desempenho individual dentro de sala, como faltas, boletins, notas individuais em cada matéria, entre outras informações referentes APENAS ao seu desempenho escolar. Não será exibido informações pessoais, como endereço, cpf, telefone entre outras, sendo essas informações exclusivas apenas a diretoria e administradores. Além disso, também será possível realizar reclamações sobre professores e serviços da escola de forma completamente anônima.
        - Professor -> Terá acesso somente às informações referentes às disciplinas e turmas pela qual ele é responsável. Dessa forma, ele poderá adicionar e alterar notas dos alunos, lançar faltas, reclamações, encaminhamentos a diretoria e advertências. Da mesma forma que o aluno, ele terá acesso as informações de desempenho dos alunos de suas turmas, referentes apenas à sua disiplina, além disso ele não terá acesso à outras informações pessoais dos alunos, apenas ao nome.
        - Diretoria -> Terá acesso a todas as informações dos alunos e professores da escola. Poderá lançar reclamações, advertências e suspensões, todas elas com sua devida justificativa à tal. Terá acesso às notas de todas as disciplinas e turmas que o aluno estiver matriculado, da mesma forma que poderá visualizar as anotações e encaminhamentos dados pelos professores ao aluno em questão, desta forma o mesmo poderá ser feito em relação às reclamações direcionadas aos professores pelos alunos.
        - Pais -> Terão o mesmo nível de acesso que os alunos, com a possibilidade de verem as reclamações, advertências e suspensões direcionadas à seus filhos.
        - Adminstradores -> Terão acesso irrestrito à todas as funcionalidades do sistema.

1. Tela inicial/Dashboard
    -  Será a primeira tela a aparecer, de forma similar a do Valorizza, mostrando informações gerais sobre os alunos, notas, desempenho da escola e desempenho escolar,de acordo com o nível de acesso do usuário em questão.
    - Será um dashboard com as principais informações do sistema, como:
        - média de notas por turma
        - quantidade de alunos matriculados
        - dados sobre as turmas
        - quantidade de professores
        - Além de outras, isso se dará por uma análise mais a frente de acordo com as necessidades iniciais do sistema.
2. Tela de consulta
3. Tela de lançamento de notas
4. Tela de cadastro (apenas administradores/diretoria)

Essas serão as telas inicias, dado que esse será apenas um MVP do projeto final, que, obviamente, será continuado.

---
## MVP

### Primeira etapa
- Montar a infra no docker
- 3 Telas iniciais (Cadastro, consulta, lançamento de notas)
- 3 Entidades inicias (aluno, professor, administrador)
- Templates de html puro
- Apenas python inicialmente

### Segunda etapa
- Separação do back e do front
- Back-end será uma api em python
- Front-end será reconstruído com react

### Terceira etapa
- Aplicar autenticação (tela de login e telas específicas)
- Criar os outros tipos de usuário
- Disponibilizar o sistema para as pessoas (nessa etapa, irei configurar para que todos possam ser administradores)


---
## Etapas de desenvolvimento
São o passo a passo para o desenvolvimento de um MVC. Vou começar desenvolvendo ele com html cru enquanto integro reatividade com o python. Posteriormente incorporo uma api criada em python com o front-end em react.

- criação do ambiente no docker
- conexao com o banco de dados
- models criados
- controlers criados
- templates criados
- a interação entre cada um funciona

Após isso ser concluído:
- prototipação das telas
- criação das telas com react
- criação da api em python 

---

## TO-DO
- Criar diagrama de classe das entidades do sistema
- Planejar as outras telas
- Esboçar telas