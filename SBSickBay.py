#!/usr/bin/python
# -*- coding: utf-8 -*-
"""SickBay @version 0.x
@link    https://github.com/KabukiStarship/SickBay.git
@file    /SickBay.py
@author  Cale McCollough <https://cale-mccollough.github.io>
@license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
reserved (R). This Source Code Form is subject to the terms of the Mozilla 
Public License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at <https://mozilla.org/MPL/2.0/>. """
 
from SBNode import SBNode
from SBDevice import SBDevice
from SBHuman import SBHuman
from SBVentilator import SBVentilator
from GHVentilator import GHVentilator
#import sched, time

#Scheduler = sched.scheduler(time.time, time.sleep)
  
# The SickBay app object.
class SBSickBay(SBNode):
  # Constants
  StateMonitoring = 1     #< State: Monitoring.
  StateShuttingDown = 2   #< State: Shutting down.
  NIDCount = 0            #< The total number of SBNodes.

  def __init__(self):
    SBNode.__init__(self, "Device", "SickBay", "Root", "The root scope.")
    self.Node = self               #< The currently selected node.
    self.Stack = []                #< The stack of SBNodes.
    self.State = self.StateMonitoring #< The app state.
    self.Devices = []              #< A list of Devices this SickBay supports.

    self.PatientsAddTestPatients()
    self.ConsoleMain()
  
  def NIDNext(self):
    Result = self.NIDCount
    self.NIDCount = Result + 1
    return Result

  # Add Device
  def DevicesAdd(self, DeviceName):
    self.Devices.append(DeviceName)

  # Console main loop.
  def ConsoleMain(self):
    print ("\n\nWelcome to SickBay.\n")
    while True:
      UserInput = input("\n> ")
      if(self.Node != None):
        self.Node.Command(self, UserInput)
      else:
        print("\nWe need to add some nodes.")
  
  # Pushes an SBNode onto the stack.
  def Push(self, NodeNew):
    self.Stack.append(self.Node)
    self.Node = NodeNew
  
  # Pops an SBNode off the stack.
  def Pop(self):
    if len(self.Stack) == 0:
      return
    self.Node = self.Stack.pop()
  
  # Enters the monitoring state.
  def MonitorBegin(self):
    #Scheduler.enter(1, 1, self.Update, ())
    #Scheduler.run()
    print("\n\nBeginning monitoring...")

  # Handler for the init app state.
  def PatientsAddTestPatients (self):
    print ("\n\nAdding test patients.")
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "John Doe 1", "M", 170.0, 70.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "John Doe 2", "M", 180.0, 75.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "John Doe 3", "M", 190.0, 80.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "John Doe 4", "M", 200.0, 85.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "Jane Doe 1", "F", 120.0, 55.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "Jane Doe 2", "F", 130.0, 60.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "Jane Doe 3", "F", 140.0, 65.0))
    self.Node.NodesAdd (SBHuman(self.NIDNext(), "Jane Doe 4", "F", 150.0, 70.0))
    self.Node.NodesAdd (GHVentilator(self.NIDNext()))
  
  # Handler for the Monitor app state.
  def StateMonitorHandle(self):
    for Patient in self.Patients:
      Patient.PrintStats()
  
  def StateShutDownHandle(self):
    print ("\n\nShutting down...")
    
  # Prints the most current and important stats to the Console.
  def PrintStats(self):
    for Patient in self.Patients:
      Patient.PrintStats()
 
  # Function that is called every x seconds to update everything.
  def Update(self):
    #print ("\n\nUpdate Time:", time.time())
    Handler = {
      1: self.StateMonitorHandle,
      2: self.StateShutDownHandle
    }
    # Get the function from switcher dictionary
    Handle = Handler.get(self.State, lambda: "Invalid state")
    # Execute the function
    Handle()
    self.PrintStats()
    #Scheduler.enter(1, 1, self.Update, ())

if __name__ == '__main__':
  SickBayConsole = SBSickBay()
  #unittest.main()