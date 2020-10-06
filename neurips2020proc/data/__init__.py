from pathlib import Path

from . import __path__ as _dir_nspath

__all__ = ["data_dir"]

data_dir = Path(list(_dir_nspath)[0])
