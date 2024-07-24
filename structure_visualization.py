import subprocess as sp
from platform import system as osname
from pathlib import Path

def run_viewer(file, vs='jmol'):
   if vs == 'jmol':
      port = 8008
      # Get the path to java and jmol.
      env_path = Path('miniconda3/envs/crystal_viewer')
      java = Path.home() / env_path / Path('bin/java')
      jmol = Path.home() / env_path / Path('share/jmol/Jmol.jar')
      jmol_args = ['-o', '-j', 'sync -8008', file]
      jmol_cmd = [java, '-jar', jmol] + jmol_args

      # The 'Windows' block ignores stdout and stderr in deference to Win10
      # hanging after one command received.  The Linux block works in Ubuntu.
      if osname() == 'Windows':
         jmol = sp.Popen(jmol_cmd, shell=False,
           stdin=sp.PIPE,
           bufsize=0,
           universal_newlines=True,
           stdout=sp.DEVNULL,
           stderr=sp.DEVNULL)
      elif osname() == 'Darwin' or osname() == "Linux":
         jmol = sp.run(jmol_cmd, shell=False,
           bufsize=0,
           universal_newlines=True)
