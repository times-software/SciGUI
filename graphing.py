import wx
import os

import numpy as np

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import \
    NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure


class MyNavigationToolbar(NavigationToolbar):
    """Extend the default wx toolbar with your own event handlers."""

    def __init__(self, canvas,legend_texts):
        super().__init__(canvas)
        # Remove some toolitems
        self.DeleteToolByPos(6)

        # We use a stock wx bitmap, but you could also use your own image file.
        # Create a file open tool.
        file_open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR)
        file_open_tool = self.InsertTool(7,wx.ID_ANY, 'Open', file_open_bmp,shortHelp = 'Import Data')
        self.Bind(wx.EVT_TOOL, self._on_file_open, id=file_open_tool.GetId())

        # Create a settings tool.
        settings_bmp = wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_TOOLBAR)
        settings_tool = self.InsertTool(9,wx.ID_ANY, 'Settings', settings_bmp,shortHelp = 'Settings')
        self.Bind(wx.EVT_TOOL, self._on_settings, id=settings_tool.GetId())
        self.legend_texts= legend_texts
        self.Realize()
        self.canvas = canvas

    def _on_file_open(self, event):
        # add some text to the Axes in a random location in axes coords with a
        # random color]
        ax = self.canvas.figure.axes[0]
        with wx.FileDialog(self,defaultDir=os.getcwd(),
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

        # Proceed loading the file chosen by the user
            file = fileDialog.GetPath()
            try:
                data  = np.loadtxt(file,unpack=True)
                if data.size >= 2:
                    # Ask user what columns they want.
                    ix=1
                    iy=2
                    parameters = ['x-axis label', 'y-axis label']
                    vals = ['1','2']
                    dlg = ParameterDialog(parameters,vals)
                    # Display as a modal dialog
                    result = dlg.ShowModal()
                    # Check which button was pressed and take the appropriate action
                    if result == wx.ID_OK:
                        print("Dialog: OK")
                        # Retrieve the parameters values and print them
                        parameter_values = dlg.GetParameters()
                        try:
                            ix=int(parameter_values[0])
                            iy=int(parameter_values[1])
                        except:
                            ix=1
                            iy=2
                elif data.size == 2:
                    ix = 1
                    iy = 2

                x = data[ix-1]
                y = data[iy-1]

                self.legend_texts=self.legend_texts + [str(file)]
                ax.plot(x,y)
                ax.legend(labels=self.legend_texts,fancybox=True, shadow=True,draggable=True,loc='upper left')
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)

        self.canvas.draw()
        event.Skip()

    def _on_settings(self,event):
       # Open a dialog.
       ax = self.canvas.figure.axes[0]
       #legend_texts = legend.get_texts() # This assumes this is a simple 2d plot. 
       parameters = ['x-axis label', 'y-axis label']
       vals = []
       vals = vals + [ax.get_xlabel()]
       vals = vals + [ax.get_ylabel()]
       vals = vals + self.legend_texts
       print(vals)
       for it, text in enumerate(self.legend_texts):
          parameters = parameters + ['Legend '+str(it)]
       dlg = ParameterDialog(parameters,vals)

       # Display as a modal dialog
       result = dlg.ShowModal()
       # Check which button was pressed and take the appropriate action
       if result == wx.ID_OK:
           print("Dialog: OK")
           # Retrieve the parameters values and print them
           parameter_values = dlg.GetParameters()
           # First 2 parameters are x-axis, y-axis
           ax.set_xlabel(parameter_values[0])
           ax.set_ylabel(parameter_values[1])
           print(len(parameter_values))
           print(parameter_values) 
           if len(parameter_values) > 2: 
              self.legend_texts = parameter_values[2:]
              ax.legend(labels=self.legend_texts,fancybox=True,shadow=True,draggable=True,loc='upper left')
              self.canvas.draw()
              #for i,val in enumerate(parameter_values[2:]):
              #   legend_texts[i].set_text(val)
           #self.canvas.draw()
           #ax.legend(fancybox=True,shadow=True)
       elif result == wx.ID_CANCEL:
           print("Dialog: Cancel")
           # Destroy the dialog window so we can close safely this one when we exit
       dlg.Destroy()

class ParameterDialog(wx.Dialog):
    """Subclass wx.Dialog to create the application-specific dialog."""
    def __init__(self, parameters, vals = None):
        # Create the dialog
        # https://docs.wxpython.org/wx.Dialog.html
        super().__init__(parent=None, title="Graph Settings")
        # Create a sizer for the data input controls 
        # https://docs.wxpython.org/wx.GridBagSizer.html
        controls = wx.GridBagSizer(5, 5)
        # Keep the input fields in an array for easy access later
        self.fields = []
        # Add the input fields: a label and text input for each required parameter
        for row, param in enumerate(parameters):
            # Label: https://docs.wxpython.org/wx.StaticText.html
            if vals is None:
               val = ""
            else:
               val = vals[row]

            label = wx.StaticText(self, label=param, style=wx.ALIGN_RIGHT)
            # Text input field: https://docs.wxpython.org/wx.TextCtrl.html
            self.fields.append(wx.TextCtrl(self, value=val, size=(120, -1)))
            controls.Add(label, pos=(row, 0), flag=wx.ALIGN_RIGHT)
            controls.Add(self.fields[row], pos=(row, 1))
        # Create the standard dialog buttons we need
        buttons = self.CreateButtonSizer(flags=wx.OK | wx.CANCEL)
        # Add the controls above the buttons
        # https://docs.wxpython.org/wx.BoxSizer.html
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(controls, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        sizer.Add(buttons, proportion=0, flag=wx.ALL | wx.EXPAND)
        # Add the sizer to the dialog and make the dialog box just the right
        # size for the contents
        self.SetSizerAndFit(sizer)

    def GetParameters(self) -> list[str]:
        """Return the values in the text fields"""
        return [field.GetValue() for field in self.fields]


class plot(wx.Frame):

    def __init__(self,file = None,title=''):
        screenSize = wx.DisplaySize()
        screen_ppi = wx.Display().GetPPI()
        screenWidth = screenSize[0]/screen_ppi[0]
        screenHeight = screenSize[1]/screen_ppi[1]
        size = (screenWidth,screenHeight)
        super().__init__(None, -1, title)
        self.figure = Figure(figsize=size)
        self.axes = self.figure.add_subplot()
        self.axes.format_coord = lambda x, y: ""
        self.axes.set_xlabel('E (eV)')
        self.axes.set_ylabel('XANES')
        self.legend_texts = []
        #for el in dir(self.axes.xaxis.label):
        #   print(el)
  

        if file is not None:
           x, y = np.loadtxt(file,usecols=(0,1),unpack=True)
           self.legend_texts = self.legend_texts + [str(file)]
           self.plt = self.axes.plot(x,y)
           self.axes.legend(labels=self.legend_texts,fancybox=True,shadow=True,draggable=True,loc='upper left')

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        print(self.legend_texts)
        self.toolbar = MyNavigationToolbar(self.canvas,self.legend_texts)
        self.toolbar.Realize()
        # By adding toolbar in sizer, we are able to put it at the bottom
        # of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)

        # update the axes menu on the toolbar
        self.toolbar.update()
        self.figure.tight_layout()
        self.SetSizer(self.sizer)
        self.Fit()
        self.Show(True)

    def _on_close(self,evt):
       obj = evt.GetEventObj()
       obj.Destroy()
