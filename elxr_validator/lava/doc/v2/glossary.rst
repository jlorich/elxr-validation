.. index:: glossary

.. _glossary:

Glossary of terms
=================

.. seealso:: :ref:`naming_conventions`

..
   Please add new terms in alphabetical order and feel free to relocate
   existing terms to match. All terms are automatically added to the Sphinx
   index. Ensure that new terms added to the glossary are also linked from the
   body of the documentation. The glossary is a reference only, users are not
   expected to need to read the entire glossary to find the information. FIXME
   - need to add many more terms here

**A** [ :term:`action level` ] [ :term:`alias` ]

**B** [ :term:`BMC` ]

**C** [ :term:`chart` ] [ :term:`ci loop` ]

**D** [ :term:`device` ] [ :term:`device dictionary` ]
[:term:`device status transition` ]
[ :term:`device tag` ] [ :term:`device type` ] [ :term:`developer image` ]
[ :term:`dispatcher` ] [ :term:`distributed deployment` ] [ :term:`DTB` ]
[ :term:`DUT` ]

**F** [ :term:`frontend` ]

**G** [ :term:`group` ]

**H** [ :term:`hacking session` ] [ :term:`health check` ]
[:term:`hidden device type` ] [ :term:`hostname` ]

**I** [ :term:`inline` ] [ :term:`interface tag` ]

**J** [ :term:`jinja2` ] [ :term:`job context` ] [ :term:`job definition` ]

**L** [ :term:`LAVA_LXC_HOME` ] [ :term:`LXC` ] [ :term:`lxc://` ]

**M** [ :term:`messageID` ] [ :term:`metadata` ] [ :term:`MultiNode` ]

**N** [ :term:`namespace` ]

**O** [ :term:`offline` ]

**P** [ :term:`parameters` ] [ :term:`PDU` ] [ :term:`physical access` ]
[ :term:`pipeline` ] [ :term:`priority` ] [ :term:`production image` ]
[ :term:`prompts` ] [ :term:`protocol` ]

**Q** [ :term:`query` ]

**R** [ :term:`refactoring` ]
[ :term:`remote worker`]
[ :term:`restricted device` ]
[ :term:`results` ]
[ :term:`retired` ]
[ :term:`role` ] [ :term:`rootfs` ] [ :term:`rootfstype` ]

**S** [ :term:`scheduler` ]

**T** [ :term:`target_group` ] [ :term:`test run` ] [ :term:`test shell` ]
[ :term:`test suite` ] [ :term:`tftp` ] [ :term:`token` ]

**U** [ :term:`UART` ]

**V** [ :term:`visibility`] [ :term:`VLANd` ]

**W** [ :term:`worker` ]

