.. # can refer to Android when *not* describing how to rebuild or modify AOSP.

.. index:: deploy lxc test job, deploy android using lxc

.. _deploy_using_lxc:

Deploying test images using LXC
###############################

Containers are lightweight virtualization technology. LXC is a userspace
interface for the Linux kernel containment features. Through a powerful API and
simple tools, it lets Linux users easily create and manage system or
application containers. The container provides a lightweight method to allow
custom software to be used on the dispatcher. The container is used to provide
transparent access.

LAVA supports LXC containers both as a standalone device type and as dynamic
transparent environments in order to interact with external devices. In either
case the :ref:`LXC protocol <lxc_protocol_reference>` is used.

.. _lava_lxc_device_type:

Using LXC as Device Type
************************

LXC is a :term:`device type` of its own and devices could be added to
dispatchers under this device type. A device of LXC device type is created
within the dispatcher in which the device is configured, as illustrated in the
following figure:

.. image:: ./images/lxc-standalone.svg
   :align: center
   :alt: LXC standalone

The LXC :term:`device type` uses the :ref:`LXC protocol
<lxc_protocol_reference>` in order to share data elements across different
actions within the job.

Protocol elements
=================

.. include:: examples/test-jobs/lxc-debian.yaml
   :code: yaml
   :start-after: path: lxc-debian.yaml
   :end-before: actions:

Sample Job Definition
=====================

.. include:: examples/test-jobs/lxc-debian.yaml
   :code: yaml

.. index:: Namespaces

.. _namespaces_with_lxc:

Namespaces
**********

Namespaces were introduced to handle use-cases specific to LXC, but the
principle can be expanded to other use-cases as and when required. In a job
definition where multiple deploy, boot and test actions are specified, there
must be a mechanism to describe how the actions are connected. This is the
primary purpose of a namespace; it is the way to tie related actions together.
The namespace itself is simply a label, test writers are advised to make the
label chosen for each namespace meaningful for the purposes of the test job.

In the example below, there are two namespaces - one for the deploy, boot and
test actions to perform inside the LXC and one for the deploy, boot and test
actions to be performed on the :term:`DUT`. To support this particular device,
the test job needs to:

#. deploy the container, including:

   * install software inside the container to control the device. In this
     case ``android-tools-fastboot``.

#. boot the container

#. deploy files to the device

   * In this case, this connects to and turns on power to the device then
     uses software in the container to push files to the device using the
     bootloader.

#. boot the device

#. run a test shell on the device

#. run a test shell in the container.

Note how the deploy, boot and test actions are interleaved. The use of
namespaces is essential for the test shell in the container to be able to find
and execute commands in the container. In this example, the software running in
the container and the software running on the device need to be handled quite
differently in each test shell. For example, when installing dependencies
inside the container running Debian, the ``apt`` package manager is available.
When installing dependencies in the test shell on the device, running
OpenEmbedded, there might not be any package manager support. The namespace
data is used to let each test shell identify the default shell and other data
about the environment in each namespace.

.. literalinclude:: examples/test-jobs/hikey-oe.yaml
     :language: yaml
     :linenos:
     :lines: 26-106
     :emphasize-lines: 3, 11, 23, 45, 64, 74

.. note:: The two test shells are *almost* identical but remember that all the
   results of this one test job will be reported together. The name of each
   test shell definition needs to be different for each test action. So the
   example uses ``name: smoke-tests-basic-oe`` for the ``hikey-oe`` namespace
   and ``name: smoke-tests-basic-ubuntu`` for the ``tlxc`` namespace.

.. seealso:: :term:`Namespace in the glossary <namespace>`,
   :ref:`connections_and_namespaces`

.. _lava_lxc_protocol_android:

Using the LXC protocol to support Android
*****************************************

.. _lava_android_naming_conventions:

LAVA Android Naming Conventions
===============================

* **production image** - a build of Android which, when deployed to a device,
  means that the device is **not** visible to ``adb``. This is typically how a
  device is configured when first sold to the consumer.

