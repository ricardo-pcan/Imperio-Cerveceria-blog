from fabric.api import env, require, task
from fabric.contrib.project import rsync_project
from fabric.colors import green

@task
def digital():
    """
    Defines variables for staging environment (http://162.243.119.21)
    """
    # User
    env.user = 'imperio'

    # Local SSH
    env.hosts = ['162.243.119.21']

    # remote directory
    env.site_dir = '/var/www/vhosts/imperiocerveceria.com'
    
    # exclude files
    env.excludes = [
        "*.pyc",
        ".DS_Store"
    ]


@task
def deploy():
    """
    Deploys application to the previously specified environment using rsync.
    """
    require("site_dir")
    require("excludes")

    rsync_project(
        remote_dir=env.site_dir,
        local_dir='src/_site/',
        exclude=env.excludes,
        delete=False
    )

    print green('Deploy exitoso.')
