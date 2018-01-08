import sys
from PySide import QtGui, QtCore
import hou

cntxt=hou.node("obj/dust_emitter")
number_child_node=0
children=cntxt.children()
for child in children:
    if child.name()=="DUST_PARM":
        number_child_node+=1
if number_child_node==0:
    hou.hda.installFile("/SCORPION/PYTHON/WALK_DUST/FINAL_CODE/DUST_PARMS.otl")
    gui_parm_nodes=cntxt.createNode("DUST_PARMS","DUST_PARM")
    dopio=hou.node("obj/dust_emitter/DOPIO")
    gui_parm_nodes.setInput(0,dopio)
    gui_parm_nodes.setDisplayFlag(True)
    cntxt.layoutChildren()



class Window(QtGui.QMainWindow):
    def __init__(self):      
        super(Window, self).__init__()
        self.setGeometry(1020,455,520,300) 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("DUST MAKER")
        self.setWindowIcon(QtGui.QIcon("/Desktop/icon/running_horse_lines___free_by_the_bone_snatcher-d57uvda.png"))
        

        self.bg=QtGui.QLabel(self)
        self.bg.setGeometry(0,0,520,300)
        self.bg.setPixmap(QtGui.QPixmap("/SCORPION/PYTHON/WALK_DUST/bg/horse_label_7.png"))
        
#CREATE LABEL

        self.robot_label=QtGui.QLabel("ROBOT",self)
        self.robot_label.setGeometry(15,30,50,35)
        self.robot_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

        self.dog_label=QtGui.QLabel("DOG",self)
        self.dog_label.setGeometry(15,60,40,35)
        self.dog_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

        self.trex_label=QtGui.QLabel("TREX 1",self)
        self.trex_label.setGeometry(15,90,40,35)
        self.trex_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

        self.monster_label=QtGui.QLabel("MONSTER",self)
        self.monster_label.setGeometry(15,120,60,35)
        self.monster_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

        self.walk_label=QtGui.QLabel("WALK",self)
        self.walk_label.setGeometry(75,5,40,35)
        self.walk_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

        self.crawl_label=QtGui.QLabel("CRAWL",self)
        self.crawl_label.setGeometry(140,5,45,35)
        self.crawl_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")
        
        self.density_label=QtGui.QLabel("DENSITY",self)
        self.density_label.setGeometry(240,10,90,35)
        self.density_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")
        
        self.velocity_label=QtGui.QLabel("VELOCITY",self)
        self.velocity_label.setGeometry(240,45,60,35)
        self.velocity_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")
        
        self.contact_label=QtGui.QLabel("CONTACT POINTS",self)
        self.contact_label.setGeometry(360,10,110,35)
        self.contact_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")
        
        self.dynamic_label=QtGui.QLabel("DYNAMIC BOUND",self)
        self.dynamic_label.setGeometry(360,45,110,35)
        self.dynamic_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

        self.density_mult_label=QtGui.QLabel("DENSITY MULT",self)
        self.density_mult_label.setGeometry(240,87,90,35)
        self.density_mult_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")
        
        self.trex2_label=QtGui.QLabel("TREX 2",self)
        self.trex2_label.setGeometry(15,150,45,35)
        self.trex2_label.setStyleSheet("QLabel{color:rgb(230,190,138)}")

#CREATE RADIO BUTTON

        self.btngp1=QtGui.QButtonGroup(self)
        self.robot_radio_btn=QtGui.QRadioButton(self)
        self.robot_radio_btn.setGeometry(80,35,20,20)
        self.robot_radio_btn.clicked.connect(self.robot_dust)
        
        self.crawl_radio_btn=QtGui.QRadioButton(self)
        self.crawl_radio_btn.setGeometry(150,35,20,20)
        self.crawl_radio_btn.clicked.connect(self.crawl_dust)

        self.dog_radio_btn=QtGui.QRadioButton(self)
        self.dog_radio_btn.setGeometry(80,65,20,20)
        self.dog_radio_btn.clicked.connect(self.dog_dust)

        self.trex1_radio_btn=QtGui.QRadioButton(self)
        self.trex1_radio_btn.setGeometry(80,95,20,20)
        self.trex1_radio_btn.clicked.connect(self.trex1_dust)

        self.monster_radio_btn=QtGui.QRadioButton(self)
        self.monster_radio_btn.setGeometry(80,125,20,20)
        self.monster_radio_btn.clicked.connect(self.monster_dust)
        
        self.trex2_radio_btn=QtGui.QRadioButton(self)
        self.trex2_radio_btn.setGeometry(80,155,20,20)
        self.trex2_radio_btn.clicked.connect(self.trex2_dust)
        
        self.btngp1.addButton(self.robot_radio_btn)
        self.btngp1.addButton(self.crawl_radio_btn)
        self.btngp1.addButton(self.dog_radio_btn)
        self.btngp1.addButton(self.trex1_radio_btn)
        self.btngp1.addButton(self.monster_radio_btn)
        self.btngp1.addButton(self.trex2_radio_btn)
        
        
        self.btngp2=QtGui.QButtonGroup(self)
        self.density_radio_btn=QtGui.QRadioButton(self)
        self.density_radio_btn.setGeometry(315,15,25,25)
        self.density_radio_btn.clicked.connect(self.density_visual)
        
        self.velocity_radio_btn=QtGui.QRadioButton(self)
        self.velocity_radio_btn.setGeometry(315,50,25,25)
        self.velocity_radio_btn.clicked.connect(self.veloctiy_visual)
        
        self.contact_radio_btn=QtGui.QRadioButton(self)
        self.contact_radio_btn.setGeometry(485,15,25,25)
        self.contact_radio_btn.clicked.connect(self.contact_visual)
        
        self.dynamic_radio_btn=QtGui.QRadioButton(self)
        self.dynamic_radio_btn.setGeometry(485,50,25,25)
        self.dynamic_radio_btn.clicked.connect(self.dynamic_visual)
        
        self.btngp2.addButton(self.density_radio_btn)
        self.btngp2.addButton(self.velocity_radio_btn)
        self.btngp2.addButton(self.contact_radio_btn)
        self.btngp2.addButton(self.dynamic_radio_btn)
        self.btngp_initial_visulaisation()

        
        
