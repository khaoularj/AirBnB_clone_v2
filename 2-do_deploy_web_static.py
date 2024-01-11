#!/usr/bin/python3
# this script distributes an archive to the web servers
# using the function do_deploy
from fabric.api import env, run, put
from os.path import exists
env.hosts = ['54.144.45.0', '52.91.150.220']


def do_deploy(archive_path):
    """the function that distributes an archive to the web server"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(
            archive_path.split('/')[1][:-4]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_path.split('/')[1],
                    archive_path.split('/')[1][:-4]))
        run("rm /tmp/{}".format(archive_path.split('/')[1]))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(archive_path.split('/')[1][:-4],
                    archive_path.split('/')[1][:-4]))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_path.split('/')[1][:-4]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_path.split('/')[1][:-4]))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
