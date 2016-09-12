*************
Tipo de Dados
*************

Python é uma linguagem de tipagem forte e dinâmica. 

.. literalinclude:: show_types.py
    :language: python
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

.. literalinclude:: dinamic_types.py
    :language: python
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

.. literalinclude:: type_error.py
    :language: python
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
    arquivos, você pode digitar simplesmente abrir o interpretador do python,
    digitando "python" no terminal (ou abrir o interpretador Python se estiver
    no Windows).

    Uma excelente alternativa é o ipython, com ele é possível autocompletar
    como se tivesse utilizando uma IDE. Para instalar é simples:

    ::

        $ pip install ipython

    Feito isso, basta digitar ipython no terminal e você poderá utilizar o
    shell interativo do Python de forma muito mais dinâmica.