#CREATE BUTTON
        
        self.sim_btn=QtGui.QPushButton("SIM",self)
        self.sim_btn.setGeometry(120,70,80,25)
        self.sim_btn.setStyleSheet("QPushButton{color:rgb(230,190,138);background-color:rgb(70,70,70)}")
        self.sim_btn.clicked.connect(self.sim_btn_click)

        self.reset_btn=QtGui.QPushButton("RESET",self)
        self.reset_btn.setGeometry(120,110,80,25)
        self.reset_btn.setStyleSheet("QPushButton{color:rgb(230,190,138);background-color:rgb(70,70,70)}")
        self.reset_btn.clicked.connect(self.reset_btn_click)
               
        
#CREATE SLIDER        
        
        self.density_mult_slider=QtGui.QSlider(self)
        self.density_mult_slider.setOrientation(QtCore.Qt.Horizontal)
        self.density_mult_slider.setGeometry(335,97,90,15)
        self.density_mult_slider.setRange(0,5)
        self.density_mult_slider.setStyleSheet("QSlider{background-color:rgba(230,190,138,15)}")
        self.density_mult_slider.valueChanged.connect(self.densitymult_slider)
        
        
#CREATE VALUE BOX

        self.density_mult_value = QtGui.QDoubleSpinBox(self)
        self.density_mult_value.setGeometry(435,95,50,20)
        self.density_mult_value.setRange(0,5)
        self.density_mult_value.valueChanged.connect(self.density_mult_value_change)
        self.density_multiplier_value()
        
        
#CREATE SEPARATOR

        self.separator=QtGui.QFrame(self)
        self.separator.setGeometry(225,15,2,111)
        self.separator.setStyleSheet("QFrame{background-color:rgb(230,190,138)}")
        self.separator.setFrameShape(QtGui.QFrame.VLine)
        
        
#############
#############
#FUNCTION
    def btngp_initial_visulaisation(self):
        self.density_radio_btn.setChecked(1)
        self.robot_radio_btn.setChecked(1)

    def density_multiplier_value(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/density')
        y=x.eval()
        self.density_mult_value.setValue(y)
        self.density_mult_slider.setValue(y)
       

    def density_mult_value_change(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/density')
        y=self.sender().value()
        x.set(y)
        self.density_mult_slider.setValue(y)
    
    def densitymult_slider(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/density')
        y=self.sender().value()
        x.set(y)
        self.density_mult_value.setValue(y)
        
    def sim_btn_click(self):
        hou.parm('/obj/dust_emitter/DUST_PARM/SIM').pressButton()
        
    def reset_btn_click(self):
        hou.parm('/obj/dust_emitter/DUST_PARM/RESET').pressButton()

    def robot_dust(self):
        x=hou.parm('/obj/animation/PICK_ANIMATION')
        x.set(0)
        
    def crawl_dust(self):
        x=hou.parm('/obj/animation/PICK_ANIMATION')
        x.set(1)
        
    def dog_dust(self):
        x=hou.parm('/obj/animation/PICK_ANIMATION')
        x.set(2)
        
    def trex1_dust(self):
        x=hou.parm('/obj/animation/PICK_ANIMATION')
        x.set(3)
        
    def monster_dust(self):
        x=hou.parm('/obj/animation/PICK_ANIMATION')
        x.set(4)
        
        
    def trex2_dust(self):
        x=hou.parm('/obj/animation/PICK_ANIMATION')
        x.set(5)
        
    def density_visual(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/input')
        x.set(0)
    
    def veloctiy_visual(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/input')
        x.set(1)
    
    def contact_visual(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/input')
        x.set(2)
    
    def dynamic_visual(self):
        x=hou.parm('/obj/dust_emitter/DUST_PARM/input')
        x.set(3)
        
        
 
app = QtGui.QApplication.instance()
dialog = Window()
dialog.show()  


