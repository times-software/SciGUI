import wx
import wx.richtext
import darkdetect
import wx.lib.scrolledpanel
import scigui.input_errors as ie
import scigui.input_definition as input_definition
import scigui.translate_input as translate_input
from scigui.input_types import *
import scigui.key_ui_element as key_ui_element

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
        
        #self.panel2.Bind(wx.EVT_SIZE,self.on_resize)

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

                self.key_ui_dict[inpkey] = key_ui_element.key_ui_elem(inpkey,self.inp_dict[inpkey],self.panel1, self.panel2)
                self.key_ui_dict[inpkey].ShowItems(False)
                i_key += 1
        else:
            first_keys = []

        for inpkey in sorted(self.inp_dict.keys()):
            # Special keyword to indicate what type of input data this is.
            # Ignore.
            if inpkey ==  '_input_type' or inpkey in first_keys: continue

            self.key_ui_dict[inpkey] = key_ui_element.key_ui_elem(inpkey,self.inp_dict[inpkey],self.panel1, self.panel2)
            self.key_ui_dict[inpkey].ShowItems(False)
            i_key += 1
    

        # Bind events (maybe this should be done above show?)
        self.panel1.Bind(wx.EVT_TOGGLEBUTTON, self.on_press_panel1_sizer)
        #self.panel2.Bind(wx.EVT_CHECKBOX, self.update_required)
        #panel2.Bind(wx.EVT_BUTTON, self.on_press_panel2)
        #self.main_notebook.AddPage(splitter_window,category)
        
        
        #return splitter_window, panel1, panel2
    #def on_resize(self,evt=None,all_keys=False):
    #    if all_keys:
    #        for key,key_ui in self.key_ui_dict.items():
    #            key_ui.help_text_ui.SetLabel(self.current_key_ui.help_text)
    #            #key_ui.help_text_ui.Wrap(int(self.panel2.GetSize().width - 10))
    #        do_layout(self.panel2)
    #    else:
    #        if hasattr(self,"current_key_ui"):
    #            self.current_key_ui.help_text_ui.SetLabel(self.current_key_ui.help_text)
    #            #self.current_key_ui.help_text_ui.Wrap(int(self.panel2.GetSize().width - 10))
    #            do_layout(self.panel2)

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
                self.current_key_ui = self.key_ui_dict[keyword]
                self.current_key_ui.ShowItems(True)
                #print('Current keyword changed:',self.current_key_ui.keyword)

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
        #self.current_key_ui.help_text_ui.Wrap(int(splitter_window.GetWindow2().GetSize().width - 10))
        # self.panel2.SetVirtualSize(self.current_key_ui.panel2_sizer.GetMinSize())
        # self.panel2.Layout()
        # self.panel2.FitInside()
        self.do_layout((self.panel1,self.panel2))

    def show_keywords(self,required_keys,useful_keys,associated_keys,highlight=False,set_current=True,colours=[wx.GREEN,wx.BLUE,wx.YELLOW]):
        # Shows a set of keywords, these will be highlighted 
        # if highlight = True.
        # If set_current, the currently selected keyword will be changed to the first
        # in this list if current selection is not in this list.
        if darkdetect.isDark():
            alpha = 50
        else:
            alpha = 255

        cols = []
        for c in colours:
            cols = cols + [(c[0],c[1],c[2],alpha)]
        for key,key_ui in self.key_ui_dict.items():
            if key in required_keys:
                #print(key, 'green')
                self.key_ui_dict[key].key_toggle.Show(True)
                self.key_ui_dict[key].key_toggle_window.Show(True)
                if highlight:
                    self.key_ui_dict[key].key_toggle_window.SetBackgroundColour(cols[0])
            elif key in useful_keys:
                #print(key, 'blue')
                self.key_ui_dict[key].key_toggle.Show(True)
                self.key_ui_dict[key].key_toggle_window.Show(True)
                if highlight:
                    self.key_ui_dict[key].key_toggle_window.SetBackgroundColour(cols[1])
            elif key in associated_keys:
                #print(key, 'yellow')
                self.key_ui_dict[key].key_toggle.Show(True)
                self.key_ui_dict[key].key_toggle_window.Show(True)
                if highlight:
                    self.key_ui_dict[key].key_toggle_window.SetBackgroundColour(cols[2])
            else:
                self.key_ui_dict[key].key_toggle.Show(False)
                self.key_ui_dict[key].key_toggle_window.Show(False)
                self.key_ui_dict[key].key_toggle_window.SetBackgroundColour(wx.NullColour)


        if set_current:
            if self.current_key_ui.keyword in required_keys:
                self.current_key_ui.ShowItems(True)
            else:
                # Show first keyword in required keys.
                self.key_ui_dict[required_keys[0]].ShowItems(True)
                self.current_key_ui = self.key_ui_dict[required_keys[0]]
                self.current_key_ui.key_toggle.SetValue(True)
                self.current_key_ui.key_toggle.SetFocus()

        #self.on_resize()

        # self.panel1.Layout()
        # self.panel2.Layout()
        # self.splitter_window.Layout()
        #col = (colour[0],colour[1],colour[2],150)
        #if highlight:
        #for key in keys:
        #    print("HL:", key)
        #    print(self.key_ui_dict[key].key_toggle_window.GetBackgroundColour())
        #    self.key_ui_dict[key].key_toggle_window.SetBackgroundColour(col)
        #    print(self.key_ui_dict[key].key_toggle_window.GetBackgroundColour())
        #self.current_key_ui.key_toggle_window.SetBackgroundColour(col)

        self.do_layout((self.panel1,self.panel2,self.splitter_window))
        #Oprint(self.current_key_ui.key_toggle_window.GetBackgroundColour())
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
        if not keys: 
            return True
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
        self.do_layout((self.panel1,self.panel2,self.splitter_window))
        return True

    def do_layout(self,windows):
        if isinstance(windows,list) or isinstance(windows,tuple):
            for window in windows:
                window.Layout()
                window.FitInside()
        else:
            windows.Layout()
            windows.FitInside()
