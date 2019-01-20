#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Get_Roaster_State

import Pyro4

roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
s = roast_control.output_current_state()
print(','.join(s.split(',')[0:2]))
# print ("{},0.0".format(roast_control.output_current_state()[0:3]))
