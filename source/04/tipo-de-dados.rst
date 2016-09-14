*************
Tipo de Dados
*************

Python é uma linguagem de tipagem forte e dinâmica. 

.. literalinclude:: example_04_1.py
    :language: python
    :caption: ex04-1
    :linenos:

Saída do programa:

::

    Eleven is a <type 'str'>
    12 is a <type 'int'>
    42.0 is a <type 'float'>

Note que não é preciso em momento algum definir o tipo do dado. O Python
detecta automáticamente o tipo da variável e atribui o tipo à mesma.

Para definir uma string basta colocar ela entre aspas simples (') ou duplas 
(").


Dinâmicamente tipada
====================

Você pode alterar o tipo de uma variável durante a execução do código e o
Python não lançará nenhuma *Exception*.

.. literalinclude:: example_04_2.py
    :language: python
    :caption: ex04-2
    :linenos:
    :emphasize-lines: 11

Agora o name é do tipo **int** como podemos ver abaixo:

::
    
    Eleven is a <type 'str'>
    12 is a <type 'int'>
    42.0 is a <type 'float'>
    11 is a <type 'int'>
    This is a stranger thing!

.. note::

   Alterar o tipo de uma variável, nunca é uma boa prática.


Fortemente tipada
=================

Linguagens de tipagem fraca, permite que você faça operações algumas operações,
sem a necessidade da realização do `cast`. Como por exemplo:

.. literalinclude:: example_04_3.py
    :language: python
    :caption: ex04-3
    :linenos:

Isso não é o caso do Python, ao realizar isso. Ele retorna o seguinte
`traceback`:

::

    Traceback (most recent call last):
      File "type_error.py", line 3, in <module>
          print(1 + name)
          TypeError: unsupported operand type(s) for +: 'int' and 'str'

Deixando claro que não é possivel somar um inteiro à uma `string`.

.. tip::

    Para fazer esses testes rápidos da linguagem sem precisar ficar criando
    arquivos, você pode simplesmente abrir o interpretador do python,
    digitando "python" no terminal (ou abrir o interpretador Python se estiver
    no Windows).

    Uma excelente alternativa é o ipython [#]_, com ele é possível
    autocompletar como se tivesse utilizando uma IDE. Para instalar é simples:

    ::

        $ pip install ipython

    Feito isso, basta digitar ipython no terminal e você poderá utilizar o
    shell interativo do Python de forma muito mais dinâmica.


Vetores, Matrizes e Conjuntos
=============================

Python possui dois tipos de listas a do tipo `list` e a do tipo `tuple`.
E qual a diferença entre um e outro?

Uma tupla é uma lista imutável. Então, você nunca consegue alterar o seu
conteúdo.

Essa diferença fica clara quando você olha os métodos que uma lista e uma tupla
possui.

**list**:

::

    append, count, extend, index, insert, pop, remove, reverse, sort.

**tuple**:

::

    count, index.

List
----

Em Python, o tamanho da lista é dinâmico bem como seu tipo. Então você não 
precisa definir o seu tamanho. Vejamos um exemplo de utilização de listas.

.. literalinclude:: example_04_4.py
    :language: python
    :caption: ex04-4
    :linenos:

::

    Size of fruits: 2
    Minions loves banana
    Newton loves apple
    Size of fruits: 3
    orange is the new black
    I don't like of banana
    Now minions loves apple

.. note::

    Para alterar o valor de um elemento do uma lista, basta utilizar a seguinte
    sintaxe:

    ::

        >>> fruits[0] = 'kiwi'
        >>> print(fruits[0])
        kiwi

.. tip::

    Para excluir a referência de um objeto você pode usar o statement `del`.
    Por exemplo:
    
    ::
    
        >>> a = 1
        >>> del a
        >>> print(a)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          NameError: name 'a' is not defined

    Você pode utilizar também em listas.

    ::

        >>> fruits = ['banana', 'apple']
        >>> del fruits[0]
        >>> print(fruits)
        ['apple']

    A diferença entre o del e o pop do list, é que o pop irá retornar o
    elemento excluído.
    
    **Garbage Collector**

    Quando você exclui uma variável utilizando o `del`, você não está apagando
    o objeto, mas sim a sua referência.

    Se você tiver duas variáveis apontando para o mesmo objeto, o objeto só vai
    sair da memória quando a última referência for excluída, assim o Garbage
    collector irá detectar que não há referências para o objeto e irá removê-lo
    da memória.


Tuple
-----

Como dito anteriormente, a principal diferença entre tuplas e listas é que 
tuplas são imutáveis.

Vamos reescrever o exemplo :ref:`ex04-4` utilizando tuples.


.. literalinclude:: example_04_5.py
    :language: python
    :caption: ex04-5
    :linenos:
    :emphasize-lines: 9, 11

Saída do programa:

::

    Size of fruits: 2
    Minions loves banana
    Newton loves apple
    Size of fruits: 2
    Size of new_fruits: 3
    orange is the new black
    I don't like of banana but i can't remove this
    minions contine to love banana

Como podemos ver, na **linha 9** a única forma de adicionar um objeto à uma 
tupla é fazendo a união entre duas listas. Já na **linha 11**, podemos ver que
a tupla original continua inalterada.

.. note::

    Caso você tente utilizar o statment `del` para tentar excluir um elemento
    de uma tupla, você receberá um sonoro exception. No próximo capítulo,
    veremos como funcionam os `slices` em Python que poderá nos ajudar nessa
    tarefa.

    ::

        >> a = (1, 2)
        >> del a[0]
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          TypeError: 'tuple' object doesn't support item deletion


Matrizes
--------

Uma matriz em Python é uma lista de lista, ou tuplas de tuplas.

.. literalinclude:: example_04_6.py
    :language: python
    :caption: ex04-6
    :linenos:

No nosso exemplo, temos uma tupla de listas. A lista responsável pelas linhas 
do tic-tac-toe são imutáveis e deve ser sempre as mesmas listas, por isso
a utilização de tuplas. As colunas em contra partida devem ser mutáveis, já
que é preciso alterar o seu conteúdo.


Set
----

Conjuntos são similiares às listas, porém, como o nome mesmo diz, são
conjuntos, ou seja, não aceita elementos duplicados.

.. literalinclude:: example_04_7.py
    :language: python
    :caption: ex04-7
    :linenos:

::

    {1, 2}

Não importa quantas vezes você adicionar um elemento ao set. Se ele já existir,
ele sempre será ignorado.

.. note::

    Para criar uma lista vazia, você basta abrir e fechar os colchetes **[]**.
    Seguindo a mesma lógica basta um par de parênteses **()**.
    
    Mas isso não é válido para criar um conjunto vazio. O par de chaves, também
    é utilizado para criação de um dicionário (Calma! Vamos falar de 
    dicionários disso logo abaixo). Então, para definir um conjunto vazio é 
    necessário fazer de forma literal. Veja um exemplo abaixo:

    ::

        >>> a = {}
        >>> print(type(a))
        <type 'dict'>
        >>> a = set()
        >>> print(type(a))
        <type 'set'>

    O construtor do `set` aceita como parâmetro um iterável [#]_. A partir
    desse iterável será gerado um conjunto.

    ::

        >>> set([1, 1, 2, 3, 3, 4])
        {1, 2, 3, 4}


Dicionários
===========

Um dict em Python, é uma estrutura de dado chave/valor. É muito simples
trabalhar com ele. Veja um exemplo abaixo:


.. literalinclude:: example_04_8.py
    :language: python
    :caption: ex04-8
    :linenos:
    :emphasize-lines: 13, 18

::

    The cartel of Pablo Escobar is Medellin
    The cartel of Pacho is Cali
    The cartel of Gustavo is Medellin
    Gustavo was killed
    The cartel of Gustavo is The Hell

Nas **linhas 1-6**, estamos definindo o dicionário, na **linha 14**, estamos
mudando o cartel do Gustavo. Já na **linha 16** surge um novo personagem - o 
Miguel -, ele pertence ao cartel de Cali.

.. note::

   A chave de um dicionário não precisa ser necessariamente uma `string`. Na 
   verdade, a chave pode ser qualquer objeto.

   O Python utiliza o sistema de hash (assunto do próximo episódio, digo,
   capítulo) para identificar se a chave solicitado está no dicionário.
   Caso não esteja, uma `exception` do tipo KeyError é lançada.

.. tip::

    Assim como em listas, você pode excluir um valor utilizando o del ou pop.

    ::

        >>> del cartes['escobar']

    ou

    :: 

        >>> cartes.pop('escobar')
        Medellin

.. rubric:: Footnotes

.. [#] Site oficial: <https://ipython.org>

.. [#] Um iterável é uma lista ou uma tupla, por exemplo. Dedicaremos um
   capítulo inteiro do livro para explicar o que é um iterável.
