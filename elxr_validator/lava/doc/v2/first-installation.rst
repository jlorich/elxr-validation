.. index:: first installation

.. _installation:

First steps installing LAVA
###########################

Initial LAVA Installation
*************************

The default installation provides an Apache2 config suitable for a simple LAVA
server at ``http://localhost/`` once enabled.

See :ref:`packaging_distribution` for more information or for debugging.

.. _lava_requirements:

Requirements to Consider Before Installing LAVA
***********************************************

.. include:: architecture-v2.rsti

Software Requirements
=====================

.. note:: LAVA is developed using Debian packaging to ensure that daemons and
   system-wide configuration is correctly updated with changes in the codebase.
   There is **no official support for pypi or python virtual environments or
   installing directly from a git directory**. See :ref:`debian_installation` for
   detailed instructions.

We currently recommend installing LAVA on `Debian`_ buster or
unstable.

LAVA software has now moved to Python3 support. This also means that Jessie
is no longer supported.

Contributions to support other distributions are welcome.

.. mention docker support here once that is merged.

.. _Debian: https://www.debian.org/

If you'd like to help us provide support for other distributions, feel free to
contact us using the :ref:`lava_devel` mailing list.

Hardware Requirements
=====================

A small LAVA instance can be deployed on fairly modest hardware. We recommend
at least 1GB of RAM to cover the runtime needs of the database server, the
application server and the web server. For storage, reserve about 20GB for
application data, especially if you wish to mirror the current public Linaro
LAVA instance.  LAVA uses append-only models, so storage requirements will grow
over time.

If you are deploying many devices and expect to be running large numbers of
jobs, you will obviously need more RAM and disk space.

Device requirements
===================

Devices you wish to deploy in LAVA need to be:

* Physically connected to the server via usb, usb-serial, or serial; or
* connected over the network via a serial console server; or
* a fastboot capable device accessible from the server; or
* a virtual machine or simulator that emulates a serial connection

.. _multinode_hardware_requirements:

MultiNode hardware requirements
===============================

If the instance is going to be sent any job submissions from third parties or
if your own job submissions are going to use MultiNode, there are additional
considerations for hardware requirements.

MultiNode is explicitly designed to synchronize test operations across multiple
test devices and running MultiNode jobs on a particular instance will have
implications for the workload of that instance. This can become a particular
problem if the instance is running on virtualized hardware with shared I/O, a
limited amount of RAM or a limited number of available cores.

.. note:: Downloading, preparing and deploying test images can result in a lot
   of synchronous I/O and if a single machine is running both the LAVA server
   and dispatcher, running synchronized MultiNode jobs can cause the load on
   that machine to rise significantly, possibly causing the server to become
   unresponsive. For this reason, it is strongly recommended that MultiNode
   instances use a separate dispatcher running on non-virtualized hardware so
   that the (possibly virtualized) server can continue to operate.

Also, consider the number of test devices connected to any one dispatcher.
MultiNode jobs will commonly compress and decompress several large test image
files in parallel. Even with a powerful multi-core machine, this can cause high
load. It is worth considering matching the number of devices to the number of
cores for parallel decompression, and matching the amount of available RAM to
the number and size of test images which are likely to be in use.

.. index:: install release, release

Which release to install
************************

The LAVA team makes regular releases (called ``production releases``),
typically monthly. These are installed onto Linaro's central instance
https://validation.linaro.org/ and they are also uploaded to Debian unstable
and backports (see :ref:`debian_installation`). These ``production releases``
using tags on the ``master`` branch.

Interim releases are made available from the :ref:`daily builds
<lava_repositories>`.

If in doubt, install the ``production`` release of ``lava-server`` from
official distribution mirrors. (Backports are included on Debian mirrors.)

The ``lava-dev`` package includes scripts to assist in local developer builds
directly from local git working copies which allows for builds using unreleased
code, development code and patches under review.

.. _install_types:

Installation Types
******************

.. _single_instance:

Single Master Instance installation
===================================

A single instance runs the web interface, the database, the scheduler and the
dispatcher on a single machine. If this machine is also running tests, the
device (or devices) under test (:term:`DUT`) will also need to be connected to
this machine, possibly over the network, using USB or using serial cables.

To install a single master instance and create a superuser, refer to
:ref:`debian_installation` installation.

LAVA V1 used to support a `distributed_instance` installation method. This has
been **removed** in V2; instead there is a much improved architecture for
remote workers using HTTP.

Detailed instructions for setting up workers follows - first, think about the
kind of configuration needed for your instance.

Master with one or more workers
===============================

You can choose whether the master has devices configured locally or only uses
devices via one or more remote workers. If you are installing and learning how
to use LAVA for the first time, it is recommended to keep things simple and
stick to a :ref:`single_instance` to start with.

Configuration outline - start simple...
---------------------------------------

* Configure the master as a :ref:`single_instance`. It will need the
  ``lava-server`` and ``lava-dispatcher`` packages installed.

* Use the Django administrative interface or command line tools to define the
  device types likely to be used with this instance.

* Prepare Device Dictionaries for your devices.

* Run some health check tests and see how things work.

...then expand
--------------

Once you are happy with your basic single-machine installation and are ready to
expand beyond that, start adding workers one at a time. For this configuration:

* The master needs the ``lava-server`` package installed, just as on a
  :ref:`single_instance`.

