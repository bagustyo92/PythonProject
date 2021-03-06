#!/usr/bin/python

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution. 
#
# The Eclipse Distribution License is available at 
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This shows an example of using the publish.single helper function.

import sys
import paho.mqtt.publish as publish


publish.single("sensor/data1", "200", hostname="139.59.225.39", password=)
publish.single("sensor/data2", "300", hostname="139.59.225.39")
publish.single("sensor/data3", "400", hostname="139.59.225.39")