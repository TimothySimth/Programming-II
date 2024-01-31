import System.Drawing
import math
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Brown
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(3, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(382, 303)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkGreen
		self._button1.Location = System.Drawing.Point(129, 322)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 110)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.CornflowerBlue
		self._button2.Location = System.Drawing.Point(3, 322)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 110)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.CornflowerBlue
		self._button3.Location = System.Drawing.Point(260, 322)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 110)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self.ClientSize = System.Drawing.Size(392, 444)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for i in range(51):
			self._listBox1.Items.Add(str(i) + "\t" + str(i**2) + "\t" + str(math.sqrt(i))) 

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		
	def Button3Click(self, sender, e):
		Application.Exit()