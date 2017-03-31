#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_vlc_commands',
    version = '0.5.0',
    description = 'VLC commands for Plover',
    author = 'Benoit Pierre',
    author_email = 'benoit.pierre@gmail.com',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop'
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = [
        'plover>=4.0.0.dev0',
        'requests',
    ],
    py_modules = [
        'plover_vlc_commands',
    ],
    entry_points = '''

    [plover.command]
    VLC_pause        = plover_vlc_commands:pause
    VLC_resume       = plover_vlc_commands:resume
    VLC_seek         = plover_vlc_commands:seek
    VLC_stop         = plover_vlc_commands:stop
    VLC_toggle_pause = plover_vlc_commands:toggle_pause

    [plover.meta]
    VLC_timestamp    = plover_vlc_commands:timestamp

    ''',
    zip_safe = True,
)
