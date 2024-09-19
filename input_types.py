from pathlib import Path
import input_errors as ie


# Define some overloaded classes for validation of input dictionaries.
class inp_str(str):
    def __new__(cls, s):
        instance = super().__new__(cls, s.strip())
        return instance


    def validate(self,range=None):
        ie.error = False
        if len(self.split()) != 1:
            ie.error = True
            ie.error_message = 'String fields should have only one word.'

        return not ie.error


class inp_paragraph(str):
    def __new__(cls,s):
        instance = super().__new__(cls,s.strip())
        return instance

    def validate(self,range=None):
        return True

class inp_file_name(str):
    def __new__(cls,s):
        instance = super().__new__(cls,str(Path(s.strip()).absolute()))
        
        return instance

    def validate(self,range=None):
        ie.error = False
        if not Path(self).is_file():
            ie.error = True
            ie.error_message = str(self) + ' is not an existing file.'
        return not ie.error
    
class inp_structure_file(str):
    def __new__(cls,s):
        instance = super().__new__(cls,str(Path(s.strip()).absolute()))
        
        return instance

    def validate(self,range=None):
        ie.error = False
        if not Path(self).is_file():
            ie.error = True
            ie.error_message = str(self) + ' is not an existing file.'
        return not ie.error

class inp_bool(str):
    def __new__(cls,b):

        b2 = b.strip()
        if b2.upper() in ['TRUE','T','.TRUE.']:
            instance = super().__new__(cls,'True')
        elif b2.upper() in ['FALSE','F','.FALSE.']:
            instance = super().__new__(cls,'')
        else:
            ie.error_message = 'Boolean types must be given as true, t, .true., false, f, or .false (case insensitive)'
            ie.error = True
            instance = super().__new__(cls,b2)
            return None

        return instance

    def validate(self,range=None):
        # String
        ie.error = False
        if self not in ['','True']:
            ie.error = True
            ie.error_message = 'Logical flags should be true, t, .true., false, f, or .false'
        return not ie.error

class inp_choice(str):
    def __new__(cls,s):
        instance = super().__new__(cls,s.strip())
        return instance

    def validate(self,range=None):
        ie.error = False
        if self not in range.split(','):
            ie.error = True
            ie.error_message = 'Invalid option. Must be one of of the values: ' + range
        print(ie.error,ie.error_message)
        return not ie.error

class inp_float(float):
    def __new__(cls,f):
        ie.error = False
        try:
            instance = super().__new__(cls,float(f))
            return instance
        except:
            ie.error = True
            ie.error_message = 'Invalid value for float type input: ' + str(f)
            return None

    def validate(self,range=None):
        #print('inside inp_float validate:',self,range)
        #print('validating float:')
        #print('range: ',range)
        #print('self: ',self)
        ie.error = False
        if self is None:
            ie.error = True
            ie.error_message = 'Invalid value for float type input: ' + str(self)
            #print('self is None.')
            return not ie.error
        if range is not None:
            r = range.split(',')
            if not r[0]: # first part is empty, only has max val
                ie.error = float(r[1]) < self
                ie.error_message = 'Value must be <= ' + r[1]
            elif not r[1]:
                #print(float(r[0]),self)
                ie.error = float(r[0]) > self
                ie.error_message = 'Value must be >= ' + r[0]
            else:
                ie.error = (float(r[0]) > self) or (self > float(r[1]))
                ie.error_message = 'Value must be in range (' + r[0] + ',' + r[1] + ')'
            #print(ie.error_message)
            #print('invalid range', ie.error_message)
        return not ie.error

class inp_int(int):
    def __new__(cls,i):
        try:
            instance = super().__new__(cls,int(i))
            return instance
        except:
            ie.error = True
            ie.error_message = 'Invalid value for int type input: ' + str(i)
            return None

    def validate(self,range=None):
        ie.error = False
        if not isinstance(self,int):
            ie.error = True
            ie.error_message = 'Invalid value for int type input: ' + str(self)
        if range is not None:
            r = range.split(',')
            if not r[0]: # first part is empty, only has max val
                ie.error = (int(r[1]) >= self)
                ie.error_message = 'Value must be <= ' + r[1]
            elif not r[1]:
                
                
                ie.error = not (int(r[0]) <= self)
                ie.error_message = 'Value must be >= ' + r[0]
            else:
                ie.error = not (int(r[0]) <= self) and (self <= int(r[1]))
                ie.error_message = 'Value must be in range (' + r[0] + ',' + r[1] + ')'

        return not ie.error
