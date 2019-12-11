#!/usr/bin/env python3
# Record mouse and keyboard actions and reproduce them identically at will
#
# Copyright (C) 2019 Mairo Rufus <akoudanilo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This module contains all the classes needed to
create the GUI
"""

import os

import control

import wx


class MainDialog(wx.Dialog):
    """
    Main windows of the app, it's a dialog to display_button the app correctly
    even with tiling WMs
    """
    app_text = ["Load Capture", "Save", "Start Capture", "Play",
                "Compile to exe", "Preferences", "Help"]
    settings_text = ["Continuous Playback", "Repeat Playback Loops",
                     "Recording Hotkey", "Playback Hotkey", "Always on Top",
                     "About"]

    def on_settings_click(self, event):
        self.MakeThePopup()
        self.settings_button.PopupMenu(self.settingspopupmenu)
        event.Skip()

    def MakeThePopup(self):
        menu = wx.Menu()
        menu.Append(wx.ID_ANY, self.settings_text[0])
        menu.Append(wx.ID_ANY, self.settings_text[1])
        menu.AppendSeparator()
        menu.Append(wx.ID_ANY, self.settings_text[2])
        menu.Append(wx.ID_ANY, self.settings_text[3])
        menu.AppendSeparator()
        menu.Append(wx.ID_ANY, self.settings_text[4])
        menu.AppendSeparator()
        menu.Append(wx.ID_ANY, self.settings_text[5])
        self.settingspopupmenu = menu

    def __init__(self, *args, **kwds):
        """
        Build the interface
        """
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.file_open_button = wx.BitmapButton(self,
                                                wx.ID_ANY,
                                                wx.Bitmap(os.path.join("..", "img", "file-upload.png"),
                                                          wx.BITMAP_TYPE_ANY))
        self.file_open_button.SetToolTip(self.app_text[0])
        self.save_button = wx.BitmapButton(self,
                                           wx.ID_ANY,
                                           wx.Bitmap(os.path.join("..", "img", "save.png"),
                                                     wx.BITMAP_TYPE_ANY))
        self.save_button.SetToolTip(self.app_text[1])
        self.record_button = wx.BitmapButton(self,
                                             wx.ID_ANY,
                                             wx.Bitmap(os.path.join("..", "img", "video.png"),
                                                       wx.BITMAP_TYPE_ANY))
        self.record_button.SetToolTip(self.app_text[2])
        self.play_button = wx.BitmapButton(self,
                                           wx.ID_ANY,
                                           wx.Bitmap(os.path.join("..", "img", "play-circle.png"),
                                                     wx.BITMAP_TYPE_ANY))
        self.play_button.SetToolTip(self.app_text[3])
        self.compile_button = wx.BitmapButton(self,
                                              wx.ID_ANY,
                                              wx.Bitmap(os.path.join("..", "img", "download.png"),
                                                        wx.BITMAP_TYPE_ANY))
        self.compile_button.SetToolTip(self.app_text[4])
        self.settings_button = wx.BitmapButton(self,
                                               wx.ID_ANY,
                                               wx.Bitmap(os.path.join("..", "img", "cog.png"),
                                                         wx.BITMAP_TYPE_ANY))
        self.settings_button.SetToolTip(self.app_text[5])

        self.Bind(wx.EVT_BUTTON, self.on_settings_click, self.settings_button)

        self.help_button = wx.BitmapButton(self,
                                           wx.ID_ANY,
                                           wx.Bitmap(os.path.join("..", "img", "question-circle.png"),
                                                     wx.BITMAP_TYPE_ANY))
        self.help_button.SetToolTip(self.app_text[6])

        self.__add_bindings()
        self.__set_properties()
        self.__do_layout()

    def load_locale(self):
        """
        Load the interface in user-defined language (default english)
        """
        pass

    def __add_bindings(self):

        # sc = control.SettingsCtrl(self)
        hb = control.AboutCtrl()
        self.Bind(wx.EVT_BUTTON, hb.action, self.help_button)

    def __set_properties(self):
        self.file_open_button.SetSize(self.file_open_button.GetBestSize())
        self.save_button.SetSize(self.save_button.GetBestSize())
        self.record_button.SetSize(self.record_button.GetBestSize())
        self.play_button.SetSize(self.play_button.GetBestSize())
        self.compile_button.SetSize(self.compile_button.GetBestSize())
        self.settings_button.SetSize(self.settings_button.GetBestSize())
        self.help_button.SetSize(self.help_button.GetBestSize())

    def __do_layout(self):
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.file_open_button, 0, 0, 0)
        main_sizer.Add(self.save_button, 0, 0, 0)
        main_sizer.Add(self.record_button, 0, 0, 0)
        main_sizer.Add(self.play_button, 0, 0, 0)
        main_sizer.Add(self.compile_button, 0, 0, 0)
        main_sizer.Add(self.settings_button, 0, 0, 0)
        main_sizer.Add(self.help_button, 0, 0, 0)
        self.SetSizer(main_sizer)
        self.Centre()
        main_sizer.Fit(self)
        self.Layout()