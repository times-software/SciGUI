import input_errors as ie
from input_types import *


# Make this a class. The class object should contain a dict() object. 
# Instantiation will be the only way to fill the dictionary. Different 
# types of configurations will be specified by a "code" string variable
# in the instantiation input.
# category will a
class input_definition_dict(dict):

    def _fill_key_info(self,help,kinds,code,importance,category,field_labels,ranges=None,
                    defaults = None, field_types = None,fexpandable=False,lexpandable=False):
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
        return key_info

    #############################################################################################
    #         BEGIN DEFINITION OF KEYWORDS FOR CORVUS
    #############################################################################################

    def __init__(self,input_type):
        self._fill_input_dict(input_type)

    # Class methods.
    # validate_input: Takes a dictionary and validates that it has the correct types, and that
    # values are in range if ranges are specified.
    # Returns error message, and the keyword that created the error.
    # def validate_input(self,inp_dict):
    #     # Loop through keys and check each key
    #     print(inp_dict.items())
    #     for key,val in inp_dict.items():
    #         print(key,val)
    #         # Skip input type key
    #         if key == '_input_type': continue

    #         # First check that key exists in input definition dictionary.
    #         if key not in self:
    #             message='Unrecognized keyword in input:' + key
    #             return message, key
            
    #         # Now check that each value in the inp_dict has the correct kind and ranges.
    #         il = 0
    #         for val_line in val:
    #             if il > len(self[key]['kinds'])-1:
    #                 if not self[key]['lexpandable']:
    #                     message = ('Too many lines defined in input for keyword: ' + key + 
    #                     '. Should be ' + str(len(self[key]['kinds'])) + ' lines of input.')
    #                     return message, key
                    
    #             # If this is line expandable, we want to use the last line of kinds defined.
    #             iline = min(il,len(self[key]['kinds'])-1)

    #             # Now loop over the fields
    #             iv = 0
    #             for v in val_line:
    #                 # Check if there are more fields than those defined.
    #                 if iv > len(self[key]['kinds'][iline]):
    #                     if not self[key]['fexpandable']:
    #                         message = ('Too many fields defined in input for keyword: ' + key +
    #                         '. Should be ' + str(len(self[key]['kinds'][iline])) + ' fields.')
    #                         return message, key

    #                 # If this is an expandable number of fields, we want to use the last kind defined.
    #                 ival = min(iv,len(self[key]['kinds'][iline])-1)

    #                 # Cast the string to the correct input type, then validate it.
    #                 new_val = self[key]['kinds'][iline][ival](v)
                    
    #                 if self[key]['ranges'] is not None:
    #                     iliner = min(il,len(self[key]['ranges'])-1)
    #                     ivalr = min(iv,len(self[key]['ranges'][iliner])-1)
    #                     is_valid, error_message = new_val.validate(self[key]['ranges'][iliner][ivalr])
    #                     if not is_valid:
    #                         message = ('Incorrect type or range for the ' + str(iv) + 'th value associated with the ' +
    #                         'keyword: ' + key + '. ' + error_message)
    #                         return message, key
    #                 else:
    #                     print(new_val,new_val.validate(None))
    #                     is_valid, error_message = new_val.validate(None)
    #                     if not new_val.validate(None)[0]:
    #                         message = ('Incorrect type for the ' + str(iv) + 'th value associated with the ' +
    #                         'keyword: ' + key + '. ' + error_message)
    #                         return message, key

    #                 iv += 1
                
    #             il += 1

    #     # no errors.
    #     return "valid", None
                
    # write_input: takes a dict and a code, validates the dictionary, and writes it as an input file with the
    # correct format for running that specific code.


    # read_input: takes a file and code. Reads the file into an input_dict and validates it. 

    # Below are the definitions of the different input types for the GUI to handle
    def _fill_input_dict(self,input_type):
        if input_type == 'corvus':
            # Special keyword holds type of input 'corvus'
            self['_input_type'] = 'corvus'
            #  target_list
            help =  ' Space separated list with all the target properties requested for this calculation. '
            kinds =  [[inp_choice]]
            code =  'general'
            importance = 'essential'
            category = 'property'
            field_labels = [['property']]
            ranges = [['xanes,xes,rixs']]
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['target_list'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  title
            help =  ' Title of this calculation. '
            kinds =  [[inp_paragraph]]
            code =  'general'
            importance = 'useful'
            category = 'property'
            field_labels = [['title']]
            ranges = None
            defaults = [['This is a Corvus calculation ']]
            field_types = None
            fexpandable = False
            lexpandable = True

            self['title'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  scratch
            help =  ' Directory for disk scratch for those Handlers that require large amounts of  disk. If the directory is not present or it can not be created, Corvus reverts  to the default.  NOTE: This input variable is not fully implemented yet. '
            kinds =  [[inp_file_name]]
            code =  'general'
            importance = 'useful'
            category = 'computation'
            field_labels = [['scratch dir']]
            ranges = None
            defaults = [['.']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['scratch'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  usesaved
            help =  ' Use previously calculated data rather than recalculating '
            kinds =  [[inp_bool]]
            code =  'general'
            importance = 'useful'
            category = 'computational'
            field_labels = [['usesaved']]
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['usesaved'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  multiprocessing_ncpu
            help =  ' Number of processors to use in multiprocessing.  This should be maximum of the number of cpus on a single  node. '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'useful'
            category = 'computational'
            field_labels = [['ncpu']]
            ranges = [['1,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['multiprocessing_ncpu'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  usehandlers
            help =  ' Explicitely declare what Handlers are to be used in the generation of the  Workflow. This helps the current simple Workflow generator when a given target  is provided by more than one Handler.  Current possible values are:     Feff, FeffRixs, Dmdw, Abinit, Vasp, Nwchem, Orca '
            kinds =  [[inp_str]]
            code =  'general'
            importance = 'useful'
            category = 'workflow'
            field_labels = [['handler']]
            ranges = [['feff,helper,vasp,siesta']]
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['usehandlers'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  method
            help =  ' Method used to compute the target. This variable is somewhat context-dependent  and is ccurrently not fully implemented.  Current possible values are:     dft, mp2, ccsd '
            kinds =  [[inp_str]]
            code =  'general'
            importance = 'not-implemented'
            category = 'method'
            field_labels = [['method']]
            ranges = [['dft,mp2,ccsd']]
            defaults = [['dft']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['method'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  xc
            help =  ' Exchange-correlation functional to use if the "method" selected is "dft".  Current possible values are:     lda, pbe, b3lyp '
            kinds =  [[inp_str]]
            code =  'general'
            importance = 'important'
            category = 'dft'
            field_labels = [['exch. corr.']]
            ranges = [['lda,gga']]
            defaults = [['lda']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['xc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  pspfiles
            help =  ' List of pseudopotentials for each atom in the system. Each line contains  the label for the atoms (usually the element % name) and the name of the file  with the pseudopotential. The required format for the files will depend on the  Handler used. '
            kinds =  [[inp_str, inp_file_name]]
            code =  'general'
            importance = 'important'
            category = 'pseudopotentials'
            field_labels = [['atom_label','psp file']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['pspfiles'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  scf_conv
            help =  ' Convergence threshold for SCF cycles (HF, DFT, etc) in au. The value set by  this variable might be internally overridden if the target requires tighter  convergence settings. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'useful'
            category = 'convergence'
            field_labels = [['conv. thr']]
            ranges = [['0,']]
            defaults = [['1.0e-5']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['scf_conv'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  keep_symm
            help =  ' Toggle the preservation of initial symmetry in optimizations. '
            kinds =  [[inp_bool]]
            code =  'general'
            importance = 'useful'
            category = 'optimization'
            field_labels = [['keep symmetry']]
            ranges = None
            defaults = [['True']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['keep_symm'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  constant_volume
            help =  ' Keep the simulation cell volume constant in cell optimizations. '
            kinds =  [[inp_bool]]
            code =  'general'
            importance = 'important'
            category = 'optimization'
            field_labels = [['constant volume']]
            ranges = None
            defaults = [['True']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['constant_volume'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nkpoints
            help =  ' Define the number of k-point in each direction of the grid for reciprocal  space simulations. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'general'
            importance = 'important'
            category = 'band_structure'
            field_labels = [['nka','nkb','nkc']]
            ranges = [['1,','1,','1,']]
            defaults = [['1', '1', '1']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nkpoints'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nqpoints
            help =  ' Define the number of q-point perturbations in each direction of the grid for  density functional perturbation theory (DFPT) simulations. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'general'
            importance = 'important'
            category = 'phonons'
            field_labels = [['nqa', 'nqb', 'nqc']]
            ranges = [['1,','1,','1,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nqpoints'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  pw_encut
            help =  ' Planwave energy cutoff for reciprocal space simulations, in au. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'important'
            category = 'basis'
            field_labels = [['pw encut']]
            ranges = [['0.0,']]
            defaults = [['15.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['pw_encut'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  numberofconfigurations
            help =  ' Set the number of configurations used in disordered systems. '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'important'
            category = 'disorder'
            field_labels = [['# of config.']]
            ranges = [['0,']]
            defaults = [['10']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['numberofconfigurations'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  clusterradius
            help =  ' Radius of clusters created from cif files in angstroms.'
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'useful'
            category = 'cluster'
            field_labels = [['rmax']]
            ranges = [['0.0,']]
            defaults = [['12.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['clusterradius'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif_input
            help =  ' cif input file name. '
            kinds =  [[inp_file_name]]
            code =  'general'
            importance = 'essential'
            category = 'structure'
            field_labels = [['cif file']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif_input'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  supercell_dimensions
            help =  ' supercell dimensions (number of cells in each direction). '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = 'supercell'
            ranges = [['1,','1,','1,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['supercell_dimensions'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ismetal
            help =  ' Toggle whether the system should be treated as a metal or as an insulator. '
            kinds =  [[inp_bool]]
            code =  'general'
            importance = 'important'
            category = 'dielectric'
            field_labels = [['is metal?']]
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ismetal'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ene_int
            help =  ' Internal (electronic) energy of the system, in au. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'useful'
            category = 'electronic'
            field_labels = 'internal energy'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ene_int'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cell_vectors
            help =  ' Normalized simulation cell vector directions. These vectors are scaled using  the "cell_scaling_iso" and "cell_scaling_abc" input variables to generate the  simulation cell. '
            kinds =  [[inp_float, inp_float, inp_float], [inp_float, inp_float, inp_float], [inp_float, inp_float, inp_float]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['x','y','z'],[None,None,None],[None,None,None]]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cell_vectors'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cell_struc_opt_flags
            help =  ' Toggle the optimization of the x, y and z coordinates of each atom in the  system. '
            kinds =  [[inp_bool, inp_bool, inp_bool]]
            code =  'general'
            importance = 'important'
            category = 'optimization'
            field_labels = [['x','y','z']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['cell_struc_opt_flags'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cell_struc_xyz_red
            help =  ' Structure of the simulation cell in reduced coordinates if the system is  extended and has periodic boundary conditions. '
            kinds =  [[inp_str, inp_float, inp_float, inp_float]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['x','y','z']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['cell_struc_xyz_red'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  number_of_atoms
            help =  ' Number of atoms in the system '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['# of atoms']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['number_of_atoms'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  species
            help =  ' chemical species and number of each species '
            kinds =  [[inp_str, inp_int]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['species','N']]
            ranges = [[None,'1,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['species'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cell_scaling_iso
            help =  ' Unitless isotropic scaling of the unit cell. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['latt. scaling']]
            ranges = [['0.0,']]
            defaults = [['1.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cell_scaling_iso'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cell_scaling_abc
            help =  ' Scaling of the a, b and c axes of the simulation cell, in Angstroms. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['a','b','c']]
            ranges = [['0,','0,','0,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cell_scaling_abc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cell_angles_abc
            help =  ' Scaling of the a, b an c axes of the simulation cell, in Angstroms. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'general'
            importance = 'important'
            category = 'structure'
            field_labels = [['alpha','beta','gamma']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cell_angles_abc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  mac_diel_const
            help =  ' Approximate value of the macroscopic dielectric constant of the system used in  some methods to accelerate convergence of the SCF cycle. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'importantce'
            category = 'optical_property'
            field_labels = [['diel. const.']]
            ranges = [['0,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['mac_diel_const'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cluster
            help =  ' Structure of the system is the system is not extended (i. e. is a molecule or  cluster). The coordinates are in Angstroms, and have xyz format, i.e.,  Atomic_symbol1 x y z  Atomic_symbol2 x y z  .  .  . '
            kinds =  [[inp_str, inp_float, inp_float, inp_float]]
            code =  'general'
            importance = 'useful'
            category = 'structure'
            field_labels = [['At. Sym.','x','y','z']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['cluster'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  absorbing_atom
            help =  ' Index of the absorbing atom for core spectroscopies such as XANES, EXAFS and  XES. The index counts from one for the first atom in the associated cluster (see above). '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'important'
            category = 'property'
            field_labels = [['abs atom index']]
            ranges = [['1,']]
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['absorbing_atom'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  absorbing_atom_type
            help =  ' Symbol of atom you would like to calculate the XANES for. Will loop over symmetry unique sites defined  in the CIF file denoted by cif_input (see below). '
            kinds =  [[inp_str]]
            code =  'general'
            importance = 'important'
            category = 'spectroscopy'
            field_labels = 'abs. atom species'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['absorbing_atom_type'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  charge
            help =  ' Net charge of the system. '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'important'
            category = 'molecule'
            field_labels = [['charge']]
            ranges = None
            defaults = [['0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['charge'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  multiplicity
            help =  ' Multiplicity of the system. '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = [['1,']]
            defaults = [['0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['multiplicity'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  spectral_broadening
            help =  ' Broadening used in some spectroscopic methods. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'importance'
            category = 'useful'
            field_labels = [['half width']]
            ranges = [['0,']]
            defaults = [['0.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['spectral_broadening'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  fermi_shift
            help =  ' Shift of the fermi-energy in eV. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'useful'
            category = 'spectrum'
            field_labels = [['fermi shift']]
            ranges = None
            defaults = [['0.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['fermi_shift'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  spin_moment
            help =  ' spin moments of atomic types  set spin moment for ferromagnetic systems.  Only allows one moment per chemical element.  Z spin_moment '
            kinds =  [[inp_int, inp_float]]
            code =  'general'
            importance = 'useful'
            category = 'magnetism'
            field_labels = [['atm sym.','mag. mom.']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['spin_moment'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  xanes_file
            help =  ' file to read xanes from - 2 column file '
            kinds =  [[inp_file_name]]
            code =  'general'
            importance = 'advanced'
            category = 'spectrum'
            field_labels = [['xas file']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['xanes_file'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  spectralFunction_file
            help =  ' file to read spectral function from - 2 column file '
            kinds =  [[inp_file_name]]
            code =  'general'
            importance = 'advance'
            category = 'spectroscopy'
            field_labels = [['spfcn file']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['spectralFunction_file'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  abinit.verbatim
            help =  ' The content of this input variable is passed as is (i. e. "verbatim") into the  input of all Abinit calculations, and it is meant to help with any Abinit  input that is currently not implemented in Corvus. Thus, it should be used  carfully to avoid inconsistencies with the automatically generated input.  Users should refed to the Abinit manual for information on this extra input. '
            kinds =  [[inp_paragraph]]
            code =  'abinit'
            importance = 'useful'
            category = 'NONE'
            field_labels = [['abinit input']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['abinit.verbatim'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  abinit.ngqpt
            help =  "Equivalent to Abinit's ngqpt input variable: Defines the number of q-point  perturbations in each direction of the grid for density functional  perturbation theory (DFPT) simulations, and is that equivalent to the general  \"nqpoints\" Corvus input variable. Please refer to the Abinit manual for  further details.  NOTE: This code-specific input variable will be replaced by the general  \"nqpoints\" variable in the future."
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'abinit'
            importance = 'important'
            category = 'phonons'
            field_labels = [['ngqx','nqqy','ngqz']]
            ranges = [['1,','1,','1,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['abinit.ngqpt'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  abinit.ng2qpt
            help =  ' Equivalent to Abinit\'s (anaddb) ng2qpt input variable: Defines the number of  q-point perturbations in each direction of the finer grid for density  functional perturbation theory (DFPT) simulations. Please refer to the  Abinit manual for further details. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'abinit'
            importance = 'important'
            category = 'phonons'
            field_labels = [['ngq2x','ngq2y','ngq2z']]
            ranges = [['1,','1,','1,']]
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['abinit.ng2qpt'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  dmdw.ioflag
            help =  ' Set the amount of output printed by DMDW. Possible values are:    0: Terse, prints out only the desired result (s^2, u^2, etc).    1: Verbose, prints out the pole frequencies and weights, as well as       estimates of the Einstein temperatures for each path.  Please refer to the DMDW section of the Feff manual for further details.  NOTE: The current format described below is temporary for compatibility with  previous versions of Corvus. This will be changed to "Integer" in the future. '
            kinds =  [[inp_paragraph]]
            code =  'dmdw'
            importance = 'useful'
            category = 'phonons,exafs'
            field_labels = [['io flag']]
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['dmdw.ioflag'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  dmdw.nlanc
            # CONTINUE HERE
            help =  ' Set the number of Lanczos poles (i. e. iterations) in DMDW. Larger values  usually improve convergence of the target quantity. However, the number of  poles should not exceed the dimensions of the subspace spanned by the  projection of the path into the appropriate eigenmodes of the Hessian. This  means that this variable should always be less than 3*N-6, where N is the  number of atoms in the system. In practice, a value of 6-8 is sufficient to  obtain converged mean square relative displacements (MSRD, or s^2) for EXAFS.  For crystallographic mean square displacements (MSD, or u^2) at least 16 poles  are usually needed. Please refer to the DMDW section of the Feff manual for  further details.  NOTE: The current format described below is temporary for compatibility with  previous versions of Corvus. This will be changed to "Integer" in the future. '
            kinds =  [[inp_paragraph]]
            code =  'dmdw'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['dmdw.nlanc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  dmdw.paths
            help =  ' Set up the path descriptors that will generate the list of paths for which  properties will be calculated. The list has the following form:    <Number of descriptors>      <Descriptor 1>      <Descriptor 2>     .     .  Each descriptor has the form:    <Number of atoms in path> <Atom index 1> ... <Max. path length (Ang)>  The atom indices can take the value 0 which acts as a wildcard for all atoms  in the system.  Examples:  2  2 1 0   3.0  3 2 0 5 6.0  This section defines 2 paths descriptors. The first one generates all paths  with two atoms, starting in atom 1 and going to all other atoms in the  systems, but subject to a maximum effective path length of 3.0 Ang. The  second one generates all paths with three atoms, starting in atom 2 and  ending in atom 5, while passing trhough all other atoms in the system, but  with a maximum effective length of 6.0 Ang.  Using the same syntax atoms can be selected to compute their u^2. For example  the paths section  1  1 0 0.0  will produce u^2 for all atoms in the system. Please refer to the DMDW  section of the Feff manual for further details.  NOTE: The current format described below is temporary for compatibility with  previous versions of Corvus. '
            kinds =  [[inp_paragraph]]
            code =  'dmdw'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['dmdw.paths'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  dmdw.tempgrid
            help =  ' Set up the temperature grid to compute the thermal properties in DMDW. It has  the following form:    <Number of temperature> <Min. temp.> <Max. temp.>  If the number of desired temperatures is just one, the maximum temperature  input is not needed. Please refer to the DMDW section of the Feff manual for  further details.  NOTE: The current format described below is temporary for compatibility with  previous versions of Corvus. '
            kinds =  [[inp_paragraph]]
            code =  'dmdw'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['dmdw.tempgrid'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.basis
            help =  ' Set the Gaussian basis set to be used in the NWChem calculations. The format  is the same as in NWChem:  <Atom label> <Basis set name>   .   .  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['nwchem.basis'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.qmd.nstep_nucl
            help =  ' Set the number of nuclear motion steps in a quantum MD simulation.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.qmd.nstep_nucl'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.qmd.dt_nucl
            help =  ' Set the time step for nuclear motion in a quantum MD simulation.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.qmd.dt_nucl'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.qmd.targ_temp
            help =  ' Set the target temperature in a quantum MD simulation.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.qmd.targ_temp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.qmd.thermostat
            help =  ' Set the thermostat type to be used in a quantum MD simulation.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.qmd.thermostat'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.qmd.print_xyz
            help =  ' Toggle printing of xyz coordinates in a quantum MD simulation.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.qmd.print_xyz'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.xc
            help =  ' Set the exchange correlation potential for an NWChem DFT simulation.  NOTE: This input variable will be superseded in the future by the more  general "xc" variable.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.xc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.mult
            help =  ' Set the multiplicity of the system for an NWChem DFT simulation.  NOTE: This input variable will be superseded in the future by the more  general "multiplicity" variable.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.mult'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.qmd.snapstep
            help =  '  '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.qmd.snapstep'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.xas.alpha
            help =  '  '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.xas.alpha'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.xas.xrayenergywin
            help =  '  '
            kinds =  [[inp_float, inp_float]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.xas.xrayenergywin'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.xas.nroots
            help =  '  '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.xas.nroots'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.xas.vec
            help =  '  '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.xas.vec'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.iter
            help =  '  '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.iter'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.charge
            help =  ' Set the net charge of the system for an NWChem DFT simulation.  NOTE: This input variable will be superseded in the future by the more  general "charge" variable.  Please refer to the NWChem manual for further details. '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.charge'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nwchem.xaselem
            help =  '  '
            kinds =  [[inp_str]]
            code =  'nwchem'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nwchem.xaselem'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  nuctemp
            help =  ' nuctemp  {  temp  Specify the temperature (in K) for the nuclear motion (DW factors). '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['300.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['nuctemp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  debyetemp
            help =  ' debyetemp  {  temp  Specify the Debye Model temperature (in K) for the calculation of EXAFS DW  factors. '
            kinds =  [[inp_float]]
            code =  'general'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['debyetemp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  dmdw_nlanczos
            help =  ' dmdw_nlanczos  {  nLanczos_Interations  Specify the number of Lanczos iterations to be done for the calculation of  EXAFS DW factors with the dynamical matrix method. '
            kinds =  [[inp_int]]
            code =  'general'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['6']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['dmdw_nlanczos'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.MPI.CMD
            help =  ' MPI command to use for parallel calculations, e.g., mpirun, srun, or mpiexec. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.MPI.CMD'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.MPI.ARGS{
            help =  ' Ramp scf radius up to final radius, starting from start_radius,  and taking n_ramp steps.  SCFRAMP start_radius n_ramp '
            kinds =  [[inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.MPI.ARGS{'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.atoms
            help =  ' feff.atoms  {  x1  y1  z1 ipot1  x2  y2  z2 ipot2  .  .  .  Specify atomic positions in cartesian coordinates (in Angstroms) and  unique potential indices of each atom in the cluster, one atom per line. '
            kinds =  [[inp_float, inp_float, inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.atoms'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.hole
            help =  ' DEPRECATED: Use feff.edge instead.  Specify the edge using the hole number ihole, e.g.,  K-edge : ihole = 1  L1-edge: ihole = 2  s02 specifies the EXAFS amplitude reduction factor, and should be set to 1. '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.hole'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.overlap
            help =  ' feff.overlap can be used to construct approximate overlapped atom potentials  when atomic coordinates are not known or specified.  NOTE: This input variable is not fully implemented yet. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.overlap'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.control
            help =  ' feff.control{ ipot ixsph ifms ipaths igenfmt iff2x }  feff.control lets you run one or more of the feff program modules  separately. There is a switch for each of six parts of feff:  0 means not to run that module, 1 means to run it. '
            kinds =  [[inp_int, inp_int, inp_int, inp_int, inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.control'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.exchange
            help =  ' feff.exchange{ iexc vr vi iexc0 }  Use feff.exchange to change the self-energy used in x-ray absorption  calculations. ixc is an index specifying the potential model to use for the  fine structure, and the optional ixc0 is the index of the model to use for  the background function. The calculated potential can be corrected by adding  a constant shift to the Fermi level given by vr0 and to a pure imaginary  "optical" potential (i.e., uniform decay) given by vi0. Typical errors in  Feff\'s self-consistent Fermi level estimate are about 1 eV.  (The feff.corrections input is similar but allows the user to make small  changes in vi0 and vr0 after the rest of the calculation is completed, for  example in a fitting process.)  Indices for the available exchange models:    0 Hedin-Lundqvist + a constant imaginary part    1 Dirac-Hara + a constant imaginary part    2 ground state + a constant imaginary part    3 Dirac-Hara + HL imag part + a constant imaginary part    5 Partially nonlocal: Dirac-Fock for core + HL for valence electrons + a      constant imaginary part '
            kinds =  [[inp_int, inp_float, inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.exchange'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.ion
            help =  ' feff.ion{ ipot ionization }  feff.ion ionizes all atoms with unique potential index ipot.  NOTE: This input variable is not fully implemented yet. '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.ion'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.title
            help =  ' Set title for this feff calculation. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['feff.title'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.folp
            help =  ' feff.folp{ ipot overlap }  Set the overlap for unique potential ipot. '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.folp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rpath
            help =  ' feff.rpath{ rmax }  Set maximum path length for path expansion calculations of EXAFS, EXELFS,  DAFS, etc. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rpath'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.debye
            help =  ' feff.debye{ Temperature Debye-Temperature idwopt }  Set temperature and Debye temperature for calculations of EXAFS Debye-Waller  factors.    idwopt - set method for calculating DW factors.  NOTE: This input variable is not fully implemented yet. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.debye'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.dmdw
            help =  ' NOTE: This input variable is not fully implemented yet. '
            kinds =  [[inp_str, inp_int, inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.dmdw'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rmultiplier
            help =  ' feff.rmultiplyer{ rmult }  Multiply coordinates of all atoms by rmult, expanding or contracting the  system. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rmultiplier'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.ss
            help =  ' Set an '
            kinds =  [[inp_int, inp_int, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.ss'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.print
            help =  ' feff.pring{ ipr_pot ipr_xsph ipr_fms ipr_path ipr_genfmt ipr_ff2x }  Set print level for each module of FEFF:    pot:      0 write \'pot.bin\' only      1 add \'misc.dat\'      2 add \'potNN.dat\'      3 add \'atomNN.dat\'    xsph:      0 write \'phase.bin\' and \'xsect.bin\' only      1 add \'axafs.dat\' and \'phase.dat\'      2 add \'phaseNN.dat\' and \'phminNN.dat\'      3 add \'ratio.dat\' (for XMCD normalization) and \'emesh.dat\'.    fms:      0 write \'gg.bin\'      1 write \'gg.dat\'    path:      0 write \'paths.dat\' only      1 add \'crit.dat\'      3 add \'fbeta\' files (plane wave |f(\beta)| approximations)      5 Write only \'crit.dat\' and do not write \'paths.dat\'. (This is useful        genfmt 0 write \'list.dat\', and write \'feff.bin\' with all paths with        importance greater than or equal to two thirds of the curved wave        importance criterion    genfmt:      0 write \'list.dat\', and write \'feff.bin\' with all paths with importance        greater than or equal to two thirds of the curved wave importance        criterion      1 write all paths to \'feff.bin\'    ff2x:      0 write \'chi.dat\' and \'xmu.dat\'      2 add \'chipNNNN.dat\' (chi(k) for each path individually)      3 add \'feffNNNN.dat\' and \'files.dat\', and do not add \'chipNNNN.dat\'        files '
            kinds =  [[inp_int, inp_int, inp_int, inp_int, inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.print'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.potentials
            help =  ' feff.potentials{    ipot iz pot_label lfms1 lfms2 stoichiometry    ...  }  Set unique potentials for FEFF calculation. '
            kinds =  [[inp_int, inp_int, inp_str, inp_int, inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.potentials'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.potentials.spin
            help =  ' feff.potentials.spin{   ipot spin_moment   ...  }  Set spin moments of atoms defined in potentials card '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.potentials.spin'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.lfms1
            help =  ' set maximum angular momentum to use in potentials '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['-1']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.lfms1'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.lfms2
            help =  ' set maximum angular momentum to use in FMS '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['-1']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.lfms2'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.nleg
            help =  ' feff.nleg{ nleg }  Set maximum number of legs to use in path expansion. A Single scattering  path has 2 legs. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.nleg'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.criteria
            help =  ' feff.criteria{ critcw critpw }  Cutoff criteria for the path expansion filtering.  critcw - tolerance for curved wave expansion  critpw - tolerance for initial plane wave approximation '
            kinds =  [[inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.criteria'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.iorder
            help =  ' feff.iorder{ iorder }  Set order of approximation when calculating effective scattering matrices. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.iorder'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.pcriteria
            help =  ' feff.pcriteria{ pcritk pcrith }  Set criteria for filtering in pathfinder. The keep-criterion pcritk looks at  the amplitude of chi (in the plane wave approximation) for the current path  and compares it to a single scattering path of the same effective length.  To set this value, consider the maximum degeneracy you expect and divide  your plane wave criterion by this number. For example, in fcc Cu, typical  degeneracies are 196 for paths with large r, and the minimum degeneracy is 6.  So a keep criterion of 0.08% is appropriate for a pw criteria of 2.5%. The  heap-criterion pcrith filters paths as the pathfinder puts all paths into a  heap (a partially ordered data structure), then removes them in order of  increasing total path length. Each path that is removed from the heap is  modified and then considered again as part of the search algorithm. The heap  filter is used to decide if a path has enough amplitude in it to be worth  further consideration. If a path can be eliminated at this point, entire  trees of derivative paths can be neglected, leading to enormous time savings.  This test does not come into play until paths with at least 4 legs are being  considered, so single scattering and triangular (2 and 3 legged) paths will  always pass this test. Because only a small part of a path is used for  this criterion, it is difficult to predict what appropriate values will be. '
            kinds =  [[inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.pcriteria'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.sig2
            help =  ' feff.sig2{ sig2 }  Set a single Debye-Waller factor for all paths, exp{-2*sig2*k**2}. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.sig2'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.xanes
            help =  ' feff.xanes{ xkmax }  Calculate XANES spectrum.    xkmax - calculate up to k = xkmax '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.xanes'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.corrections
            help =  ' feff.corrections{ vrcorr vicorr }  Correct the Fermi cutoff and broadening in the final spectrum calculation.  vrcorr - Shift Fermi cutoff by -vrcorr.  vicorr - Add extra Lorenzian broadening with half width at half max of vicorr. '
            kinds =  [[inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.corrections'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.afolp
            help =  ' feff.afolp{ folpx }  Set maximum overlap for automatic overlap search.  folpx - maximum overlap allowed. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.afolp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.exafs
            help =  ' feff.exafs{ xkmax xkstep }  Calculate EXAFS spectrum.  xkmax  - calculate spectrum up to k = xkmax  xkstep - calculate in steps of xkstep '
            kinds =  [[inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.exafs'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.polarization
            help =  ' feff.polarization{ x y z }  Set polarization vector of x-rays in cartesian coordinates of input file. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.polarization'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.ellipticity
            help =  ' feff.ellipticity{ elpty x y z }  Set the ellipticity of the x-rays.  This card is used with the feff.polarization.    elpty   - ratio of amplitudes of electric field in the two orthogonal              directions of elliptically polarized light. Only the absolute              value of the ratio is important for nonmagnetic materials. The              present code can distinguish left- and right-circular polarization              only with the feff.xmcd or feff.xncd. A zero value of the              ellipticity corresponds to linear polarization, and unity to              circular polarization. The default value is zero.    x, y, z - coordinates of any nonzero vector in the direction of the              incident beam. This vector should be approximately normal to the              polarization vector '
            kinds =  [[inp_float, inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.ellipticity'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rgrid
            help =  '  '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rgrid'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rphases
            help =  ' feff.rphases{ UseRealPhases }  Set real phase shift approximation.  UseRealPhases - use real phase shift if true. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rphases'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.nstar
            help =  ' feff.nstar{ WriteNStar }  Write nstar.dat with effective coordination number N*. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.nstar'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.nohole
            help =  ' feffnohole{ UseNoHole }  Do not use a hole in the calculation.  DEPRECATED - Use feff.corehole instead. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.nohole'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.sig3
            help =  ' feff.sig3{ alphat thetae }  Set first and third cumulants for single scattering paths:    alphat - first cumulant    thetae - third cumulant '
            kinds =  [[inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.sig3'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.jumprm
            help =  ' feff.jumprm{ UseRemoveJump }  If true, smooth the jump between muffin tin potentials and interstitial. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.jumprm'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.mbconv
            help =  ' Deprecated: Should not be used. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.mbconv'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.spin
            help =  ' feff.spin{ ispin sx sy sz }  Specify the type of spin-dependent calculation for spin along the (x, y, z)  direction, along the z-axis by default. The SPIN card is required for the  calculation of all spin-dependent effects, including XMCD and SPXAS.    ispin:       2 spin-up SPXAS and LDOS      -2 spin-down SPXAS and LDOS       1 spin-up portion of XMCD calculations      -1 spin-down portion of XMCD calculations '
            kinds =  [[inp_int, inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.spin'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.edge
            help =  ' feff.edge{ edgeLabel }  Set edge to calculate for XAS, XES, EELS, and other related spectra. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['feff.edge'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.scf
            help =  ' feff.scf{ rfms1 lfms1 nscmt ca nmix }  Use self-consistent field calculation of potentials.    rfms1 - radius of cluster to use for scf calculations.    lfms1 - 0 for solids, 1 for molecules    nscmt - maximum number of iterations in SCF calculation.    ca    - convergence factor for Broyden algorithm    nmix  - number of initial iterations of mixing algorithm to use. '
            kinds =  [[inp_float, inp_int, inp_int, inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.scf'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.fms
            help =  ' feff.fms{ rfms lfms2 minv toler1 toler2 rdirec }  Use full multiple-scattering.  rfms   - radius of cluster to use for fms calculation.  lfms1  - 0 for solids, 1 for molecules  minv   - set algorithm for matrix inversion           0: LU decomposition           2: Lanczos           3: Broyden (less reliable)  toler1 - tolerance to stop recursion and Broyden algorithm  toler2 - sets the matrix element of the Gt matrix to zero if its value is           less than toler2  rdirec - sets the matrix element of the Gt matrix to zero if the distance           between atoms is larger than rdirec '
            kinds =  [[inp_float, inp_int, inp_int, inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.fms'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.ldos
            help =  ' feff.ldos{ emin emax broadening npoints }  Run angular momentum project density of states calculations.  emin       - minimum energy of energy grid.  emax       - maximum energy of energy grid.  broadening - Lorenzian broadening to use in calculation.  npoints    - number of energy points in grid. '
            kinds =  [[inp_float, inp_float, inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.ldos'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.interstitial
            help =  ' feff.interstitial{ inters vtot }  The construction of the interstitial potential and density may be changed by  using this card. inters = 1 might be useful when only the surroundings of the  absorbing atom are specified in \'feff.inp\'. inters defines how to find the  interstitial potential.     inters=0: The interstitial potential is found by averaging over the               entire extended cluster in \'feff.inp\'. (Default)     inters=1: the interstitial potential is found locally around the               absorbing atom.     vtot:     the volume per atom normalized by ratmin3               (vtot=(volume per atom)/ratmin3), where ratmin is the shortest               bond for the absorbing atom. This quantity defines the total               volume (needed to calculate the interstitial density) of the               extended cluster specified in \'feff.inp\'. If vtot <= 0 then the               total volume is calculated as a sum of Norman sphere volumes.               Otherwise, total volume = nat * (vtot * ratmin3), where nat is               the number of atoms in an extended cluster. '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.interstitial'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.cfaverage
            help =  ' Obsolete: Do not use. '
            kinds =  [[inp_int, inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.cfaverage'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.s02
            help =  ' feff.s02{ s02 }  Set EXAFS amplitude reduction factor. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.s02'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.xes
            help =  ' feff.xes{ emin emax estep }  Calculate x-ray emission spectrum.    emin  - minimum energy of calculation.    emax  - maximum energy of calculation    estep - energy step of calculation '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.xes'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.danes
            help =  ' feff.danes{ xkmax xkstep estep }\n  Calculate diffraction anomalous near edge structure.  xkmax  - calculate up to k = xkmax  xkstep - use steps of size xkstep  estep  - near the edge, use steps calculated from estep '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.danes'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.fprime
            help =  ' feff.fprime{ emin emax estep }\n  emin  - minimum energy of calculation.  emax  - maximum energy of calculation  estep - energy step of calculation  Calculate atomic scattering factor f\' '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.fprime'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rsigma
            help =  ' feff.rsigma{ UseRealSelfEnergy }  If true use only real part of self-energy. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rsigma'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.xmcd
            help =  ' feff.xmcd{ xkmax xkstep estep }  Caluclate x-ray magnetic (or natural) circular dichroism    xkmax  - calculate up to k = xkmax    xkstep - use steps of size xkstep    estep  - near the edge, use steps calculated from estep '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.xmcd'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.multipole
            help =  ' feff.multipole{ le2 l2lp }  Set multipole expansion approximation. Specifies which multipole transitions  to include in the calculations. The options are: only dipole (le2 = 0,  default), dipole and magnetic dipole (le2 = 1), dipole and quadrupole  (le2 = 2). This cannot be used with NRIXS and is not supported with EXELFS  and ELNES. The additional field l2lp can be used to calculate individual  dipolar contributions coming from L -> L + 1 (l2lp = 1) and from L -> L - 1  (l2lp = -1). Notice that in polarization dependent data there is also a  cross term, which is calculated only when l2lp = 0 '
            kinds =  [[inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.multipole'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.unfreezef
            help =  ' feff.unreezef{ UnfreezeFOrbitals }  If true, allow f-orbitals to relax during SCF calculation. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.unfreezef'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.tdlda
            help =  ' feff.tdlda{ ifxc }  Use TDLDA to calculate x-ray absorption spectrum.  ifxc - set algorithm for tdlda approximation         0: use static approximation for screening of the x-ray field         1: use approximate dynamic screening of x-ray field and core-hole. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.tdlda'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.pmbse
            help =  '  '
            kinds =  [[inp_int, inp_int, inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.pmbse'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.mpse
            help =  ' feff.mpse{ ipl npl }  Use many-pole model self-energy. This requires the loss function, which can  be provided externally, or approximated using feff.opcons.    ipl - Set method for self-energy inclusion:           1: use an "average" self-energy which is applied to the whole              system (default).           2: use a density dependendent self-energy which is              different at every point inside the muffin-tin radius. '
            kinds =  [[inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.mpse'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.sfconv
            help =  ' feff.sfconv{ UseSpectralFunctionConvolution }  If true, convolve spectrum with spectral function to account for  multi-electron excitations. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.sfconv'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.self
            help =  ' feff.self{ PrintSelfEnergy }  Print out quasiparticle self-energy calculated during spectral-function  convolution calculations. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.self'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.sfse
            help =  ' feff.sfse{ k }  Print out off shell self-energy Sigma(k,E) calculated during  spectral-function convolution calculations. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.sfse'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rconv
            help =  ' Advanced: Print running convolution with the spectral function. '
            kinds =  [[inp_float, inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rconv'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.elnes
            help =  ' This card is not implements yet. '
            kinds =  [[inp_float, inp_float, inp_float], [inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['feff.elnes'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.exelfs
            help =  ' This card is not implemented yet. '
            kinds =  [[inp_float], [inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.exelfs'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.magic
            help =  ' This card is not implemented yet. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.magic'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.absolute
            help =  ' feff.absolue{ UseAbsoluteUnits }  Print spectrum in absolute units instead of normalizing. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.absolute'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.symmetry
            help =  ' feff.symmetry{ UseSymmetry }  If false, turn off symmetry considerations in path expansion. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.symmetry'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.real
            help =  ' Advanced: Use real phase shifts. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.real'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.reciprocal
            help =  ' Work in reciprocal space (k-space calculation). '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.reciprocal'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.sgroup
            help =  ' Specify space group by number (1 - 230). '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.sgroup'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.lattice
            help =  ' This card specifies the lattice. First, its type must be specified using a single letter : P for  primitive, F for face centered cubic, I for body centered cubic, H for hexagonal. The following  three lines give the three basis vectors in Carthesian Angstrom coordinates. They are multiplied  by scale (e.g., 0.529177 to convert from bohr to Angstrom).  feff.lattice{ P 3.18800  ax ay az  bx by bz  cx cy cz '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.lattice'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.kmesh
            help =  ' Specify the kmesh.  feff.kmesh nkp(x) [nkpy nkpz [ktype [usesym] ] ]  This card specifies the mesh of k-vectors used to sample the full Brillouin Zone for the evaluation  of Brillouin Zone integrals. Nkp is the number of points used in the full zone. It can be specified  either as ”nkpx nkpy nkpz”, ”nkp”, or ”nkp 0 0”. If usesym = 1, the zone is reduced to its  irreducible wedge using the symmetry options specified in file symfile, which must be present  in the working directory. The k-mesh is constructed using the tetrahedron method of Bloechl  et al., Phys. Rev. B, 1990. The parameter ktype is meant for time-saving only and means:   ktype=1 : regular mesh of nkp points for all modules   ktype=2 : use nkp points for ldos/fms and nkp/5 points for pot (significant time savings)   ktype=3 : use nkp points for ldos/fms and nkp/5 points for pot (near edge) ; reduce nkp  for all modules as we get away from near-edge (somewhat experimental)  * use a k-mesh of 1000 points in the full BZ.  feff.kmesh{ 1000 }  * use a k-mesh of 10x5x3 points for a large, irregular cell.  feff.kmesh{ 10 5 3 }  * use a k-mesh of 1000 points and try to save time:  feff.kmesh{ 1000 0 0 3 } '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['feff.kmesh'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.strfac
            help =  ' feff.strfac{ eta gmax rmax }  This card gives three non-physical internal parameters for the calculation of the KKR structure  factors : the Ewald parameter and a multiplicative cutoff factor for sums over reciprocal (gmax)  and real space (rmax) sums. Multiplicative means the code makes a ’smart’ guess of a cutoff  radius, but if one suspects something fishy is going on, one can here e.g. use gmax=2 to multiply  this guess by 2. Eta is an absolute number. Given the stability of the Ewald algorithm, it  shouldn’t be necessary to use this card. Its use is not recommended. Only active in combination  with the feff.reciprocal card. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.strfac'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.corehole
            help =  ' feff.corehole{ CoreHoleApproximation }  Set method for calculating corehole interaction.  CoreHoleApproximation -                          None: Do not use a corehole.                          FSR : Final-state rule                          RPA : Use RPA dielectric function to calculate                                screening of core-hole. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.corehole'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.target
            help =  ' feff.target{ ic }  Specifies the location of the absorber atom for reciprocal space calculations. It is entry ic of the  feff.ATOMS card if an feff.ATOMS card and feff.LATTICE card are used. In conjunction with the cif_input  card it is entry ic the list of atoms as given in the ‘.cif’ file (i.e., a list of the crystallographically  inequivalent atom positions in the unit cell). The target needs to be specified also for NOHOLE  calculations. Note that this cannot be specified in the feff.POTENTIALS list because periodic  boundary conditions would then produce an infinite number of core holes.  * calculate a spectrum for the second atom in the feff.ATOMS list or CIF file.  feff.TARGET{ 2 } '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.target'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.egrid
            help =  ' This card can be used to customize the energy grid. The EGRID card is followed by lines  specifying the type of grid, minimum and maximum values for the grid, and the grid step, i.e.  grid_type grid_min grid_max grid_step  The grid type parameter is a string that can take the values e_grid, k_grid, or exp_grid. When  using the e_grid or k_grid grid types, grid_min, grid_max, and grid_step are given in eV or Å −1  respectively. For the exp_grid type, grid_min and grid_max are the minimum and maximum  grid values in eV, and grid_step is the exponential, i.e.    E_i = E_Min + (E_max-E_Min)*[exp(grid_step ∗ i) − 1.0].  A fourth grid type user grid is also available for feff. user grid is followed by an arbitrary  number of lines, each specifying an energy point in eV , i.e.,  user_grid  0.1  1.5  3.45  6.0  .  .  . '
            kinds =  [[inp_str, inp_str, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.egrid'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.coordinates
            help =  ' feff.coordinates{ i }  i must be an integer from 1 through 6. It specifies the units of the atoms of the unit cell given  in the ATOMS card for reciprocal space calculations. If the card is omitted, the default value  icoord = 3 is assumed. FIX check this  1. Cartesian coordinates, Angstrom units. Like feff - you can copy from a real-space  feff.inp file if your lattice vectors coincide with atoms in that feff.inp file.  2. Cartesian coordinates, fractional units (i.e., fractions of the lattice vectors ; should be  numbers between 0 and 1). Similar to feff.  3. Cartesian coordinates, units are fractional with respect to FIRST lattice vector. Like  SPRKKR. (default)  4. Given in lattice coordinates, in fractional units. Like WIEN2k (but beware of some  ‘funny’ lattice types, e.g. rhombohedral, in WIEN2k case.struct if you’re copy-pasting )  5. Given in lattice coordinates, units are fractional with respect to FIRST lattice vector.  6. Given in lattice coordinates, Angstrom units. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.coordinates'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.extpot
            help =  ' Not currently workding. Do not use. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.extpot'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.chbroad
            help =  ' feff.chbroad{ ichbroad }  Set method of calculating core-hole lifetime broadening.  ichbroad -             0: Calculate Green\'s function at energy with imaginary part equal                to Gamma_CH/2.             1: Convolve final spectrum with Lorenzian of full width at                half-max Gamma_ch. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.chbroad'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.chsh
            help =  ' feff.chsh{ ich }  Correct chemical shift.  ich = 0 or 1. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.chsh'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.dims
            help =  ' feff.dims{ nmax lmax }  Set maximum dimensions for fms calculations.  nmax - maximum number of atoms in fms matrix.  lmax - maximum angular momentum of fms matrix. '
            kinds =  [[inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.dims'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.nrixs
            help =  '  '
            kinds =  [[inp_int], [inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['feff.nrixs'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.ljmax
            help =  ' For use in calculations of NRIXS. Not implemented yet. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.ljmax'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.ldec
            help =  ' For use in calculations of NRIXS. Not implemented yet. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.ldec'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.setedge
            help =  ' feff.setedge{ UseEdgeTable }  Use table of experimental edge energies. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.setedge'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.eps0
            help =  ' feff.eps0{ eps0 }  Set dielectric constant used for many-pole self-energy calculations. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.eps0'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  opcons.usesaved
            help =  ' feff.opcons{ }  Calculate loss function using an atomic approximation. '
            kinds =  [[inp_bool]]
            code =  'opcons'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['opcons.usesaved'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.opcons
            help =  ' Calculate the dielectric function of the material within the  atomic approximation. Very fast. Used to calculate loss.dat for  use with feff.mpse self-energy calculations. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.opcons'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.numdens
            help =  '  '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.numdens'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.preps
            help =  ' feff.preps{ PrintEpsilon }  Print dielectric function as calculated by feff.opcons. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.preps'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.egapse
            help =  ' feff.egapse{ egap }  Use this gap energy when applying the many-pole self-energy. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.egapse'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.chwidth
            help =  ' feff.chwidth{ gamma_ch }  Set core-hole width instead of using FEFF\'s internal table of widths. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.chwidth'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.restart
            help =  ' Not implemented yet. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.restart'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.config
            help =  ' Not implemented yet. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.config'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.screen
            help =  ' The screen module, which calculates the RPA core hole potential, is a ’silent’ module: it has  no obvious input but instead runs entirely on default values. Using the feff.SCREEN card you  can change these default values. They will be written to an optional ‘screen.inp’ file (which  you can also edit manually). The feff.SCREEN card can occur more than once in ‘feff.inp’; all  entries will be applied to the calculation. parameter must be one of : ner (40), nei (20), maxl  (4), irrh (1), iend (0), lfxc (0), emin (-40 eV), emax (0 eV), eimax (2 eV), ermin (0.001 eV),  rfms (4.0), nrptx0 (251). For most calculations the default values given (between brackets) are  fine. Occasionally we’ve changed rfms, maxl, or emin. Note that the screen is only active with  feff.COREHOLE{ RPA }.  * Set the cluster radius for the RPA potential calculation higher than the default of 4.0  feff.COREHOLE{ RPA }  feff.SCREEN{ rfms 5.0 } '
            kinds =  [[inp_str, inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['feff.screen'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.cif
            help =  ' Specify a cif input file. Dangerous. Use cif_input instead. '
            kinds =  [[inp_str]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.cif'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.equivalence
            help =  ' feff.equivalence{ ieq }  This optional card is only active in combination with the CIF card. It tells feff how to  generate potential types from the list of atom positions in the ‘cif’ file.  If ieq = 1, the crystallographic equivalence as expressed in the ‘cif’ file is respected; that  is, every separate line containing a generating atom position will lead to a separate potential  type. This means that, e.g., in HOPG graphite, the two generating positions will give rise to  two independent C potentials. This is also the default behavior if the EQUIVALENCE card is  not specified.  If ieq = 2, unique potentials are assigned based on atomic number Z only. That is, all  C atoms will share a C potential and so on. This is how most feff calculations are run.  Whether it is sensible or not to do this depends on the system and on the property one wishes  to calculate. Keep in mind that feff is a muffin tin code, and may therefore be indifferent  to certain differences between crystallographically inequivalent sites. On the other hand, if  an element occurs in the crystal with different oxidation states, it may be necessary to assign  separate potentials to these different types in order to describe the crystal properly and get  accurate spectra.  If ieq = 3, unique potentials are assigned based on atomic number Z and the first shell.  This can be useful e.g. to treat larger systems with crystal defects, where only first neighbors  of the defect need to be treated differently from all more distant atoms of a certain Z. (To be  implemented.)  If ieq = 4, a hybrid of methods 1 and 2 is used. That is, if the number of unique crystallo-  graphic positions does not exceed a hard-coded limit (nphx=9 in the current version), they are  treated with the correct crystallographic equivalence. If the number of unique crystallographi-  cally inequivalent sites is larger, they get combined by atomic number Z. This ad hoc approach  is a practical way of simply limiting the number of unique potentials. This makes sense be-  cause, first of all, there are certain hardcoded limits that would require recompilation of the  code, requiring more RAM memory and more work than a user may want to do. '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['1']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.equivalence'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.compton
            help =  ' Not implemented yet. '
            kinds =  [[inp_float, inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.compton'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rhozzp
            help =  ' Not implemented yet. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rhozzp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.cgrid
            help =  ' Not implemented yet. '
            kinds =  [[inp_float, inp_int, inp_int, inp_int, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.cgrid'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.corval
            help =  ' feff.corval{ emin }  The core-valence separation energy is found by scanning the DOS within an energy window.  The emin parameter sets the lower bound (in eV) of this energy window. It is 70 eV by  default. For some materials it is necessary to lower this bound, e.g. to 100 eV. For example,  when SCF convergence is elusive because occupation numbers for one or more l-values are  changing drastically between SCF iterations due to states moving above and below a poor  estimate of the core-valence separation energy. We plan to replace the current mechanism by a  more robust and automated algorithm, but in the meantime users can use the CORVAL card  to handle some of these difficult cases. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.corval'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.siggk
            help =  ' Not implemented yet. '
            kinds =  [[inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.siggk'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.temperature
            help =  ' feff.temperature{ etemp iscfxc }  The TEMP card sets the electronic temperature and the exchange-correlation potential. etemp  = 0 (default). etemp is in eV. There are 4 different options for the exchange-correlation  potential.  iscfxc     No temperature dependent exchange correlations        11 von-Barth Hedin 1971 (default)        12 Perdew-Zunger     Explicitly temperature dependent exchange correlations        21 Perrot Dharma-Wardana 1984        22 KSDT (recommended) '
            kinds =  [[inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.temperature'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.density
            help =  ' Not implemented yet. '
            kinds =  [[inp_str, inp_str, inp_str], [inp_float, inp_float, inp_float], [inp_int, inp_int, inp_int], [inp_float, inp_float, inp_float], [inp_float, inp_float, inp_float], [inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.density'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rixs
            help =  ' feff.RIXS {gam_Ei gam_El xmu}  The RIXS card sets the parameters for the RIXS calculation. It must be used with a workflow  or script to produce RIXS.  gam_Ei     Broadening to use in the incident energy direction.  gam_El     Broadening to use in the energy loss direction.  xmu     Fermi energy to use for the RIXS calculation, if not present, the fermi level calculated in     the SCF step will be used. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rixs'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.rlprint
            help =  ' Advanced used in RIXS calculations, but automated by corvus. Prints real scattering wavefunction R_l. '
            kinds =  [[inp_bool]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.rlprint'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.hubbard
            help =  ' Not currently working. '
            kinds =  [[inp_float, inp_float, inp_float, inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.hubbard'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.crpa
            help =  ' Not currently working. '
            kinds =  [[inp_int, inp_float]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.crpa'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  feff.scxc
            help =  '  '
            kinds =  [[inp_int]]
            code =  'feff'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['feff.scxc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.expert
            help =  ' Use verbatim expert setting for orca. '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['orca.expert'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.convergencestrategy
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['NormalConv']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.convergencestrategy'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.cpcm
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.cpcm'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.method
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['B3LYP']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.method'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.runtype
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['OPT']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.runtype'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.amass
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['Mass2016']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.amass'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.usesymm
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.usesymm'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.frozencore
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.frozencore'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.allowrhf
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.allowrhf'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.ri
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.ri'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.grid
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['GRID4']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.grid'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.method.gridx
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.method.gridx'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.hftyp
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['RHF']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.hftyp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.fracocc
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.fracocc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.smeartemp
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.smeartemp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.keepints
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.keepints'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.keepdens
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.keepdens'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.readints
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.readints'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.usecheapints
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.usecheapints'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.valformat
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.valformat'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.kmatrix
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.kmatrix'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.jmatrix
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.jmatrix'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.scfmode
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.scfmode'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.maxiter
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.maxiter'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.guess
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.guess'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.autostart
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['True']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.autostart'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.convergence
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['NORMALSCF']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.convergence'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.diis
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.diis'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.kdiis
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.kdiis'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.nr
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.nr'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.soscf
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.soscf'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.cnvdamp
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.cnvdamp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.cnvshift
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.cnvshift'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.scf.uno
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.scf.uno'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.basis.basis
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['def2-TZVP']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.basis.basis'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.basis.decontract
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.basis.decontract'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.mp2
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.mp2'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.mp2type
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['MP2']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.mp2type'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.ci
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.ci'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.citype
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['CCSD']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.citype'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.tole
            help =  '  '
            kinds =  [[inp_float]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.tole'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.tolrmsg
            help =  '  '
            kinds =  [[inp_float]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.tolrmsg'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.tolmaxg
            help =  '  '
            kinds =  [[inp_float]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.tolmaxg'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.tolrmsd
            help =  '  '
            kinds =  [[inp_float]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.tolrmsd'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.tolrmaxd
            help =  '  '
            kinds =  [[inp_float]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.tolrmaxd'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.geom.optimizationquality
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['TIGHTOPT']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.geom.optimizationquality'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.coords.units
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.coords.units'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.rel.method
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.rel.method'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.rel.soctype
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.rel.soctype'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.output.printlevel
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.output.printlevel'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.output.print
            help =  '  '
            kinds =  [[inp_str]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.output.print'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.output.xyzfile
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.output.xyzfile'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  orca.output.pdbfile
            help =  '  '
            kinds =  [[inp_bool]]
            code =  'orca'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['orca.output.pdbfile'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.MPI.CMD{
            help =  ' Specify number of time steps for RT-TDDFT run. '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.MPI.CMD{'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.PAO.EnergyShift{
            help =  ' Specify energy shift to control basis cutoff radii.  Specify the time step for RT-TDDFT run. '
            kinds =  [[inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.PAO.EnergyShift{'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.TD.ShapeOfEfield
            help =  ' Specify the shape of the field for the RT-TDDFT run.  Options are:  step     - Turn off dipole field at time 0.  halfstep - Dipole field changes from full strength to 1/2             strength at time 0.  delta    - Dipole field with time dependence delta(t).  const    - Turn on dipole field at time 0.  sine     - Dipole field with damped sine wave time dependence,             with optional Gaussian envelope to create quasi-harmonic             wave packet.  core     - turn on core-hole potential at time 0.  core2    - GS with full core-hole. Excited states from linear response after. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.TD.ShapeOfEfield'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.TD.CoreExcitedAtom
            help =  ' Set which atom will be the absorbing atom, i.e., which atoms the  core-hole will be centered on '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.TD.CoreExcitedAtom'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.TD.CorePerturbationCharge
            help =  ' Set the core-hole charge. '
            kinds =  [[inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.TD.CorePerturbationCharge'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.TD.mxPC
            help =  ' Maximum number of points to use for predictor-corrector algorith. '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['2']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.TD.mxPC'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Diag.DivideAndConquer
            help =  '  '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.Diag.DivideAndConquer'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.LongOutput
            help =  ' Output lots of info. '
            kinds =  [[inp_bool]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['True']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.LongOutput'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.MeshCutoff
            help =  ' Energy that defines the real-space grid. Point spacing scales as 1/sqrt(E_c). '
            kinds =  [[inp_float, inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['120.0', 'Ry']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.MeshCutoff'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.XC.functional
            help =  ' Set flavor of exchange-correlation functional, i.e., LDA or GGA. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['GGA']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.XC.functional'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.XC.authors
            help =  ' Set authors of exchange correlation functional. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['PBE']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.XC.authors'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.LatticeConstant
            help =  ' Set an overall multiplicative constant for the lattice parameters. '
            kinds =  [[inp_float, inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.LatticeConstant'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Block.PAO.Basis
            help =  ' Set siesta basis manually '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['siesta.Block.PAO.Basis'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Block.LatticeParameters
            help =  ' Set lattice parameters, i.e.,  a b c alpha beta gamma '
            kinds =  [[inp_float, inp_float, inp_float, inp_float, inp_float, inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.Block.LatticeParameters'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.MaxSCFIterations
            help =  ' Max number of SCF iterations allowed. '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['100']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.MaxSCFIterations'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.UseSaveData
            help =  ' Use saved data to start siesta calculation '
            kinds =  [[inp_bool]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['False']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.UseSaveData'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.DM.InitSpin.AF
            help =  ' Set magnetic behavior of system to antiferromagnetic if true.  Default is false and will be set up as ferromagnetic. '
            kinds =  [[inp_bool]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.DM.InitSpin.AF'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.SpinPolarized
            help =  ' Include spin in calculation.  Value should be yes or no. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.SpinPolarized'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.DM.NumberBroyden
            help =  '  '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.DM.NumberBroyden'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.DM.NumberPulay
            help =  ' Set number of Pulay steps '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.DM.NumberPulay'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.DM.MixingWeight
            help =  ' Mixing weight for the density matrix. '
            kinds =  [[inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['0.10']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.DM.MixingWeight'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.DM.Tolerance
            help =  ' Convergence tolerance for elements of the density matrix '
            kinds =  [[inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['1.0e-4']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.DM.Tolerance'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.SolutionMethod
            help =  ' Method for solving the eigenvalue problem. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['diagon']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.SolutionMethod'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.PAO.BasisType
            help =  ' Define basis type  split: Split-valence scheme for multiple-zeta. The split is based on different radii.  splitgauss: Same as split but using Gaussian functions.  nodes: Generalized PAO’s.  nonodes: The original PAO’s are used, multiple-zeta is generated by changing the  scale-factors, instead of using the excited orbitals.  filteret: Use the filterets as a systematic basis set. The size of the basis set is  controlled by the filter cut-off for the orbitals. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['split']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.PAO.BasisType'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.PAO.BasisSize
            help =  ' Define basis size. Can be SZ, DZ, SZP, DZP. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['DZP']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.PAO.BasisSize'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.ElectronicTemperature
            help =  ' Set electronic teperature used to define occupation numbers during SCF. '
            kinds =  [[inp_float, inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['1.0', 'K']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.ElectronicTemperature'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.NumberOfAtoms
            help =  ' Indicate number of atoms in unit cell. '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.NumberOfAtoms'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.NumberOfSpecies
            help =  ' Indicate number of species in unit cell. '
            kinds =  [[inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.NumberOfSpecies'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Block.ChemicalSpeciesLabel
            help =  ' Indicate the different chemical species in the unit cell.  Format:  SpeciesIndex1 AtomicNumber1 AtomicSymbol1  SpeciesIndex2 AtomicNumber2 AtomicSymbol2  ... '
            kinds =  [[inp_int, inp_int, inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.Block.ChemicalSpeciesLabel'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.AtomicCoordinatesFormat
            help =  ' Specify units and format of atomic coordinates.  Borh            - cartesian in Bohr.  Ang             - cartesian in Angstrom.  ScaledCartesian - cartesian scaled by lattice constant.  Fractional      - coordinates are given in units of the lattice vectors. '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['Fractional']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.AtomicCoordinatesFormat'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Block.AtomicCoordinatesAndAtomicSpecies
            help =  ' Specify coordinates of each atom as well as the species index.  x1 y1 z1 SpeciesIndex1  x2 y2 z2 SpeciesIndex2  ... '
            kinds =  [[inp_float, inp_float, inp_float, inp_int]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['siesta.Block.AtomicCoordinatesAndAtomicSpecies'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Coreresponse.Broadening
            help =  '  '
            kinds =  [[inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['0.5']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.Coreresponse.Broadening'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.Beta.Broadening
            help =  '  '
            kinds =  [[inp_float]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['0.1']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['siesta.Beta.Broadening'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  siesta.expert
            help =  '  '
            kinds =  [[inp_str]]
            code =  'siesta'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['siesta.expert'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  phsf.numtimepoints
            help =  '  '
            kinds =  [[inp_int]]
            code =  'phsf'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['40000']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['phsf.numtimepoints'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  phsf.broadening
            help =  '  '
            kinds =  [[inp_float]]
            code =  'phsf'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['0.5']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['phsf.broadening'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  phsf.ekeqp
            help =  '  '
            kinds =  [[inp_float, inp_float]]
            code =  'phsf'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['0.0', '0.0']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['phsf.ekeqp'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif2cell.cif_input
            help =  ' Crystallographic information file to use. '
            kinds =  [[inp_str]]
            code =  'cif2cell'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif2cell.cif_input'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif2cell.program
            help =  ' Program for cif2cell to write input for. '
            kinds =  [[inp_str]]
            code =  'cif2cell'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif2cell.program'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif2cell.outfile
            help =  ' Write output to outfile '
            kinds =  [[inp_str]]
            code =  'cif2cell'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif2cell.outfile'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif2cell.supercell
            help =  '  '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'cif2cell'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif2cell.supercell'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif2cell.cartesian
            help =  ' make output in cartesian form '
            kinds =  [[inp_bool]]
            code =  'cif2cell'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif2cell.cartesian'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cif2cell.atomicunits
            help =  ' print coordinates in bohr rather than angstroms '
            kinds =  [[inp_bool]]
            code =  'cif2cell'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cif2cell.atomicunits'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  cfavg.target
            help =  '  '
            kinds =  [[inp_str]]
            code =  'cfavg'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['cfavg.target'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  fit.target
            help =  '  '
            kinds =  [[inp_str]]
            code =  'fit'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['fit.target'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  fit.parameters
            help =  '  '
            kinds =  [[inp_str, inp_float]]
            code =  'fit'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['fit.parameters'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  fit.datafile
            help =  '  '
            kinds =  [[inp_str]]
            code =  'fit'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['fit.datafile'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  fit.bond
            help =  '  '
            kinds =  [[inp_int]]
            code =  'fit'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = True


            self['fit.bond'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.photon.operator
            help =  ' Select the operator to be used to calculate the (diple or quad) '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['dipole']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.photon.operator'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.photon.polarization
            help =  ' Direction of polarization for XANES or XES calculations '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.photon.polarization'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.photon.qhat
            help =  ' Direction of q-vector for quadrupole or NRIXS calculations '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.photon.qhat'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.photon.energy
            help =  ' Set energy of x-rays at edge '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.photon.energy'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.para_prefix
            help =  ' Set the command to use for parallel runs, i.e., mpirun, mpiexec etc,  along with any flags to use. '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.para_prefix'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.ser_prefix
            help =  ' prefix for serial parts of the code, for example, cut3d should be run  with only 1 processor, i.e., mpirun -n 1 '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.ser_prefix'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.dft
            help =  ' Which DFT code to use: qe - QuantumEspresso, abi - ABINIT '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = [['abi']]
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.dft'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.scratch
            help =  ' Where to write scratch files '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.scratch'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.acell
            help =  ' Scaling in Bohr for the primitive vectors of the unit cell '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.acell'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.rprim
            help =  ' Primitive vectors of unit cell '
            kinds =  [[inp_float, inp_float, inp_float], [inp_float, inp_float, inp_float], [inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.rprim'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.ntypat
            help =  ' Number of different types (usually species) of atom in the unit cell. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.ntypat'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.znucl
            help =  ' List of length ntypat with atomic numbers of each type of atom in the unit cell '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.znucl'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.natom
            help =  ' Number of atoms in the unit cell '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.natom'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.typat
            help =  ' Type of each atom in the unit cell denoted by the integer index corresponding  to the ocean.znucl list of atomic numbers. This list must be in the same  as the coordinates listed in ocean.xred '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.typat'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.xred
            help =  ' Reduced coordinats of atoms in the unit cell. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['ocean.xred'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.diemac
            help =  ' Macroscopic dielectric matrix. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.diemac'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.nspin
            help =  ' Choose paramagnetic (nspin = 1), or spin dependent (nspin = 2). '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.nspin'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.smag
            help =  ' Controls initial magnetism for the DFT calculations. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['ocean.smag'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.smag.ixc
            help =  ' Used for abinit runs in smag card. Don\'t know the meaning at the moment.  This should be combiened with ocean.smag to write the card to the ocean  input. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.smag.ixc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.ldau
            help =  ' Controls the U parameters for the DFT run. Only works with QuantumEspresso  currently. Not sure what the parameters are, but I believe they are  logical flag to run/not run LDA+U, U for each atom that has spin  associated with smag. '
            kinds =  [[inp_bool], [inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['ocean.ldau'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.zymb
            help =  ' For use with QE. Each element listed in ocean.znucle can have a symbol  associated with it. '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.zymb'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.pp_list
            help =  ' Names of the pseudopotential files to be used listed in the same order as  ocean.znucl '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['ocean.pp_list'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.ecut
            help =  ' Plane wave basis truncation energy in Rydberg '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.ecut'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.nkpt
            help =  ' Number of k-points in each direction used to sample the  cell for the calculation of the  final states. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.nkpt'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.ngkpt
            help =  ' Number of k-points in each direction used to sample the cell for  the ground-state calculation of the density. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.ngkpt'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.nbands
            help =  ' Number of bands for the final state calculations. This includes valence and conduction bands. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.nbands'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.screen.nbands
            help =  ' Number of bands to use for the screening calculations. This requires a large  number of bands. Should be about 100eV above the Fermi level, but convergence  should be checked. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.screen.nbands'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.occopt
            help =  ' Controls determination of occupation. Most important  values are:  1 - States are all doubly degenerate and either occupied or empty depending on band.  3 - States are all doubly degenerate but can have fractional occupations      depending on Fermi function. Suitable for metals. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.occopt'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.fband
            help =  ' Determines the number of occupied bands to be included in the SCF calculation  of the density. For insulators the default (fband = 0.125) is fine, but  for metals the highest band the in the density calculation should have no  occupation weight. Using fband, the number of bands is determined by  n = natom*fband. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.fband'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.toldfe
            help =  ' Total energy convergence parameter for the density run. Default is 10^(-6) '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.toldfe'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.tolwfr
            help =  ' Convergence criterium for the non-scf wave-function calculations.  Default is 10^(-16) '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.tolwfr'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.nstep
            help =  ' Maximum number of iterations for the DFT SCF calculations. Default is 50 '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.nstep'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.screen.nkpt
            help =  ' Number of k-point to be used for the screening calculations. Default is 2 2 2,  and is sufficient for a wide variety of systems, although very small unit  cells might require more, and large unit cells may only require gamma point. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.screen.nkpt'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.abpad
            help =  ' For the calculation of the final state wavefunctions, the convergence of the  highest bands can be very slow. The calculation can be sped up by adding some  throwaway bands at teh top. These bands are not considered when checking for convergence. ocean.abpad adds bands to the calculation. Only used for abinit. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.abpad'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.dft_energy_range
            help =  ' Instead of setting the number of bands (ocean.nbands) the user may request  an energy range in eV for the final state wave-functions. This is an estimate  using the volume of the unit cell and may be unreliable. Default is 25 eV. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.dft_energy_range'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.screen_energy_range
            help =  ' Instead of setting number of bands for the screening, the user may request  an energy range in eV. This is only an estimate, and may need to be converged. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.screen_energy_range'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.k0
            help =  ' DFT states are calculated using a shifted k-point grid. The first k-point is  given by:    1/(N_k(1)*k0(1)), 1/(N_k(2)*k0(2), 1/(N_k(3)*k0(3)  where N_k is given by ocean.nkpt. The default shift is k0 = 1/8, 2/8, 3/8. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.k0'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.degauss
            help =  ' Broadening for the smearing function in Ryd. for metallic occupations in the  DFT calculations. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.degauss'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.opf.program
            help =  ' Use oncvpsp UPS pseudopotentials with qe '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.opf.program'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.opf.fill
            help =  ' atomic number followed by the name of the .fill file to use for this calculation. '
            kinds =  [[inp_int, inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.opf.fill'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.opf.opts
            help =  ' atomic number followed by the name of the .opts file to use for this calculation. '
            kinds =  [[inp_int, inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.opf.opts'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.edges
            help =  ' Specify the atoms and edges to calculate. Each edge entry consists of 3  integers. The first, if greater than zero, is the index of the atom for  which the edge should be calculated. The second and third numbers are the  principle quantum number and angular momentum.  \'1 2 1\' denotes the L edges of the first atom  If the first number is negative, then it is interpreted as -Z, where  Z is the atomic number, and in that case edges of all atoms with that  atomic number will be calculated.  \'-22 2 1\' will run the L edges of every titanium atom in the cell. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = True


            self['ocean.edges'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.screen.shells
            help =  ' The screening calculation is RPA at small radius and a model at large radius.  Teh cross-over between the RPA and model is set by shells in Bohr.  Several different radii can be chosen to look at the convergence.  Convergence is usually reached at arount 3-4 Bohr. The supercell defined by  ocean.paw.nkpt must have dimensions larger than the radius specified by  ocean.screen.shells or results may be unreliable. The default of 3.5 Bohr is  usually OK. Values > 6 Bohr should not be used. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.screen.shells'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.rad
            help =  ' One of the screening radius as defined by ocean.screen.shells that will be  used in the BSE calculation. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.rad'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.scfac
            help =  ' The is the Slater integral factor to scale the slater integrals. For 3d  transition metals 0.8 is a reasonable value, while 0.6 is better for  f-electron atoms. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.scfac'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.core_offset
            help =  ' If true, core-level shift will be calculated, false, no shift, or a number  to specify the shift by hand. '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.core_offset'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.opf.hfkgrid
            help =  ' The first parameter sets the grid for hfk.x, and should be left at 2000.  The second determines the maximum number of proejectors per angular momentum  channel. The default of 20 will work for many calculations. '
            kinds =  [[inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.opf.hfkgrid'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.xmesh
            help =  ' Wave-functions are converted into the NIST BSE format and condensed onto a  grid of size ocean.cnbse.xmesh. Default is guessed in the code. '
            kinds =  [[inp_int, inp_int, inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.xmesh'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.mode
            help =  ' Which spectroscopy to calculate: "XAS", "XES"  NRIXS and XRS are treated the same as XAS. '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.mode'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.niter
            help =  ' Number of Haydock iterations. Default is 100. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.niter'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.metal
            help =  ' If True, the code will complain unless occopt is 3. If False, the codes  expects occopt = 1. '
            kinds =  [[inp_bool]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.metal'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.spin-orbit
            help =  ' If ocean.spin-orbit >= 0, the code will not automatically calculate the  spin-orbit splitting. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.spin-orbit'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.photon_q
            help =  ' For UV/VIS and RIXS calculations, the valence and conduction band states  must be offset from each other (by the momentum that is absorbed or  transferred). This sets that momentum offset in units of the reciprocal  lattice vectors of the system. Default is 0 0 0. '
            kinds =  [[inp_float, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.photon_q'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.strength
            help =  ' Sets the strength for the two interaction terms in the BSE Hamiltonian.  Default is 1, and for emission 0. This can be changed for analysis. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.strength'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.solver
            help =  ' Choose between Haydock algorithm (full spectrum, no excitons) or GMRES  (single energy, exciton density). '
            kinds =  [[inp_str]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.solver'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.gmres.elist
            help =  ' List of energies at which to run the GMRES algorithm in eV. Lowest  unoccupied state is set at zero without the core-hole. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = True
            lexpandable = False


            self['ocean.cnbse.gmres.elist'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.gmres.erange
            help =  ' Use energies at with even spacing specified by  emin emax estep '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.gmres.erange'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.gmres.nloop
            help =  ' Restart GMRES algorithm will restart if the subspace grows to size nloop. '
            kinds =  [[inp_int]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.gmres.nloop'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.gmres.gprc
            help =  ' Set Lorenzian broadening in Hartree in the GMRES algorithm when  pre-conditioning. Default is 0.5, which should be reasonable for K edges. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.gmres.gprc'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.gmres.ffff
            help =  ' Sets convergence criterion for GMRES. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.gmres.ffff'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.broaden
            help =  ' Half? width of broadening in eV for the spectrum. Must be larger than zero.  Suggested value is the core-hole broadening. '
            kinds =  [[inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.broaden'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)


            #  ocean.cnbse.spect_range
            help =  ' Sets energies over which the spectrum will be calculated.  nsteps emin emax '
            kinds =  [[inp_int, inp_float, inp_float]]
            code =  'ocean'
            importance = 'IMPORTANTCE'
            category = 'NONE'
            field_labels = 'NONE'
            ranges = None
            defaults = None
            field_types = None
            fexpandable = False
            lexpandable = False


            self['ocean.cnbse.spect_range'] = self._fill_key_info(help,kinds,
                            code,importance,category,field_labels,ranges, defaults,
                            field_types,fexpandable,lexpandable)
