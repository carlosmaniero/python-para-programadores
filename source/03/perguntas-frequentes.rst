********************
Perguntas Frequentes
********************

Quem vem de outra linguagem, já tem muito bem definido os processos e
ferramentas que utilizam para desenvolver software. Quando eu digo que programo
em Python, as reações são sempre muito similiares. Tudo começa com um sonoro:

::
    
    - Nossa! Em Python?

E em seguida começa uma série de perguntas sobre a linguagem. Eu listei
algumas delas aqui.


Python é compilada?
===================

Não!

Python é uma linguagem interpretada. Você pode também escrever bibliotecas
Python utilizando C ou C++ [#]_, isso não é muito comum, mas necessário em
alguns casos.

Provavelmente, se você está acostumado com linguagens compiladas, uma das
preocupações que você terá será em como distribuir a sua aplicação sem ceder o
código-fonte.

Acho que essa não é uma preocupaçãoa muito relevante, a não ser que você esteja
fazendo alguma aplicação para desktop, que será distribuída de forma orgânica e
que você não terá controle sobre quem irá instalar a sua aplicação, você
consegue resolver isso de forma jurídica, através de contratos.

Se sua aplicação, rodar em um servidor - uma aplicações web -, por exemplo,
você pode limitar o acesso do seu cliente aos servidores. Hoje em dia, boa
parte das linguagens modernas são interpretadas. Não vejo isso como um grande
problema.

Qual IDE utilizar?
==================

Digo mais uma vez que Python é uma linguagem extremamente simples e isso
facilita um bocado na hora de programar e dar manutenção nos projetos.

Por isso, não há uma real necessidade de uma IDE complexa e cheia de recursos
para programar em Python. Na verdade, você ṕode programar em Python utilizando
qualquer dispositívo em que seja possível bater meia dúzia de teclas.

Certa vez, esqueci o meu editor de texto aberto, minha gatinha passou sobre o
teclado e quando fui ver, ela havia feito um "Hello World" em Python.

Eu particularmente, utilizo o Vim [#]_, há uma infinidade de editores bons. 
Vejo muitos programadores Python utilizando o Atom e o Sublime.

Existem também IDEs comerciais e cheia de recursos para quem está acostumado
como Visual Studio (que inclusive tem uma versão que suporta Python [#]_),
Netbeans [#]_ e Eclipse [#]_, como o PyCharm [#]_, que acredito eu, seja a 
IDE mais completa para desenvolvimento Python.

Só roda no Linux?
=================

Não!

Eu não sei onde nem quando surgiu esse mito de que Python é uma linguagem
exclusiva para ambientes Linux, mas é apenas lenda urbana.

Até um tempo atrás, dependendo do que você fosse fazer, era muito melhor
utilizar um sistema operacional Unix-like. Instalar uma biblioteca compilada
no Windows era um suplício. Mas até esse tipo de biblioteca já está mais fácil
de instalar hoje em dia.

Temos também ferramentas como o Docker, que utilizando o conceito de
containers, permite que tenhamos um ambiente Linux dentro do Windows, Mac e o
próprio Linux de forma muito mais simples do que se utilizassemos
virtualização. É uma excelente prática para manter a compatibilidade com o
ambiente em que o seu software irá rodar.

.. note:: Docker é uma ferramenta poderosíssima e tem ganhado bastante
   destaque nas comunidades open sources. 

   Recomendo muito que estudem e apliquem em seus projetos. Existem excelentes
   ferramentas de orquestração como o
   `Docker Compose <https://docs.docker.com/compose/>`_ que facilitam e muito
   essa tarefa.


Dá pra desenvolver Web em Python?
=================================

Dá e como dá!
Python é excelente para desenvolver Web, dos projetos que eu participei
utilizando Python, eram em sua grande maioria, projetos web.

Existe um set imenso de Frameworks [#]_ que nos ajudam nessa tarefa.
Entre os mais populares estão o Django [#]_ e o Flask [#]_.

Padrão de Codificação
=====================

Assim como a maioria das linguagens, Python também possui um padrão de
codigicação ela está é descrina na PEP8 [#]_. Haverá um capítulo desse livro
para falar a respeito disso. 

.. todo::
   
    Colocar a página do livro

Existem algumas coisas que para programadores de outras linguagens como Java 
podem aparecer absurdas. Mas como tempo, você não só se acostuma, mas consegue
ver que aquele padrão torna seu código muito mais legível.


.. rubric:: Footnotes

.. [#] `Extending Python with C or C++ 
   <https://docs.python.org/2/extending/extending.html>`_

.. [#] `Configurações do meu Vim <https://github.com/carlosmaniero/vim/>`_

.. [#] `Ferramentas Python para Visual Studio
   <https://www.visualstudio.com/pt-br/features/python-vs.aspx>`_

.. [#] `Python support in NetBeans
   <http://wiki.netbeans.org/Python>`_ (em inglês)

.. [#] `PyDev <http://www.pydev.org/>`_ (em inglês)

.. [#] `PyCharm <https://www.jetbrains.com/pycharm/>`_ (em inglês)

.. [#] `Web Frameworks for Python
   <https://wiki.python.org/moin/WebFrameworks>`_ (em inglês)

.. [#] `Django <https://www.djangoproject.com/>`_ - The web framework for
   perfectionists with deadlines. (em inglês)

.. [#] `Flask <http://flask.pocoo.org/>`_ Web development, one drop at a time.
   (em inglês)

.. [#] `PEP 8 -- Style Guide for Python Code
   <https://www.python.org/dev/peps/pep-0008/>`_
