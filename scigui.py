import wx
import wx.lib.scrolledpanel
import input_errors as ie
import sys
from io import StringIO
#import os, sys, subprocess, shutil #, resource
#import readconfig
import input_definition
import translate_input
from input_types import *
import os, subprocess
import pathlib
import structure_visualization
import graphing
#import subprocess
from time import sleep

""" Make general scigui classes for each gui element: Frame, panel, notbook, 
    split panel, sizer, text control, spin control, combo box, file chooser. 
    Inside, have possibility to use wx, tk, ...
"""
__ui_type = 'wx'

class input_element():
    def __init__(self,parent, kind, name_lbl = None, label = None, min_size = None, default = None, range = None):
        # Make a vertical sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # If label exists, create a label to go above the input_widget
        if label is None: 
            lbl = ' '
        else:
            lbl = label
        
        self.kind = kind
        self.label_text = wx.StaticText(parent, label = lbl,style=wx.ALIGN_LEFT)
        self.sizer.Add(self.label_text,1,wx.TOP,2)

        text_size = self.label_text.GetTextExtent("W")
        if min_size is None: min_size = (text_size[0]*10, text_size[1]*2)
    
        min_size2 = min_size
        if kind.__name__ == 'inp_float':
            # Float input
            
            if default is not None:
                try:
                    val = float(default)
                except:
                    print('Wrong default or kind for keyword: ', name_lbl, ' in config file.')
                    print('Should be float.')
                    exit()
                self.widget = wx.TextCtrl(parent,value=default,name=name_lbl,style=wx.ALIGN_LEFT)
                self.default = default
                #inp_elem = wx.lib.agw.floatspin.FloatTextCtrl(panel,name=name_lbl)
            else:
                self.widget = wx.TextCtrl(parent,name=name_lbl,style=wx.ALIGN_LEFT)
                self.default = ''
                #inp_elem = wx.lib.agw.floatspin.FloatTextCtrl(panel,name=name_lbl)
            #inp_elem.Bind(wx.EVT_KILL_FOCUS,self.validate_float)
            self.widget.Bind(wx.EVT_KEY_UP, lambda event: self.validate_float(event, range))
            self.widget.Bind(wx.EVT_KILL_FOCUS, lambda event: self.validate_float(event, range))
            self.widget.Bind(wx.EVT_CHAR,self.validate_float_chars)
        elif kind.__name__ == 'inp_int':
            # Integer input. Add spin control
            if default is not None:
                try:
                    val = int(default)
                except:
                    print('Wrong default or kind for keyword: ', name_lbl, ' in config file.')
                    print('Should be integer.')
                    exit()
                self.widget = wx.SpinCtrl(parent,min=-100, max=100, initial=val,name=name_lbl,style=wx.ALIGN_LEFT)
                self.default = val
            else:
                self.widget = wx.SpinCtrl(parent,min=-100, max=100, initial=0,name=name_lbl,style=wx.ALIGN_LEFT)
                self.default = 0
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
            self.default = val
            if val:
                lbl = "True"
            else:
                lbl = "False"

            self.widget = wx.ToggleButton(parent,label=lbl,name=name_lbl,style=wx.ALIGN_LEFT)
            self.widget.SetValue(val)
            self.widget.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleButtonLabel)
            
        elif kind.__name__ == 'inp_str': 
            # String input
            if default is not None:
                self.widget = wx.TextCtrl(parent,value=default,name=name_lbl,style=wx.ALIGN_LEFT)
                self.default = default
            else:
                self.widget = wx.TextCtrl(parent,name=name_lbl,style=wx.ALIGN_LEFT)
                self.default = ''
        elif kind.__name__ == 'inp_paragraph':
            # Paragraph?
            if default is not None:
                self.widget = wx.TextCtrl(parent,value=default,name=name_lbl,style=wx.TE_MULTILINE|wx.HSCROLL|wx.ALIGN_LEFT)
                self.default = default
            else:
                self.widget = wx.TextCtrl(parent,name=name_lbl,style=wx.TE_MULTILINE|wx.HSCROLL|wx.ALIGN_LEFT)
                self.default = ''
        elif kind.__name__ == 'inp_file_name':
            self.widget = wx.FilePickerCtrl(parent, name = name_lbl,style=wx.ALIGN_LEFT)
            self.widget.Bind(wx.EVT_FILEPICKER_CHANGED,self.on_file_change)
            min_size2 = (min_size[0]*2,min_size[1])
            self.default = ''
        elif kind.__name__ == 'inp_structure_file':
            self.widget = wx.FilePickerCtrl(parent, name = name_lbl,style=wx.ALIGN_LEFT)
            self.widget.Bind(wx.EVT_FILEPICKER_CHANGED,self.on_file_change)
            self.view_button = wx.Button(parent,label='View',name=name_lbl,style=wx.ALIGN_LEFT)
            self.view_button.Bind(wx.EVT_BUTTON,self.view_structure)
            min_size2 = (min_size[0]*2,min_size[1])
            self.default = ''
        elif kind.__name__ == 'inp_choice':
            #print('range=',range)
            #exit()
            self.widget = wx.Choice(parent,name = name_lbl, choices = [''] + range.split(','))
            self.default = ''
        else:
            ie.error_message = 'Invalid type in input_types.py: ' + kind.__name__
            ie.input_error = True
            ie.error_type = 'fatal'
            print(ie.error_message)
            exit()
   
        if min_size2[0] > 0 and min_size[1] > 0:
                #wx.CallAfter(self.widget.SetMinSize,min_size2)
            self.widget.SetMinSize,min_size2
        else:
            self.widget.SetMinSize((80,20))
        #    
        #self.widget.SetMinSize(min_size2)
        self.sizer.Add(self.widget,1,wx.TOP,2)
        if kind.__name__ == 'inp_structure_file':
            self.sizer.Add(self.view_button,1,wx.TOP,2)
            self.view_button.Enable(False)


    def Reset(self):
        self.SetValue(self.default)
        if self.kind.__name__ == 'inp_float':
            # Float input
            if self.default is not None:
                self.widget.SetValue(self.default)
            else:
                self.widget.SetValue('')
            
        elif self.kind.__name__ == 'inp_int':
            # Integer input. Add spin control
            if self.default is not None:
                self.widget.SetValue(int(self.default))
            else:
                self.widget.SetValue(0)
        elif self.kind.__name__ == 'inp_bool':
            # Logical input
            if self.default is not None:
                val = self.default
            else:
                val = False
            
            if val:
                lbl = "True"
            else:
                lbl = "False"

            self.widget.SetLabel(lbl)
            self.widget.SetValue(val)
            
        elif self.kind.__name__ == 'inp_str': 
            # String input
            if self.default is not None:
                self.widget.SetValue(self.default) 
            else:
                self.widget.SetValue('')
        elif self.kind.__name__ == 'inp_paragraph':
            # Paragraph?
            if self.default is not None:
                self.widget.SetValue(self.default)
            else:
                self.widget.SetValue('')
        elif self.kind.__name__ == 'inp_file_name':
            if self.default is not None:
                self.widget.SetValue(self.default)
            else:
                self.widget.SetValue('')
        elif self.kind.__name__ == 'inp_structure_file':
            if self.default is not None:
                self.widget.SetValue(self.default)
                self.view_button.Enable(False)
            else:
                selt.widget.SetValue('')
            
        elif self.kind.__name__ == 'inp_choice':
            self.widget.SetValue('')

    def Show(self,val):
        self.label_text.Show(val)
        self.widget.Show(val)
        if hasattr(self,'view_button'): self.view_button.Show(val)
        self.sizer.Layout()

    def Enable(self,val):
        self.widget.Enable(val)

    def on_file_change(self,evt):
        print(self.widget.GetValue())
        if hasattr(self,'view_button'):
            file = inp_structure_file(self.widget.GetValue())
            print(file,file.validate())
            if file.validate(): 
                self.view_button.Enable(True)
            else:
                self.view_button.Enable(False)

    def view_structure(self,evt):
        # This is a structure field, so it's widget is a filepicker.
        structure_file = inp_structure_file(self.widget.GetValue()) 
        structure_visualization.run_viewer(structure_file)

    def ToggleButtonLabel(self,evt):
        obj = evt.GetEventObject()
        if obj.GetValue():
            label = "True"
        else:
            label = "False"
        obj.SetLabel(label)

    def GetValue(self):
        return self.widget.GetValue()
    
    def SetValue(self,val):
        self.widget.SetValue(val)
        if self.kind.__name__ == 'inp_structure_file':
            self.view_button.Enable(True)
        elif self.kind.__name__ == 'inp_bool':
            if self.widget.GetValue():
                label = "True"
            else:
                label = "False"
            self.widget.SetLabel(label)

    def validate_float(self,evt,range=None):
        #print('validating float')
        obj = evt.GetEventObject()
        val=obj.GetValue()
        ie.error = False
        if val == '': return
        inp_fl = inp_float(str(val))
        if ie.error:
            obj.SetForegroundColour(wx.RED)
            obj.SetFocus()
            obj.SetInsertionPointEnd()
            #evt.Skip()
            return

        #print('Testing outside', range, inp_fl>=0.0) 
        if inp_fl.validate(range):
            val=float(obj.GetValue())
            obj.SetForegroundColour('')
            evt.Skip()
        else:
            obj.SetForegroundColour(wx.RED)
            #floatErrorDialog = wx.MessageDialog(self,"ERROR: Input requires float.",style=wx.ICON_NONE)
            #if floatErrorDialog.ShowModal() == wx.ID_OK:
            #floatErrorDialog.Destroy()
            obj.SetFocus()
            obj.SetInsertionPointEnd()

        #evt.Skip()
        return

    def validate_float_chars(self,evt):
        key = evt.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            evt.Skip()
            return

        if chr(key) in "0123456789-.eE":
            evt.Skip()
            return
        
        return
        
