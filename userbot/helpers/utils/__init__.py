from .extdl import *
from .paste import *
flag = True
check = 0
while flag:
    try:
        from . import format as _format
        from . import tools as _nandetools
        from . import utils as _nandeutils
        from .events import *
        from .format import htmlmentionuser, mentionuser, parse_pre

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
