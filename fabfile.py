# coding=utf-8

from fabric.api import local, run, cd, env
from fabric.colors import green

env.use_ssh_config = True
env.shell = '/bin/sh -c'

env.hosts = ['sakura']

def sakura():

  print(green('Deploying...'))

  with cd('www/imageroundr'):
    run('git pull')

  print(green('Done.'))
