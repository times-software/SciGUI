import scigui.scigui as sg
import wx
class MyApp(wx.App):
    def OnInit(self):
        self.frame = sg.Frame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        # self.frame.Show()
        return True      




#if __name__ == '__main__':
def start():
    app = MyApp(0)
    #frame = MyFrame()
    app.MainLoop()
