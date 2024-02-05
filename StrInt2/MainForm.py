import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Lime
		self._label1.Location = System.Drawing.Point(-3, -5)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Text"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(102, -5)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(90, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.Location = System.Drawing.Point(-3, 44)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(99, 88)
		self._button1.TabIndex = 2
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Lime
		self._button2.Location = System.Drawing.Point(93, 44)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 88)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Lime
		self._button3.Location = System.Drawing.Point(192, 44)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 88)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Lime
		self._label2.Location = System.Drawing.Point(-3, 18)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Anagrams?"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightGreen
		self._label3.Location = System.Drawing.Point(103, 20)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(188, 23)
		self._label3.TabIndex = 6
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(192, -5)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(99, 20)
		self._textBox2.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(292, 130)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "StrInt2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text.lower()
		word2 = self._textBox2.Text.lower()
		if len(word) != len(word2):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = word2.index(c)
				if index != -1:
					word2 = word2[0:index] + word2[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(word2) == 0)