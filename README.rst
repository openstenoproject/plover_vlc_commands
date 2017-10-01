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

-  ``VLC_pause``, ``VLC_resume``, ``VLC_stop``, ``VLC_toggle_pause``:
   self explanatory
-  ``VLC_seek``: seek the video, for example ``{PLOVER:VLC_seek:-10s}``
   to seek backward 10 seconds, ``{PLOVER:VLC_seek:+1m}`` to seek
   forward 1 minute
