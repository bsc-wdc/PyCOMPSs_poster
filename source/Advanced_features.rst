===================
PyCOMPSs decorators
===================

The @task is the basic decorator which is used to identify a method that will become a task at execution time. The directionality of the method parameters are indicated in the @task annotation as "IN" (when the parameter is read, default value), "OUT" (when the parameter is written), or "INOUT" (when the parameter is read and written).

.. code-block:: python

    @task(c=INOUT)
    def multiply(a, b, c):
	c += a*b


Constraints
===========

PyCOMPSs supports the definition of constraints on the tasks, i.e., specific
hardware or software that is required to execute the tasks. Sample constraints
can be a given number of CPU cores or a minimum amount of memory to be
allocated in the node.

.. code-block:: python

    @constraint(memory_size=6.0, processor_performance="5000")
    @task(c=INOUT)
    def myfunc(a, b, c):
        # ...

Versions
========

PyCOMPSs also supports the definition of multiple versions of the same task
type: i.e., a specific version for a general-purpose processor and another one
for a GPU.

.. code-block:: python

    @implement(source_class="myclass", method="myfunc")
    @constraint(memory_size=1.0, processor_type="ARM")
    @task(c=INOUT)
    def myfunc_in_the_edge(a, b, c):
        # ...

Linking with other programming models
=====================================

A task can be more than a sequential function: can be a  sequential task run in
a single core, a multicore task or a task spanning into multiple nodes of a
cluster or a cloud.

PyCOMPSs is also very flexible with regard to the nature of the tasks that compose
their applications, with features to support other programming models, such as
OpenMP, OmpSs or MPI, and also with external binaries. In this sense, a PyCOMPSs
application can be a large workflow that orchestrates multiple MPI simulations
and then executes some analytics in Python, for example.

.. code-block:: python

    @constraint(computing_units="248")
    @mpi(runner="mpirun", computingNodes= "16", ...)
    @task(returns=int, stdOutFile=FILE_OUT_STDOUT, ...)
    def nems(stdOutFile, stdErrFile):
        pass


Integration with Numba
======================

PyCOMPSs has been integrated with Numba just in time compilation. Tasks in PyCOMPSs can be annotated with the @jit decorator below the @task decorator. An alternative syntax is to use the "numba='jit'" clause inside the @task decorator. The code of the tasks is passed to the Numba compiler and the compiled version used at execution time.

The two alternative syntaxes are shown below:

.. code-block:: python

    @task(returns=1)
    @jit()
    def numba_func(a, b):
        ...

.. code-block:: python

    @task(numba='jit')
    def jit_func(a, b):
        ...
