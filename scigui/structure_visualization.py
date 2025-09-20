import subprocess as sp
from platform import system as osname
from pathlib import Path
import configparser
from shutil import which



def run_viewer(file, vs='jmol'):
   if vs == 'jmol':
      # Check for java.
      print("Attempting to start structure visualization software.")
      try:
         java_path = which("java")
         print("Java found:", java_path)
      except:
         print("Java not found:")
         return (True, "Java not found. Aborting visualization.")

      # Get the path to jmol from the .ini file.
      print("Attempting to read configuration file.")
      config = configparser.ConfigParser()
      try:
         config.read(Path.home() / '.Corvus' / 'scigui.ini')
         print("scigui.ini found.")
         print(config)
         try:
            jmol_path = config['visualization']['jmol_path']
            print("Jmol found: ", jmol_path)
         except:
            print("Jmol not found: aborting")
            return (True, 'Jmol path not found in config file.')

      except:
         print("No scigui.ini config file found. Attempting to find jmol.")
         try:
            jmol_path = Path(which("jmol"))
            if not jmol_path.is_file(): return (True, 'jmol not found.')
            print("Jmol found: ", jmol_path)
         except:
            print("Jmol not found: aborting visualization.")
            return (True, 'Config file not found.')

      port = 8008
      # Get the path to java and jmol.
      #env_path = Path('miniconda3/envs/Corvus')

      # The 'Windows' block ignores stdout and stderr in deference to Win10
      # hanging after one command received.  The Linux block works in Ubuntu.
      if osname() == 'Windows':
         java = Path(java_path)
         if not java.is_file(): 
             print('java not found')
             return (True,'java not found.')
         jmol = Path(jmol_path)
         if not jmol.is_file(): 
             print('jmol not found')
             return (True, 'jmol not found.')
         jmol_args = [file]
         jmol_cmd = [jmol] + jmol_args
         jmol = sp.Popen(jmol_cmd, shell=False,
           stdin=sp.PIPE,
           bufsize=0,
           universal_newlines=True,
           stdout=sp.DEVNULL,
           stderr=sp.DEVNULL)
      elif osname() == 'Darwin' or osname() == "Linux":
         #java = Path(java_path) / Path('java')
         #if not java.is_file(): return (True,'java not found.')
         jmol_args = [file]
         print(jmol_path)
         jmol_cmd = [jmol_path] + [file]
         jmol = sp.Popen(jmol_cmd, shell=False,
           bufsize=0,
           universal_newlines=True)