"""
TO DO: 
2. Add notebook tabs for each category of input (to be added to config file).
   Categories:
      Structure (or maybe system)
      computational (MPI, multiprocessing, etc)
      code_specific (one for each code)
      DFT?

Questions:
Default values - How should they propagate to codes? What if they should be different for different
                 codes? I think if there are code specific defaults, there should be no generic default.

"""
""" input_page is a class that consists of one page with a split panel. The left side holds keywords, and the right
    side holds the options for each keyword on the left side. 
    input:
        inp_dict - dictionary that holds all information about keywords to add to the input_page.
        parent - parent window of the input page."""
        
class input_page():
    def __init__(self,parent,inp_def):
        self.inp_dict = inp_def.inp_def_dict
        # Make everything below this into a function InputPage
        self.splitter_window = wx.SplitterWindow(parent)
        # Give it a sizer so that it can resize with the main frame.
        #main_sizer = wx.BoxSizer(wx.HORIZONTAL) # Don't need this

        # Add scroll panels inside each of the sides of the split window. 
        self.panel1 = wx.lib.scrolledpanel.ScrolledPanel(self.splitter_window, -1, style=wx.SIMPLE_BORDER)
        self.panel1.SetupScrolling()
        self.panel2 = wx.lib.scrolledpanel.ScrolledPanel(self.splitter_window, -1, style=wx.SIMPLE_BORDER)
        self.panel2.SetupScrolling()

        # Add sizers for each of the scrolled panels.
        self.panel1_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel2_sizer = wx.BoxSizer(wx.VERTICAL)

        #Set the sizers for each panel.
        #main_panel.SetSizer(main_sizer)
        self.panel1.SetSizer(self.panel1_sizer)
        self.panel2.SetSizer(self.panel2_sizer)

        # Below we will loop over the input keywords
        # Hold index of the sizer that holds input fields for each keyword.
        i_key = 0
        
        
        self.key_ui_dict = {}
        if hasattr(inp_def,'first_keys'): 
            # First show the "first_keys", then show rest in alphabetical order.
            first_keys = inp_def.first_keys
            for inpkey in first_keys:
                # Special keyword to indicate what type of input data this is.
                # Ignore.
                if inpkey ==  '_input_type': continue

                self.key_ui_dict[inpkey] = key_ui_elem(inpkey,self.inp_dict[inpkey],self.panel1, self.panel2)
                self.key_ui_dict[inpkey].ShowItems(False)
                i_key += 1
        else:
            first_keys = []

        for inpkey in sorted(self.inp_dict.keys()):
            # Special keyword to indicate what type of input data this is.
            # Ignore.
            if inpkey ==  '_input_type' or inpkey in first_keys: continue

            self.key_ui_dict[inpkey] = key_ui_elem(inpkey,self.inp_dict[inpkey],self.panel1, self.panel2)
            self.key_ui_dict[inpkey].ShowItems(False)
            i_key += 1
    

        # Bind events (maybe this should be done above show?)
        self.panel1.Bind(wx.EVT_TOGGLEBUTTON, self.on_press_panel1_sizer)
        #self.panel2.Bind(wx.EVT_CHECKBOX, self.update_required)
        #panel2.Bind(wx.EVT_BUTTON, self.on_press_panel2)
        #self.main_notebook.AddPage(splitter_window,category)
        
        
        #return splitter_window, panel1, panel2

    def on_press_panel1_sizer(self,event):
        # Get the toggle that was pressed.
        obj = event.GetEventObject()
        # Validate that the currently viewed key_ui is valid.
        if hasattr(self,"current_key_ui"):
            is_valid,message = self.current_key_ui.validate_key_values()
            if not is_valid:
                md = wx.MessageDialog(self.splitter_window,message)
                md.ShowModal()
                obj.SetValue(False)
                return None
            else:
                keyword = obj.GetLabelText()
                obj.SetValue(True)
                self.current_key_ui.ShowItems(False)
                self.current_key_ui.key_toggle.SetValue(False)
                self.key_ui_dict[keyword].ShowItems(True)
                self.current_key_ui = self.key_ui_dict[keyword]

        # Get the keyword from the button text.
        #for key,key_ui_elem in self.key_ui_dict.items():
        #    if key_ui_elem.keyword == keyword:
                #print(keyword,key_ui_elem.keyword)
        #        key_ui_elem.ShowItems(True)
        #        self.current_key_ui = key_ui_elem
        #    else:
        #        key_ui_elem.key_toggle.SetValue(False)
        #        key_ui_elem.ShowItems(False)

        splitter_window = self.current_key_ui.panel1.GetParent()
        self.current_key_ui.help_text_ui.Wrap(int(splitter_window.GetWindow2().GetSize().width - 5))
        # self.panel2.SetVirtualSize(self.current_key_ui.panel2_sizer.GetMinSize())
        # self.panel2.Layout()
        # self.panel2.FitInside()
        do_layout(self.panel2)

    def show_keywords(self,keys,highlight=False,colour = wx.GREEN,set_current=True):
        # Shows a set of keywords, these will be highlighted 
        # if highlight = True.
        # If set_current, the currently selected keyword will be changed to the first
        # in this list if current selection is not in this list.
        if not keys: return
        for key in keys:
            self.key_ui_dict[key].key_toggle.Show(True)
            self.key_ui_dict[key].key_toggle_window.Show(True)

        if set_current:
            if self.current_key_ui.keyword in keys:
                self.current_key_ui.ShowItems(True)
            else:
                # Show first keyword in required keys.
                self.key_ui_dict[keys[0]].ShowItems(True)
                self.current_key_ui = self.key_ui_dict[keys[0]]
                self.current_key_ui.key_toggle.SetValue(True)
                self.current_key_ui.key_toggle.SetFocus()

        # self.panel1.Layout()
        # self.panel2.Layout()
        # self.splitter_window.Layout()
        if highlight:
            for key in keys:
                #print("HL:", key)
                col = (colour[0],colour[1],colour[2],150)
                self.key_ui_dict[key].key_toggle_window.SetBackgroundColour(col)
        do_layout((self.panel1,self.panel2,self.splitter_window))
        # Call highlighting after layout?
        #va = self.current_key_ui.key_toggle.GetClassDefaultAttributes()
        


    def show_only_keywords(self,keys):
        # Shows a set of keywords, hiding all others
        # Calling this with an empty keys list will hide all
        # keywords.
        for key,key_ui in self.key_ui_dict.items():
            key_ui.ShowItems(False)
            key_ui.key_toggle.Show(False)
            key_ui.key_toggle_window.Show(False)
            key_ui.key_toggle_window.SetBackgroundColour(wx.NullColour)

        key_panels = []
        if not keys: return
        for key in keys:
            self.key_ui_dict[key].key_toggle_window.Show(True)
            key_panels = key_panels + self.key_ui_dict[key].key_toggle_window
            self.key_ui_dict[key].key_toggle.Show(True)

        if self.current_key_ui.keyword in keys:
            self.current_key_ui.ShowItems(True)
        else:
            # Show first keyword in required keys.
            self.key_ui_dict[keys[0]].ShowItems(True)
            self.current_key_ui = self.key_ui_dict[keys[0]]
            self.current_key_ui.key_toggle.SetValue(True)
            self.current_key_ui.key_toggle.SetFocus()

        # self.panel1.Layout()
        # self.panel2.Layout()
        # self.splitter_window.Layout()
        do_layout((self.panel1,self.panel2,self.splitter_window))

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
        self.panel2 = panel2
        self.help_text = keyword.strip() + ':' + '\n' + '\n'.join(key_dict['help'])

        self.panel1_sizer = panel1.GetSizer()
        self.panel2_sizer = panel2.GetSizer()
        self.key_toggle_window = wx.Panel(self.panel1,style=wx.BORDER_THEME)
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
        
        # In the right window, add a vertical sizer which will contain the help text, 
        # then all of the lines of input for this keyword. 
        self.key_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel2_sizer.Add(self.key_sizer,wx.ALL|wx.EXPAND,0)
        
        # Add the help text to the key_sizer next.
        self.help_text_ui = wx.StaticText(panel2, label =self.help_text,style=wx.ALIGN_LEFT)

        # Make the text wrap at the edge of the right side panel. 
        #help_text.Wrap(self.splitter_window.GetWindow1().GetSize()[1])
        self.key_sizer.Add(self.help_text_ui,0,wx.LEFT|wx.ALIGN_LEFT|wx.EXPAND,10)

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
            inp_elem = input_element(self.panel2, kind, name_lbl = name_lbl, label = label, min_size = min_size, default = default, range = rng)
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
    
    def ShowItems(self,val):
        self.key_sizer.ShowItems(val)
        for ui_elem_line in self.ui_elems:
            for ui_elem in ui_elem_line:
                ui_elem.Show(val)
        #self.panel2_sizer.Layout()
        do_layout(self.panel2)
    
    def Highlight(self):
        self.key_toggle.SetOwnForegroundColour(wx.GREEN)



    ################################################################################
    #      EVENT PROCESSING FOR key_ui_elem class
    ################################################################################
             

    def add_ui_column(self,evt=None):
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
                

            inp_elem = input_element(self.panel2,kind,default = default,name_lbl = self.keyword,range = rng)
            is_enabled = self.enable_checkbox.GetValue()
            inp_elem.Enable(is_enabled)
            self.par_sizers[irow].Add(inp_elem.sizer,0,wx.LEFT|wx.ALIGN_LEFT,10)
            self.ui_elems[irow] = self.ui_elems[irow] + [inp_elem]
            self.kinds[irow] = self.kinds[irow] + [kind]
            irow += 1
        #self.panel2_sizer.Layout()
        self.panel2.SetVirtualSize(self.panel2_sizer.GetMinSize())
        do_layout(self.panel2)


    def add_ui_row(self,evt=None):
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
        do_layout(self.panel2)
        

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

