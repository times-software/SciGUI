import wx
import wx.richtext
from scigui.wx_extensions import *
import scigui.input_errors as ie
from scigui.input_types import *
import scigui.structure_visualization as structure_visualization

""" Make general scigui classes for each gui element: Frame, panel, notbook, 
    split panel, sizer, text control, spin control, combo box, file chooser. 
    Inside, have possibility to use wx, tk, ...
"""
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
                self.widget = wx.SpinCtrl(parent,min=-100, max=100, initial=val,name=name_lbl)
                self.default = val
            else:
                self.widget = wx.SpinCtrl(parent,min=-100, max=100, initial=0,name=name_lbl)
                self.default = 0
        elif kind.__name__ == 'inp_bool':
            # Logical input/
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
            self.widget = wx.FilePickerCtrl(parent, name = name_lbl,style=wx.ALIGN_LEFT|wx.FLP_USE_TEXTCTRL)
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
            self.widget.SetMinSize(min_size2)
        else:
            self.widget.SetMinSize((80,20))
        #    
        #self.widget.SetMinSize(min_size2)
        self.sizer.Add(self.widget,1,wx.TOP,3)
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
        #print(self.widget.GetValue())
        if hasattr(self,'view_button'):
            file = inp_structure_file(self.widget.GetValue())
            #print(file,file.validate())
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
