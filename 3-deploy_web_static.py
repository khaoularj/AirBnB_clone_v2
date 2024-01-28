#!/usr/bin/python3
# this script creates and distributes an archive to the
# web servers, using the function deploy
from pack_web_static import do_pack
from do_deploy_web_static import do_deploy
from fabric.api import env
env.hosts = ['54.144.45.0', '52.91.150.220']


def deploy():
    """function that creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
