=================
Changelog History
=================


Intake-esm v2019.10.15
=======================

Features
--------

- Rewrite `intake-esm`'s core based on `(esm-collection-spec)`_ Earth System Model Collection specification
  (:pr:`135`) `Anderson Banihirwe`_, `Matthew Long`_, `Ryan Abernathey`_


.. _(esm-collection-spec): https://github.com/NCAR/esm-collection-spec


Breaking changes
----------------

- Replaced `intake.open_esm_metadatastore()` with `intake.open_esm_datastore()`, see the API reference for more details.
- `intake-esm` won't build collection catalogs anymore. `intake-esm` now expects an ESM collection JSON file
  as input. This JSON should conform to the `(esm-collection-spec)`_ Earth System Model Collection specification.



Intake-esm v2019.08.23
=======================


Features
--------
- Add `mistral` data holdings to `intake-esm-datastore` (:pr:`133`) `Aaron Spring`_

- Add support for `NA-CORDEX`_ data holdings. (:pr:`115`) `Julia Kent`_

- Replace `.csv` with `netCDF` as serialization format when saving the built collection to disk.
  With `netCDF`, we can record very useful information into the global attributes of the netCDF dataset.
  (:pr:`119`) `Anderson Banihirwe`_

  .. code-block:: python

    >>> import intake
    >>> col = intake.open_esm_metadatastore(collection_input_definition="GLADE-CMIP5")
    >>> col.ds
    <xarray.Dataset>
    Dimensions:          (index: 615296)
    Coordinates:
    * index            (index) int64 0 1 2 3 4 ... 615292 615293 615294 615295
    Data variables:
        resource         (index) object ...
        resource_type    (index) object ...
        direct_access    (index) bool True True True True ... True True True True
        activity         (index) object ...
        ensemble_member  (index) object ...
        experiment       (index) object ...
        file_basename    (index) object ...
        file_fullpath    (index) object ...
        frequency        (index) object ...
        institute        (index) object ...
        mip_table        (index) object ...
        model            (index) object ...
        modeling_realm   (index) object ...
        product          (index) object ...
        temporal_subset  (index) object ...
        variable         (index) object ...
        version          (index) object ...
    Attributes:
        created_at:             2019-08-07T18:05:09.371259
        intake_esm_version:     2019.5.11.post153
        intake_version:         0.5.2
        intake_xarray_version:  0.3.1
        collection_spec:        {"name": "GLADE-CMIP5", "collection_type": "cmip5...
        name:                   GLADE-CMIP5
        collection_type:        cmip5

- Add string representation of `ESMMetadataStoreCatalog`` object (:pr:`122`) `Anderson Banihirwe`_


- Automatically build missing collections by calling ``esm_metadatastore(collection_name="GLADE-CMIP5")``
  if the specified collection is part of the curated collections in `intake-esm-datastore`_.
  (:pr:`124`) `Anderson Banihirwe`_

  .. code-block:: python

    >>> import intake
    >>> col = intake.open_esm_metadatastore(collection_name="GLADE-CMIP5")
    >>> # if "GLADE-CMIP5" collection isn't built already, the above is equivalent to:
    >>> col = intake.open_esm_metadatastore(collection_input_definition="GLADE-CMIP5")

- Revert back to using official DRS attributes when building CMIP5 and CMIP6 collections.
  (:pr:`126`) `Anderson Banihirwe`_

- Add ``.df`` property for interfacing with the built collection via dataframe
  To maintain backwards compatiblity. (:pr:`127`) `Anderson Banihirwe`_

- Add ``unique()`` and ``nunique()`` methods for summarizing count and unique values in a collection.
  (:pr:`128`) `Anderson Banihirwe`_

  .. code-block:: python

    >>> import intake
    >>> col = intake.open_esm_metadatastore(collection_name="GLADE-CMIP5")
    >>> col
    GLADE-CMIP5 collection catalogue with 615853 entries:
            > 3 resource(s)

            > 1 resource_type(s)

            > 1 direct_access(s)

            > 1 activity(s)

            > 218 ensemble_member(s)

            > 51 experiment(s)

            > 312093 file_basename(s)

            > 615853 file_fullpath(s)

            > 6 frequency(s)

            > 25 institute(s)

            > 15 mip_table(s)

            > 53 model(s)

            > 7 modeling_realm(s)

            > 3 product(s)

            > 9121 temporal_subset(s)

            > 454 variable(s)

            > 489 version(s)

    >>> col.nunique()
    resource                3
    resource_type           1
    direct_access           1
    activity                1
    ensemble_member       218
    experiment             51
    file_basename      312093
    file_fullpath      615853
    frequency               6
    institute              25
    mip_table              15
    model                  53
    modeling_realm          7
    product                 3
    temporal_subset      9121
    variable              454
    version               489
    dtype: int64
    >>> col.unique(columns=['frequency', 'modeling_realm'])
    {'frequency': {'count': 6, 'values': ['mon', 'day', '6hr', 'yr', '3hr', 'fx']},
    'modeling_realm': {'count': 7, 'values': ['atmos', 'land', 'ocean', 'seaIce', 'ocnBgchem',
    'landIce', 'aerosol']}}

.. _NA-CORDEX: https://na-cordex.org/
.. _intake-esm-datastore: https://github.com/NCAR/intake-esm-datastore


Bug Fixes
----------

-  For CMIP6, extract ``grid_label`` from directory path instead of file name. (:pr:`127`) `Anderson Banihirwe`_


Internal Changes
----------------




Intake-esm v2019.8.5
=====================


Features
--------

- Support building collections using inputs from intake-esm-datastore repository.
  (:pr:`79`) `Anderson Banihirwe`_

- Ensure that requested files are available locally before loading data into xarray datasets.
  (:pr:`82`) `Anderson Banihirwe`_ and `Matthew Long`_

- Split collection definitions out of config. (:pr:`83`) `Matthew Long`_

- Add ``intake-esm-builder``, a CLI tool for building collection from the command line. (:pr:`89`) `Anderson Banihirwe`_

- Add support for CESM-LENS data holdings residing in AWS S3. (:pr:`98`) `Anderson Banihirwe`_

- Sort collection upon creation according to order-by-columns, pass urlpath through stack for use in parsing collection filenames (:pr:`100`) `Paul Branson`_

Bug Fixes
----------

- Fix bug in ``_list_files_hsi()`` to return list instead of filter object.
  (:pr:`81`) `Matthew Long`_ and `Anderson Banihirwe`_

- ``cesm._get_file_attrs`` fixed to break loop when longest `stream` is matched. (:pr:`80`) `Matthew Long`_

- Restore ``non_dim_coords`` to data variables all the time. (:pr:`90`) `Anderson Banihirwe`_

- Fix bug in ``intake_esm/cesm.py`` that caused ``intake-esm`` to exclude hourly (1hr, 6hr, etc..) CESM-LE data.
  (:pr:`110`) `Anderson Banihirwe`_

- Fix bugs in ``intake_esm/cmip.py`` that caused improper regular expression matching for ``table_id`` and ``grid_label``.
  (:pr:`113`) & (:issue:`111`) `Naomi Henderson`_ and `Anderson Banihirwe`_


Internal Changes
----------------

- Refactor existing functionality to make intake-esm robust and extensible. (:pr:`77`) `Anderson Banihirwe`_

- Add ``aggregate._override_coords`` function to override dim coordinates except time
  in case there's floating point precision difference. (:pr:`108`) `Anderson Banihirwe`_

- Fix CESM-LE ice component peculiarities that caused intake-esm to load data improperly.
  The fix separates variables for `ice` component into two separate components:

  - ``ice_sh``: for southern hemisphere
  - ``ice_nh``: for northern hemisphere

  (:pr:`114`) `Anderson Banihirwe`_


Intake-esm v2019.5.11
======================


Features
---------

- Add implementation for The Gridded Meteorological Ensemble Tool (GMET) data holdings (:pr:`61`) `Anderson Banihirwe`_
- Allow users to specify exclude_dirs for CMIP collections (:pr:`63`) & (:issue:`62`) `Anderson Banihirwe`_
- Keep CMIP6 ``tracking_id`` in merge_keys (:pr:`67`) `Anderson Banihirwe`_
- Add implementation for ERA5 datasets (:pr:`68`) `Anderson Banihirwe`_


Intake-esm v2019.4.26
======================


Features
---------

- Add implementations for ``CMIPCollection`` and ``CMIPSource`` (:pr:`38`) `Anderson Banihirwe`_
- Add support for CMIP6 data (:pr:`46`) `Anderson Banihirwe`_
- Add implementation for The Max Planck Institute Grand Ensemble (MPI-GE) data holdings (:pr:`52`) & (:issue:`51`) `Aaron Spring`_ and `Anderson Banihirwe`_
- Return dictionary of datasets all the time for consistency (:pr:`56`) `Anderson Banihirwe`_

Bug Fixes
----------

- Include multiple netcdf files in same subdirectory (:pr:`55`) & (:issue:`54`) `Naomi Henderson`_ and `Anderson Banihirwe`_


Intake-esm v2019.2.28
======================

Features
---------

- Allow CMIP integration (:pr:`35`) `Anderson Banihirwe`_

Bug Fixes
----------

- Fix bug on build catalog and move `exclude_dirs` to `locations` (:pr:`33`) `Matthew Long`_


Trivial/Internal Changes
------------------------

- Change Logger, update dev-environment dependencies, and formatting fix in input.yml (:pr:`31`) `Matthew Long`_
- Update CircleCI workflow (:pr:`32`) `Anderson Banihirwe`_
- Rename package from `intake-cesm` to `intake-esm` (:pr:`34`) `Anderson Banihirwe`_


.. _`Aaron Spring`: https://github.com/aaronspring
.. _`Anderson Banihirwe`: https://github.com/andersy005
.. _`Julia Kent`: https://github.com/jukent
.. _`Matthew Long`: https://github.com/matt-long
.. _`Naomi Henderson`: https://github.com/naomi-henderson
.. _`Paul Branson`: https://github.com/pbranson
.. _`Ryan Abernathey`: https://github.com/rabernat
