Plover VLC commands
===================

Add support for controlling VLC from Plover.

Setup
-----

-  create ``vlc.json`` in the same directory as your configuration, set
   those settings that differ from defaults, e.g.:

   .. code:: json

       {
         "host": "localhost",
         "port": "8080",
         "user": "",
         "pass": "password"
       }

-  start VLC with the HTTP interface enabled, e.g.:
   ``vlc --extraintf http --http-password password ...``

Available commands
------------------

- ``VLC_pause``, ``VLC_resume``, ``VLC_stop``, ``VLC_toggle_pause``:
  self explanatory
- ``VLC_rate``: change the rate of playback, for example
  ``{PLOVER:VLC_rate:0.5}`` to halve the playback speed, or
  ``{PLOVER:VLC_rate:2.0}`` to double it. Percentage and relative
  rate changes are also supported: ``{PLOVER:VLC_rate:-10%}``.
- ``VLC_seek``: seek the video, for example ``{PLOVER:VLC_seek:-10s}``
  to seek backward 10 seconds, ``{PLOVER:VLC_seek:+1m}`` to seek forward
  1 minute, or ``{PLOVER:VLC_seek:50%}`` to seek to the halfway point.

Timestamp support
-----------------

A custom meta to get the current video timestamp is also provided:
``VLC_timestamp``. For example using ``{[inaudible ^}{:VLC_timestamp}{^]}``
would translate to something like: ``[inaudible 00:08:01]``.

Release history
---------------

0.6.5
~~~~~

* add timestamp support

0.6.4
~~~~~

* fix rate command documentation
* add support for percentage and relative rate changes

0.6.3
~~~~~

* improve seek command documentation
* add rate command
