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

  log('sakura')

import time
import datetime

def log(task='none'):
  log = (
    "task:%s\t"
    "host:%s\t"
    "user:%s\t"
    "time:%s\t"
  ) % (task, env.hosts, env.user, str(datetime.datetime.utcnow().isoformat()) + '+00:00')

  open('.fablog', 'a').write(log.strip() + '\n')

def push():
  local('git push hub HEAD')