.. glossary::

  action level
    The :term:`pipeline` is organized into sections and levels. The first
    section of the pipeline is given level 1. Sub tasks of that section start
    with level 1.1 and so on. Log files and job definitions will refer to
    actions using the level. Details of the action can then be accessed using
    the level as the location: ``job/8360/definition#2.4.5``

    .. seealso:: :ref:`pipeline_construction`

  alias
    A string which can be used to relate the descriptive device-type name to a
    particular list of aliases which could be used to lookup the matching
    device-type. This can be useful to list the :term:`device tree blobs <DTB>`
    which can be used with this device-type. (Aliases can be used in job
    submissions directly.)

  BMC
    A Baseboard Management Controller (BMC) is an embedded controller
    on a computer mainboard which allows external monitoring and
    management of the computer system.

  chart
    A chart allows users to track :term:`results` over time using
    :term:`queries <query>`.

  ci loop
    Continuous Integration (CI) typically involves repeated automated
    submissions using automated builds of the artifacts prompted by
    modifications made by developers. Providing feedback to the developers on
    whether the automated build passed or failed creates a loop. LAVA is
    designed as one component of a ci loop.

    .. seealso:: :ref:`ci_loop`, :ref:`continuous_integration` and
      :term:`metadata`

  device
    A device in LAVA is an instance of a :term:`device type`.

    * Test writers: see :term:`device tag`

    * Admins: see :ref:`create_device_database` and :term:`device dictionary`.

    * Developers: see :ref:`naming_conventions`

  device dictionary
    The device dictionary holds data which is specific to one device within a
    group of devices of the same device type. For example, the power control
    commands which reference a single port number. The dictionary itself is a
    key:value store within the LAVA server database which admins can modify to
    set configuration values according to the :term:`pipeline` design.

    .. seealso:: :ref:`device_dictionary_help`,
      :ref:`create_device_dictionary`, :ref:`configuring_serial_ports`
      and :ref:`viewing_device_dictionary_content`.

  device status transition
    A record of when a device changed :ref:`device_status`, who caused the
    transition, when the transition took place as well as any message assigned
    to the transition. Individual transitions can be viewed in LAVA at
    ``<server>scheduler/transition/<ID>`` where the ID is a sequential integer.
    If the transition was caused by a job, this view will link to that job.

  device tag
    A tag is a device specific label which describes specific hardware
    capabilities of this specific device. Test jobs using tags will fail if no
    suitable devices exist matching the requested device tag or tags. Tags are
    typically used when only a proportion of the devices of the specified type
    have hardware support for a particular feature, possibly because those
    devices have peripheral hardware connected or enabled. A device tag can
    only be created or assigned to a particular device by a lab admin. When
    requesting tags, remember to include a description of what the tagged
    device can provide to a Test Job.

    .. seealso:: :ref:`device_tags_example`

  device type
    The common type of a number of devices in LAVA. The device type may have a
    :term:`health check` defined. Devices with the same device type will run
    the same health check at regular intervals. See :ref:`device_types`.

  developer image
    A build of Android which, when deployed to a device, means that the device
    **is visible** to ``adb``. Devices configured this way will be able to have
    the image replaced using any machine, just be connecting a suitable cable,
    so these images are not typically deployed onto hardware which will be sold
    to the customer without having this image replaced with a production image.

    .. seealso:: :ref:`lava_lxc_protocol_android`

  dispatcher
    A machine to which multiple devices are connected. The dispatcher has
    ``lava-dispatcher`` installed and passes the commands to the device and
    other processes involved in running the LAVA test. A dispatcher does not
    need to be at the same location as the server which runs the scheduler. The
    term ``dispatcher`` relates to how the machine operates the
    ``lava-dispatch`` process using ``lava-worker``. The related term
    :term:`worker` relates to how the machine appears from the server.

  distributed deployment
    A method of installing LAVA involving a single server and one or
    more :term:`remote workers <remote worker>` which communicate with the
    master using HTTP. This method spreads the load of running tests on
    devices multiple dispatchers.

  DTB
    Device Tree Blob - file describing hardware configuration,
    commonly used on ARM devices with the Linux kernel. See
    https://en.wikipedia.org/wiki/Device_tree for more information.

  DUT
    Device Under Test - a quick way to refer to the :term:`device` in LAVA.

  frontend
    ``lava-server`` provides a generic `frontend` consisting of the Results,
    Queries, Job tables, Device tables and Charts. Many projects will need to
    customize this data to make it directly relevant to the developers. This is
    supported using the :ref:`xml_rpc` and REST API support.

    .. seealso:: :ref:`what_is_lava_not` and :ref:`custom_result_handling`.

  group
    LAVA uses the Django local group configuration (synchronizing
    Django groups with external groups like LDAP is **not** supported).
    Users can be added to groups after the specified group has been
    created by admins using the :ref:`django_admin_interface` or the
    ``lava-server manage groups`` and ``lava-server manage users``
    command line support.

  hacking session
    A test job which uses a particular type of test definition to allow users
    to connect to a test device and interact with the test environment
    directly. Normally implemented by installing and enabling an SSH daemon
    inside the test image. Not all devices can support hacking sessions.

    .. seealso:: :ref:`hacking_session`.

  health check
    A test job for one specific :term:`device type` which is automatically run
    at regular intervals to ensure that the physical device is capable of
    performing the minimum range of tasks. If the health check fails on a
    particular device, LAVA will automatically put that device :term:`offline`.
    Health checks have higher :term:`priority` than any other jobs.

    .. seealso:: :ref:`health_checks`.

  hidden device type
    A device type can be hidden by the LAVA administrators. Devices of a
    :ref:`v2_hidden_device_type` will only be visible to owners of at least
    once device of this type. Other users will not be able to access the job
    output, device status transition pages or bundle streams of devices of a
    hidden type. Devices of a hidden type will be shown as ``Unavailable`` in
    tables of test jobs and omitted from tables of devices and device types if
    the user viewing the table does not own any devices of the hidden type.

  hostname
    The unique name of this device in this LAVA instance, used to link all
    jobs, results and device information to a specific device configuration.

  inline
    A type of test definition which is contained within the job submission
    instead of being fetched from a URL. These are useful for debugging tests
    and are recommended for the synchronization support within
    :term:`MultiNode` test jobs.

    .. seealso:: :ref:`inline_test_definitions`

  interface tag
     An interface tag is similar to :term:`device tag` but operate **solely**
     within the :term:`VLANd` support. An interface tag may be related to the
     link speed which is achievable on a particular switch and port - it may
     also embed information about that link.

     .. seealso:: :ref:`vland_device_tags`.

  jinja2
    Jinja2 is a templating language for Python, modelled after Django’s
    templates. It is used in LAVA for device-type configuration, as it allows
    conditional logic and variable substitution when generating device
    configuration for the dispatcher.

    .. seealso:: http://jinja.pocoo.org/docs/dev/

  job context
    Test job definitions can include the ``context:`` dictionary at the top
    level. This is used to set values for selected variables in the device
    configuration, subject to the administrator settings for the device
    templates and device dictionary. A common :ref:`example
    <explain_first_job>` is to instruct the template to use the
    ``qemu-system-x86_64`` executable when starting a QEMU test job using the
    value ``arch: amd64``. All device types support variables in the job
    context.

    .. seealso:: :ref:`override_variables_context` and
      :ref:`multinode_roles`

  job definition
    The original YAML submitted to create a job in LAVA is retained in the
    database and can be viewed directly from the job log. Although the YAML is
    the same, the YAML may well have changed since the job was submitted, so
    some care is required when modifying job definitions from old jobs to make
    a new submission. If the job was a :term:`MultiNode` job, the MultiNode
    definition will be the unchanged YAML from the original submission; the job
    definition will be the parsed YAML for this particular device within the
    MultiNode job.

  LAVA_LXC_HOME
    The path within :term:`LXC` set to ``/lava-lxc`` by default. From the host
    machine this path would be something like
    ``/var/lib/lxc/{container-name}/rootfs/lava-lxc``. Any files downloaded by
    :ref:`deploy_to_download` will be copied to this location which can then be
    accessible from within the container.

  LXC
    `Linux containers <https://en.wikipedia.org/wiki/LXC>`_ are used in LAVA to
    allow custom configurations on the dispatcher for each use. The extra
    utilities or services are transparently available to the pipeline code and
    selected device nodes can also be made available, depending on admin
    configuration of the devices.

    .. seealso:: :ref:`deploy_using_lxc`, :ref:`lxc_deploy`,
      :ref:`feedback_using_lxc` and :ref:`lxc_protocol_reference`

  lxc://
    This is a URL scheme specific to LAVA which points to files available in
    :term:`LAVA_LXC_HOME`. An URL like ``lxc:///boot.img`` will refer to
    ``/var/lib/lxc/{container-name}/rootfs/lava-lxc/boot.img`` on the host or
    ``/lava-lxc/boot.img`` within the :term:`LXC`. This URL scheme is valid
    only when :ref:`lxc_protocol_reference` is defined in the test job. It also
    only makes sense for the ``deploy`` and ``boot`` actions.

    .. note:: Pay attention to 3 forward slashes in the URL when referring to a
              file.

    .. seealso:: :ref:`deploy_to_download`

  messageID
    Each message sent using the :ref:`multinode_api` uses a ``messageID`` which
    is a string, unique within the group. It is recommended to make these
    strings descriptive (use underscores instead of spaces). The messageID will
    be included the the log files of the test.

  metadata
    Test jobs should include metadata relating to the files used within the
    job. Metadata consists of a key and a value, there is no limit to the
    number of key value pairs as long as each key is unique within the metadata
    for that test job.

    .. seealso:: :ref:`job_metadata`

  MultiNode
     A single test job which runs across multiple devices, or using
     multiple independent connections to the same device.

     .. seealso:: :ref:`multinode_api`.

  namespace
    A simple text label which is used to tie related actions together within a
    test job submission where multiple deploy, boot or test actions are
    defined. A common use case for namespaces is the use of :term:`LXC` in a
    test job where some actions are to be executed inside the LXC and some on
    the :term:`DUT`. The namespace is used to store the temporary locations of
    files and other dynamic data during the running of the test job so that,
    for example, the test runner is able to execute the correct test definition
    YAML. Namespaces are set in the test job submission.

    .. seealso:: :term:`protocol in the glossary <protocol>`,
      :ref:`namespaces_with_lxc`, :ref:`deploy_using_lxc` and
      :ref:`lava_lxc_protocol_android`

  offline
    A status of a device which allows jobs to be submitted and reserved for the
    device but where the jobs will not start to run until the device is online.
    Devices enter the offline state when a health check fails on that device or
    the administrator puts the device offline.

  parameters
    Parameters are used in a number of contexts in LAVA.

    * For the use of parameters to control test jobs see
      :ref:`test_action_parameters` and :ref:`overriding_constants`.

    * For the use of parameters within the codebase of the pipeline, see
      :ref:`developer_guide` and :ref:`naming_conventions`.

  PDU
    PDU is an abbreviation for Power Distribution Unit - a network-controlled
    set of relays which allow the power to the devices to be turned off and on
    remotely. Many PDUs are supported by ``pdudaemon`` to be able to
    hard reset devices in LAVA.

  physical access
    The user or group with physical access to the device, for example to fix a
    broken SD card or check for possible problems with physical connections.
    The user or group with physical access is recommended to be one of the
    superusers.

  pipeline
    Within LAVA, the ``pipeline`` is the V2 model for the dispatcher code where
    submitted jobs are converted to a pipeline of discrete actions - each
    pipeline is specific to the structure of that submission and the entire
    pipeline is validated before the job starts. The model integrates concepts
    like fail-early, error identification, avoid defaults, fail and diagnose
    later, as well as giving test writers more rope to make LAVA more
    transparent. See :ref:`dispatcher_design` and :ref:`pipeline_use_cases`.

  priority
    A job has a default priority of ``Medium``. This means that the job will be
    scheduled according to the submit time of the job, in a list of jobs of the
    same priority. Every :term:`health check` has a higher priority than any
    submitted job and if a health check is required, it will **always** run
    before any other jobs. Priority only has any effect while the job is queued
    as ``Submitted``.

  production image
    A build of Android which, when deployed to a device, means that the device is
    **not** visible to ``adb``. This is typically how a device is configured when
    first sold to the consumer.

    .. seealso:: :ref:`lava_lxc_protocol_android`

  prompts
   A list of prompt strings which the test writer needs to specify in advance
   and which LAVA will use to determine whether the boot was successful. One of
   the specified prompts **must** match before the test can be started.

  protocol
    A protocol in LAVA is a method of interacting with external services using
    an :abbr:`API (Application Programming Interface)` instead of with direct
    shell commands or via a test shell. Examples of services in LAVA which use
    protocols include :term:`LXC`, :term:`MultiNode` and :term:`VLANd`. The
    protocol defines which API calls are available through the LAVA interface
    and the Pipeline determines when the API call is made.

    .. seealso:: :ref:`protocols`

  query
    See :ref:`result_queries`. Queries are used to identify test jobs and
    associated results which match specified criteria based on the results or
    metadata.

  refactoring
    Within LAVA, the process of developing the :term:`pipeline` code in
    parallel with the existing code, resulting in new elements alongside old
    code - possibly disabled on some instances. See :ref:`dispatcher_design`
    and :ref:`pipeline_use_cases`.

  remote worker
    A dispatcher with devices attached which does not have a web frontend but
    which uses an HTTP connection to a remote lava-server to control the
    operation of test jobs on the attached devices.

    .. seealso:: :ref:`growing_your_lab`

  restricted device
    A restricted device can only accept job submissions from the device owner.
    If the device owner is a group, all users in that group can submit jobs to
    the device.

  results
    LAVA results provide a generic view of how the tests performed within a
    test job. Results from test jobs provide support for :term:`queries
    <query>`, :term:`charts <chart>` and :ref:`downloading results
    <downloading_results>` to support later analysis and :term:`frontends
    <frontend>`. Results can be viewed whilst the test job is running. Results
    are also generated during the operation of the test job outside the test
    action itself. All results are referenced solely using the test job ID.

    .. seealso:: :ref:`recording_test_results`, :ref:`custom_result_handling` and
      :ref:`viewing_results`.

  retired
    A device is retired when it can no longer be used by LAVA. A retired device
    allows historical data to be retained in the database, including log files,
    result bundles and state transitions. Devices can also be retired when the
    device is moved from one instance to another.

  role
    An arbitrary label used in MultiNode tests to determine which tests are run
    on the devices and inside the YAML to determine how the devices
    communicate.

  rootfs
     A tarball for the root file system.

  rootfstype
     Filesystem type for the root filesystem, e.g. ext2, ext3, ext4.

  scheduler
    There is a single scheduler in LAVA, running on the server. The
    scheduler is responsible for assigning devices to submitted test jobs.

    .. seealso:: :ref:`scheduling`

  target_group
    In :term:`MultiNode`, the single submission is split into multiple test
    jobs which all share a single ``target_group`` which uses a string as a
    unique ID. The ``target_group`` is usually transparent to test writers but
    underpins how the rest of the MultiNode API operates.

  test case
    An individual test case records a single test event as a pass or fail
    along with measurements, units or a reference.

    .. seealso:: :ref:`results_intro`

  test run
    The result from a single test definition execution. The individual id and
    result of a single test within a test run is called the :term:`Test Case
    <test case>`.

  test shell
    Most test jobs will boot into a POSIX type shell, much like if the user had
    used ``ssh``. LAVA uses the test shell to execute the tests defined in the
    Lava Test Shell Definition(s) specified in the job definition.

  test set
    Test writers can choose to subdivide a single :term:`test suite` into
    multiple sets, for example to handle repetition or changes to the
    parameters used to run the tests.

    .. seealso:: :ref:`test_set_results`

  test suite
    Individual test cases are aggregated into a test suite and given the name
    specified in the test job definition. The Test Suite is created when
    results are generated in the running test job. LAVA uses a reserved test
    suite called ``lava`` for results generated by the actions running the test
    job itself. Results in the ``lava`` suite contain details like the commit
    hash of the test definitions, messages from exceptions raised if the job
    ends Incomplete and other data about how the test behaved.

    .. seealso:: :ref:`results_test_suite`

  tftp
    Trivial File Transfer Protocol (TFTP) is a file transfer protocol, mainly
    to serve boot images over the network to other machines (e.g. for PXE
    booting). The protocol is managed by the `tftpd-hpa package
    <https://tracker.debian.org/pkg/tftp-hpa>`_ and **not** by LAVA directly.

  token
    LAVA uses tokens to authenticate users via the :ref:`xml_rpc` and REST APIs.

    .. seealso:: :ref:`authentication_tokens`

  UART
    A :abbr:`UART (Universal asynchronous receiver-transmitter)` is the most
    common way to make a serial connection to a :term:`DUT`. Some devices can
    support multiple UARTs. This can be useful as a way to isolate the test
    shell processing from kernel messages.

    .. seealso:: `UART article on Wikipedia
       <https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter>`_
       and :ref:`multiple_serial_support`.

  visibility
    Supports values of ``public``, ``personal`` and ``group`` and
    controls who is allowed to view the job and the results generated
    by the job. This includes whether the results are available to
    queries and to charts::

     visibility: personal

    or::

     visibility: public

    ``group`` visibility setting should list the groups users must be
    in to be allowed to see the job. If more than one :term:`group` is
    listed, users must be in all the listed groups to be able to view
    the job or the results::

     visibility:
       group:
         - developers
         - project

    In this example, users must be members of both ``developers`` group
    and ``project`` group. Groups must already exist in the Django
    configuration for the instance.

  VLANd
    VLANd is a daemon to support virtual local area networks in LAVA. This
    support is specialized and requires careful configuration of the entire
    LAVA instance, including the physical layout of the switches and the
    devices of that instance.

    .. seealso:: :ref:`vland_in_lava` or :ref:`admin_vland_lava`.

  worker
    The worker is responsible for running the ``lava-worker`` daemon to start
    and monitor test jobs running on the dispatcher. Each server has a
    worker installed by default. When a dispatcher is added to the master as a
    separate machine, this worker is a :term:`remote worker`. The admin decides
    how many devices to assign to which worker. In large instances, it is
    common for all devices to be assigned to remote workers to manage the load
    on the master.

