#!/usr/bin/python3
"""this script generates a .tgz archive
from the contents of the web_static folder of the
AirBnB Clone repo, using the function do_pack"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """this function generates a .tgz archive"""

    if not os.path.exists("versions"):
        local("mkdir -p versions")

    time = "%Y%m%d%H%M%S"
    arch_name = "web_static_{}.tgz".format(datetime.utcnow().strftime(time))

    print("Packing web_static to versions/{}".format(arch_name))

    command = "tar -cvzf versions/{} web_static".format(arch_name)
    result = local(command)

    if result.failed:
        return None
    else:
        print("web_static packed: versions/{} -> {}Bytes"
              .format(arch_name, os.path.getsize("versions/{}"
                                                 .format(arch_name))))
        return "versions/{}".format(arch_name)


if __name__ == "__main__":
    result = do_pack()
    if result:
        size = os.path.getsize(result)
        print("web_static packed: {} -> {}Bytes".format(result, size))
