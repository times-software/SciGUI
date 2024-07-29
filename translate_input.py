import re
import input_definition
import input_errors


# Define an text_input class. 
class input_dict(dict):

    def __init__(self,input_type):
        self.update({'_input_type': input_type})

    @classmethod
    def from_file(cls,infile,input_type):
        inp_dict = cls(input_type)
        inp_dict.read_text_input(infile)
        return inp_dict

    def read_text_input(self,infile):
        try:
            input_type = self['_input_type']
        except:
            print('Error: \'_input_type\' not defined in input definition dictionary.')
            exit()

        #inp_def = corvus_keys_dict.input_definition_dict('corvus')
        reader_function = read_corvus_input
        inp_dict, is_valid, error_message = reader_function(infile)
        self.update(inp_dict)
        return is_valid, error_message



    def write_text_input(self,outfile):
        try:
            input_type = self['_input_type']
        except:
            print('Error: \'_input_type\' not defined in input definition dictionary.')
            exit()
        writer_function = write_corvus_input
        writer_function(self,outfile)
# We should have other types of input readers and writers as well. 
# Reads a corvus input file and returns a dictionary: keyword -> list(list())
def read_corvus_input(file):
   # Get the input_definition dictionary.
   inp_def = input_definition.input_definition_dict('corvus')
   # Get full string of file text.
   with open(file) as f:
      lines = f.readlines()

   # Remove lines that start with # (comments)
   lines2 = []
   for l in lines:
      if '#' in l:
         # Ignore comments.
         l2 = l.split('#')[0].strip()
      else:
         l2 = l.strip()

      if len(l2) > 0:
         lines2 = lines2 + [l2]

   # Combine all lines into a single string.
   clean_str = '\n'.join(lines2)
   #print(clean_str)
   # Find keywords. First one at beginning, all others between } {
   key_list = list(filter(None,re.split(',|\{|\}',clean_str)[0:-1]))
   #print(key_list)
   inp_dict = {}
   ik = 0
   #print(key_list)
   is_valid = True
   message =  ''
   while ik < len(key_list):
      key = key_list[ik].replace('\n','')
      #print(inp_def[key]['kinds'][0][0].__name__)
      if inp_def.inp_def_dict[key]['kinds'][0][0].__name__ == 'inp_paragraph':
         # If this is a paragraph type, we need a list of lists. Each inner list
         # is a single string holding an entire line of text.
         is_valid = True
         message = ''
         inp_dict[key] = [list(filter(None,key_list[ik+1].split('\n')))]
      else:
         # This is not a paragraph, interpret each separate word as a field.
         inp_key_vals = [v.split() for v in list(filter(None,key_list[ik+1].split('\n')))]
         print('inp_key_vals',inp_key_vals)
         inp_dict[key],is_valid,message = cast_input_key_vals(inp_key_vals,key,inp_def.inp_def_dict)

      if not is_valid:
         return inp_dict, is_valid, message
      ik += 2

   return inp_dict, is_valid, message

# Cast string values to the correct types, validating as we go.
# returns - new_values, is_valid, error_message
def cast_input_key_vals(vals,key,inp_dict):
   #print('##############')
   #print(key,val)
   #print('##############')
   #print()
   # Set up a new list to hold the casted values.
   new_vals = []
   # Skip input type key
   if key == '_input_type': 
       # Make sure that this is a one word input.
       if len(vals) > 1:
         message = '_input_type must be a single word.'
         error = True
         new_vals = val
         return new_vals, False, message

   # First check that key exists in input definition dictionary.
   if key not in inp_dict:
         message='Unrecognized keyword in input:' + key
         new_vals = vals 
         return new_vals, False, message
   
   # Now check that each value in this set has the correct kind and ranges.
   il = 0
   for val_line in vals:
         if il > len(inp_dict[key]['kinds'])-1:
            if not inp_dict[key]['lexpandable']:
               message = ('Too many lines defined in input for keyword: ' + key + 
               '. Should be ' + str(len(inp_dict[key]['kinds'])) + ' lines of input.')
               return vals, False, message
            
         # If this is line expandable, we want to use the last line of kinds defined.
         iline = min(il,len(inp_dict[key]['kinds'])-1)

         # Now loop over the fields
         iv = 0
         new_val_line = []
         for v in val_line:
            # Check if there are more fields than those defined.
            if iv > len(inp_dict[key]['kinds'][iline]):
               if not inp_dict[key]['fexpandable']:
                     message = ('Too many fields defined in input for keyword: ' + key +
                     '. Should be ' + str(len(inp_dict[key]['kinds'][iline])) + ' fields.')
                     return vals, False, message

            # If this is an expandable number of fields, we want to use the last kind defined.
            ival = min(iv,len(inp_dict[key]['kinds'][iline])-1)

            # Cast the string to the correct input type, then validate it.
            print(key,inp_dict[key]['kinds'][iline][ival])
            new_val = inp_dict[key]['kinds'][iline][ival](v)
            if input_errors.error: 
               message = input_errors.error_message
               input_errors.error_message = 'Incorrect type in field #' + str(iv+1) + ' of keyword: ' + key + \
                                   '. ' + message
            
            print(key,inp_dict[key]['ranges'])
            print('new_val=',new_val,v)
            if inp_dict[key]['ranges'] is not None:
               print(key,inp_dict[key]['ranges'])
               # If ranges exist for this keyword, check that input value is in range.
               # List of ranges can be shorter than list of fields or list of kinds. Use
               # last defined ranges element to check ranges.
               iliner = min(il,len(inp_dict[key]['ranges'])-1)
               ivalr = min(iv,len(inp_dict[key]['ranges'][iliner])-1)
               is_valid = new_val.validate(inp_dict[key]['ranges'][iliner][ivalr])
               if not is_valid:
                     message = ('Incorrect type or range for field #' + str(iv+1) + ' associated with the ' +
                     'keyword: ' + key + '. ' + input_errors.error_message)
                     return vals, False, message
            else:
               # No ranges were defined for this keyword.
               #print(new_val,new_val.validate(None))
               if not new_val.validate(None):
                     message = ('Incorrect type for field #' + str(iv+1) + ' associated with the ' +
                     'keyword: ' + key + '. ' + input_errors.error_message)
                     return vals, False, message
               
            new_val_line = new_val_line + [new_val]
            iv += 1
         
         new_vals = new_vals + [new_val_line]
         il += 1

   # no errors.
   return new_vals, True, 'valid'

def write_corvus_input(values_dict,file):
   print('values_dict',values_dict)
   with open(file,"w") as inp_file:
      for key,lines in values_dict.items():
         print(key,lines)
         inp_file.write(key)
         inp_file.write('{\n')
         for line in lines:
            str_line = ' '.join([str(v) for v in line])
            inp_file.write(str_line + '\n')

         inp_file.write('}\n') 
