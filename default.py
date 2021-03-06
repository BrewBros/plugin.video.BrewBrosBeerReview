# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by:Brew Bros
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.BrewBrosBeerReview'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCxxV3Iyk54RUv2BvMZrI3CA"#BrewBrosBeerReview

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="BrewBrosBeerReview",

        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://battleforliberty.com/wp-content/uploads/2017/06/beer-793x526.jpg",
		fanart="Img.youtube.com/vi/Mljo103nzH8&t=4s500/maxtesdefault.jpg",

        folder=True )


   
		
run()
