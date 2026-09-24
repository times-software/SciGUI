import sys

if sys.platform == "win32":
    try:
        import ctypes
        # 1. Define the API function
        SetProcessDpiAwarenessContext = ctypes.windll.user32.SetProcessDpiAwarenessContext
        
        # 2. CRITICAL FOR 64-BIT: Explicitly set the argument type to a pointer/handle width
        SetProcessDpiAwarenessContext.argtypes = [ctypes.c_void_p]
        
        # 3. Pass the PerMonitorV2 handle value (-4) safely
        SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
    except Exception as e:
        # Fallback for older Windows 10 setups
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            pass

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
    print("Initializing ...",flush=True)
    app = MyApp(0)
    #frame = MyFrame()
    app.MainLoop()
