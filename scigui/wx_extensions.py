import wx

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