# wx class extensions (definition of new instance methods)
# Make a GetValue() class function for wx.FilePickerCtrl
def GetValue(self):
    if isinstance(self,wx.FilePickerCtrl):
        return self.GetPath()
    elif isinstance(self,wx.Choice):
        return self.GetStringSelection()

def SetValue(self,val):
    if isinstance(self,wx.FilePickerCtrl):
        self.SetPath(val)
    elif isinstance(self,wx.Choice):
        self.SetSelection(self.FindString(val))


wx.FilePickerCtrl.GetValue = GetValue
wx.Choice.GetValue = GetValue
wx.FilePickerCtrl.SetValue = SetValue
wx.Choice.SetValue = SetValue

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        super().__init__(parent=None, title='Corvus')
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        #wx.Frame.__init__(self, *args, **kwds)
        self.defaultFile = 'corvus.in'
        self.infile = None
        # Set the datafiles
        self.datafile = None

        # Initialize the input definition
        self.inp_def = input_definition.input_definition_dict('corvus')
        self.inpdict = self.inp_def.inp_def_dict
        self.input_type = self.inpdict['_input_type']
        del self.inpdict['_input_type'] # For now delete this. Might need it in the future?
        # Get categories:
        
        self.categories = ['all'] + sorted(set(','.join([v['category'].lower() for v in self.inpdict.values()]).split(',')))
        self.codes = ['all'] + sorted(set([v['code'].lower() for v in self.inpdict.values()]))
        
        #print(self.categories)
        #print(self.codes)

        # Initialize the main window
        #First retrieve the screen size of the device
        screenSize = wx.DisplaySize()
        screenWidth = int(screenSize[0]/3*2)
        screenHeight = int(screenSize[1]/3*2)
        top_panel_size = (screenWidth,int(screenHeight/8))
        top_panel_border = int(top_panel_size[1]/10)
        self.SetSize(wx.Size(screenWidth, screenHeight))

        # Make a menu-bar
        # Initialize the menu.
        filemenu= wx.Menu()
        helpmenu= wx.Menu()
        item_open = filemenu.Append(wx.ID_ANY, "Open", "Open")
        self.id_open = item_open.GetId()
        item_save = filemenu.Append(wx.ID_ANY, "Save", "Save")
        self.id_save = item_save.GetId()
        item_about = helpmenu.Append(wx.ID_ANY, "About","About")
        self.id_about = item_about.GetId()
        item_doc = helpmenu.Append(wx.ID_ANY,"Doc","Doc")
        self.id_doc = item_doc.GetId()
        item_exit = filemenu.Append(wx.ID_ANY,"Exit","Exit")
        self.id_exit = item_exit.GetId()

        # Construct the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"File") # Integrating the "filemenu" to the MenuBar
        menuBar.Append(helpmenu,"Help")
        self.SetMenuBar(menuBar)  # Attaching the MenuBar to the Frame.
        self.Bind(wx.EVT_MENU, self.menuhandler)
        
        # Add a splitter window with top and bottom panes.
        self.splitter_window0 = wx.SplitterWindow(self)
        self.top_panel = wx.Panel(self.splitter_window0)
        self.top_panel_sizer = wx.GridBagSizer()
        #self.top_panel_hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.runButton = wx.Button(self.top_panel,label="Run")
        #self.runButton.SetBackgroundColour((0, 230, 0, 100))
        #self.top_panel_sizer.Add(self.writeInputButton,1,wx.ALL,5)
        self.top_panel_sizer.Add(self.runButton,(0,0),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.runButton.Bind(wx.EVT_BUTTON,self.run)
        self.quick_start_choice = wx.Choice(self.top_panel,name = "quick_start", choices = ['Quick Start'] + list(self.inp_def.predefined.keys()))
        self.quick_start_choice.SetSelection(self.quick_start_choice.FindString('Quick Start'))
        self.top_panel_sizer.Add(self.quick_start_choice,(0,1),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.quick_start_choice.Bind(wx.EVT_CHOICE,self.set_values_from_predefined)
        self.show_enabled_checkbox = wx.CheckBox(self.top_panel,label='Show only enabled input')
        #self.top_panel_sizer.Add(self.show_enabled_checkbox,1,wx.ALL,5)
        filter_start = 15
        self.top_panel_sizer.Add(self.show_enabled_checkbox,(0,filter_start + 2),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.show_enabled_checkbox.Bind(wx.EVT_CHECKBOX,self.filter_keywords)
        self.category_choice = wx.Choice(self.top_panel,name = "category", choices = self.categories)
        self.category_choice.SetSelection(self.category_choice.FindString('property'))
        #self.top_panel_sizer.Add(self.category_choice,1,wx.ALL,5)
        self.top_panel_sizer.Add(self.category_choice,(0,filter_start),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.category_choice.Bind(wx.EVT_CHOICE,self.filter_keywords)
        self.code_choice = wx.Choice(self.top_panel,name = "code", choices = self.codes)
        self.code_choice.SetSelection(self.code_choice.FindString('general'))
        self.top_panel_sizer.Add(self.code_choice,(0,filter_start+1),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.code_choice.Bind(wx.EVT_CHOICE,self.filter_keywords) 
        #wx.CallAfter(self.code_choice.SetLabel, 'code')
        #wx.CallAfter(print("label ",self.code_choice.GetLabel()))

        #self.top_panel_sizer.Add()
        self.Show()
        self.top_panel.SetSizer(self.top_panel_sizer)

        # Add a notebook so that this is one page.
        self.main_notebook = wx.Notebook(self.splitter_window0)

        # Read in the configuration file to obtain information about all of the 
        # keywords. (May want to read in information on implementations, running, etc as well.)
        # This will be held in a dictionary of dictionaries. The keys of the ourter dictionary
        # are the input keywords. The keys of the inner dictionary hold information about the
        # input fields. For now, they have the following keys:
        # kinds    - list of lists. Each outer element is a list of data types, given by a single 
        #            character, I = int, F = float, S = string, 
        #            P = paragraph, and L = logical. Last field in the inner list can also be ...
        #            which indicates possible repeats of the previous field if there is one, or 
        #            possible repeats of the previous line if ... is the only element in the 
        #            current list.
        # help     - help description for this keyword
        # defaults - default values if any.
        # Will want to add more later, i.e., names, importance, category, and anything else 
        # necessary or convenient.
        
        #self.inpdict = readconfig.read_config_file()
     
        #exit()
        self.values_dict = dict()
      
        # Make a split window. Left side will show all keywords (cards), right side will
        # show the input fields of the currently selected keyword.
        # The ui_elem_dict will hold the ui elements associated with each keyword. 
        self.ui_elem_dict = dict()
        self.inp_page = input_page(self.main_notebook,self.inp_def)
        self.main_notebook.AddPage(self.inp_page.splitter_window,"category: property, code: general")

        #self.showNextButton = wx.Button(self.top_panel,label="Next")
        #self.top_panel_sizer.Add(self.showNextButton,1,wx.ALL,5)
        #self.top_panel_sizer.Add(self.showNextButton,(1,0),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        #self.showNextButton.Bind(wx.EVT_BUTTON,self.show_next_required)

        # Plotting
        self.plotButton = wx.Button(self.top_panel,label="Plot")
        #self.top_panel_sizer.Add(self.showNextButton,1,wx.ALL,5)
        self.top_panel_sizer.Add(self.plotButton,(1,1),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.plotButton.Bind(wx.EVT_BUTTON,self.on_plot_button)

        self.showAllRequired = wx.CheckBox(self.top_panel,label="Show all required")
        #self.top_panel_sizer.Add(self.showAllRequired,1,wx.ALL,5)
        self.top_panel_sizer.Add(self.showAllRequired,(1,15),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        self.showAllRequired.Bind(wx.EVT_CHECKBOX,self.show_all_required)
        #splitter_window1, panel1, panel2 = self.MakeInputPage("All Keywords")
        #splitter_window2, panel3, panel4 = self.MakeInputPage("Copy of All Keywords")
        # Put the two panels inside the split window.
        # This needs to happen after self.Show(). How should this be done?
        # For now, just call self.Show here.
        #values_dict,is_valid,message = translate_input.read_corvus_input('corvus.inp')
        #print('Valid input: ', is_valid)
        #if is_valid: self.set_values(values_dict)
        self.Show()
        #self.key_ui_dict['cell_struc_xyz_red'].set_values([['A',0,0,0],['B',1.0,1.0,1.0]])

        self.splitter_window0.SplitHorizontally(self.top_panel,self.main_notebook,int(screenHeight/7))
        self.inp_page.splitter_window.SplitVertically(self.inp_page.panel1,self.inp_page.panel2,int(screenWidth/4))
        #splitter_window2.SplitVertically(panel3,panel4,0)
        self.Bind(wx.EVT_CLOSE,self.onExit)

        self.Layout()
        self.required = ['target_list']
        self.show_required(self.required[0])
        #print('required at initialization',self.required)

    def get_values_dict(self):
        self.values_dict = {}
        for key,key_ui in self.inp_page.key_ui_dict.items():
            if key_ui.enable_checkbox.GetValue(): self.values_dict[key] = key_ui.get_values()

    def set_values(self,values_dict):
        for key,val in values_dict.items():
            self.inp_page.key_ui_dict[key].set_values(val)
            self.inp_page.key_ui_dict[key].ShowItems(False)


    def save_as(self):
        with wx.FileDialog(self, "Save As", defaultFile=self.defaultFile,
            style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT|wx.FD_CHANGE_DIR) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            self.infile = fileDialog.GetPath()
            try:
                self.get_values_dict()
                translate_input.write_corvus_input(self.values_dict,self.infile)

            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)

            dir = pathlib.Path(self.infile).parent
            os.chdir(dir)
    #####################################################################
    # Event handlers
    #####################################################################

    def run(self,evt):
        if self.input_type == 'corvus':
            import re
            import sys
            from corvus.controls import oneshot

            if self.infile is None:
                self.save_as()
                # Check if corvus.in exists already and ask if overwrite if it
                # does.
            elif Path(self.infile).is_file():
                # Check if user wants to overwrite the current file or save in a different directory.
                message = 'The current input file:\n' + self.infile + '\nwill be overwritten.' + \
                         ' Continue or save to a new file?'
                with wx.MessageDialog(self.splitter_window0,message,style=wx.YES_NO|wx.CANCEL) as md:
                    md.SetYesNoCancelLabels('Continue', 'Save As', 'Cancel')
                    answer = md.ShowModal()
                    if  answer == wx.ID_CANCEL:
                        return
                    elif answer == wx.ID_YES:
                        self.get_values_dict()
                        translate_input.write_corvus_input(self.values_dict,self.infile)
                    elif answer == wx.ID_NO:
                        self.save_as()
            
            title = 'Corvus is running ...' 
            message = 'This will take time. You can see the output on the associated terminal.'
            with wx.Dialog(self.splitter_window0,title=title,style=wx.CAPTION) as md:
                text = wx.StaticText(md,label=message,style=wx.ALIGN_CENTRE_HORIZONTAL)
                text.Wrap(md.GetSize()[0]-10)
                #md.CreateTextSizer(message,md.GetSize()[0]-10)
                #md.CreateTextSizer(message,50)
                md.Show()
                wx.Yield()
                sys.argv = ['run-corvus','-i',self.infile]
                sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
                try:
                    oneshot()
                except SystemExit:
                    pass
                md.Destroy()
            message = 'Corvus is finished.'
            with wx.MessageDialog(self.splitter_window0,message,style=wx.OK) as md:
                answer = md.ShowModal()

    def on_plot_button(self,evt):
        if self.datafile is None:
            graphing.plot()
        else:
            graphing.plot(self.datafile)
    # Show only the kewords selected by the filter choices.
    #def show_only_required_keywords(self):
    def set_values_from_predefined(self,evt):
        obj = evt.GetEventObject()
        predef = obj.GetString(obj.GetSelection())
        if predef == "Quick Start":
            #evt.Skip()
            return
        key_list = []
        associated_key_list = []
        vals_dict = {}
        for key,value in self.inp_def.predefined.items():
            if key == predef:
                pred_dict = value
                for k,v in pred_dict.items():
                    if k == '_required':
                        # Show these keywords, and highlight. Don't set enabled.
                        key_list = key_list + v
                    elif k == '_associated':
                        associated_key_list = associated_key_list + v
                    else:
                        # Set the values and show
                        key_list = key_list + [k]
                        vals_dict[k] = v
        message = 'Would you like to overwrite your settings with new ones? If no, the relevant keywords will be shown' + \
        'without changing the settings.'
        md = wx.MessageDialog(self.splitter_window0,message,style=wx.YES_NO|wx.CANCEL)
        answer = md.ShowModal()
        if  answer == wx.ID_CANCEL:
                        return
        elif answer == wx.ID_YES:
            self.Reset()
            self.set_values(vals_dict)
        # Fist hide all keywords
        self.inp_page.show_only_keywords([])
        # Now show required keywords with highlighted green outline.
        if key_list: self.inp_page.show_keywords(key_list,highlight=True,set_current=True)
        # Now show associated keywords highlighted blue
        if associated_key_list: self.inp_page.show_keywords(associated_key_list,highlight=True,colour=wx.BLUE,set_current=False)
        self.code_choice.SetSelection(self.code_choice.FindString('all'))
        self.category_choice.SetSelection(self.category_choice.FindString('all'))
        #evt.Skip()


    def show_next_required(self,evt):
        # Validate current key.
        if self.required:
            # Get the current reuirement.
            req = self.required[0]
            if req in self.categories:
                # This is an entire category of keywords. Need to check if at least one of them is valid.
                is_valid = True
                keys = [key for key in self.inpdict if req in self.inpdict[key]['category']]
                
                # Check if current keyword is part of keys. If it is, set req to current keyword and continue.
                if not hasattr(self.inp_page,"current_key_ui"):
                    is_valid = False
                    message = 'Requirement not met. One of the current keywords in the category ' + req + \
                        ' must be filled out. Please select a keyword from the left panel and fill it out.'
                    md = wx.MessageDialog(self.inp_page.splitter_window,message)
                    md.ShowModal()
                    return
                if self.inp_page.current_key_ui.keyword not in keys:
                    is_valid = False
                    message = 'Requirement not met. One of the current keywords in the category ' + req + \
                        ' must be filled out. Please select a keyword from the left panel and fill it out.'
                    md = wx.MessageDialog(self.inp_page.splitter_window,message)
                    md.ShowModal()
                    return
                else:
                    # The current keyword is an element of the category. We will want to add it's required keys to the list.
                    req = self.inp_page.current_key_ui.keyword

            
            # Now check that the currently selected keyword has valid input.
            if hasattr(self.inp_page,"current_key_ui"):
                is_valid,message = self.inp_page.current_key_ui.validate_key_values()
                if not is_valid:
                    md = wx.MessageDialog(self.inp_page.splitter_window,message)
                    md.ShowModal()
                    return
                else:
                    # Delete the first requirement and move to next.
                    self.required.pop(0)
                    if req in self.inpdict: self.update_required(req)
                    #print('required inside show_next: ', self.required,req)
                    
                    # If this was the last requirement, disable the button.
                    if not self.required:
                        # Disable next button and show all enabled keywords.
                        #self.showNextButton.Disable()
                        self.show_filtered(all_categories = True, all_codes=True, only_enabled = True)
                        return
                    self.show_required(self.required[0])
            else:
                message = "Something is wrong in show_next_required. current_key_ui not set."
                md = wx.MessageDialog(self.inp_page.splitter_window,message)
                md.ShowModal()    
        else:
            message = "Something is wrong in show_next_required. self.required is empty."
            md = wx.MessageDialog(self.inp_page.splitter_window,message)
            md.ShowModal()

    def show_required(self,req):
        # Required can be a specific keyword, or it could be an entire category,
        # such as "structure".
        if req in self.inp_page.key_ui_dict:
            self.show_and_enable_keyword(req)
        elif req in self.categories:
            self.category_choice.SetSelection(self.category_choice.FindString(req))
            self.show_filtered()

    def show_all_required(self,evt):
        #print(self.required)
        if self.showAllRequired.GetValue():
            #print('box checked')
            if self.required:
                #print('required is not empty')
                # Get all required keys.
                keys = [key for key in self.required if key in self.inpdict]
                # Get all required categories.
                categories = [c for c in self.required if c in self.categories]
                # Get all keys from each category
                ckeys = []
                # Get code filter
                code = self.code_choice.GetString(self.code_choice.GetSelection())
                for c in categories:
                    if code == 'all':
                        ckeys = ckeys + [key for key in self.inpdict if c in self.inpdict[key]['category']]
                    else:
                        ckeys = ckeys + [key for key in self.inpdict if (c in self.inpdict[key]['category'] and code in self.inpdict[key]['code'])]
                keys = keys + ckeys
                # Check if keys have more than one category or more than one code, and show all if they do.
                all_codes = False
                all_categories = False
                category = self.category_choice.GetString(self.category_choice.GetSelection())
                for key in keys:
                    if self.inpdict[key]['code'] != code:
                        all_codes = True
                        break
                for key in keys:
                    if self.inpdict[key]['category'] != code:
                        all_categories = True
                        break
                
                self.show_filtered(all_categories = all_categories, all_codes = all_codes)
                #print('required inside show_all_required:')
                #print(keys)
                self.inp_page.show_only_keywords(keys)
                do_layout((self.inp_page.panel1,self.inp_page.panel2))
                #self.inp_page.panel1_sizer.Layout()
                #self.inp_page.panel2.Layout()
        else:
            # Unchecked. Show all keywords.
            if self.required:
                # If there are still required keywords, show the current one.
                self.show_required(self.required[0])
            else:
                # Show all keywords
                self.show_filtered(only_enabled = True, all_categories = True, all_codes = True)
                    
                
    def update_required(self,key):
        # Get new required keys/categories from this key.
        #print('start of update_required')
        #print(self.required)
        if 'required' not in self.inpdict[key]: return
        
        if self.inpdict[key]['required'] is None:
            return
        else:
            # If there is only one element of the "required"
            # dictionary, update with this value.
            if len(self.inpdict[key]['required']) == 1:
                self.required = self.inpdict[key]['required'] + self.required
            else:
                # Now the "required" dictionary holds one list 
                # for each possible value of the option of the keyword, 
                # and there could be multiple values associated with a single keyword.
                vals = self.inp_page.key_ui_dict[key].get_values()
                new_reqs = []
                for val_line in vals:
                    for val in val_line:                
                        # Get the value of the associated choice ui element
                        if str(val) in self.inpdict[key]['required']:
                            #print(str(val),self.inpdict[key]['required'][str(val)])
                            new_reqs = new_reqs + self.inpdict[key]['required'][str(val)]

                self.required = new_reqs + self.required                
            
            # Get rid of duplicates 
            req = []
            [req.append(x) for x in self.required if x not in req]
            self.required = req
    
    def show_and_enable_keyword(self,keyword):
        for key,key_ui_elem in self.inp_page.key_ui_dict.items():
            if key_ui_elem.keyword == keyword:
                #print(keyword,key_ui_elem.keyword)
                key_ui_elem.ShowItems(True)
                key_ui_elem.enable_checkbox.SetValue(True)
                key_ui_elem.key_toggle.SetValue(True)
                key_ui_elem.key_toggle.Show(True)
                key_ui_elem.key_toggle_window.Show(True)
                self.inp_page.current_key_ui = key_ui_elem
                key_ui_elem.enable_keyword_elements(True)
            else:
                key_ui_elem.key_toggle.SetValue(False)
                key_ui_elem.key_toggle.Show(False)
                key_ui_elem.key_toggle_window.Show(False)
                key_ui_elem.ShowItems(False)

        splitter_window = self.inp_page.current_key_ui.panel1.GetParent()
        self.inp_page.current_key_ui.help_text_ui.Wrap(int(splitter_window.GetWindow2().GetSize().width - 5))
        self.inp_page.current_key_ui.panel2.SetVirtualSize(self.inp_page.current_key_ui.panel2_sizer.GetMinSize())
        #self.inp_page.current_key_ui.panel2.Layout()
        #self.inp_page.panel1_sizer.Layout()
        do_layout((self.inp_page.panel1,self.inp_page.panel2))

    def Reset(self):
        for key,key_ui in self.inp_page.key_ui_dict.items():
            key_ui.Reset()
            
    def filter_keywords(self,evt):
        self.show_filtered()
        #print('show_filtered triggered: ',evt)

    def show_filtered(self,all_categories=False, all_codes=False,only_enabled=False):
        # Filter keywords by code, category, and enabled if show_enabled_only is checkted.
        # Get current selections.
        if only_enabled:
            self.show_enabled_checkbox.SetValue(True)
        if all_categories:
            self.category_choice.SetSelection(self.category_choice.FindString('all'))
        if all_codes:
            self.code_choice.SetSelection(self.code_choice.FindString('all'))
            
        show_only_enabled = self.show_enabled_checkbox.GetValue()
        category = self.category_choice.GetString(self.category_choice.GetSelection())
        code = self.code_choice.GetString(self.code_choice.GetSelection())
        self.main_notebook.SetPageText(0,'category: ' + category + ', code: ' + code)
        
        

        for key,key_ui in self.inp_page.key_ui_dict.items():
            enabled = key_ui.enable_checkbox.GetValue()
            in_category = category in self.inpdict[key]['category'].lower() or (category == 'all')
            in_code = code in self.inpdict[key]['code'].lower() or (code == 'all')
            #print('show_only_enabled, enabled, in_category, in_code')
            #print(show_only_enabled, enabled, in_category, in_code)
            if show_only_enabled and not enabled:
                show = False
            else:
                # Now filter by category and code.
                if in_category and in_code:
                    show = True
                else:
                    show = False

            key_ui.key_toggle.Show(show)
            key_ui.key_toggle_window.Show(show)
            if key_ui.key_toggle.GetValue(): key_ui.ShowItems(show)

            # panel1_sizer = key_ui.panel1_sizer
            # panel1_sizer.Layout()
            # self.inp_page.panel1.Layout()
            # self.inp_page.splitter_window.Layout()
            # self.inp_page.panel1.FitInside()
            # self.inp_page.panel2.Layout()
            # self.inp_page.panel2.FitInside()
            do_layout((self.inp_page.panel1,self.inp_page.panel2))

    #def validate_current_keyword(self,evt):


    # Write the input file - triggered by button.   
    def write_input_file(self,evt):
        self.get_values_dict()
        translate_input.write_corvus_input(self.values_dict,'corvus.in')

    # Runs on exit (menu->quit or red x)
    def onExit(self, evt):
        self.Destroy()


    # Handles menu events - file -> open, about, save, quit    
    def menuhandler(self,evt):
        id = evt.GetId()
        if id == self.id_open:
            with wx.FileDialog(self, "Open input file",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     # the user changed their mind

                try:
                    # Proceed loading the file chosen by the user
                    pathname = fileDialog.GetPath()
                    message = 'This will reset all previous input selections.\nContinue?'
                    md = wx.MessageDialog(self,message,style=wx.YES_NO)
                    if md.ShowModal() == wx.ID_NO:
                        return
                    
                    self.Reset()
                    self.infile = str(pathname)
                    dir = pathlib.Path(pathname).parent
                    os.chdir(dir)
                    self.values_dict,is_valid,message = translate_input.read_corvus_input(pathname)
                    
                    
                except IOError:
                    wx.LogError("Cannot open file '%s'." % newfile)

                if not is_valid:
                    msg1 = 'Error in input file ' + pathname + ".\n" 
                    md = wx.MessageDialog(self, msg1 + message)
                    md.ShowModal()
                    return

                self.set_values(self.values_dict)
                # Set the filter and code to all, and set show only enabled.
                
                self.show_filtered(all_categories = True, all_codes = True, only_enabled=True)
                self.inp_page.current_key_ui.ShowItems(True)
                

                
        elif id == self.id_about:
            about_dialog = wx.MessageDialog(self, "Sci-GUI version 0.00")
            about_dialog.ShowModal()
        elif id == self.id_doc:
            message = "Documentation for Corvus GUI built with Sci-GUI. \n\n" + \
                "1. Window structure: \n" + \
                "    a) Top panel holds run controls and keyword filters.\n" + \
                "    b) Left panel holds list of keywords as toggle buttons.\n" + \
                "    c) Right panel shows elements of the selected keyword, along with help." + \
                "       Use the 'enable' checkbox to enable the keyword and fill out the arguments." + \
                "\n" + \
                "2. "
            about_dialog = wx.MessageDialog(self, message)
            about_dialog.ShowModal()
        elif id == self.id_save:
            self.get_values_dict()
            with wx.FileDialog(self, "Save As",
                       style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT|wx.FD_CHANGE_DIR) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     # the user changed their mind

                # Proceed saving to the file chosen by the user
                self.infile = fileDialog.GetPath()
                try:
                    self.get_values_dict()
                    translate_input.write_corvus_input(self.values_dict,self.infile)

                except IOError:
                    wx.LogError("Cannot open file '%s'." % newfile)
        elif id == self.id_exit:
            self.OnExit(evt)

def do_layout(windows):
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
