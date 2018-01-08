# DUSTMAKER

		Reel : ( https://vimeo.com/249388964 )
		Password: reel2018

## Description:

## Department: FX

This tool was created for any form of contact dust.Character/s could be walking or 
running.This tool can also work with a crowd system. This was initially based on a 
requirement for shots which involved repeated walk cycles of different kinds of animals.
The selection of character/s is made with the help of a GUI.

ground plane calculation:
If there is no ground plane available from layout,
This tool can also calculate a ground plane based on walk cycle of the character/s.


## Getting Started
We need an object merge which contains the path of the walk cycle.

This code is split based on 2 shelf tools:

		1. creating dust based on imported walk cycle

		2. Building GUI - to switch between the character 

## Creating dust 
the first tool would create all the sop nodes and a dop network required to 
create the dust simulation.

## Building the GUI
I have tested the dust maker with a variety of characters with different animations.
The second tool opens a GUI from which user can change which character / animation
they would like to run the dust maker on.

## Prerequisites
This tool is built for Houdini
It is tested on Linux and OSX
This code is written using Python 2.7 and PySide
Houdini 15.5 supports Pyside by default.



## Features of the tool

		1. This Tool allows FX department to create dust simulations with minimal
		artistic involvement.This task can be automated further to run from a shell on batch mode. This would mean fx can concentrate on more complex elements instead of repetitive fx like foot dust.
		
		2. This Tool can work with crowds as well.

		3. Automatic ground calculation means that fx can try the setup with rough 
		animation even before layout has actually setup a ground plane

		4. The tool automatically resizes container size based on character size and 
		motion to keep the sim super light weight to calculate. 

		5. The UI has option to jump between different characters / animation

		6. There are controls of user to simulate / reset the sim
		
		7. The UI allows user to visualize density / velocity / contact points of emission

		8. There is a post sim density control in the GUI.


## STEPS:

		1. Create an object merge inside a geo node with path of animation.

		2. Click on the ‘IMPORT_ALL_DUST_CHAR_FILES’ shelf tool. It create node inside 
		the geo node and will name the geo node as 'dust_emitter'
				parentnode.setName("dust_emitter") 
				
## dust_emitter creation:

		1. Checks for selection of object merge node if not will display message.
				sel_node = hou.selectedNodes()
				if len(sel_node) < 1:
		   			 hou.ui.displayMessage('select a node')
		   		if node.type().name()!="object_merge":
            		hou.ui.displayMessage("wrong node selected \n please select an object_merge")
					 
		2. Create nodes 
				node = geo.createNode("xform")
				
		3. Set input to all created nodes
				node.setInput(0,node)
				
		4. Set parameter of nodes
				parameter = node.parm(“parm_name”)
				parameter.set(value)
				Or if it is an expression:
				parameter.setExpression(“expression”)
				
		5. Create dop network to do dust simulation and is imported by creating dopio node

		6. The dopio preset parameter is set using:
				dopioprsts={"node":dopio, "script_value0":"pyro"}
				dopio.hm().invokePresetMenu(dopioprsts) 

## Creation of GUI:
		
		1. An otl is imported to change they density of dust and visualization
			hou.hda.installFile("/SCORPION/PYTHON/WALK_DUST/FINAL_CODE/DUST_PARMS.otl")
			gui_parm_nodes=cntxt.createNode("DUST_PARMS","DUST_PARM")

		2. Created graphical user interface with pyside

		3. Window title is 'DUST MAKER' with a horse gallop icon

		4. Has some labels for selecting the character animation and selecting the
		display of simulation.

		Size and position of label is set using setGeometry. 
		Text color style is done by setStyleSheet
				self.robot_label=QtGui.QLabel("ROBOT",self)
				self.robot_label.setGeometry(15,30,50,35)
				self.robot_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")
		5. Two radio button groups are used.
		One group helps to select animation and another helps to select visualization
	        	self.btngp1=QtGui.QButtonGroup(self)
	        	self.robot_radio_btn=QtGui.QRadioButton(self)
	        	self.btngp1.addButton(self.robot_radio_btn)

	    	6. There are push buttons to do simulation of dust of selected character and 
	    	a reset to clear previous simulation
	        	self.sim_btn=QtGui.QPushButton("SIM",self)
	        	self.sim_btn.clicked.connect(self.sim_btn_click)
	        	hou.parm('/obj/dust_emitter/DUST_PARM/SIM').pressButton()

	    	7. There is a density multiplier to vary density of dust even after simulation
	        	self.density_mult_slider=QtGui.QSlider(self)
	        	self.density_mult_slider.setOrientation(QtCore.Qt.Horizontal)
	        	self.density_mult_value = QtGui.QDoubleSpinBox(self)
	        	x=hou.parm('/obj/dust_emitter/DUST_PARM/density')
	        	y=x.eval()
	        	self.density_mult_value.setValue(y)
	        	self.density_mult_slider.setValue(y)
                                           


## FINAL RESULT:

		Reel : ( https://vimeo.com/249388964 )

		Password: reel2018

		Reel Time: 1-2 min


## LIVE SYSTEM
This tool can be easily used in production, as it is built using Houdini and Python
It has been tested and used on Linux and OSX

## Built With
		sublime text 2

		github for versioning

## Authors
This code is entirely written by Meera George.
It was developed in production for my previous company,
This is a simplified version of the same code.

## Acknowledgments
I would like to thank
GITHUB, CODEFIGHTS.COM, UDEMY, ODFORCE SCRIPTING FORUM,CG SOCIETY,
SIDEFX FORUM which helped me complete this tool.


