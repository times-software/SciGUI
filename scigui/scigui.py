import wx
#import wx.richtext
import wx.lib.scrolledpanel
import scigui.input_errors as ie
import sys
import scigui.input_definition as input_definition
import scigui.translate_input as translate_input
from scigui.input_types import *
import os
import pathlib
import scigui.graphing as graphing
from threading import Thread
import scigui.input_page as input_page
import scigui.key_ui_element as key_ui_element

class Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        super().__init__(parent=None, title='Corvus')
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        #wx.Frame.__init__(self, *args, **kwds)
        self.defaultFile = 'corvus.in'
        self.infile = None
        # Set the datafiles
        self.datafile = None
        self.is_running = False
        self.run_aborted = False

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
        #col = wx.GREEN
        #col = (col[0],col[1],col[2],150)
        #self.top_panel.SetBackgroundColour(col)
        #sleep(1)
        #self.top_panel.SetBackgroundColour('')
        #sleep(1)
        #self.top_panel.SetBackgroundColour(col)
        #wx.CallAfter(self.code_choice.SetLabel, 'code')
        #wx.CallAfter(print("label ",self.code_choice.GetLabel()))

        #self.top_panel_sizer.Add()
        #self.Show()
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
        self.inp_page = input_page.input_page(self.main_notebook,self.inp_def)
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

        #self.showAllRequired = wx.CheckBox(self.top_panel,label="Show all required")
        #self.top_panel_sizer.Add(self.showAllRequired,1,wx.ALL,5)
        #self.top_panel_sizer.Add(self.showAllRequired,(1,15),flag=wx.TOP|wx.LEFT,border=top_panel_border)
        #self.showAllRequired.Bind(wx.EVT_CHECKBOX,self.show_all_required)
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
        self.splitter_window0.SetMinimumPaneSize(int(screenHeight/10))
        self.inp_page.splitter_window.SplitVertically(self.inp_page.panel1,self.inp_page.panel2,int(screenWidth/4))
        self.inp_page.splitter_window.SetMinimumPaneSize(int(screenWidth/8))
        #splitter_window2.SplitVertically(panel3,panel4,0)
        self.Bind(wx.EVT_CLOSE,self.onExit)

        self.required = ['target_list']
        self.inp_page.current_key_ui = self.inp_page.key_ui_dict['target_list']
        #self.inp_page.show_only_keywords([])
        #wx.Yield()
        #wx.CallAfter(self.inp_page.show_keywords,['target_list'],[],[],highlight=True,set_current=True)
        #self.inp_page.panel1.SetBackgroundColour((0,0,0,255))
        #self.inp_page.panel1.SetBackgroundColour(wx.ColourDatabase().Find('DARK_SLATE_GREY'))
        self.inp_page.show_keywords(['target_list'],[],[],highlight=True,set_current=True)
        self.inp_page.current_key_ui.ShowItems(True)
        self.inp_page.current_key_ui.enable_checkbox.SetValue(True)
        self.inp_page.current_key_ui.enable_keyword_elements(True)
        self.show_enabled_checkbox.SetValue(True)
        #self.inp_page.on_resize(None,True)
        do_layout(self)
        self.run(None,True)
        
        #sleep(1)
        #self.inp_page.show_only_keywords([])
        #self.inp_page.show_keywords(['target_list'],highlight=True,set_current=True,colour=wx.BLUE)

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
                return False    # the user changed their mind

            # Proceed loading the file chosen by the user
            self.infile = fileDialog.GetPath()
            try:
                self.get_values_dict()
                translate_input.write_corvus_input(self.values_dict,self.infile)

            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)

            dir = pathlib.Path(self.infile).parent
            os.chdir(dir)
            return True
    #####################################################################
    # Event handlers
    #####################################################################

    def abort(self,evt=None):
        obj = evt.GetEventObject()
        obj.SetLabel('Aborting ...')
        f = open('abort_corvus.txt','w')
        f.write('True')
        f.close()
        while self.thread.is_alive():
            wx.Yield()


        self.run_aborted = True
        self.runButton.Enable(True)
        
    def run(self,evt=None,init=False):
        if self.input_type == 'corvus':
            import re
            import sys
            from corvus.controls import oneshot
            # Run corvus with --version to load the libraries. This will make the first run load faster.
            if init:
                sys.argv = ['run-corvus','-v']
                sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
                try:
                    self.thread = Thread(target=oneshot)
                except SystemExit:
                    pass

                self.thread.start()
                return
                
            # If a process is running allow it to abort, then return.
            if self.is_running:
                message = 'Corvus is currently running. Abort the current run?'
                if wx.MessageDialog(self.splitter_window0,message,style=wx.YES_NO).ShowModal() == wx.ID_NO:
                    return
                else:
                    self.abort()

            self.is_running = True
            self.runButton.Enable(False)
            if self.infile is None:
                if not self.save_as(): 
                    self.is_running = False
                    self.runButton.Enable(True)
                    return
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
                        self.is_running = False
                        self.runButton.Enable(True)
                        return
                    elif answer == wx.ID_YES:
                        self.get_values_dict()
                        translate_input.write_corvus_input(self.values_dict,self.infile)
                    elif answer == wx.ID_NO:
                        if not self.save_as(): 
                            self.is_running = False
                            self.runButton.Enable(True)
                            return
           
            if not self.values_dict: 
                message = 'You have not enabled any keywords. The input file is empty and corvus will not run.'
                with wx.MessageDialog(self.splitter_window0,message,style=wx.OK) as md:
                    md.ShowModal()
                    self.is_running = False
                    self.runButton.Enable(True)
                    return

            title = 'Corvus is running ...' 
            message = 'This will take time. You can see the \noutput on the associated terminal.'
            md = wx.Dialog(self.splitter_window0,title=title)
            text = wx.StaticText(md,label=message,style=wx.ALIGN_CENTRE_HORIZONTAL)
            md_sizer = wx.BoxSizer(wx.VERTICAL)
            md_sizer.Add(text,0,wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL,10)
            abort_button = wx.Button(md,label='Abort Calculation',style=wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL)
            md_sizer.Add(abort_button,0,wx.ALL|wx.ALIGN_CENTRE,20)
            abort_button.Bind(wx.EVT_BUTTON,self.abort)
            md.SetSizer(md_sizer) 
            text.Wrap(md.GetSize()[0]-10)
            sys.argv = ['run-corvus','-i',self.infile]
            sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
            try:
                self.thread = Thread(target=oneshot)
            except SystemExit:
                pass
            self.thread.start()
            md.Show()
            while self.thread.is_alive():
                wx.Yield()
            if self.run_aborted:
                message = 'Corvus was aborted.'
                self.run_aborted = False
            else:
                message = 'Corvus is finished.'
            text.SetLabel(message)
                
            wx.CallLater(3000,md.Destroy)
            
            self.is_running = False
            self.runButton.Enable(True)

    def on_plot_button(self,evt):
        if self.datafile is None:
            graphing.plot()
        else:
            graphing.plot(self.datafile)
    # Show only the kewords selected by the filter choices.
    #def show_only_required_keywords(self):
    def set_values_from_predefined(self,evt):
        obj = evt.GetEventObject()
        # Turn of the show only enabled checkbox.
        self.show_enabled_checkbox.SetValue(False)
        predef = obj.GetString(obj.GetSelection())
        if predef == "Quick Start":
            #evt.Skip()
            return
        key_list = []
        useful_key_list = []
        associated_key_list = []
        vals_dict = {}
        for key,value in self.inp_def.predefined.items():
            if key == predef:
                pred_dict = value
                for k,v in pred_dict.items():
                    if k == '_required':
                        # Show these keywords, and highlight. Don't set enabled.
                        key_list = key_list + v
                    elif k == '_useful':
                        useful_key_list = useful_key_list + v
                    elif k == '_associated':
                        associated_key_list = associated_key_list + v
                    else:
                        # Set the values and show
                        key_list = key_list + [k]
                        vals_dict[k] = v
        message = 'Would you like to overwrite your settings with new ones? If no, the relevant keywords will be shown ' + \
        'without changing the settings.'
        md = wx.MessageDialog(self.splitter_window0,message,style=wx.YES_NO|wx.CANCEL)
        answer = md.ShowModal()
        if  answer == wx.ID_CANCEL:
                        return
        elif answer == wx.ID_YES:
            self.Reset()
            self.set_values(vals_dict)
        # Fist hide all keywords
        #self.inp_page.show_only_keywords([])
        #wx.Yield()
        # Now show required keywords with highlighted color outline.
        self.inp_page.show_keywords(key_list,useful_key_list,associated_key_list,highlight=True,set_current=True)
        self.code_choice.SetSelection(self.code_choice.FindString('all'))
        self.category_choice.SetSelection(self.category_choice.FindString('all'))
        self.Layout()
        
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
        #print('Wrap size:',int(splitter_window.GetWindow2().GetSize().width - 5))
        #self.inp_page.current_key_ui.help_text_ui.Wrap(int(splitter_window.GetWindow2().GetSize().width - 10))
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
            self.onExit(evt)

def do_layout(windows):
    if isinstance(windows,list) or isinstance(windows,tuple):
        for window in windows:
            window.Layout()
            window.FitInside()
    else:
        windows.Layout()
        windows.FitInside()