* **developer image** - a build of Android which, when deployed to a device,
  means that the device **is visible** to ``adb``. Devices configured this way
  will be able to have the image replaced using any machine, just by connecting
  a suitable cable, so these images are not typically deployed onto hardware
  which will be sold to the customer without having this image replaced with a
  production image.

Introduction
============

Installing tools like ``adb`` and ``fastboot`` on the dispatcher can be
problematic. Some of these issues arise from the need to put many different
types of devices onto a single dispatcher, other issues arise from needing to
use different versions of the build on the devices. Testing an old system may
require downgrading support like ``openjdk``, new devices or new builds may
require upgrading the same support. Containers isolate this variation so that
each testjob can have a suitable container instead of needing to deal with
changes on the dispatcher:

#. **Shared lock issues** - Tools can require use of ``flock`` and similar
   methods to distinguish a connection to one device from another.

#. **Version disparities** - different device versions, different OS versions,
   may require different support in debug tools like ``adb`` and ``fastboot``.

#. **hardware issues** - USB hub variability.

.. seealso:: :ref:`lxc_deploy` for more information on the administration of
   LXC for LAVA.

.. figure:: images/lxc.svg
    :width: 80%
    :align: center
    :alt: LXC in LAVA

Using the ``lava-lxc`` protocol, a Lava Test Shell is provided inside the LXC
to support installing and configuring whatever tools, packages and files which
the testjob will need to use. Installing ``adb`` in this test shell removes the
need to have a POSIX type shell on the device. Files can be pushed and pulled
from the device and executed using the Android support in the image.

.. _lava_android_requirements:

Requirements and Limitations
============================

#. The image deployed to the device **must** enable the Android Debug Bridge,
   i.e. a :term:`developer image`. This means enabling developer access over
   USB or TCP. This rules out the use of production images.

#. A list of packages to install into the bare container to provide the
   necessary tools to communicate with the device.

#. The LXC depends on underlying kernel architecture. For armel, armhf, etc.
   dispatcher should run on these architectures.

#. Each distribution has its own template and the templates do not have common
   options. It can be difficult to have generic support for all distributions.

#. :term:`namespaces <namespace>` to relate different job actions to run in the
   LXC and for the device.

Protocol elements
=================

.. include:: examples/test-jobs/hi6220-hikey.yaml
   :code: yaml
   :start-after: path: hi6220-hikey.yaml
   :end-before: - boot:

.. index:: LXC - feedback, feedback output

.. _feedback_using_lxc:

Feedback from the device
========================

Actions within the LXC can cause the device to emit messages on the serial
console. Some devices can have problems maintaining the serial connection if
this data is not flushed and the data itself can be useful to test writers to
debug issues and failures.

LAVA automatically reads from all other :term:`namespaces <namespace>` whilst
processing the test shell in another namespace and outputs this as ``feedback``
data. When viewing a test job log file, feedback can be turned on or off using
the buttons at the top of the log file.

To support feedback, the ``lava-test-shell``
:ref:`individual_connection_timeout_overrides` is set to 10 seconds by default.
(There are no suitable prompts to match, so reading feedback continues until
the connection timeout is reached, without failing the test shell itself.)

.. seealso:: :ref:`timeouts`

Differences between LXC releases
================================

The release specified in the ``lava-lxc`` protocol will determine some of the
packages which will need to be installed in the container. In particular, any
container based on a Debian later than ``jessie`` will need two packages to be
added to the setup of the container before the container can be used:
``systemd`` and ``systemd-sysv``. These two packages **must** be specified in
the deployment list.

In addition, some packages will have been renamed between releases. For example,
``android-tools-adb`` exists in Debian unstable but it is an old build and will
at some point be replaced by ``adb`` which is also available in unstable but not
in ``jessie``.

.. caution:: Always check the availability of the packages needed for particular
   releases by using a local chroot or VM. Only packages which are included in
   the specified release can be installed using the deployment list. Packages
   from other repositories will have to be installed using the test definition.

Sample Job Definition
=====================

.. include:: examples/test-jobs/hi6220-hikey.yaml
   :code: yaml
