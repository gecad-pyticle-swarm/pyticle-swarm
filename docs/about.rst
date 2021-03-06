=====================
About Pytcicle Swarm
=====================

The Pyticle Swarm is a library created with Python 3.9 capable of running a particle swarm optimization for an array given a fitness function.
To use it simply install anaconda ou any other software that allows the creation of a python environment and you will be able to run it.

The library has dependencies on the following packages:

* numpy
* matplotlib
* matplotlib-inline
* joblib

To create an anaconda environment run:

.. code-block:: console

    $ conda create -n {name_of_environment} python=3.9

To activate the anaconda environment execute:

.. code-block:: console

    $ conda activate {name_of_environment}

To install the library simply run:

.. code-block:: console

    $ pip install pyticle-swarm

To upgrade the library run:

.. code-block:: console

    $ pip install pyticle-swarm -U

To import the library and the PSO algorithm:

.. code-block:: python

    from pyticleswarm import run_pso

To try the example given in github_:

.. _github: https://github.com/gecad-pyticle-swarm/pyticle-swarm
    
.. code-block:: console

    $ python example.py

Pyticle Swarm was developed at GECAD - Research Group on Intelligent Engineering and Computing for Advanced Innovation and Development by:
    * Bruno Veiga - btsve@isep.ipp.pt
    * Ricardo Faia -  rfmfa@isep.ipp.pt
    * Tiago Pinto - tcp@isep.ipp.pt
    * Zita Vale - zav@isep.ipp.pt

.. image:: gecad.png
		:width: 20em
		:align: center 

.. toctree::
    :maxdepth: 2

    CHANGELOG