BTMux Template IO
=================

This module is used to parse BattletechMUX (BTMux) template files. In the future,
this could be expanded to having write support for template files.

If you don't know what any of this means, this module probably won't be of
any use or interest to you. It's very niche, and I keep it here mostly for
my own tracking.

Requirements
------------

* Python 2.7 (but not Python 3)

CLI MTF to BTMux conversion examples
------------------------------------

Converting an entire directory of MTF files to a directory of BTMux
template files::

    mtfconvdir mtfs/ btmux/game.run/mechs/

Converting a single MTF file to BTMux, printing output to stdout::

    mtfconv mtfs/test_mtf.mtf -

Same thing, but write to a file this time::

    mtfconv mtfs/test_mtf.mtf btmux/game.run/mechs/TESTMECH


Legal Mumbo Jumbo
-----------------

Copyright (C) 2014 `Gregory Taylor`_

This software is licensed under the BSD License.

.. _Gregory Taylor: http://gc-taylor.com
