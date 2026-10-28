# Requisitos

Esse projeto é a criação de um sistema de gestão escolar, que tem como objetivo criar um sistema SGE para a melhor gerência de notas e alunos de uma escola.

## Funcionalidades Obrigatórias
| ID   | Funcionalidade                                                                                |
| ---- | --------------------------------------------------------------------------------------------- |
| RF01 | Cadastrar, listar, consultar, editar e desativar alunos.                                      |
| RF02 | Cadastrar, listar, consultar e editar disciplinas e turmas, e vincular disciplinas às turmas. |
| RF03 | Matricular um aluno em uma turma e cancelar a matrícula.                                      |
| RF04 | Lançar notas por aluno, disciplina e avaliação.                                               |
| RF05 | Registrar a frequência (chamada) de uma aula, com presença ou falta de cada aluno da turma.   |
| RF06 | Consultar o boletim do aluno, com notas, média, frequência e situação por disciplina.         |
| RF07 | Listar os alunos em risco por nota ou por falta.                                              |
| RF08 | Pesquisar alunos por nome ou matrícula e filtrar por turma.                                   |

## Regras de negócio
| ID   | Regra |
| ---- | ----- |
| RN01 | Todo aluno possui: ID, nome, matrícula (código), data de nascimento, e-mail e situação (ativo/inativo). Nome e matrícula são obrigatórios; a matrícula é única; o e-mail deve ter formato válido.                                                                                                               |
| RN02 | Toda disciplina possui código (único), nome e carga horária maior que zero.|
| RN03 | Toda turma possui código (único), nome, ano letivo, turno (manhã, tarde ou noite) e capacidade máxima (inteiro maior que zero). Uma disciplina não pode ser vinculada duas vezes à mesma turma.|
| RN04 | A desativação do aluno é lógica: o registro não é excluído, o histórico (matrículas, notas e frequência) é preservado e o aluno inativo não pode ser matriculado nem receber novos lançamentos. |
| RN05 | Só aluno ativo pode ser matriculado. Não pode haver duas matrículas ativas do mesmo aluno na mesma turma. A matrícula não pode ultrapassar a capacidade da turma (contam apenas matrículas ativas). O cancelamento é lógico e libera a vaga. |
| RN06 | A nota é um valor entre 0 e 10, com até duas casas decimais, vinculada a uma matrícula ativa, a uma disciplina ofertada na turma do aluno, à descrição da avaliação (ex.: Prova 1) e à data. |
| RN07 | Existe um único registro de frequência por matrícula, disciplina e data. A data não pode ser futura. O registro da chamada de uma aula é uma operação única: ou todos os alunos são registrados, ou nenhum. |
| RN08 | Média = média aritmética das notas do aluno na disciplina. Frequência (%) = presenças ÷ total de aulas registradas × 100. Ambas são calculadas pelo sistema e nunca digitadas. |
| RN09 | Parâmetros desta avaliação: média mínima 6,0 e frequência mínima 75%. Em cada disciplina, o aluno está regular quando atende aos dois parâmetros e em risco (por nota, por falta ou por ambos) quando não atende a pelo menos um. A situação só é calculada se houver ao menos uma nota ou uma aula registrada. |

## Requisitos não funcionais
| ID    | Requisito não funcional          | Descrição                                                                                              |
| ----- | -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| RNF01 | Velocidade no processamento      | O sistema deve retornar as informações da forma mais rápida possível                                   |
| RNF02 | Responsividade                   | O sistema deve ser otimizado para todas as plataformas, tanto web quanto mobile                        |
| RNF03 | Segurança                        | O sistema deve ser seguro contra a maioria das vulnerabilidades web já conhecidas                      |
| RNF04 | Versionamento e documentação     | Cada alteração, criação ou atualização de alguma parte do sistema deve ser documentada da devida forma |

## Principais usuários
- Professores
- Alunos
- Pais
- Diretoria
- Administradores