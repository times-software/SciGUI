import subprocess as sp
from platform import system as osname
from pathlib import Path

def run_viewer(file, vs='jmol'):
   if vs == 'jmol':
      port = 8008
      # Get the path to java and jmol.
      env_path = Path('miniconda3/envs/Corvus')
      

      # The 'Windows' block ignores stdout and stderr in deference to Win10
      # hanging after one command received.  The Linux block works in Ubuntu.
      if osname() == 'Windows':
         java = Path.home() / env_path / Path('Library/bin/java.exe')
         if not java.is_file(): 
             print('java not found')
             return (True,'java not found.')
         jmol = Path.home() / env_path / Path('Library/share/jmol/Jmol.jar')
         if not jmol.is_file(): 
             print('jmol not found')
             return (True, 'jmol not found.')
         jmol_args = ['-o', '-j', 'sync -8008', file]
         jmol_cmd = [java, '-jar', jmol] + jmol_args
         jmol = sp.Popen(jmol_cmd, shell=False,
           stdin=sp.PIPE,
           bufsize=0,
           universal_newlines=True,
           stdout=sp.DEVNULL,
           stderr=sp.DEVNULL)
      elif osname() == 'Darwin' or osname() == "Linux":
         java = Path.home() / env_path / Path('bin/java')
         if not java.is_file(): return (True,'java not found.')
         jmol = Path.home() / env_path / Path('share/jmol/Jmol.jar')
         if not jmol.is_file(): retur (True, 'jmol not found.')
         jmol_args = ['-o', '-j', 'sync -8008', file]
         jmol_cmd = [java, '-jar', jmol] + jmol_args
         jmol = sp.Popen(jmol_cmd, shell=False,
           bufsize=0,
           universal_newlines=True)
