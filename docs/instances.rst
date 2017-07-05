Instances
~~~~~~~~~

Default instance to be used when no ``decent_instance`` is given to
the Objects!

.. code-block:: python

   from decent.instance import shared_decent_instance

   account = Account("xeroc")
   # is equivalent with 
   account = Account("xeroc", decent_instance=shared_decent_instance())

.. automethod:: decent.instance.shared_decent_instance
.. automethod:: decent.instance.set_shared_decent_instance
