#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Jun 29 14:50:07 2008

import wx, reprap.preferences

# begin wxGlade: extracode
# end wxGlade



class PreferencesPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PreferencesPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        
        self.prefHandler = reprap.preferences.PreferenceHandler(self,  "plotter_svg.conf")
        
        # default values for preferences

        self.prefHandler.load()
        self.setPrefValues()

    def __set_properties(self):
        # begin wxGlade: PreferencesPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PreferencesPanel.__do_layout
        pass
        # end wxGlade
    # Set values of frame control
    def setPrefValues(self):
        #self.choice_mode.SetSelection(self.pref_plotMode)
        pass
    
    def savePrefValues(self):
        #self.pref_plotMode = int(self.choice_mode.GetSelection())
        self.prefHandler.save()

# end of class PreferencesPanel


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = PreferencesPanel(self, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_2")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.panel_1, 1, wx.ALL|wx.EXPAND, 10)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_2 = MyDialog(None, -1, "")
    app.SetTopWindow(dialog_2)
    dialog_2.Show()
    app.MainLoop()
