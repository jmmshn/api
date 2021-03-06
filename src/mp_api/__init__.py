# coding: utf-8
""" Primary MAPI module """
from pkg_resources import get_distribution, DistributionNotFound
from monty.serialization import loadfn

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = None  # type: ignore

from mp_api.core.settings import MAPISettings
from pathlib import Path

settings = MAPISettings()

try:
    if Path(settings.app_path).exists():
        mapi = loadfn(settings.app_path)
        app = mapi.app
    else:
        app = None
        if settings.debug:
            print(f"Failed loading App at {settings.app_path}")

except Exception as e:
    # Something went wrong with loading default app
    if settings.debug:
        print("Failed loadning App")
        print(e)
        app = None
