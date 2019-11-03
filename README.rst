====
yapq
====


.. image:: https://img.shields.io/pypi/v/yapq.svg
        :target: https://pypi.python.org/pypi/yapq

.. image:: https://img.shields.io/travis/ginkooo/yapq.svg
        :target: https://travis-ci.org/ginkooo/yapq

.. image:: https://readthedocs.org/projects/yapq/badge/?version=latest
        :target: https://yapq.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/Ginkooo/yapq/shield.svg
     :target: https://pyup.io/repos/github/Ginkooo/yapq/
     :alt: Updates



Yet Another Python Queue


* Free software: MIT license
* Documentation: https://yapq.readthedocs.io.


Usage
-----

>>> from yapq import Yapq
>>> yapq = Yapq()
>>> yapq.start()
>>> result = yapq.enqueue(lambda a, b: a + b, 5, 3)
>>> result.get()
8


Installing
----------

``pip install yapq``


Features
--------

* Executing tasks in thread-based workers

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
