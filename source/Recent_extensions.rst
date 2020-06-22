===================
· Recent extensions
===================

Failure management and exceptions
=================================

A recent extension to PyCOMPSs is an interface that enables the programmer to
give hints about how to proceed in case of failure of individual tasks.
This new feature enables the workflow execution to continue in the occurrence of
individual task failures. The programmer can also define timeouts to tasks.

.. code-block:: python

    @task(file_path=FILE_INOUT, on_failure='CANCEL_SUCCESSORS')
    def task(file_path):
        # ...
        if cond :
            raise Exception()


Another new mechanism enables to throw exceptions from tasks that are captured
by the main program. This mechanism is combined with the definition of task groups. When a task in the group throws an exception, then the outstanding tasks in the group are canceled and the main program can define a new alternative behaviour.

This enables the definition of very dynamic workflows that depend on the actual
results of the tasks.

.. code-block:: python

    @task(file_path=FILE_INOUT)
    def comp_task(file_path):
        # ...
        raise COMPSsException("Exception")

.. code-block:: python

    def test_cancellation(file_name):
        try:
            with TaskGroup('failedGroup'):
                long_task(file_name)
                long_task(file_name)
                executed_task(file_name)
                comp_task(file_name)
        except COMPSsException:
            print("COMPSsException caught")
            write_two(file_name)
        write_two(file_name)




Support for data streams
========================

A new interface to support streaming data in tasks has been defined
Tasks that exchange streamed data persist while streams are not closed
(data-flow tasks).

This extension enables the combination of Task and Data Flows (Hybrid Flows)
using the same programming model and allows developers to build complex Data
Science pipelines with different approaches.

.. code-block:: python

    @task(fds=STREAM_OUT)
    def sensor(fds):
        # ...
        while not end():
            data = get_data_from_sensor()
            f.write(data)
        fds.close()


.. code-block:: python

    @task(fds_sensor=STREAM_IN, filtered=OUT)
    def filter(fds_sensor, filtered):
        # ...
        while not fds_sensor.is_closed():
            get_and_filter(fds_sensor, filtered)


