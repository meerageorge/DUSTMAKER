# DUSTMAKER

## Description:

## Department: FX

For shots that need to emit dust from the ground when some charater is walking or running or animated from one point to another in anyway we can use this tool. This was done based on a requirement for shots which involed repeated walk cycles of different kinds of animals

So for that the walk cycle of the all characters was called and made it possible to switch the character and do the dust simulation based on which character dust was 
required. The selection of walk cycle was made little more with the help of a GUI. This tool does not require a ground plane. It is automatically calculated.


## Getting Started
We need animated scene file of charcter or characters and a geo node having an object merge which contains the path of the walk cycle.
This shelf tool has 2 parts:

		1. creating dust for the walk cycle

		2. Building GUI - to switch between the character 

## Creating dust 
Create an object merge inside a geo node. Give the path of animation out node in the obj path of object merge and select the object merge and click the shelf tool.
It will create some nodes and a dop network to create dust simulation and also create a dopio node to import the simulation.

## Building the GUI
This part is to graphically change the character of animation and change the visualisation of simulation of dust like velocity or bounding box or source.
Inaddition to that I have tried to change density of dust after simulation.
    
## Prerequisites
This tool is built for Houdini
It is tested on Linux and OSX
This code is written using Python 2.7 and PySide
Houdini 15.5 supports Pyside by default.



## Features of the tool

		1.The Tool allows FX department to create dust simulation on clicking it after
		just combine all kinds of walk cycle from one point to another and of different
		characters on to a switch node and out its path to a new object merge in a 
		geometry node

		2.The Tool also allows it to manually modify the dust parameters.

		3.The Tool works with all form of character with any number of legs or can even 
		work for moving objects

		4.The Tool allows the user to switch the character and animation.

		5.The Tool has additional change the visualisation of velocity, density or bounds 
		or contact points

		6.The Tool automatically ensures that dust is generated only from contact points 
		and is visible as long as it is completely dissipated

## STEPS:

		1. Create an object merge inside a geo node. Give the path of the animation out 
		to the obj path of object merge

		2. Click on the ‘IMPORT_ALL_DUST_CHAR_FILES’ shelf tool. It create node inside 
		the geo node and will name the geo node 'dust_emitter'
				parentnode.setName("dust_emitter") 
				
## dust_emitter creation:

		1. Checks for selection of object merge node if not will display message.
				sel_node = hou.selectedNodes()
				if len(sel_node) < 1:
		   			 hou.ui.displayMessage('select a node')
		   		if node.type().name()!="object_merge":
            		hou.ui.displayMessage("wrong node selected\nplease select an object_merge")
					 
		2. Create nodes 
				node=geo.createNode("xform")
				
		3. Set input to all created nodes
				node.setInput(0,node)
				
		4. Set parameter of nodes
				parameter=node.parm(“parm_name”)
				parameter.set(value)
				Or if it is an expression:
				parameter.setExpression(“expression”)
				
		5. Create dop network to do dust simulation and is imported by creating dopio node

		6. The dopio preset parameter is set using:
				dopioprsts={"node":dopio, "script_value0":"pyro"}
				dopio.hm().invokePresetMenu(dopioprsts) 

## Creation of GUI:
		
		1. An otl is improted to change they density of dust and visualitation

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
		One group helps to select animation and another helps to select visualisation
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