* A worker only needs the ``lava-dispatcher`` package installed.

  .. seealso:: :ref:`pipeline installation
     <setting_up_pipeline_instance>`.

As you expand your setup, you will also need to do some configuration of
communications between the master and the worker(s), which rely on HTTP
as an underlying technology. Workers on the same (trusted) network as the
master can work fine without using authentication and encryption, but if you
are going to be hosting workers on a remote network then it is **strongly**
recommended to use HTTPS to communicate with the server

* On your new worker, configure ``lava-worker`` to look for the server

* On the master, use the Django administration interface to add
  details of the new worker to the database.

* On the master, configure the Device Dictionaries for all the devices
  attached to the new worker.

* Assign devices to the new worker.

* Run health checks and be sure that all the devices on the new worker
  are properly configured and working.

* Repeat for additional workers as needed.

.. index:: coordinator

LAVA Coordinator setup
======================

If you are expecting to support MultiNode jobs in your LAVA setup, there is a
third component needed. The LAVA Coordinator manages the extra message passing
needed between the various nodes in a MultiNode group of devices. Nodes connect
to the LAVA Coordinator daemon via TCP (default port: 3079). A single
coordinator can manage groups from multiple instances if desired. If the
network configuration uses a firewall, ensure that this port is open for
connections from MultiNode dispatchers.

If multiple coordinators are necessary on a single machine (e.g. to test
different versions of the coordinator during development), each coordinator
needs to be configured for a different port.

If the dispatcher is installed on the same machine as the coordinator, the
dispatcher can use the packaged configuration file with the default hostname of
``localhost``.

Each dispatcher then needs a copy of the LAVA Coordinator configuration file
(JSON syntax), modified to point back to the hostname of the coordinator:

Example JSON, modified for a coordinator on a machine with a fully qualified
domain name:

.. code-block:: json

  {
    "port": 3079,
    "blocksize": 4096,
    "poll_delay": 3,
    "coordinator_hostname": "control.lab.org"
  }

An IP address can be specified instead, if appropriate.

Each dispatcher needs to use the same port number and blocksize as is
configured for the Coordinator on the specified machine. The poll_delay is the
number of seconds each node will wait before polling the coordinator again.

.. _serial_connections:

Setting Up Serial Connections to LAVA Devices
=============================================

LAVA controls the DUT using a serial connection, except for emulated devices
like QEMU.

LAVA can support :ref:`multiple serial connections <connections>` per
DUT. The recommended method for creating a serial connection is to use
:ref:`ser2net` to provide a connection using the telnet client. This
allows simple and clean disconnection and allows LAVA to use the
connection over the network. Other tools (conmux, minicom) have been
tried but showed reliability problems when used at scale. LAVA is not
able to directly access a device node.

.. seealso:: :ref:`growing_your_lab` and :ref:`serial_console_support`
   for information about hardware.

`ser2net` is the recommendation based on several million test jobs.

.. seealso:: :ref:`serial_console_support` for information about hardware.

.. caution:: Make sure your serial connection configuration is :ref:`backed up
   <admin_backups>` as it can be an awkward process to manually establish which
   path in ``/dev/serial/by-id`` is which cable and therefore connected to
   which device.

.. _ser2net:

Ser2net daemon
--------------

ser2net provides a way for a user to connect from a network connection to a
serial port, usually over telnet.

http://ser2net.sourceforge.net/

``ser2net`` is a dependency of ``lava-dispatcher``, so will be
installed automatically.

Example config (in /etc/ser2net.conf)::

 #port:connectiontype:idle_timeout:serial_device:baudrate databit parity stopbit
 7001:telnet:0:/dev/serial/by-id/serial_path:115200 8DATABITS NONE 1STOPBIT LOCAL

.. note:: In the above example we have the idle_timeout as 0 which specifies a
   infinite idle_timeout value. 0 is the recommended value. If the user prefers
   to give a positive finite idle_timeout value, then there is a possibility
   that long running jobs may terminate due to inactivity on the serial
   connection.

   Always use paths in ``/dev/serial/by-id/`` in the configuration to prevent
   connections being lost when devices reenumerate.

   The LOCAL flag is necessary if you connect modem control lines (for example a
   full RS232 cable) to prevent connection aborts on DUT power cycling.

StarTech rackmount usb
----------------------

* udev rules::

   SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="ST167570", SYMLINK+="rack-usb02"
   SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="ST167569", SYMLINK+="rack-usb01"
   SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="ST167572", SYMLINK+="rack-usb04"
   SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="ST167571", SYMLINK+="rack-usb03"

This will create a symlink in /dev called rack-usb01 etc. which can then be
addressed in the :ref:`ser2net` config file.

.. index:: contact, bug reports

Contact and bug reports
***********************

Please report bugs using the LAVA Users mailing list:
https://lists.lavasoftware.org/mailman3/lists/lava-users.lists.lavasoftware.org/

You can also report bugs using ``reportbug`` and the Debian Bug Tracking
System: https://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=lava-server

Feel free to contact us at validation (at) linaro (dot) org and on
the ``#linaro-lava`` channel on OFTC but note that IRC is not well suited to
some discussions. Problems with device configuration or test job failures
usually benefit from being able to attach the full configuration to an email
to the lava-users mailing list.
