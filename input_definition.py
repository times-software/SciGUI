import input_errors as ie
from input_types import *


# Make this a class. The class object should contain a dict() object. 
# Instantiation will be the only way to fill the dictionary. Different 
# types of configurations will be specified by a "code" string variable
# in the instantiation input.
# category will a
class input_definition_dict():

   def _fill_key_info(self,help,kinds,code,importance,category,field_labels,ranges=None,
                  defaults = None, field_types = None,fexpandable=False,lexpandable=False,required=None):
      key_info = dict()
      key_info['help'] = help
      key_info['kinds'] = kinds

      key_info['code'] = code
      key_info['importance'] = importance
      key_info['category'] = category
      key_info['field_labels'] = field_labels
      if field_types is not None:
            key_info['field_types'] = field_types
      key_info['ranges'] = ranges
      key_info['fexpandable'] = fexpandable
      key_info['lexpandable'] = lexpandable
      key_info['defaults'] = defaults
      key_info['required'] = required
      return key_info

   #############################################################################################
   #         BEGIN DEFINITION OF KEYWORDS FOR CORVUS
   #############################################################################################

   def __init__(self,input_type):
      self.input_type = input_type
      self.required_keys = {}
      self.inp_def_dict = dict()
      self._fill_input_dict(input_type)
      self.predefined = {}
      self.set_predefined()
      if input_type == 'corvus':
         self.first_keys = ['target_list']

   def set_predefined(self):
      # List predefined sets of keywords corresponding to certain types of calculations. To be used
      # for a "Quick Start" menu option.
      if self.input_type == 'corvus':
         self.predefined = {'FEFF spectrum from CIF': \
                            {'target_list':[['cfavg'],['helper']], \
                                                    '_required': ['cfavg_target','cif_input','absorbing_atom_type','feff.edge'], \
                                                    '_associated':['feff.fms','feff.scf','feff.exchange']}, \
                           'FEFF spectrum from Mat. Proj. id': {'target_list':[['cfavg'],['helper']], \
                                                    '_required': ['cfavg_target','mp_id','mp_apikey','absorbing_atom_type','feff.edge']}, \
                           'FEFF xanes of a single absorber': {'target_list':[['xanes'],['feff']], \
                                                               '_required':['feff.edge','absorbing_atom','cluster']}, \
                           'FEFF EXAFS of a single absorber': {'target_list':[['exafs'],['feff']], \
                                                               '_required':['feff.edge','absorbing_atom','cluster']}, \
                           'FEFF XES of a single absorber': {'target_list':[['xes'],['feff']], \
                                                               '_required':['feff.edge','absorbing_atom','cluster']}, \
                           'FEFF RIXS of a single absorber': {'target_list':[['rixs','feff']], \
                                                               '_required':['feff.edge','absorbing_atom','cluster']} \
         }
         

   def set_associated(self):
      pass

   # Below are the definitions of the different input types for the GUI to handle
   def _fill_input_dict(self,input_type):
      if input_type == 'corvus':
            # Special keyword holds type of input 'corvus'
            self.inp_def_dict['_input_type'] = 'corvus'

            ###################################################
            #   Start definition of keywords for corvus
            ###################################################

            #  target_list
            help =  ['Space separated list with all the target properties requested for this calculation, followed' + \
                     ' by line with space separated list of codes to be used for calculation of the corresponding property. ', 
                     'Possible properties to chose from:',
                     ' 1. xanes,xes,rixs - calculate XANES spectrum of a single site.', 
                     ' 2. cfavg - Calculate the configurational average over sites in a crystal structure. Choose the property to average using cfavg_target.']
            kinds =  [
               [ inp_choice ],[inp_choice],
               ]
            code =  'general'
            importance =  'essential'
            category =  'property'
            field_labels =  [['property'],['code']]
            ranges =  [['xanes,exafs,xes,rixs,cfavg'],['feff,siesta,ocean,vasp,abinit,orca,helper']]
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  {'cfavg': ['cfavg_target'], 'xanes': ['cluster', 'absorbing_atom', 'feff.edge'], 'xes': ['cluster', 'absorbing_atom', 'feff.edge'], 'rixs': ['cluster', 'absorbing_atom', 'feff.edge']}
            self.inp_def_dict["target_list"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  title
            help =  ['Title of this calculation.']
            kinds =  [
               [ inp_paragraph ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'system'
            field_labels =  [['title']]
            ranges =  None
            defaults =  [['This is a Corvus calculation ']]
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["title"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  scratch
            help =  ['Directory for disk scratch for those Handlers that require large amounts of', 'disk. If the directory is not present or it can not be created, Corvus reverts', 'to the default.', 'NOTE: This input variable is not fully implemented yet.']
            kinds =  [
               [ inp_file_name ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'computational'
            field_labels =  [['scratch dir']]
            ranges =  None
            defaults =  [['.']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["scratch"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  usesaved
            help =  ['Use previously calculated data rather than recalculating']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'computational'
            field_labels =  [['usesaved']]
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["usesaved"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  multiprocessing_ncpu
            help =  ['Number of processors to use in multiprocessing.', 'This should be maximum of the number of cpus on a single', 'node.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'computational'
            field_labels =  [['ncpu']]
            ranges =  [['1,']]
            defaults =  [[1]]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["multiprocessing_ncpu"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            # polarization
            help = ['Set 3 different polarization directions to calculate in cartesian coordinates.',
                    'By default, these are set to x, y, z, i.e., ',
                     '  polarization{',
                     '     1.0 0.0 0.0',
                     '     0.0 1.0 0.0',
                     '     0.0 0.0 1.0',
                     '     }']

            kinds = [[inp_int, inp_int, inp_int],
                     [inp_int, inp_int, inp_int],
                     [inp_int, inp_int, inp_int]]

            code = 'general'

            importance = 'useful'
            category = 'spectrum'
            defaults = None
            ranges = None
            field_labels = [['x', 'y', 'z']]
            fexpandable = False
            lexpandable = True
            req = None
            self.inp_def_dict["polarization"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            # atomic_charge
            help = ['charge to be placed on each atoms of a given species.',
                    'atomic_symbol charge',
                    '...']
            
            kinds = [[inp_str, inp_float]]
            code = 'general'
            importance = 'useful'
            category = 'system_properties'
            field_labels = [['Atom', 'charge']]
            defaults = None
            field_types = None
            ranges = None
            fexpandable = False
            lexpandable = True
            req = None
            self.inp_def_dict["atomic_charge"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            # materials project keywords
            # mp_id
            help = ['Single material project id. Can be mp-NNNN or just the number.']
            kinds = [[inp_str]]
            code = 'general'
            importance = 'useful'
            category = 'structure'
            field_labels = [['mp-id']]
            defaults = None
            field_types = None
            ranges = None
            fexpandable = False
            lexpandable = False
            req = {'all': ['mp_apikey']}
            self.inp_def_dict["mp_id"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            # mp_apikey
            help = ['API key for the materials project.']
            kinds = [[inp_str]]
            code = 'general'
            importance = 'useful'
            category = 'structure'
            field_labels = [['apikey']]
            defaults = None
            fexpandable = False
            lexpandable = False
            req = None
            self.inp_def_dict["mp_apikey"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            
            #  usehandlers
            help =  ['Explicitely declare what Handlers are to be used in the generation of the', 'Workflow. This helps the current simple Workflow generator when a given target', 'is provided by more than one Handler.', 'Current possible values are:', 'Feff, FeffRixs, Dmdw, Abinit, Vasp, Nwchem, Orca']
            kinds =  [
               [ inp_str ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'method'
            field_labels =  [['handler']]
            ranges =  [['feff,helper,vasp,siesta']]
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["usehandlers"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  method
            help =  ['Method used to compute the target. This variable is somewhat context-dependent', 'and is ccurrently not fully implemented.', 'Current possible values are:', 'dft, mp2, ccsd']
            kinds =  [
               [ inp_str ],
               ]
            code =  'general'
            importance =  'not-implemented'
            category =  'method'
            field_labels =  [['method']]
            ranges =  [['dft,mp2,ccsd']]
            defaults =  [['dft']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["method"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  xc
            help =  ['Exchange-correlation functional to use if the "method" selected is "dft".', 'Current possible values are:', 'lda, pbe, b3lyp']
            kinds =  [
               [ inp_str ],
               ]
            code =  'general'
            importance =  'important'
            category =  'method,dft'
            field_labels =  [['exch. corr.']]
            ranges =  [['lda,gga']]
            defaults =  [['lda']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["xc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  pspfiles
            help =  ['List of pseudopotentials for each atom in the system. Each line contains', 'the label for the atoms (usually the element % name) and the name of the file', 'with the pseudopotential. The required format for the files will depend on the', 'Handler used.']
            kinds =  [
               [ inp_str, inp_file_name ],
               ]
            code =  'general'
            importance =  'important'
            category =  'method,dft,pseudopotentials'
            field_labels =  [['atom_label', 'psp file']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["pspfiles"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  scf_conv
            help =  ['Convergence threshold for SCF cycles (HF, DFT, etc) in au. The value set by', 'this variable might be internally overridden if the target requires tighter', 'convergence settings.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'scf,convergence'
            field_labels =  [['conv. thr']]
            ranges =  [['0,']]
            defaults =  [['1.0e-5']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["scf_conv"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  keep_symm
            help =  ['Toggle the preservation of initial symmetry in optimizations.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'optimization'
            field_labels =  [['keep symmetry']]
            ranges =  None
            defaults =  [['True']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["keep_symm"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  constant_volume
            help =  ['Keep the simulation cell volume constant in cell optimizations.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'general'
            importance =  'important'
            category =  'optimization'
            field_labels =  [['constant volume']]
            ranges =  None
            defaults =  [['True']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["constant_volume"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nkpoints
            help =  ['Define the number of k-point in each direction of the grid for reciprocal', 'space simulations.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'electrons,reciprocal'
            field_labels =  [['nka', 'nkb', 'nkc']]
            ranges =  [['1,', '1,', '1,']]
            defaults =  [['1', '1', '1']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nkpoints"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nqpoints
            help =  ['Define the number of q-point perturbations in each direction of the grid for', 'density functional perturbation theory (DFPT) simulations.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'phonons,reciprocal'
            field_labels =  [['nqa', 'nqb', 'nqc']]
            ranges =  [['1,', '1,', '1,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nqpoints"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  pw_encut
            help =  ['Planwave energy cutoff for reciprocal space simulations, in au.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'important'
            category =  'basis,dft,electrons'
            field_labels =  [['pw encut']]
            ranges =  [['0.0,']]
            defaults =  [['15.0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["pw_encut"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  numberofconfigurations
            help =  ['Set the number of configurations used in disordered systems.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'md,disorder'
            field_labels =  [['# of config.']]
            ranges =  [['0,']]
            defaults =  [['10']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["numberofconfigurations"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  clusterradius
            help =  ['Radius of clusters created from cif files.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'structure'
            field_labels =  [['rmax']]
            ranges =  [['0.0,']]
            defaults =  [['12.0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["clusterradius"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif_input
            help =  ['cif input file name.']
            kinds =  [
               [ inp_structure_file ],
               ]
            code =  'general'
            importance =  'essential'
            category =  'structure'
            field_labels =  [['cif file']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif_input"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  supercell_dimensions
            help =  ['supercell dimensions (number of cells in each direction).']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure,reciprocal'
            field_labels =  [['n1','n2','n3']]
            ranges =  [['1,', '1,', '1,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["supercell_dimensions"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ismetal
            help =  ['Toggle whether the system should be treated as a metal or as an insulator.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'general'
            importance =  'important'
            category =  'system properties'
            field_labels =  [['is metal?']]
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ismetal"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ene_int
            help =  ['Internal (electronic) energy of the system, in au.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'system properties'
            field_labels =  [['internal energy']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ene_int"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cell_vectors
            help =  ['Normalized simulation cell vector directions. These vectors are scaled using', 'the "cell_scaling_iso" and "cell_scaling_abc" input variables to generate the', 'simulation cell.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               [ inp_float, inp_float, inp_float ],
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['x', 'y', 'z'], [None, None, None], [None, None, None]]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cell_vectors"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cell_struc_opt_flags
            help =  ['Toggle the optimization of the x, y and z coordinates of each atom in the', 'system.']
            kinds =  [
               [ inp_bool, inp_bool, inp_bool ],
               ]
            code =  'general'
            importance =  'important'
            category =  'optimization,structure'
            field_labels =  [['x', 'y', 'z']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["cell_struc_opt_flags"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cell_struc_xyz_red
            help =  ['Structure of the simulation cell in reduced coordinates if the system is', 'extended and has periodic boundary conditions.']
            kinds =  [
               [ inp_str, inp_float, inp_float, inp_float ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['type', 'x', 'y', 'z']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["cell_struc_xyz_red"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  number_of_atoms
            help =  ['Number of atoms in the system']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['# of atoms']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["number_of_atoms"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  species
            help =  ['chemical species and number of each species']
            kinds =  [
               [ inp_str, inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['species', 'N']]
            ranges =  [[None, '1,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["species"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cell_scaling_iso
            help =  ['Unitless isotropic scaling of the unit cell.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['latt. scaling']]
            ranges =  [['0.0,']]
            defaults =  [['1.0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cell_scaling_iso"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cell_scaling_abc
            help =  ['Scaling of the a, b an c axes of the simulation cell, in Angstroms.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['a', 'b', 'c']]
            ranges =  [['0,', '0,', '0,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cell_scaling_abc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cell_angles_abc
            help =  ['Scaling of the a, b an c axes of the simulation cell, in Angstroms.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'general'
            importance =  'important'
            category =  'structure'
            field_labels =  [['alpha', 'beta', 'gamma']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cell_angles_abc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  mac_diel_const
            help =  ['Approximate value of the macroscopic dielectric constant of the system used in', 'some methods to accelerate convergence of the SCF cycle.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'importantce'
            category =  'system properties'
            field_labels =  [['diel. const.']]
            ranges =  [['0,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["mac_diel_const"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cluster
            help =  ['Structure of the system is the system is not extended (i. e. is a molecule or', 'cluster). The coordinates are in Angstroms, and have xyz format, i.e.,', 'Atomic_symbol1 x y z', 'Atomic_symbol2 x y z', '.', '.', '.']
            kinds =  [
               [ inp_str, inp_float, inp_float, inp_float ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'structure'
            field_labels =  [['At. Sym.', 'x', 'y', 'z']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["cluster"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  absorbing_atom
            help =  ['Index of the absorbing atom for core spectroscopies such as XANES, EXAFS and', 'XES. The index counts from one for the first atom in the associated cluster (see above).']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'spectrum'
            field_labels =  [['abs atom index']]
            ranges =  [['1,']]
            defaults =  [[1]]
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["absorbing_atom"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  absorbing_atom_type
            help =  ['Symbol of atom you would like to calculate the XANES for. Will loop over symmetry unique sites defined', 'in the CIF file denoted by cif_input (see below).']
            kinds =  [
               [ inp_str ],
               ]
            code =  'general'
            importance =  'important'
            category =  'spectrum'
            field_labels =  [['atom spec.']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["absorbing_atom_type"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  charge
            help =  ['Net charge of the system.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'important'
            category =  'system properties'
            field_labels =  [['charge']]
            ranges =  None
            defaults =  [['0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["charge"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  multiplicity
            help =  ['Multiplicity of the system.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'IMPORTANCE'
            category =  'system properties, spin, magnetism'
            field_labels = None
            ranges =  [['1,']]
            defaults =  [['0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["multiplicity"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  spectral_broadening
            help =  ['Broadening used in some spectroscopic methods.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'importance'
            category =  'spectrum'
            field_labels =  [['half width']]
            ranges =  [['0,']]
            defaults =  [['0.0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["spectral_broadening"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  fermi_shift
            help =  ['Shift of the fermi-energy in eV.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'spectrum'
            field_labels =  [['fermi shift']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["fermi_shift"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  spin_moment
            help =  ['spin moments of atomic types', 'set spin moment for ferromagnetic systems.', 'Only allows one moment per chemical element.', 'Z spin_moment']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'general'
            importance =  'useful'
            category =  'spin,magnetism'
            field_labels =  [['atm sym.', 'mag. mom.']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["spin_moment"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  xanes_file
            help =  ['file to read xanes from - 2 column file']
            kinds =  [
               [ inp_file_name ],
               ]
            code =  'general'
            importance =  'advanced'
            category =  'spectrum'
            field_labels =  [['xas file']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["xanes_file"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  spectralFunction_file
            help =  ['file to read spectral function from - 2 column file']
            kinds =  [
               [ inp_file_name ],
               ]
            code =  'general'
            importance =  'advanced'
            category =  'spectrum'
            field_labels =  [['spfcn file']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["spectralFunction_file"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  abinit.verbatim
            help =  ['The content of this input variable is passed as is (i. e. "verbatim") into the', 'input of all Abinit calculations, and it is meant to help with any Abinit', 'input that is currently not implemented in Corvus. Thus, it should be used', 'carfully to avoid inconsistencies with the automatically generated input.', 'Users should refed to the Abinit manual for information on this extra input.']
            kinds =  [
               [ inp_paragraph ],
               ]
            code =  'abinit'
            importance =  'useful'
            category =  'general'
            field_labels =  [['abinit input']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["abinit.verbatim"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  abinit.ngqpt
            help =  ["Equivalent to Abinit's ngqpt input variable: Defines the number of q-point", 'perturbations in each direction of the grid for density functional', 'perturbation theory (DFPT) simulations, and is that equivalent to the general', '"nqpoints" Corvus input variable. Please refer to the Abinit manual for', 'further details.', '', 'NOTE: This code-specific input variable will be replaced by the general', '"nqpoints" variable in the future.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'abinit'
            importance =  'important'
            category =  'phonons,reciprocal'
            field_labels =  [['ngqx', 'nqqy', 'ngqz']]
            ranges =  [['1,', '1,', '1,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["abinit.ngqpt"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  abinit.ng2qpt
            help =  ["Equivalent to Abinit's (anaddb) ng2qpt input variable: Defines the number of", 'q-point perturbations in each direction of the finer grid for density', 'functional perturbation theory (DFPT) simulations. Please refer to the', 'Abinit manual for further details.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'abinit'
            importance =  'important'
            category =  'phonons,reciprocal'
            field_labels =  [['ngq2x', 'ngq2y', 'ngq2z']]
            ranges =  [['1,', '1,', '1,']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["abinit.ng2qpt"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  dmdw.ioflag
            help =  ['Set the amount of output printed by DMDW. Possible values are:', '0: Terse, prints out only the desired result (s^2, u^2, etc).', '1: Verbose, prints out the pole frequencies and weights, as well as', 'estimates of the Einstein temperatures for each path.', 'Please refer to the DMDW section of the Feff manual for further details.', '', 'NOTE: The current format described below is temporary for compatibility with', 'previous versions of Corvus. This will be changed to "Integer" in the future.']
            kinds =  [
               [ inp_paragraph ],
               ]
            code =  'dmdw'
            importance =  'useful'
            category =  'phonons,exafs,spectrum'
            field_labels =  [['io flag']]
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["dmdw.ioflag"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  dmdw.nlanc
            help =  ['Set the number of Lanczos poles (i. e. iterations) in DMDW. Larger values', 'usually improve convergence of the target quantity. However, the number of', 'poles should not exceed the dimensions of the subspace spanned by the', 'projection of the path into the appropriate eigenmodes of the Hessian. This', 'means that this variable should always be less than 3*N-6, where N is the', 'number of atoms in the system. In practice, a value of 6-8 is sufficient to', 'obtain converged mean square relative displacements (MSRD, or s^2) for EXAFS.', 'For crystallographic mean square displacements (MSD, or u^2) at least 16 poles', 'are usually needed. Please refer to the DMDW section of the Feff manual for', 'further details.', '', 'NOTE: The current format described below is temporary for compatibility with', 'previous versions of Corvus. This will be changed to "Integer" in the future.']
            kinds =  [
               [ inp_paragraph ],
               ]
            code =  'dmdw'
            importance =  'IMPORTANCE'
            category =  'computational,spectrum,phonons'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["dmdw.nlanc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  dmdw.paths
            help =  ['Set up the path descriptors that will generate the list of paths for which', 'properties will be calculated. The list has the following form:', '<Number of descriptors>', '<Descriptor 1>', '<Descriptor 2>', '.', '.', '', 'Each descriptor has the form:', '<Number of atoms in path> <Atom index 1> ... <Max. path length (Ang)>', '', 'The atom indices can take the value 0 which acts as a wildcard for all atoms', 'in the system.', '', 'Examples:', '', '2', '2 1 0   3.0', '3 2 0 5 6.0', '', 'This section defines 2 paths descriptors. The first one generates all paths', 'with two atoms, starting in atom 1 and going to all other atoms in the', 'systems, but subject to a maximum effective path length of 3.0 Ang. The', 'second one generates all paths with three atoms, starting in atom 2 and', 'ending in atom 5, while passing trhough all other atoms in the system, but', 'with a maximum effective length of 6.0 Ang.', 'Using the same syntax atoms can be selected to compute their u^2. For example', 'the paths section', '', '1', '1 0 0.0', '', 'will produce u^2 for all atoms in the system. Please refer to the DMDW', 'section of the Feff manual for further details.', '', 'NOTE: The current format described below is temporary for compatibility with', 'previous versions of Corvus.']
            kinds =  [
               [ inp_paragraph ],
               ]
            code =  'dmdw'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs,phonons'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["dmdw.paths"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  dmdw.tempgrid
            help =  ['Set up the temperature grid to compute the thermal properties in DMDW. It has', 'the following form:', '', '<Number of temperature> <Min. temp.> <Max. temp.>', '', 'If the number of desired temperatures is just one, the maximum temperature', 'input is not needed. Please refer to the DMDW section of the Feff manual for', 'further details.', '', 'NOTE: The current format described below is temporary for compatibility with', 'previous versions of Corvus.']
            kinds =  [
               [ inp_paragraph ],
               ]
            code =  'dmdw'
            importance =  'IMPORTANCE'
            category =  'temperature,phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["dmdw.tempgrid"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.basis
            help =  ['Set the Gaussian basis set to be used in the NWChem calculations. The format', 'is the same as in NWChem:', '', '<Atom label> <Basis set name>', '.', '.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["nwchem.basis"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.qmd.nstep_nucl
            help =  ['Set the number of nuclear motion steps in a quantum MD simulation.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'md'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.qmd.nstep_nucl"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.qmd.dt_nucl
            help =  ['Set the time step for nuclear motion in a quantum MD simulation.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'md'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.qmd.dt_nucl"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.qmd.targ_temp
            help =  ['Set the target temperature in a quantum MD simulation.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'md'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.qmd.targ_temp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.qmd.thermostat
            help =  ['Set the thermostat type to be used in a quantum MD simulation.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'md'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.qmd.thermostat"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.qmd.print_xyz
            help =  ['Toggle printing of xyz coordinates in a quantum MD simulation.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'md'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.qmd.print_xyz"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.xc
            help =  ['Set the exchange correlation potential for an NWChem DFT simulation.', 'NOTE: This input variable will be superseded in the future by the more', 'general "xc" variable.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.xc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.mult
            help =  ['Set the multiplicity of the system for an NWChem DFT simulation.', 'NOTE: This input variable will be superseded in the future by the more', 'general "multiplicity" variable.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.mult"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.qmd.snapstep
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'md'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.qmd.snapstep"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.xas.alpha
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.xas.alpha"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.xas.xrayenergywin
            help =  []
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.xas.xrayenergywin"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.xas.nroots
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.xas.nroots"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.xas.vec
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.xas.vec"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.iter
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.iter"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.charge
            help =  ['Set the net charge of the system for an NWChem DFT simulation.', 'NOTE: This input variable will be superseded in the future by the more', 'general "charge" variable.', '', 'Please refer to the NWChem manual for further details.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.charge"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nwchem.xaselem
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'nwchem'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nwchem.xaselem"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  nuctemp
            help =  ['', 'nuctemp', '', 'temp', '', 'Specify the temperature (in K) for the nuclear motion (DW factors).']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'IMPORTANCE'
            category =  'temperature,exafs,spectrum,md'
            field_labels = None
            ranges =  None
            defaults =  [['300.0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["nuctemp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  debyetemp
            help =  ['', 'debyetemp', '', 'temp', '', 'Specify the Debye Model temperature (in K) for the calculation of EXAFS DW', 'factors.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'general'
            importance =  'IMPORTANCE'
            category =  'temperature,exafs,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["debyetemp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  dmdw_nlanczos
            help =  ['', 'dmdw_nlanczos', '', 'nLanczos_Interations', '', 'Specify the number of Lanczos iterations to be done for the calculation of', 'EXAFS DW factors with the dynamical matrix method.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'general'
            importance =  'IMPORTANCE'
            category =  'phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['6']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["dmdw_nlanczos"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.MPI.CMD
            help =  ['MPI command to use for parallel calculations, e.g., mpirun, srun, or mpiexec.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.MPI.CMD"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.MPI.ARGS
            help =  []
            kinds =  [
               [inp_str],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.MPI.ARGS"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.atoms
            help =  ['', 'feff.atoms', '', 'x1  y1  z1 ipot1', 'x2  y2  z2 ipot2', '.', '.', '.', '', 'Specify atomic positions in cartesian coordinates (in Angstroms) and', 'unique potential indices of each atom in the cluster, one atom per line.']
            kinds =  [
               [ inp_float, inp_float, inp_float, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.atoms"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.hole
            help =  ['DEPRECATED: Use feff.edge instead.', '', 'Specify the edge using the hole number ihole, e.g.,', 'K-edge : ihole = 1', 'L1-edge: ihole = 2', 's02 specifies the EXAFS amplitude reduction factor, and should be set to 1.']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.hole"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.overlap
            help =  ['feff.overlap can be used to construct approximate overlapped atom potentials', 'when atomic coordinates are not known or specified.', 'NOTE: This input variable is not fully implemented yet.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.overlap"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.control
            help =  ['', 'feff.control', '', 'feff.control lets you run one or more of the feff program modules', 'separately. There is a switch for each of six parts of feff:', '0 means not to run that module, 1 means to run it.']
            kinds =  [
               [ inp_int, inp_int, inp_int, inp_int, inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.control"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.exchange
            help =  ['feff.exchange', 'Use feff.exchange to change the self-energy used in x-ray absorption', 'calculations. ixc is an index specifying the potential model to use for the', 'fine structure, and the optional ixc0 is the index of the model to use for', 'the background function. The calculated potential can be corrected by adding', 'a constant shift to the Fermi level given by vr0 and to a pure imaginary', '"optical" potential (i.e., uniform decay) given by vi0. Typical errors in', "Feff's self-consistent Fermi level estimate are about 1 eV.", '(The feff.corrections input is similar but allows the user to make small', 'changes in vi0 and vr0 after the rest of the calculation is completed, for', 'example in a fitting process.)', '', 'Indices for the available exchange models:', '0 Hedin-Lundqvist + a constant imaginary part', '1 Dirac-Hara + a constant imaginary part', '2 ground state + a constant imaginary part', '3 Dirac-Hara + HL imag part + a constant imaginary part', '5 Partially nonlocal: Dirac-Fock for core + HL for valence electrons + a', 'constant imaginary part']
            kinds =  [
               [ inp_int, inp_float, inp_float, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.exchange"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.ion
            help =  ['feff.ion', 'feff.ion ionizes all atoms with unique potential index ipot.', 'NOTE: This input variable is not fully implemented yet.']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.ion"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.title
            help =  ['Set title for this feff calculation.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.title"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.folp
            help =  ['feff.folp', 'Set the overlap for unique potential ipot.']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.folp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rpath
            help =  ['feff.rpath', 'Set maximum path length for path expansion calculations of EXAFS, EXELFS,', 'DAFS, etc.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rpath"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            # feff.equivalence_nmax
            help = ['Set the maximum number of potentials per species to use. Effects feff.equivalence{ 2 }']
            kinds = [[inp_int]]
            code = 'feff'
            importance = 'useful'
            category = 'scf,potentials'
            field_labels = 'nmax'
            ranges = [['1,']]
            defaults = [[5]]
            field_types = None
            fexpandable = False
            lexpandable = False
            req = None
            self.inp_def_dict["feff.equivalence_nmax"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)

            #  feff.debye
            help =  ['feff.debye', 'Set temperature and Debye temperature for calculations of EXAFS Debye-Waller factors.', 
                     '   feff.debye{ temp debye_temp }', 
                     'NOTE: This input variable is not fully implemented yet.']
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.debye"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.dmdw
            help =  ['NOTE: This input variable is not fully implemented yet.']
            kinds =  [
               [ inp_str, inp_int, inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.dmdw"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rmultiplier
            help =  ['feff.rmultiplyer', 'Multiply coordinates of all atoms by rmult, expanding or contracting the', 'system.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rmultiplier"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.ss
            help =  ['Set an']
            kinds =  [
               [ inp_int, inp_int, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.ss"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.print
            help =  ['feff.pring', 'Set print level for each module of FEFF:', 'pot:', "0 write 'pot.bin' only", "1 add 'misc.dat'", "2 add 'potNN.dat'", "3 add 'atomNN.dat'", '', 'xsph:', "0 write 'phase.bin' and 'xsect.bin' only", "1 add 'axafs.dat' and 'phase.dat'", "2 add 'phaseNN.dat' and 'phminNN.dat'", "3 add 'ratio.dat' (for XMCD normalization) and 'emesh.dat'.", '', 'fms:', "0 write 'gg.bin'", "1 write 'gg.dat'", '', 'path:', "0 write 'paths.dat' only", "1 add 'crit.dat'", "5 Write only 'crit.dat' and do not write 'paths.dat'. (This is useful", "genfmt 0 write 'list.dat', and write 'feff.bin' with all paths with", 'importance greater than or equal to two thirds of the curved wave', 'importance criterion', '', 'genfmt:', "0 write 'list.dat', and write 'feff.bin' with all paths with importance", 'greater than or equal to two thirds of the curved wave importance', 'criterion', "1 write all paths to 'feff.bin'", '', 'ff2x:', "0 write 'chi.dat' and 'xmu.dat'", "2 add 'chipNNNN.dat' (chi(k) for each path individually)", "3 add 'feffNNNN.dat' and 'files.dat', and do not add 'chipNNNN.dat'", 'files']
            kinds =  [
               [ inp_int, inp_int, inp_int, inp_int, inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.print"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.potentials
            help =  ['feff.potentials', 'ipot iz pot_label lfms1 lfms2 stoichiometry', '...', '', 'Set unique potentials for FEFF calculation.', '']
            kinds =  [
               [ inp_int, inp_int, inp_str, inp_int, inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.potentials"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.potentials.spin
            help =  ['feff.potentials.spin', 'ipot spin_moment', '...', '', 'Set spin moments of atoms defined in potentials card']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.potentials.spin"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.lfms1
            help =  ['set maximum angular momentum to use in potentials']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure,spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['-1']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.lfms1"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.lfms2
            help =  ['set maximum angular momentum to use in FMS']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure,spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['-1']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.lfms2"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.nleg
            help =  ['feff.nleg', 'Set maximum number of legs to use in path expansion. A Single scattering', 'path has 2 legs.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.nleg"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.criteria
            help =  ['feff.criteria', 'Cutoff criteria for the path expansion filtering.', 'critcw - tolerance for curved wave expansion', 'critpw - tolerance for initial plane wave approximation']
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.criteria"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.iorder
            help =  ['feff.iorder', 'Set order of approximation when calculating effective scattering matrices.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.iorder"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.pcriteria
            help =  ['feff.pcriteria', 'Set criteria for filtering in pathfinder. The keep-criterion pcritk looks at', 'the amplitude of chi (in the plane wave approximation) for the current path', 'and compares it to a single scattering path of the same effective length.', 'To set this value, consider the maximum degeneracy you expect and divide', 'your plane wave criterion by this number. For example, in fcc Cu, typical', 'degeneracies are 196 for paths with large r, and the minimum degeneracy is 6.', 'So a keep criterion of 0.08% is appropriate for a pw criteria of 2.5%. The', 'heap-criterion pcrith filters paths as the pathfinder puts all paths into a', 'heap (a partially ordered data structure), then removes them in order of', 'increasing total path length. Each path that is removed from the heap is', 'modified and then considered again as part of the search algorithm. The heap', 'filter is used to decide if a path has enough amplitude in it to be worth', 'further consideration. If a path can be eliminated at this point, entire', 'trees of derivative paths can be neglected, leading to enormous time savings.', 'This test does not come into play until paths with at least 4 legs are being', 'considered, so single scattering and triangular (2 and 3 legged) paths will', 'always pass this test. Because only a small part of a path is used for', 'this criterion, it is difficult to predict what appropriate values will be.']
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.pcriteria"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.sig2
            help =  ['feff.sig2', 'Set a single Debye-Waller factor for all paths, exp']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.sig2"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.xanes
            help =  ['feff.xanes', 'Calculate XANES spectrum.', 'xkmax - calculate up to k = xkmax']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.xanes"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.corrections
            help =  ['feff.corrections', 'Correct the Fermi cutoff and broadening in the final spectrum calculation.', 'vrcorr - Shift Fermi cutoff by -vrcorr.', 'vicorr - Add extra Lorenzian broadening with half width at half max of vicorr.']
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.corrections"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.afolp
            help =  ['feff.afolp', 'Set maximum overlap for automatic overlap search.', 'folpx - maximum overlap allowed.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'scf,potentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.afolp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.exafs
            help =  ['feff.exafs', 'Calculate EXAFS spectrum.', 'xkmax  - calculate spectrum up to k = xkmax', 'xkstep - calculate in steps of xkstep']
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'property,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.exafs"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.polarization
            help =  ['feff.polarization', 'Set polarization vector of x-rays in cartesian coordinates of input file.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.polarization"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.ellipticity
            help =  ['feff.ellipticity', 'Set the ellipticity of the x-rays.', 'This card is used with the feff.polarization.', 'elpty   - ratio of amplitudes of electric field in the two orthogonal', 'directions of elliptically polarized light. Only the absolute', 'value of the ratio is important for nonmagnetic materials. The', 'present code can distinguish left- and right-circular polarization', 'only with the feff.xmcd or feff.xncd. A zero value of the', 'ellipticity corresponds to linear polarization, and unity to', 'circular polarization. The default value is zero.', 'x, y, z - coordinates of any nonzero vector in the direction of the', 'incident beam. This vector should be approximately normal to the', 'polarization vector']
            kinds =  [
               [ inp_float, inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.ellipticity"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rgrid
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational,grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rgrid"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rphases
            help =  ['feff.rphases', 'Set real phase shift approximation.', 'UseRealPhases - use real phase shift if true.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rphases"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.nstar
            help =  ['feff.nstar', 'Write nstar.dat with effective coordination number N*.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.nstar"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.nohole
            help =  ['feffnohole', 'Do not use a hole in the calculation.', 'DEPRECATED - Use feff.corehole instead.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.nohole"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.sig3
            help =  ['feff.sig3', 'Set first and third cumulants for single scattering paths:', 'alphat - first cumulant', 'thetae - third cumulant']
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.sig3"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.jumprm
            help =  ['feff.jumprm', 'If true, smooth the jump between muffin tin potentials and interstitial.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'scf,potentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.jumprm"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.mbconv
            help =  ['Deprecated: Should not be used.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'DEPRECATED'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.mbconv"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.spin
            help =  ['feff.spin', 'Specify the type of spin-dependent calculation for spin along the (x, y, z)', 'direction, along the z-axis by default. The SPIN card is required for the', 'calculation of all spin-dependent effects, including XMCD and SPXAS.', 'ispin:', '2 spin-up SPXAS and LDOS', '-2 spin-down SPXAS and LDOS', '1 spin-up portion of XMCD calculations', '-1 spin-down portion of XMCD calculations']
            kinds =  [
               [ inp_int, inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.spin"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.edge
            help =  ['feff.edge', 'Set edge or edges to calculate for XAS, XES, EELS, RIXS and other related spectra.', \
                     'For RIXS, one can use the special option "val" to do valence to core RIXS.' ]
            kinds =  [
               [ inp_choice ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  [['K,L1,L2,L3,M1,M2,M3,M4,M5,N1,N2,N3,N4,N5,N6,N7,val']]
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.edge"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.scf
            help =  ['feff.scf', 'Use self-consistent field calculation of potentials.', 'rfms1 - radius of cluster to use for scf calculations.', 'lfms1 - 0 for solids, 1 for molecules', 'nscmt - maximum number of iterations in SCF calculation.', 'ca    - convergence factor for Broyden algorithm', 'nmix  - number of initial iterations of mixing algorithm to use.']
            kinds =  [
               [ inp_float, inp_int, inp_int, inp_float, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'scf,potentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.scf"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.fms
            help =  ['feff.fms', 'Use full multiple-scattering.', 'rfms   - radius of cluster to use for fms calculation.', 'lfms1  - 0 for solids, 1 for molecules', 'minv   - set algorithm for matrix inversion', '0: LU decomposition', '2: Lanczos', '3: Broyden (less reliable)', 'toler1 - tolerance to stop recursion and Broyden algorithm', 'toler2 - sets the matrix element of the Gt matrix to zero if its value is', 'less than toler2', 'rdirec - sets the matrix element of the Gt matrix to zero if the distance', 'between atoms is larger than rdirec']
            kinds =  [
               [ inp_float, inp_int, inp_int, inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.fms"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.ldos
            help =  ['feff.ldos', 'Run angular momentum project density of states calculations.', 'emin       - minimum energy of energy grid.', 'emax       - maximum energy of energy grid.', 'broadening - Lorenzian broadening to use in calculation.', 'npoints    - number of energy points in grid.']
            kinds =  [
               [ inp_float, inp_float, inp_float, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.ldos"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.interstitial
            help =  ['feff.interstitial', 'The construction of the interstitial potential and density may be changed by', 'using this card. inters = 1 might be useful when only the surroundings of the', "absorbing atom are specified in 'feff", 'interstitial potential.', 'inters=0: The interstitial potential is found by averaging over the', "entire extended cluster in 'feff", 'inters=1: the interstitial potential is found locally around the', 'absorbing atom.', 'vtot:     the volume per atom normalized by ratmin3', '(vtot=(volume per atom)/ratmin3), where ratmin is the shortest', 'bond for the absorbing atom. This quantity defines the total', 'volume (needed to calculate the interstitial density) of the', "extended cluster specified in 'feff", 'total volume is calculated as a sum of Norman sphere volumes.', 'Otherwise, total volume = nat * (vtot * ratmin3), where nat is', 'the number of atoms in an extended cluster.']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'scf,potentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.interstitial"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.cfaverage
            help =  ['Obsolete: Do not use.']
            kinds =  [
               [ inp_int, inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'DEPRECATED'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.cfaverage"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.s02
            help =  ['feff.s02', 'Set EXAFS amplitude reduction factor.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'ADVANCED'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.s02"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.xes
            help =  ['feff.xes', 'Calculate x-ray emission spectrum.', 'emin  - minimum energy of calculation.', 'emax  - maximum energy of calculation', 'estep - energy step of calculation']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.xes"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.danes
            help =  ['feff.danes', 'Calculate diffraction anomalous near edge structure.', 'xkmax  - calculate up to k = xkmax', 'xkstep - use steps of size xkstep', 'estep  - near the edge, use steps calculated from estep']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.danes"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.fprime
            help =  ['feff.fprime', 'emin  - minimum energy of calculation.', 'emax  - maximum energy of calculation', 'estep - energy step of calculation', "Calculate atomic scattering factor f'"]
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.fprime"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rsigma
            help =  ['feff.rsigma', 'If true use only real part of self-energy.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rsigma"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.xmcd
            help =  ['feff.xmcd', 'Caluclate x-ray magnetic (or natural) circular dichroism', 'xkmax  - calculate up to k = xkmax', 'xkstep - use steps of size xkstep', 'estep  - near the edge, use steps calculated from estep']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,magnetism,spin'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.xmcd"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.multipole
            help =  ['feff.multipole', 'Set multipole expansion approximation. Specifies which multipole transitions', 'to include in the calculations. The options are: only dipole (le2 = 0,', 'default), dipole and magnetic dipole (le2 = 1), dipole and quadrupole', '(le2 = 2). This cannot be used with NRIXS and is not supported with EXELFS', 'and ELNES. The additional field l2lp can be used to calculate individual', 'dipolar contributions coming from L -> L + 1 (l2lp = 1) and from L -> L - 1', '(l2lp = -1). Notice that in polarization dependent data there is also a', 'cross term, which is calculated only when l2lp = 0']
            kinds =  [
               [ inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.multipole"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.unfreezef
            help =  ['feff.unreezef', 'If true, allow f-orbitals to relax during SCF calculation.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'scf,potentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.unfreezef"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.tdlda
            help =  ['feff.tdlda', 'Use TDLDA to calculate x-ray absorption spectrum.', 'ifxc - set algorithm for tdlda approximation', '0: use static approximation for screening of the x-ray field', '1: use approximate dynamic screening of x-ray field and core-hole.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.tdlda"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.pmbse
            help =  []
            kinds =  [
               [ inp_int, inp_int, inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.pmbse"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.mpse
            help =  ['feff.mpse', 'Use many-pole model self-energy. This requires the loss function, which can', 'be provided externally, or approximated using feff.opcons.', 'ipl - Set method for self-energy inclusion:', '1: use an "average" self-energy which is applied to the whole', 'system (default).', '2: use a density dependendent self-energy which is', 'different at every point inside the muffin-tin radius.']
            kinds =  [
               [ inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.mpse"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.sfconv
            help =  ['feff.sfconv', 'If true, convolve spectrum with spectral function to account for', 'multi-electron excitations.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.sfconv"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.self
            help =  ['feff.self', 'Print out quasiparticle self-energy calculated during spectral-function', 'convolution calculations.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.self"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.sfse
            help =  ['feff.sfse', 'Print out off shell self-energy Sigma(k,E) calculated during', 'spectral-function convolution calculations.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.sfse"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rconv
            help =  ['Advanced: Print running convolution with the spectral function.']
            kinds =  [
               [ inp_float, inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rconv"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.elnes
            help =  ['This card is not implements yet.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.elnes"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.exelfs
            help =  ['This card is not implemented yet.']
            kinds =  [
               [ inp_float ],
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.exelfs"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.magic
            help =  ['This card is not implemented yet.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.magic"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.absolute
            help =  ['feff.absolue', 'Print spectrum in absolute units instead of normalizing.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.absolute"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.symmetry
            help =  ['feff.symmetry', 'If false, turn off symmetry considerations in path expansion.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,exafs'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.symmetry"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.real
            help =  ['Advanced: Use real phase shifts.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure,method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.real"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.reciprocal
            help =  ['Work in reciprocal space (k-space calculation).']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure,method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.reciprocal"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.sgroup
            help =  ['Specify space group by number (1 - 230).']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.sgroup"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.lattice
            help =  ['This card specifies the lattice. First, its type must be specified using a single letter : P for', 'primitive, F for face centered cubic, I for body centered cubic, H for hexagonal. The following', 'three lines give the three basis vectors in Carthesian Angstrom coordinates. They are multiplied', 'by scale (e.g., 0.529177 to convert from bohr to Angstrom).', 'feff.lattice', 'ax ay az', 'bx by bz', 'cx cy cz']
            kinds =  [
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.lattice"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.kmesh
            help =  ['Specify the kmesh.', 'feff.kmesh nkp(x) [nkpy nkpz [ktype [usesym] ] ]', 'This card specifies the mesh of k-vectors used to sample the full Brillouin Zone for the evaluation', 'of Brillouin Zone integrals. Nkp is the number of points used in the full zone. It can be specified', 'either as ”nkpx nkpy nkpz”, ”nkp”, or ”nkp 0 0”. If usesym = 1, the zone is reduced to its', 'irreducible wedge using the symmetry options specified in file symfile, which must be present', 'in the working directory. The k-mesh is constructed using the tetrahedron method of Bloechl', 'et al., Phys. Rev. B, 1990. The parameter ktype is meant for time-saving only and means:', 'ktype=1 : regular mesh of nkp points for all modules', 'ktype=2 : use nkp points for ldos/fms and nkp/5 points for pot (significant time savings)', 'ktype=3 : use nkp points for ldos/fms and nkp/5 points for pot (near edge) ; reduce nkp', 'for all modules as we get away from near-edge (somewhat experimental)', '* use a k-mesh of 1000 points in the full BZ.', 'feff.kmesh', '* use a k-mesh of 10x5x3 points for a large, irregular cell.', 'feff.kmesh', '* use a k-mesh of 1000 points and try to save time:', 'feff.kmesh']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.kmesh"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.strfac
            help =  ['feff.strfac', 'This card gives three non-physical internal parameters for the calculation of the KKR structure', 'factors : the Ewald parameter and a multiplicative cutoff factor for sums over reciprocal (gmax)', 'and real space (rmax) sums. Multiplicative means the code makes a ’smart’ guess of a cutoff', 'radius, but if one suspects something fishy is going on, one can here e.g. use gmax=2 to multiply', 'this guess by 2. Eta is an absolute number. Given the stability of the Ewald algorithm, it', 'shouldn’t be necessary to use this card. Its use is not recommended. Only active in combination', 'with the feff.reciprocal card.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.strfac"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.corehole
            help =  ['feff.corehole', 'Set method for calculating corehole interaction.', 'CoreHoleApproximation -', 'None: Do not use a corehole.', 'FSR : Final-state rule', 'RPA : Use RPA dielectric function to calculate', 'screening of core-hole.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.corehole"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.target
            help =  ['feff.target', 'Specifies the location of the absorber atom for reciprocal space calculations. It is entry ic of the', 'feff.ATOMS card if an feff.ATOMS card and feff.LATTICE card are used. In conjunction with the cif_input', 'card it is entry ic the list of atoms as given in the ‘.cif’ file (i.e., a list of the crystallographically', 'inequivalent atom positions in the unit cell). The target needs to be specified also for NOHOLE', 'calculations. Note that this cannot be specified in the feff.POTENTIALS list because periodic', 'boundary conditions would then produce an infinite number of core holes.', '* calculate a spectrum for the second atom in the feff.ATOMS list or CIF file.', 'feff.TARGET']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.target"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.egrid
            help =  ['This card can be used to customize the energy grid. The EGRID card is followed by lines', 'specifying the type of grid, minimum and maximum values for the grid, and the grid step, i.e.', '', 'grid_type grid_min grid_max grid_step', '', 'The grid type parameter is a string that can take the values e_grid, k_grid, or exp_grid. When', 'using the e_grid or k_grid grid types, grid_min, grid_max, and grid_step are given in eV or Å −1', 'respectively. For the exp_grid type, grid_min and grid_max are the minimum and maximum', 'grid values in eV, and grid_step is the exponential, i.e.', '', 'E_i = E_Min + (E_max-E_Min)*[exp(grid_step ∗ i) − 1.0].', '', 'A fourth grid type user grid is also available for feff. user grid is followed by an arbitrary', 'number of lines, each specifying an energy point in eV , i.e.,', 'user_grid', '0.1', '1.5', '3.45', '6.0', '.', '.', '.']
            kinds =  [
               [ inp_str, inp_str, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.egrid"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.coordinates
            help =  ['feff.coordinates', 'i must be an integer from 1 through 6. It specifies the units of the atoms of the unit cell given', 'in the ATOMS card for reciprocal space calculations. If the card is omitted, the default value', 'icoord = 3 is assumed. FIX check this', '1. Cartesian coordinates, Angstrom units. Like feff - you can copy from a real-space', 'feff', '2. Cartesian coordinates, fractional units (i.e., fractions of the lattice vectors ; should be', 'numbers between 0 and 1). Similar to feff.', '3. Cartesian coordinates, units are fractional with respect to FIRST lattice vector. Like', 'SPRKKR. (default)', '4. Given in lattice coordinates, in fractional units. Like WIEN2k (but beware of some', '‘funny’ lattice types, e.g. rhombohedral, in WIEN2k case.struct if you’re copy-pasting )', '5. Given in lattice coordinates, units are fractional with respect to FIRST lattice vector.', '6. Given in lattice coordinates, Angstrom units.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.coordinates"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.extpot
            help =  ['Not currently workding. Do not use.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'scf,potentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.extpot"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.chbroad
            help =  ['feff.chbroad', 'Set method of calculating core-hole lifetime broadening.', 'ichbroad -', "0: Calculate Green's function at energy with imaginary part equal", 'to Gamma_CH/2.', '1: Convolve final spectrum with Lorenzian of full width at', 'half-max Gamma_ch.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.chbroad"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.chsh
            help =  ['feff.chsh', 'Correct chemical shift.', 'ich = 0 or 1.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.chsh"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.dims
            help =  ['feff.dims', 'Set maximum dimensions for fms calculations.', 'nmax - maximum number of atoms in fms matrix.', 'lmax - maximum angular momentum of fms matrix.']
            kinds =  [
               [ inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.dims"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.nrixs
            help =  []
            kinds =  [
               [ inp_int ],
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.nrixs"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.ljmax
            help =  ['For use in calculations of NRIXS. Not implemented yet.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.ljmax"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.ldec
            help =  ['For use in calculations of NRIXS. Not implemented yet.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.ldec"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.setedge
            help =  ['feff.setedge', 'Use table of experimental edge energies.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.setedge"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.eps0
            help =  ['feff.eps0', 'Set dielectric constant used for many-pole self-energy calculations.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.eps0"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  opcons.usesaved
            help =  ['feff.opcons', 'Calculate loss function using an atomic approximation.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'opcons'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["opcons.usesaved"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.opcons
            help =  ['Calculate the dielectric function of the material within the', 'atomic approximation. Very fast. Used to calculate loss.dat for', 'use with feff.mpse self-energy calculations.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.opcons"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.numdens
            help =  []
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.numdens"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.preps
            help =  ['feff.preps', 'Print dielectric function as calculated by feff.opcons.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.preps"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.egapse
            help =  ['feff.egapse', 'Use this gap energy when applying the many-pole self-energy.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.egapse"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.chwidth
            help =  ['feff.chwidth', "Set core-hole width instead of using FEFF's internal table of widths."]
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.chwidth"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.restart
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.restart"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.config
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'potentials,structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.config"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.screen
            help =  ['The screen module, which calculates the RPA core hole potential, is a ’silent’ module: it has', 'no obvious input but instead runs entirely on default values. Using the feff.SCREEN card you', 'can change these default values. They will be written to an optional ‘screen', 'you can also edit manually). The feff.SCREEN card can occur more than once in ‘feff', 'entries will be applied to the calculation. parameter must be one of : ner (40), nei (20), maxl', '(4), irrh (1), iend (0), lfxc (0), emin (-40 eV), emax (0 eV), eimax (2 eV), ermin (0.001 eV),', 'rfms (4.0), nrptx0 (251). For most calculations the default values given (between brackets) are', 'fine. Occasionally we’ve changed rfms, maxl, or emin. Note that the screen is only active with', 'feff.COREHOLE', '* Set the cluster radius for the RPA potential calculation higher than the default of 4.0', 'feff.COREHOLE', 'feff.SCREEN']
            kinds =  [
               [ inp_str, inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["feff.screen"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.cif
            help =  ['Specify a cif input file. Dangerous. Use cif_input instead.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.cif"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.equivalence
            help =  ['feff.equivalence', 'This optional card is only active in combination with the CIF card. It tells feff how to', 'generate potential types from the list of atom positions in the ‘cif’ file.', 'If ieq = 1, the crystallographic equivalence as expressed in the ‘cif’ file is respected; that', 'is, every separate line containing a generating atom position will lead to a separate potential', 'type. This means that, e.g., in HOPG graphite, the two generating positions will give rise to', 'two independent C potentials. This is also the default behavior if the EQUIVALENCE card is', 'not specified.', 'If ieq = 2, unique potentials are assigned based on atomic number Z only. That is, all', 'C atoms will share a C potential and so on. This is how most feff calculations are run.', 'Whether it is sensible or not to do this depends on the system and on the property one wishes', 'to calculate. Keep in mind that feff is a muffin tin code, and may therefore be indifferent', 'to certain differences between crystallographically inequivalent sites. On the other hand, if', 'an element occurs in the crystal with different oxidation states, it may be necessary to assign', 'separate potentials to these different types in order to describe the crystal properly and get', 'accurate spectra.', 'If ieq = 3, unique potentials are assigned based on atomic number Z and the first shell.', 'This can be useful e.g. to treat larger systems with crystal defects, where only first neighbors', 'of the defect need to be treated differently from all more distant atoms of a certain Z. (To be', 'implemented.)', 'If ieq = 4, a hybrid of methods 1 and 2 is used. That is, if the number of unique crystallo-', 'graphic positions does not exceed a hard-coded limit (nphx=9 in the current version), they are', 'treated with the correct crystallographic equivalence. If the number of unique crystallographi-', 'cally inequivalent sites is larger, they get combined by atomic number Z. This ad hoc approach', 'is a practical way of simply limiting the number of unique potentials. This makes sense be-', 'cause, first of all, there are certain hardcoded limits that would require recompilation of the', 'code, requiring more RAM memory and more work than a user may want to do.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'potentials,scf'
            field_labels = None
            ranges =  None
            defaults =  [['1']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.equivalence"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.compton
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_float, inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.compton"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rhozzp
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rhozzp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.cgrid
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_float, inp_int, inp_int, inp_int, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.cgrid"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.corval
            help =  ['feff.corval', 'The core-valence separation energy is found by scanning the DOS within an energy window.', 'The emin parameter sets the lower bound (in eV) of this energy window. It is 70 eV by', 'default. For some materials it is necessary to lower this bound, e.g. to 100 eV. For example,', 'when SCF convergence is elusive because occupation numbers for one or more l-values are', 'changing drastically between SCF iterations due to states moving above and below a poor', 'estimate of the core-valence separation energy. We plan to replace the current mechanism by a', 'more robust and automated algorithm, but in the meantime users can use the CORVAL card', 'to handle some of these difficult cases.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'potentials,scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.corval"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.siggk
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'phonons,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.siggk"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.temperature
            help =  ['feff.temperature', 'The TEMP card sets the electronic temperature and the exchange-correlation potential. etemp', '= 0 (default). etemp is in eV. There are 4 different options for the exchange-correlation', 'potential.', 'iscfxc', 'No temperature dependent exchange correlations', '11 von-Barth Hedin 1971 (default)', '12 Perdew-Zunger', 'Explicitly temperature dependent exchange correlations', '21 Perrot Dharma-Wardana 1984', '22 KSDT (recommended)']
            kinds =  [
               [ inp_float, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'temperature,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.temperature"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.density
            help =  ['Not implemented yet.']
            kinds =  [
               [ inp_str, inp_str, inp_str ],
               [ inp_float, inp_float, inp_float ],
               [ inp_int, inp_int, inp_int ],
               [ inp_float, inp_float, inp_float ],
               [ inp_float, inp_float, inp_float ],
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'electronic structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.density"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rixs
            help =  ['feff.RIXS', 'The RIXS card sets the parameters for the RIXS calculation. It must be used with a workflow', 'or script to produce RIXS.', 'gam_Ei', 'Broadening to use in the incident energy direction.', '', 'gam_El', 'Broadening to use in the energy loss direction.', '', 'xmu', 'Fermi energy to use for the RIXS calculation, if not present, the fermi level calculated in', 'the SCF step will be used.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'spectrum,property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rixs"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.rlprint
            help =  ['Advanced used in RIXS calculations, but automated by corvus. Prints real scattering wavefunction R_l.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.rlprint"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.hubbard
            help =  ['Not currently working.']
            kinds =  [
               [ inp_float, inp_float, inp_float, inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.hubbard"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.crpa
            help =  ['Not currently working.']
            kinds =  [
               [ inp_int, inp_float ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.crpa"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  feff.scxc
            help =  []
            kinds =  [
               [ inp_int ],
               ]
            code =  'feff'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["feff.scxc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.expert
            help =  ['Use verbatim expert setting for orca.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'general'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["orca.expert"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.convergencestrategy
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  [['NormalConv']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.convergencestrategy"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.cpcm
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.cpcm"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.method
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['B3LYP']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.method"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.runtype
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['OPT']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.runtype"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.amass
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['Mass2016']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.amass"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.usesymm
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.usesymm"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.frozencore
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.frozencore"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.allowrhf
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.allowrhf"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.ri
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.ri"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.grid
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method,grids'
            field_labels = None
            ranges =  None
            defaults =  [['GRID4']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.grid"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.method.gridx
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method,grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.method.gridx"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.hftyp
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  [['RHF']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.hftyp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.fracocc
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.fracocc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.smeartemp
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.smeartemp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.keepints
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.keepints"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.keepdens
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.keepdens"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.readints
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.readints"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.usecheapints
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.usecheapints"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.valformat
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.valformat"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.kmatrix
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.kmatrix"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.jmatrix
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.jmatrix"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.scfmode
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.scfmode"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.maxiter
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.maxiter"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.guess
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.guess"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.autostart
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  [['True']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.autostart"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.convergence
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  [['NORMALSCF']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.convergence"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.diis
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.diis"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.kdiis
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.kdiis"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.nr
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.nr"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.soscf
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.soscf"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.cnvdamp
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.cnvdamp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.cnvshift
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.cnvshift"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.scf.uno
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.scf.uno"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.basis.basis
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  [['def2-TZVP']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.basis.basis"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.basis.decontract
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.basis.decontract"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.mp2
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.mp2"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.mp2type
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['MP2']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.mp2type"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.ci
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.ci"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.citype
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['CCSD']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.citype"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.tole
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.tole"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.tolrmsg
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.tolrmsg"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.tolmaxg
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.tolmaxg"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.tolrmsd
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.tolrmsd"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.tolrmaxd
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.tolrmaxd"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.geom.optimizationquality
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'optimization'
            field_labels = None
            ranges =  None
            defaults =  [['TIGHTOPT']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.geom.optimizationquality"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.coords.units
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.coords.units"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.rel.method
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.rel.method"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.rel.soctype
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.rel.soctype"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.output.printlevel
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.output.printlevel"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.output.print
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.output.print"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.output.xyzfile
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.output.xyzfile"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  orca.output.pdbfile
            help =  []
            kinds =  [
               [ inp_bool ],
               ]
            code =  'orca'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["orca.output.pdbfile"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.MPI.CMD
            help =  []
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.MPI.CMD"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.PAO.EnergyShift
            help =  ['Specify energy shift to control basis cutoff radii.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.PAO.EnergyShift"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.TD.ShapeOfEfield
            help =  ['Specify the shape of the field for the RT-TDDFT run.', 'Options are:', 'step     - Turn off dipole field at time 0.', 'halfstep - Dipole field changes from full strength to 1/2', 'strength at time 0.', 'delta    - Dipole field with time dependence delta(t).', 'const    - Turn on dipole field at time 0.', 'sine     - Dipole field with damped sine wave time dependence,', 'with optional Gaussian envelope to create quasi-harmonic', 'wave packet.', 'core     - turn on core-hole potential at time 0.', 'core2    - GS with full core-hole. Excited states from linear response after.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.TD.ShapeOfEfield"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.TD.CoreExcitedAtom
            help =  ['Set which atom will be the absorbing atom, i.e., which atoms the', 'core-hole will be centered on']
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.TD.CoreExcitedAtom"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.TD.CorePerturbationCharge
            help =  ['Set the core-hole charge.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.TD.CorePerturbationCharge"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.TD.mxPC
            help =  ['Maximum number of points to use for predictor-corrector algorith.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  [['2']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.TD.mxPC"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Diag.DivideAndConquer
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.Diag.DivideAndConquer"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.LongOutput
            help =  ['Output lots of info.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'output'
            field_labels = None
            ranges =  None
            defaults =  [['True']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.LongOutput"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.MeshCutoff
            help =  ['Energy that defines the real-space grid. Point spacing scales as 1/sqrt(E_c).']
            kinds =  [
               [ inp_float, inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'grids'
            field_labels = None
            ranges =  None
            defaults =  [['120.0', 'Ry']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.MeshCutoff"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.XC.functional
            help =  ['Set flavor of exchange-correlation functional, i.e., LDA or GGA.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['GGA']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.XC.functional"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.XC.authors
            help =  ['Set authors of exchange correlation functional.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  [['PBE']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.XC.authors"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.LatticeConstant
            help =  ['Set an overall multiplicative constant for the lattice parameters.']
            kinds =  [
               [ inp_float, inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.LatticeConstant"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Block.PAO.Basis
            help =  ['Set siesta basis manually']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["siesta.Block.PAO.Basis"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Block.LatticeParameters
            help =  ['Set lattice parameters, i.e.,', 'a b c alpha beta gamma']
            kinds =  [
               [ inp_float, inp_float, inp_float, inp_float, inp_float, inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.Block.LatticeParameters"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.MaxSCFIterations
            help =  ['Max number of SCF iterations allowed.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  [['100']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.MaxSCFIterations"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.UseSaveData
            help =  ['Use saved data to start siesta calculation']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  [['False']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.UseSaveData"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.DM.InitSpin.AF
            help =  ['Set magnetic behavior of system to antiferromagnetic if true.', 'Default is false and will be set up as ferromagnetic.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.DM.InitSpin.AF"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.SpinPolarized
            help =  ['Include spin in calculation.', 'Value should be yes or no.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.SpinPolarized"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.DM.NumberBroyden
            help =  []
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.DM.NumberBroyden"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.DM.NumberPulay
            help =  ['Set number of Pulay steps']
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.DM.NumberPulay"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.DM.MixingWeight
            help =  ['Mixing weight for the density matrix.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  [['0.10']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.DM.MixingWeight"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.DM.Tolerance
            help =  ['Convergence tolerance for elements of the density matrix']
            kinds =  [
               [ inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  [['1.0e-4']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.DM.Tolerance"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.SolutionMethod
            help =  ['Method for solving the eigenvalue problem.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  [['diagon']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.SolutionMethod"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.PAO.BasisType
            help =  ['Define basis type', 'split: Split-valence scheme for multiple-zeta. The split is based on different radii.', 'splitgauss: Same as split but using Gaussian functions.', 'nodes: Generalized PAO’s.', 'nonodes: The original PAO’s are used, multiple-zeta is generated by changing the', 'scale-factors, instead of using the excited orbitals.', 'filteret: Use the filterets as a systematic basis set. The size of the basis set is', 'controlled by the filter cut-off for the orbitals.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  [['split']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.PAO.BasisType"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.PAO.BasisSize
            help =  ['Define basis size. Can be SZ, DZ, SZP, DZP.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  [['DZP']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.PAO.BasisSize"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.ElectronicTemperature
            help =  ['Set electronic teperature used to define occupation numbers during SCF.']
            kinds =  [
               [ inp_float, inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'temperature'
            field_labels = None
            ranges =  None
            defaults =  [['1.0', 'K']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.ElectronicTemperature"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.NumberOfAtoms
            help =  ['Indicate number of atoms in unit cell.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.NumberOfAtoms"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.NumberOfSpecies
            help =  ['Indicate number of species in unit cell.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.NumberOfSpecies"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Block.ChemicalSpeciesLabel
            help =  ['Indicate the different chemical species in the unit cell.', 'Format:', 'SpeciesIndex1 AtomicNumber1 AtomicSymbol1', 'SpeciesIndex2 AtomicNumber2 AtomicSymbol2', '...']
            kinds =  [
               [ inp_int, inp_int, inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.Block.ChemicalSpeciesLabel"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.AtomicCoordinatesFormat
            help =  ['Specify units and format of atomic coordinates.', 'Borh            - cartesian in Bohr.', 'Ang             - cartesian in Angstrom.', 'ScaledCartesian - cartesian scaled by lattice constant.', 'Fractional      - coordinates are given in units of the lattice vectors.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  [['Fractional']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.AtomicCoordinatesFormat"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Block.AtomicCoordinatesAndAtomicSpecies
            help =  ['Specify coordinates of each atom as well as the species index.', 'x1 y1 z1 SpeciesIndex1', 'x2 y2 z2 SpeciesIndex2', '...']
            kinds =  [
               [ inp_float, inp_float, inp_float, inp_int ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["siesta.Block.AtomicCoordinatesAndAtomicSpecies"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Coreresponse.Broadening
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['0.5']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.Coreresponse.Broadening"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.Beta.Broadening
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['0.1']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["siesta.Beta.Broadening"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  siesta.expert
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'siesta'
            importance =  'IMPORTANCE'
            category =  'general'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["siesta.expert"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  phsf.numtimepoints
            help =  []
            kinds =  [
               [ inp_int ],
               ]
            code =  'phsf'
            importance =  'IMPORTANCE'
            category =  'spectrum,grids'
            field_labels = None
            ranges =  None
            defaults =  [['40000']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["phsf.numtimepoints"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  phsf.broadening
            help =  []
            kinds =  [
               [ inp_float ],
               ]
            code =  'phsf'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['0.5']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["phsf.broadening"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  phsf.ekeqp
            help =  []
            kinds =  [
               [ inp_float, inp_float ],
               ]
            code =  'phsf'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['0.0', '0.0']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["phsf.ekeqp"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif2cell.cif_input
            help =  ['Crystallographic information file to use.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'cif2cell'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif2cell.cif_input"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif2cell.program
            help =  ['Program for cif2cell to write input for.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'cif2cell'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif2cell.program"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif2cell.outfile
            help =  ['Write output to outfile']
            kinds =  [
               [ inp_str ],
               ]
            code =  'cif2cell'
            importance =  'IMPORTANCE'
            category =  'structure,output'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif2cell.outfile"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif2cell.supercell
            help =  []
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'cif2cell'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif2cell.supercell"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif2cell.cartesian
            help =  ['make output in cartesian form']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'cif2cell'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif2cell.cartesian"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cif2cell.atomicunits
            help =  ['print coordinates in bohr rather than angstroms']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'cif2cell'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["cif2cell.atomicunits"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  cfavg_target
            help =  []
            kinds =  [
               [ inp_choice ],
               ]
            code =  'general'
            importance =  'IMPORTANCE'
            category =  'property'
            field_labels = None
            ranges =  [['xanes,xes,rixs']]
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  {'xanes': ['structure', 'absorbing_atom_type', 'feff.edge'], 'xes': ['structure', 'absorbing_atom_type', 'feff.edge'], 'rixs': ['structure', 'absorbing_atom_type', 'feff.edge']}

            self.inp_def_dict["cfavg_target"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  fit.target
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'fit'
            importance =  'IMPORTANCE'
            category =  'property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["fit.target"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  fit.parameters
            help =  []
            kinds =  [
               [ inp_str, inp_float ],
               ]
            code =  'fit'
            importance =  'IMPORTANCE'
            category =  'fitting'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["fit.parameters"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  fit.datafile
            help =  []
            kinds =  [
               [ inp_str ],
               ]
            code =  'fit'
            importance =  'IMPORTANCE'
            category =  'fitting'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["fit.datafile"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  fit.bond
            help =  []
            kinds =  [
               [ inp_int ],
               ]
            code =  'fit'
            importance =  'IMPORTANCE'
            category =  'fitting'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  True
            req =  None

            self.inp_def_dict["fit.bond"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.photon.operator
            help =  ['Select the operator to be used to calculate the (diple or quad)']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  [['dipole']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.photon.operator"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.photon.polarization
            help =  ['Direction of polarization for XANES or XES calculations']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.photon.polarization"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.photon.qhat
            help =  ['Direction of q-vector for quadrupole or NRIXS calculations']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.photon.qhat"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.photon.energy
            help =  ['Set energy of x-rays at edge']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.photon.energy"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.para_prefix
            help =  ['Set the command to use for parallel runs, i.e., mpirun, mpiexec etc,', 'along with any flags to use.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.para_prefix"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.ser_prefix
            help =  ['prefix for serial parts of the code, for example, cut3d should be run', 'with only 1 processor, i.e., mpirun -n 1']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.ser_prefix"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.dft
            help =  ['Which DFT code to use: qe - QuantumEspresso, abi - ABINIT']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'dft,method'
            field_labels = None
            ranges =  None
            defaults =  [['abi']]
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.dft"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.scratch
            help =  ['Where to write scratch files']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.scratch"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.acell
            help =  ['Scaling in Bohr for the primitive vectors of the unit cell']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.acell"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.rprim
            help =  ['Primitive vectors of unit cell']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               [ inp_float, inp_float, inp_float ],
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.rprim"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.ntypat
            help =  ['Number of different types (usually species) of atom in the unit cell.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.ntypat"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.znucl
            help =  ['List of length ntypat with atomic numbers of each type of atom in the unit cell']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.znucl"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.natom
            help =  ['Number of atoms in the unit cell']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.natom"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.typat
            help =  ['Type of each atom in the unit cell denoted by the integer index corresponding', 'to the ocean.znucl list of atomic numbers. This list must be in the same', 'as the coordinates listed in ocean.xred']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.typat"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.xred
            help =  ['Reduced coordinats of atoms in the unit cell.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["ocean.xred"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.diemac
            help =  ['Macroscopic dielectric matrix.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.diemac"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.nspin
            help =  ['Choose paramagnetic (nspin = 1), or spin dependent (nspin = 2).']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.nspin"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.smag
            help =  ['Controls initial magnetism for the DFT calculations.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["ocean.smag"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.smag.ixc
            help =  ["Used for abinit runs in smag card. Don't know the meaning at the moment.", 'This should be combiened with ocean.smag to write the card to the ocean', 'input.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spin,magnetism'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.smag.ixc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.ldau
            help =  ['Controls the U parameters for the DFT run. Only works with QuantumEspresso', 'currently. Not sure what the parameters are, but I believe they are', 'logical flag to run/not run LDA+U, U for each atom that has spin', 'associated with smag.']
            kinds =  [
               [ inp_bool ],
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["ocean.ldau"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.zymb
            help =  ['For use with QE. Each element listed in ocean.znucle can have a symbol', 'associated with it.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'structure'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.zymb"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.pp_list
            help =  ['Names of the pseudopotential files to be used listed in the same order as', 'ocean.znucl']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'method,pseudopotentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["ocean.pp_list"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.ecut
            help =  ['Plane wave basis truncation energy in Rydberg']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.ecut"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.nkpt
            help =  ['Number of k-points in each direction used to sample the', 'cell for the calculation of the', 'final states.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.nkpt"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.ngkpt
            help =  ['Number of k-points in each direction used to sample the cell for', 'the ground-state calculation of the density.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.ngkpt"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.nbands
            help =  ['Number of bands for the final state calculations. This includes valence and conduction bands.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.nbands"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.screen.nbands
            help =  ['Number of bands to use for the screening calculations. This requires a large', 'number of bands. Should be about 100eV above the Fermi level, but convergence', 'should be checked.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal,spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.screen.nbands"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.occopt
            help =  ['Controls determination of occupation. Most important', 'values are:', '1 - States are all doubly degenerate and either occupied or empty depending on band.', '3 - States are all doubly degenerate but can have fractional occupations', 'depending on Fermi function. Suitable for metals.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.occopt"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.fband
            help =  ['Determines the number of occupied bands to be included in the SCF calculation', 'of the density. For insulators the default (fband = 0.125) is fine, but', 'for metals the highest band the in the density calculation should have no', 'occupation weight. Using fband, the number of bands is determined by', 'n = natom*fband.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.fband"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.toldfe
            help =  ['Total energy convergence parameter for the density run. Default is 10^(-6)']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.toldfe"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.tolwfr
            help =  ['Convergence criterium for the non-scf wave-function calculations.', 'Default is 10^(-16)']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.tolwfr"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.nstep
            help =  ['Maximum number of iterations for the DFT SCF calculations. Default is 50']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'scf,convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.nstep"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.screen.nkpt
            help =  ['Number of k-point to be used for the screening calculations. Default is 2 2 2,', 'and is sufficient for a wide variety of systems, although very small unit', 'cells might require more, and large unit cells may only require gamma point.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.screen.nkpt"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.abpad
            help =  ['For the calculation of the final state wavefunctions, the convergence of the', 'highest bands can be very slow. The calculation can be sped up by adding some', 'throwaway bands at teh top. These bands are not considered when checking for convergence. ocean.abpad adds bands to the calculation. Only used for abinit.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.abpad"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.dft_energy_range
            help =  ['Instead of setting the number of bands (ocean.nbands) the user may request', 'an energy range in eV for the final state wave-functions. This is an estimate', 'using the volume of the unit cell and may be unreliable. Default is 25 eV.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.dft_energy_range"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.screen_energy_range
            help =  ['Instead of setting number of bands for the screening, the user may request', 'an energy range in eV. This is only an estimate, and may need to be converged.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.screen_energy_range"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.k0
            help =  ['DFT states are calculated using a shifted k-point grid. The first k-point is', 'given by:', '1/(N_k(1)*k0(1)), 1/(N_k(2)*k0(2), 1/(N_k(3)*k0(3)', 'where N_k is given by ocean.nkpt. The default shift is k0 = 1/8, 2/8, 3/8.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'basis,reciprocal,grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.k0"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.degauss
            help =  ['Broadening for the smearing function in Ryd. for metallic occupations in the', 'DFT calculations.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'scf'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.degauss"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.opf.program
            help =  ['Use oncvpsp UPS pseudopotentials with qe']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'pseudopotentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.opf.program"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.opf.fill
            help =  ['atomic number followed by the name of the .fill file to use for this calculation.']
            kinds =  [
               [ inp_int, inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'pseudopotentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.opf.fill"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.opf.opts
            help =  ['atomic number followed by the name of the .opts file to use for this calculation.']
            kinds =  [
               [ inp_int, inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'pseudopotentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.opf.opts"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.edges
            help =  ['Specify the atoms and edges to calculate. Each edge entry consists of 3', 'integers. The first, if greater than zero, is the index of the atom for', 'which the edge should be calculated. The second and third numbers are the', 'principle quantum number and angular momentum.', "'1 2 1' denotes the L edges of the first atom", 'If the first number is negative, then it is interpreted as -Z, where', 'Z is the atomic number, and in that case edges of all atoms with that', 'atomic number will be calculated.', "'-22 2 1' will run the L edges of every titanium atom in the cell."]
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  True
            req =  None

            self.inp_def_dict["ocean.edges"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.screen.shells
            help =  ['The screening calculation is RPA at small radius and a model at large radius.', 'Teh cross-over between the RPA and model is set by shells in Bohr.', 'Several different radii can be chosen to look at the convergence.', 'Convergence is usually reached at arount 3-4 Bohr. The supercell defined by', 'ocean.paw.nkpt must have dimensions larger than the radius specified by', 'ocean.screen.shells or results may be unreliable. The default of 3.5 Bohr is', 'usually OK. Values > 6 Bohr should not be used.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'screening'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.screen.shells"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.rad
            help =  ['One of the screening radius as defined by ocean.screen.shells that will be', 'used in the BSE calculation.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.rad"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.scfac
            help =  ['The is the Slater integral factor to scale the slater integrals. For 3d', 'transition metals 0.8 is a reasonable value, while 0.6 is better for', 'f-electron atoms.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.scfac"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.core_offset
            help =  ['If true, core-level shift will be calculated, false, no shift, or a number', 'to specify the shift by hand.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.core_offset"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.opf.hfkgrid
            help =  ['The first parameter sets the grid for hfk.x, and should be left at 2000.', 'The second determines the maximum number of proejectors per angular momentum', 'channel. The default of 20 will work for many calculations.']
            kinds =  [
               [ inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'grids,pseudopotentials'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.opf.hfkgrid"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.xmesh
            help =  ['Wave-functions are converted into the NIST BSE format and condensed onto a', 'grid of size ocean.cnbse.xmesh. Default is guessed in the code.']
            kinds =  [
               [ inp_int, inp_int, inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.xmesh"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.mode
            help =  ['Which spectroscopy to calculate: "XAS", "XES"', 'NRIXS and XRS are treated the same as XAS.']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'property'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.mode"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.niter
            help =  ['Number of Haydock iterations. Default is 100.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum,computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.niter"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.metal
            help =  ['If True, the code will complain unless occopt is 3. If False, the codes', 'expects occopt = 1.']
            kinds =  [
               [ inp_bool ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'system properties'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.metal"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.spin-orbit
            help =  ['If ocean.spin-orbit >= 0, the code will not automatically calculate the', 'spin-orbit splitting.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.spin-orbit"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.photon_q
            help =  ['For UV/VIS and RIXS calculations, the valence and conduction band states', 'must be offset from each other (by the momentum that is absorbed or', 'transferred). This sets that momentum offset in units of the reciprocal', 'lattice vectors of the system. Default is 0 0 0.']
            kinds =  [
               [ inp_float, inp_float, inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.photon_q"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.strength
            help =  ['Sets the strength for the two interaction terms in the BSE Hamiltonian.', 'Default is 1, and for emission 0. This can be changed for analysis.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum,method'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.strength"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.solver
            help =  ['Choose between Haydock algorithm (full spectrum, no excitons) or GMRES', '(single energy, exciton density).']
            kinds =  [
               [ inp_str ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.solver"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.gmres.elist
            help =  ['List of energies at which to run the GMRES algorithm in eV. Lowest', 'unoccupied state is set at zero without the core-hole.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational, grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  True
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.gmres.elist"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.gmres.erange
            help =  ['Use energies at with even spacing specified by', 'emin emax estep']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum,grids'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.gmres.erange"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.gmres.nloop
            help =  ['Restart GMRES algorithm will restart if the subspace grows to size nloop.']
            kinds =  [
               [ inp_int ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'computational'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.gmres.nloop"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.gmres.gprc
            help =  ['Set Lorenzian broadening in Hartree in the GMRES algorithm when', 'pre-conditioning. Default is 0.5, which should be reasonable for K edges.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.gmres.gprc"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.gmres.ffff
            help =  ['Sets convergence criterion for GMRES.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'convergence'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.gmres.ffff"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



            #  ocean.cnbse.broaden
            help =  ['Half? width of broadening in eV for the spectrum. Must be larger than zero.', 'Suggested value is the core-hole broadening.']
            kinds =  [
               [ inp_float ],
               ]
            code =  'ocean'
            importance =  'IMPORTANCE'
            category =  'spectrum'
            field_labels = None
            ranges =  None
            defaults =  None
            field_types =  None
            fexpandable =  False
            lexpandable =  False
            req =  None

            self.inp_def_dict["ocean.cnbse.broaden"] = self._fill_key_info(help,kinds,
                  code,importance,category,field_labels,ranges,defaults,
                  field_types,fexpandable,lexpandable,req)



