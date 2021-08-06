# coding: utf-8
""" Primary MAPI module """
import os
from pkg_resources import get_distribution, DistributionNotFound
from monty.serialization import loadfn
from mp_api.matproj import MPRester

try:
    __version__ = get_distribution(__package__).version
    from setuptools_scm import get_version
    __version__ = get_version(root='../../', relative_to=__file__)
except (DistributionNotFound, ImportError, LookupError):  # pragma: no cover
    __version__ = os.environ.get("SETUPTOOLS_SCM_PRETEND_VERSION")

from mp_api.core.settings import MAPISettings
from pathlib import Path

settings = MAPISettings()

try:  # pragma: no cover
    if Path(settings.app_path).exists():
        mapi = loadfn(settings.app_path)
        app = mapi.app
    else:
        app = None
        if settings.debug:
            print(f"Failed loading App at {settings.app_path}")

except Exception as e:  # pragma: no cover
    # Something went wrong with loading default app
    if settings.debug:
        print("Failed loading App")
        print(e)
        app = None
