channels-bug-connection-closed
==============================

Minimal repro for `Channels bug #1091 <https://github.com/django/channels/issues/1091>`__.

To setup:

.. code-block:: console

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install channels daphne django

Then run with:

.. code-block:: console

    $ ./manage.py test
    ...
    ======================================================================
    ERROR: test_websocket (example.tests.ExampleConsumerTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/.../python3.10/site-packages/django/db/backends/base/base.py", line 301, in _cursor
        return self._prepare_cursor(self.create_cursor(name))
      File "/.../python3.10/site-packages/django/db/backends/sqlite3/base.py", line 177, in create_cursor
        return self.connection.cursor(factory=SQLiteCursorWrapper)
    sqlite3.ProgrammingError: Cannot operate on a closed database.

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "/.../python3.10/site-packages/asgiref/sync.py", line 218, in __call__
        return call_result.result()
      File "/Users/chainz/.pyenv/versions/3.10.8/lib/python3.10/concurrent/futures/_base.py", line 451, in result
        return self.__get_result()
      File "/Users/chainz/.pyenv/versions/3.10.8/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
        raise self._exception
      File "/.../python3.10/site-packages/asgiref/sync.py", line 284, in main_wrap
        result = await self.awaitable(*args, **kwargs)
      File "/Users/chainz/tmp/channelstest/example/tests.py", line 10, in test_websocket
        connected, subprotocol = await communicator.connect()
      File "/.../python3.10/site-packages/channels/testing/websocket.py", line 36, in connect
        response = await self.receive_output(timeout)
      File "/.../python3.10/site-packages/asgiref/testing.py", line 79, in receive_output
        self.future.result()
      File "/.../python3.10/site-packages/channels/consumer.py", line 94, in app
        return await consumer(scope, receive, send)
      File "/.../python3.10/site-packages/channels/consumer.py", line 62, in __call__
        await await_many_dispatch([receive], self.dispatch)
      File "/.../python3.10/site-packages/channels/utils.py", line 50, in await_many_dispatch
        await dispatch(result)
      File "/.../python3.10/site-packages/channels/consumer.py", line 73, in dispatch
        await handler(message)
      File "/.../python3.10/site-packages/channels/generic/websocket.py", line 173, in websocket_connect
        await self.connect()
      File "/Users/chainz/tmp/channelstest/example/consumers.py", line 8, in connect
        await basic_query()
      File "/.../python3.10/site-packages/asgiref/sync.py", line 435, in __call__
        ret = await asyncio.wait_for(future, timeout=None)
      File "/Users/chainz/.pyenv/versions/3.10.8/lib/python3.10/asyncio/tasks.py", line 408, in wait_for
        return await fut
      File "/.../python3.10/site-packages/asgiref/current_thread_executor.py", line 22, in run
        result = self.fn(*self.args, **self.kwargs)
      File "/.../python3.10/site-packages/channels/db.py", line 13, in thread_handler
        return super().thread_handler(loop, *args, **kwargs)
      File "/.../python3.10/site-packages/asgiref/sync.py", line 476, in thread_handler
        return func(*args, **kwargs)
      File "/Users/chainz/tmp/channelstest/example/consumers.py", line 14, in basic_query
        with connection.cursor() as cursor:
      File "/.../python3.10/site-packages/django/utils/asyncio.py", line 26, in inner
        return func(*args, **kwargs)
      File "/.../python3.10/site-packages/django/db/backends/base/base.py", line 323, in cursor
        return self._cursor()
      File "/.../python3.10/site-packages/django/db/backends/base/base.py", line 300, in _cursor
        with self.wrap_database_errors:
      File "/.../python3.10/site-packages/django/db/utils.py", line 91, in __exit__
        raise dj_exc_value.with_traceback(traceback) from exc_value
      File "/.../python3.10/site-packages/django/db/backends/base/base.py", line 301, in _cursor
        return self._prepare_cursor(self.create_cursor(name))
      File "/.../python3.10/site-packages/django/db/backends/sqlite3/base.py", line 177, in create_cursor
        return self.connection.cursor(factory=SQLiteCursorWrapper)
    django.db.utils.ProgrammingError: Cannot operate on a closed database.

