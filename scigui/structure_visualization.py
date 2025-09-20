import subprocess as sp
from platform import system as osname
from pathlib import Path
import configparser
from shutil import which

def read_ini(filename):
    """
    Attempts to read an INI file using various UTF encodings.

    Args:
        filename (str): The path to the INI file.

    Returns:
        configparser.ConfigParser or None: A populated ConfigParser object if successful,
                                         None otherwise.
    """
    encodings_to_try = ['utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be']
    config = configparser.ConfigParser()

    for encoding in encodings_to_try:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                config.read_file(f)
            print(f"Successfully read '{filename}' with encoding: {encoding}")
            return config
        except UnicodeDecodeError:
            print(f"Failed to read '{filename}' with encoding: {encoding} (UnicodeDecodeError)")
            continue
        except Exception as e:
            print(f"An unexpected error occurred while reading '{filename}' with encoding {encoding}: {e}")
            continue

    print(f"Could not read '{filename}' with any of the attempted UTF encodings.")
    return None

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
      try:
          config = read_ini(Path.home() / '.Corvus' / 'scigui.ini')
      #   config.read(Path.home() / '.Corvus' / 'scigui.ini')
          print("scigui.ini found.")
      #   print(config)
          try:
             jmol_path = config['visualization']['jmol_path']
             print("Jmol found: ", jmol_path)
          except:
             print("Jmol not found: aborting")
             return (True, 'Jmol path not found in config file.')
      #
      except:
         print("No scigui.ini config file found. Attempting to find jmol.")
         try:
            jmol_path = Path(which("jmol")).parent
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
      print(osname())
      if osname() == 'Windows':
         java = Path(java_path)
         if not java.is_file(): 
             print('java not found')
             return (True,'java not found.')
         jmol = Path(jmol_path).parent / 'Jmol.jar'
         if not jmol.is_file(): 
             print('jmol not found')
             return (True, 'jmol not found.')
         jmol_args = ["-jar", jmol, file]
         jmol_cmd = [java] + jmol_args
         jmol = sp.Popen(jmol_cmd, shell=False,
           stdin=sp.PIPE,
           bufsize=0,
           universal_newlines=True,
           stdout=sp.DEVNULL,
           stderr=sp.DEVNULL)
      elif osname() == 'Darwin' or osname() == "Linux":
         java = Path(java_path)
         if not java.is_file(): return (True,'java not found.')
         jmol_args = [file]
         print(jmol_path)
         jmol_cmd = [java, '-jar', jmol_path / Path('Jmol.jar')] + [file]
         jmol = sp.Popen(jmol_cmd, shell=False,
           bufsize=0,
           universal_newlines=True)
