import wx
import wx.richtext
import wx.lib.scrolledpanel
import scigui.input_errors as ie
from scigui.input_types import *
import scigui.input_element as input_element


"""key_ui_elem is an object that holds all ui elements associated with a single keyword.
    Each keyword has a toggle button, and option widgets. The option widgets will be shown if
    the toggle button is pressed. 
    key_dict holds the information needed to know what ui elements are required."""
class key_ui_elem():
    def __init__(self,keyword,key_dict,panel1, panel2, min_size=None):
        # Add the key toggle button.
        #print(keyword)
        self.keyword = keyword
        self.min_size = min_size
        self.key_dict = key_dict
        self.required = key_dict['required']
        # Get the number of required fields and lines
        n_line = 0
        self.n_required_fields = []
        for kind_line in self.key_dict['kinds']:
            n_line += n_line
            n_field = 0
            for kind in kind_line:
                n_field += 1
            self.n_required_fields = self.n_required_fields + [n_field]

        self.panel1 = panel1
        #print(wx.ColourDatabase().Find('DARK SLATE GREY'))
        self.panel2 = panel2
        #if keyword == 'feff.fms': 
        #    print(key_dict['help'])
        #    print('\n'.join(key_dict['help']))

        self.panel1_sizer = panel1.GetSizer()
        self.panel2_sizer = panel2.GetSizer()
        self.key_toggle_window = wx.Panel(self.panel1,style=wx.BORDER_NONE)
        self.key_toggle_window.Bind(wx.EVT_SYS_COLOUR_CHANGED, self.OnColourChanged)
        #if self.key_toggle_window.CanSetTransparent:
        #    self.key_toggle_window.SetTransparent(50)
        #self.panel1_sizer.Add(self.key_toggle_window,0,wx.ALIGN_LEFT|wx.LEFT,5)
        self.panel1_sizer.Add(self.key_toggle_window,proportion = 0, flag=wx.ALIGN_LEFT|wx.TOP|wx.LEFT,border=5)
        self.key_toggle_sizer = wx.BoxSizer(wx.VERTICAL)
        self.key_toggle = wx.ToggleButton(self.key_toggle_window, label=keyword)
        #self.key_toggle_sizer.Add(self.key_toggle,0,wx.ALL,0)
        self.key_toggle_sizer.Add(self.key_toggle,proportion = 0,flag=wx.ALL,border=2)
        self.key_toggle_window.SetSizer(self.key_toggle_sizer)
        #self.panel1_sizer.Add(self.key_toggle,0,wx.ALIGN_LEFT|wx.ALL,5)
        
        # Add the help text to the key_sizer next.
        self.help_text = keyword.strip() + '\n' + '\n'.join(key_dict['help'])
        self.help_text_ui = wx.richtext.RichTextCtrl(panel2,value=self.help_text,
                       style=wx.ALIGN_LEFT|wx.TE_WORDWRAP|wx.TE_MULTILINE|wx.TE_READONLY|wx.BORDER_SIMPLE)
        #self.help_text_ui.Enable(False)
        # Make the text wrap at the edge of the right side panel. 
        #help_text.Wrap(self.splitter_window.GetWindow1().GetSize()[1])
        self.panel2_sizer.Add(self.help_text_ui,1,wx.ALL|wx.ALIGN_LEFT|wx.EXPAND,10)
        self.help_text_ui.Bind(wx.EVT_KEY_DOWN,self.on_key_down)

        # In the right window, add a vertical sizer which will contain the help text, 
        # then all of the lines of input for this keyword. 
        self.key_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel2_sizer.Add(self.key_sizer,1,wx.ALL|wx.EXPAND,0)
        

        # Make a checkbox to use this input:
        self.enable_checkbox = wx.CheckBox(panel2, label="Enable:",name=keyword)
        self.key_sizer.Add(self.enable_checkbox,0,wx.LEFT|wx.TOP|wx.ALIGN_LEFT,15)
        self.enable_checkbox.Bind(wx.EVT_CHECKBOX,self.enable_keyword)
        
        # Get labels for this keyword.
        labels = key_dict['field_labels']

        # Loop over different kinds of input for this keyword for each line (row).
        # kinds is a list of lis
        # ts, so loop over outer and inner.
        i_line = 0
        self.ui_elems = []
        self.kinds = []
        self.par_sizers = []
        self.defaults = []
        #print('key_ranges=',key_dict['ranges'])

        for kind_line in key_dict["kinds"]:
            # label_sizer = None
            # # Set the labels for this line. 
            # labels = self.set_labels(i_line,key_dict)
            # if labels is not None:
            #     label_sizer = wx.BoxSizer(wx.HORIZONTAL)
            #     # Now add a static text for each label
            #     if len(labels) > 1:
            #         for label in labels:
            #             if label is not None:
            #                 lbl = wx.StaticText(panel2, label = label,style=wx.ALIGN_LEFT)
            #                 label_sizer.Add(lbl,1,wx.LEFT,20)
            #     else:
            #         # Use same label for all elements
            #         if labels[0] is not None:
            #             for i,k in enumerate(kind_line):
            #               lbl = wx.StaticText(panel2, label =labels[0],style=wx.ALIGN_LEFT)
                
            #     if label_sizer is not None: self.key_sizer.Add(label_sizer,0,wx.ALL|wx.EXPAND,10)

            # Get the ranges if any.
            if key_dict['ranges'] is not None:
                # Gets the last defined line of ranges
                range_line = key_dict['ranges'][min(i_line,len(key_dict['ranges'])-1)]
            else:
                range_line = None

            # Get the defaults if any.
            if key_dict["defaults"] is not None:
                default_line = key_dict["defaults"][i_line]
            else:
                default_line = None

            if labels is None:
                if i_line == 0:
                    label_line = [' ']
                else:
                    label_line = None
            elif len(labels) == 1:
                # Only one line. 
                if i_line == 0:
                    label_line = labels[0]
                else:
                    label_line = None
            else:
                # Multiple lines.
                label_line = labels[i_line]

            # Set the input handlers to use for this line of kinds (data types).
            par_sz,ui_elems = self.get_input_handler_row(kind_line,default_line,keyword,
                                                         ranges = range_line,min_size = min_size, labels = label_line)
            #self.key_sizer.Add(par_sz,0,wx.ALL|wx.EXPAND,2)
            self.key_sizer.Add(par_sz,0,wx.ALL|wx.EXPAND,2)
            self.par_sizers = self.par_sizers + [par_sz]
            self.ui_elems = self.ui_elems + [ui_elems]
            self.defaults = self.defaults + [default_line]
            self.kinds = self.kinds + [kind_line]

            i_line += 1

        # If this keyword is field or line expandable, add an extra par_sizer
        if key_dict['fexpandable'] or key_dict['lexpandable']:
            par_sz = wx.BoxSizer(wx.HORIZONTAL)
            self.expander_sizer = par_sz
            self.key_sizer.Add(par_sz,0,wx.ALL|wx.EXPAND,10)

            # If this keyword is field expandable, create an "Add row" button.
            if key_dict['lexpandable']:
                self.row_button = wx.Button(self.panel2,label='Add Row',name=keyword)
                self.row_button.Bind(wx.EVT_BUTTON,self.add_ui_row)
                self.row_button.Disable()
                par_sz.Add(self.row_button,0,wx.LEFT,20)

            # If this keyword is field expandable, create an "Add Colunn" button.
            if key_dict['fexpandable']:
                self.column_button = wx.Button(self.panel2,label='Add Column',name=keyword)
                self.column_button.Bind(wx.EVT_BUTTON,self.add_ui_column)
                self.column_button.Disable()
                par_sz.Add(self.column_button,0,wx.LEFT,20)

        # At start, no keyword options are shown.
        #self.panel2_sizer.Hide(self.key_sizer)

    def on_key_down(self,evt):
        pass

    def Reset(self):
        self.enable_checkbox.SetValue(False)
        self.enable_keyword_elements(False)
        for ui_line in self.ui_elems:
                for uie in ui_line:
                    uie.Reset()
        

         

    def set_labels(self,iline,key_dict):
        if key_dict['field_labels'] is None: return None
        # Get the number of lines in the field_labels list.
        nlines = len(key_dict['field_labels'])
        if nlines == 1:
            if iline == 0:
                labels = key_dict['field_labels'][0]
            else:
                labels = None
        else:
            labels = key_dict['field_labels'][iline]

        return labels
                 
    
    def get_input_handler_row(self,kind_line,default_line,name_lbl,ranges = None, min_size=None,labels = None):
        # Make a new sizer for this row.
        par_sz = wx.BoxSizer(wx.HORIZONTAL)
        #print('ranges=',ranges)
        #print(self.keyword)
        #print('outside labels=',labels)
        #print(kind_line)
        # Loop over data types (kinds) in this line and add a widget for each.
        i_field = 0
        #print(default_line,kind_line,len(kind_line),name_lbl)
        ui_elems = []
        for kind in kind_line:
            if kind != '...':
                if default_line is not None:
                    default = default_line[i_field]
                else:
                    default = None
            else:
                default = None
            if ranges is not None:
                rng = ranges[min(i_field,len(ranges)-1)]
            else:
                rng = None

            if labels is None:
                label = ' '
            elif len(labels) == 1:
                # Single label only.
                label = labels[0]
            else:
                #print(i_field,labels)
                label = labels[i_field]

            #inp_elem = self.get_input_handler_field(kind,default,name_lbl,range = rng,min_size = min_size)
            inp_elem = input_element.input_element(self.panel2, kind, name_lbl = name_lbl, label = label, min_size = min_size, default = default, range = rng)
            inp_elem.Enable(self.enable_checkbox.GetValue())

            par_sz.Add(inp_elem.sizer,0,wx.LEFT|wx.ALIGN_LEFT,10)
            ui_elems = ui_elems + [inp_elem]
            
            i_field += 1
        return par_sz, ui_elems
    
    """
    get_input_haldler_field:
    Creates a new widget according to data type held in kind. kind_len is the number
    of fields in the row that this is associated with. name_lbl will be used to name
    the widget.
    Returns: widget (wx.Window)
    ! NOT USED ANYMORE. NOW USE input_element class.
    """
    def get_input_handler_field(self,kind,default,name_lbl,range = None, min_size=None):
        #print(name_lbl,kind.__name__)
        min_size2 = min_size
        if kind.__name__ == 'inp_float':
            # Float input
            
            if default is not None:
                try:
                    val = float(default)
                except:
                    print('Wrong default or kind for keyword: ', name_lbl, ' in config file.')
                    print('Should be float.')
                inp_elem = wx.TextCtrl(self.panel2,value=default,name=name_lbl)
                #inp_elem = wx.lib.agw.floatspin.FloatTextCtrl(panel,name=name_lbl)
            else:
                inp_elem = wx.TextCtrl(self.panel2,name=name_lbl)
                #inp_elem = wx.lib.agw.floatspin.FloatTextCtrl(panel,name=name_lbl)
            #inp_elem.Bind(wx.EVT_KILL_FOCUS,self.validate_float)
            inp_elem.Bind(wx.EVT_KEY_UP, lambda event: self.validate_float(event, range))
            inp_elem.Bind(wx.EVT_CHAR,self.validate_float_chars)
        elif kind.__name__ == 'inp_int':
            # Integer input. Add spin control
            if default is not None:
                try:
                    val = int(default)
                except:
                    print('Wrong default or kind for keyword: ', name_lbl, ' in config file.')
                    print('Should be integer.')
                inp_elem = wx.SpinCtrl(self.panel2,min=-100, max=100, initial=val,name=name_lbl)
            else:
                inp_elem = wx.SpinCtrl(self.panel2,min=-100, max=100, initial=0,name=name_lbl)
        elif kind.__name__ == 'inp_bool':
            # Logical input
            if default is not None:
                if default == "True":
                    val = True
                elif default == "False":
                    val = False
                else:
                    print('Wrong default or kind for keyword: ', name_lbl, ' in config file.')
                    print('Should be integer.')
                    exit()
            else:
                val = False
            
            if val:
                lbl = "True"
            else:
                lbl = "False"

            inp_elem = wx.ToggleButton(self.panel2,label=lbl,name=name_lbl)
            inp_elem.SetValue(val)
            inp_elem.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleButtonLabel)
            
        elif kind.__name__ == 'inp_str': 
            # String input
            if default is not None:
                inp_elem = wx.TextCtrl(self.panel2,value=default,name=name_lbl)
            else:
                inp_elem = wx.TextCtrl(self.panel2,name=name_lbl)
        elif kind.__name__ == 'inp_paragraph':
            # Paragraph?
            if default is not None:
                inp_elem = wx.TextCtrl(self.panel2,value=default,name=name_lbl,style=wx.TE_MULTILINE|wx.HSCROLL)
            else:
                inp_elem = wx.TextCtrl(self.panel2,name=name_lbl,style=wx.TE_MULTILINE|wx.HSCROLL)
        elif kind.__name__ == 'inp_file_name':
            inp_elem = wx.FilePickerCtrl(self.panel2, name = name_lbl)
            min_size2 = (min_size[0]*2,min_size[1])
        elif kind.__name__ == 'inp_choice':
            #print('range=',range)
            #exit()
            inp_elem = wx.Choice(self.panel2,name = name_lbl, choices = [''] + range.split(','))
        else:
            ie.error_message = 'Invalid type in input_types.py: ' + kind.__name__
            ie.input_error = True
            ie.error_type = 'fatal'
    
        if min_size2 is not None:
            inp_elem.SetMinSize(min_size2)
            

        return inp_elem
   
    
    def OnColourChanged(self,evt):
        obj = evt.GetEventObject()
        col = obj.GetBackgroundColour()
        if col[3] == 255:
            new_col = (col[0],col[1],col[2],50)
        else:
            new_col = (col[0],col[1],col[2],255)
        obj.SetBackgroundColour(new_col)

    def validate_key_values(self,evt=None): 
        # Compare number of non-empty fields with required number of fields 
        # for each line. 
        #    1. If element is field expandable, we can have empty
        #       fields beyond the last required field.
        #    2. If element is line expandable, we can have empty
        #       lines beyond the last required line, but lines cannot
        #       be partially empty.
        if not self.enable_checkbox.GetValue():
            return True, ''

        values = []
        nrf = []
        message = "Unfilled required fields found in input for this keyword.\n" \
                + "Please disable this keyword or fill the empty fields."
        i_line_max = len(self.n_required_fields) - 1
        for ui_line in self.ui_elems:
            val_line = []
            n_fields = 0
            for elem in ui_line:
                elem
                v = elem.GetValue()
                # Empty strings will not be included in the output.
                # Need to add a "validate keyword" that checks that all
                # required fields are filled.
                if str(v):
                    val_line = val_line + [v]
                    n_fields = n_fields + 1
                else:
                    break # ignore any fields past the first empty one.

            if val_line:
                values = values + [val_line]
                nrf = nrf + [n_fields]
                ind = min(len(self.n_required_fields)-1,len(nrf)-1)
                if self.key_dict['fexpandable']:
                    if n_fields < self.n_required_fields[ind]:
                        return False,message
                else:
                    if n_fields != self.n_required_fields[ind]:
                        return False,message
            else:
                break # ignore any lines past the first empty one

        # Check that number of lines is same as number of required lines,
        # or >= if keyword_ui is line expandable.
        #print(nrf,self.n_required_fields)
        if self.key_dict['lexpandable']:
            if len(nrf) < len(self.n_required_fields):
               return False,message
        else:
            if len(nrf) != len(self.n_required_fields):
               return False,message

        return True, ''

    def get_values(self):
        # This is easy. We can assume that the types of non-empty fields is
        # correct, but need to validate that no required fields are empty.
        # No need to validate anything.
        values = []
        for ui_line in self.ui_elems:
            val_line = []
            for elem in ui_line:
                v = elem.GetValue()
                # Empty strings will not be included in the output.
                # Need to add a "validate keyword" that checks that all
                # required fields are filled.
                if str(v):
                    val_line = val_line + [v]
            if val_line:
                values = values + [val_line]

        return values
    
    def set_values(self,values):
        # set_values will be used when opening an input file to set the values of the 
        # ui fields. They should already be validated and type cast, and checked for 
        # the appropriate number of fields.
        # Enable this keyword
        self.enable_checkbox.SetValue(True)
        self.enable_keyword_elements(True)

        # Now go line by line, setting values, and adding new fields/lines as needed.
        iline = 0
        #print(self.kinds)
        for value_line in values:
            ifield = 0
            if len(self.kinds)-1 < iline:
                # Create a new line for these fields
                self.add_ui_row()
            for value in value_line:
                if len(self.kinds[iline])-1 < ifield:
                    self.add_ui_column()
                
                inp_type = type(self.ui_elems[iline][ifield].GetValue())
                self.ui_elems[iline][ifield].SetValue(inp_type(value))
                ifield += 1
            iline += 1

    def enable_keyword_elements(self,val):
        for ui_line in self.ui_elems:
            for element in ui_line:
                element.Enable(val) 

        if hasattr(self,"column_button"):
            self.column_button.Enable()
        if hasattr(self,"row_button"):
            self.row_button.Enable()
    
    def ShowItems(self,val,layout=True):
        #self.help_text_ui.Wrap(int(self.panel2.GetSize().width - 10))
        self.help_text_ui.Show(val)
        self.key_sizer.ShowItems(val)
        for ui_elem_line in self.ui_elems:
            for ui_elem in ui_elem_line:
                ui_elem.Show(val)
        #self.panel2_sizer.Layout()
        if layout: self.do_layout(self.panel2)
    
    def Highlight(self,col):
        self.key_toggle_window.SetOwnForegroundColour(col)



    ################################################################################
    #      EVENT PROCESSING FOR key_ui_elem class
    ################################################################################
             
    def add_ui_column(self,evt=None,layout=True):
        # Insert a new field at the end of each line of ui_elements
        irow = 0
        while irow <= len(self.par_sizers)-1:
            # Make a copy of the last field
            kind = self.kinds[min(irow,len(self.kinds)-1)][-1]
            
            if self.key_dict['ranges'] is not None:
                #print(irow)
                rng = self.key_dict['ranges'][irow][-1]
                self.key_dict['ranges'][irow] = self.key_dict['ranges'][irow] + [rng]
            else:
                rng = None

            if self.key_dict["defaults"] is not None:
                default = key_dict["defaults"][irow][-1]
                self.key_dict['defaults'][irow] = self.key_dict['defaults'][irow] + [default]
            else:
                default = None
                

            inp_elem = input_element.input_element(self.panel2,kind,default = default,name_lbl = self.keyword,range = rng)
            is_enabled = self.enable_checkbox.GetValue()
            inp_elem.Enable(is_enabled)
            self.par_sizers[irow].Add(inp_elem.sizer,0,wx.LEFT|wx.ALIGN_LEFT,10)
            self.ui_elems[irow] = self.ui_elems[irow] + [inp_elem]
            self.kinds[irow] = self.kinds[irow] + [kind]
            irow += 1
        #self.panel2_sizer.Layout()
        self.panel2.SetVirtualSize(self.panel2_sizer.GetMinSize())
        if layout: self.do_layout(self.panel2)


    def add_ui_row(self,evt=None,layout=False):
        # Set the input handlers to use for this line of kinds (data types).
        kind_line = self.kinds[-1]

        # Get the defaults if any.
        if self.key_dict["defaults"] is not None:
            default_line = self.key_dict["defaults"][-1]
            self.key_dict["defaults"] = self.key_dict["defaults"] + [default_line]
        else:
            default_line = None
        
        if self.key_dict['ranges'] is not None:
            # Gets the last defined line of ranges
            range_line = self.key_dict['ranges'][-1]
            self.key_dict['ranges'] = self.key_dict['ranges'] + [range_line]
        else:
            range_line = None


        par_sz,ui_elems = self.get_input_handler_row(kind_line,default_line,self.keyword,
                                                         ranges = range_line)
        
        # Update the attributes and key dictionary.
        self.kinds = self.kinds + [kind_line]
        
        # Insert this into the key_sizer
        index = self.key_sizer.GetItemCount() - 1
        self.key_sizer.Insert(index,par_sz,0,wx.ALL|wx.EXPAND,2)
        self.par_sizers.insert(-1,par_sz)
        self.ui_elems = self.ui_elems + [ui_elems]
        #self.panel2_sizer.Layout()
        self.panel2.SetVirtualSize(self.panel2_sizer.GetMinSize())
        if layout: self.do_layout(self.panel2)
        

    # What to do when enable is checked/unchecked. Enable/disable all input fields 
    # associated with this specific keyword.
    def enable_keyword(self,evt):
        # Enable all widgets inside key_sizer
        obj = evt.GetEventObject()
        keyword = obj.GetName()
        val = obj.GetValue()

        self.enable_keyword_elements(val)

    def ToggleButtonLabel(self,evt):
        obj = evt.GetEventObject()
        if obj.GetValue():
            label = "True"
        else:
            label = "False"
        obj.SetLabel(label)

    def validate_float(self,evt,range=None):
        #print('validating float')
        obj = evt.GetEventObject()
        val=obj.GetValue()
        ie.error = False
        inp_fl = inp_float(str(val))
        if ie.error:
            obj.SetForegroundColour(wx.RED)
            obj.SetFocus()
            #evt.Skip()
            return

        if inp_fl.validate(range):
            val=float(obj.GetValue())
            obj.SetForegroundColour(wx.BLACK)
        else:
            obj.SetForegroundColour(wx.RED)
            #floatErrorDialog = wx.MessageDialog(self,"ERROR: Input requires float.",style=wx.ICON_NONE)
            #if floatErrorDialog.ShowModal() == wx.ID_OK:
            #floatErrorDialog.Destroy()

            obj.SetFocus()

        #evt.Skip()
        return

    def validate_float_chars(self,evt):
        key = evt.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            #evt.Skip()
            return

        if chr(key) in "0123456789-.eE":
            #evt.Skip()
            return
        
        return


    def do_layout(self,windows):
        if isinstance(windows,list) or isinstance(windows,tuple):
            for window in windows:
                window.Layout()
                window.FitInside()
        else:
            windows.Layout()
            windows.FitInside()
    


# class MyApp(wx.App):
#     def OnInit(self):
#         self.frame = Frame(None, wx.ID_ANY, "")
#         self.SetTopWindow(self.frame)
#         # self.frame.Show()
#         return True      




# if __name__ == '__main__':
#     app = MyApp(0)
#     #frame = MyFrame()
#     app.MainLoop()
