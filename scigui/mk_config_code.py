import scigui.readconfig
inp_dict = readconfig.read_config_file()

def flatten(xss):
    return [x for xs in xss for x in xs]

def getkinds(kinds,defaults):
    new_kinds = []
    new_defaults = []
    fexpandable = False
    lexpandable = False
    id = 0
    for k_line in kinds:
        new_k_line = []
        new_d_line = []
        for k in k_line:
            if k != '...':
               new_k_line = new_k_line + [k]
            else:
               if len(k_line) > 1:
                  fexpandable = True
               else:
                  lexpandable = True
        new_d_line = defaults[id][0:len(new_k_line)]
        if len(new_k_line) != 0:
           new_kinds = new_kinds + [new_k_line]
        if len(new_d_line) != 0:
           new_defaults = new_defaults + [new_d_line]
        print(defaults)
        print(new_defaults)
    return new_kinds,new_defaults,fexpandable,lexpandable


with open('tmp.config', 'w') as f:
        for key,keydict in inp_dict.items():
            print('# ', key, file=f)
            print('help = ',"'",' '.join(keydict['help']).strip(),"'",file=f)
            kinds,defaults,fexpandable,lexpandable = getkinds(keydict['kinds'],keydict['defaults'])
            print('kinds = ',kinds,file=f)
            if '.' in key:
                print('code = ', "'"+key.split('.')[0].strip()+"'",file=f)
            else:
                print('code = ', "'general'",file=f)
            print("importance = 'IMPORTANTCE'",file=f)
            print("category = 'NONE'",file=f)
            print("field_labels = 'NONE'",file=f)
            print("ranges = None",file=f)
            if all(d is None for d in flatten(defaults)):
                print("defaults = None",file=f)
            else:
                print("defaults =",defaults,file=f)
 
            print("field_types = None",file=f)
            print("fexpandable =",fexpandable,file=f)
            print("lexpandable =",lexpandable,file=f)
            print("\n",file=f)
            print("corvus_input_keys['" + key + """'] = fill_key_info(help,kinds,
                   code,importance,category,field_labels,ranges, defaults,
                   field_types,fexpandable,lexpandable)""",file=f)
            print("\n",file=f)

