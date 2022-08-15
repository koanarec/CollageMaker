<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
	Inherits System.Windows.Forms.Form

	'Form overrides dispose to clean up the component list.
	<System.Diagnostics.DebuggerNonUserCode()>
	Protected Overrides Sub Dispose(ByVal disposing As Boolean)
		Try
			If disposing AndAlso components IsNot Nothing Then
				components.Dispose()
			End If
		Finally
			MyBase.Dispose(disposing)
		End Try
	End Sub

	'Required by the Windows Form Designer
	Private components As System.ComponentModel.IContainer

	'NOTE: The following procedure is required by the Windows Form Designer
	'It can be modified using the Windows Form Designer.  
	'Do not modify it using the code editor.
	<System.Diagnostics.DebuggerStepThrough()>
	Private Sub InitializeComponent()
		Me.PictureBox1 = New System.Windows.Forms.PictureBox()
		Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
		Me.Label1 = New System.Windows.Forms.Label()
		Me.Label2 = New System.Windows.Forms.Label()
		Me.TextBox1 = New System.Windows.Forms.TextBox()
		Me.TextBox2 = New System.Windows.Forms.TextBox()
		Me.Button2 = New System.Windows.Forms.Button()
		Me.Button1 = New System.Windows.Forms.Button()
		Me.PictureBox2 = New System.Windows.Forms.PictureBox()
		Me.Button4 = New System.Windows.Forms.Button()
		CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
		CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).BeginInit()
		Me.SuspendLayout()
		'
		'PictureBox1
		'
		Me.PictureBox1.Location = New System.Drawing.Point(12, 196)
		Me.PictureBox1.Name = "PictureBox1"
		Me.PictureBox1.Size = New System.Drawing.Size(774, 493)
		Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		Me.PictureBox1.TabIndex = 1
		Me.PictureBox1.TabStop = False
		'
		'OpenFileDialog1
		'
		Me.OpenFileDialog1.FileName = "OpenFileDialog1"
		'
		'Label1
		'
		Me.Label1.AutoSize = True
		Me.Label1.Location = New System.Drawing.Point(1049, 12)
		Me.Label1.Name = "Label1"
		Me.Label1.Size = New System.Drawing.Size(261, 25)
		Me.Label1.TabIndex = 2
		Me.Label1.Text = "Enter resolution of final collage:"
		'
		'Label2
		'
		Me.Label2.AutoSize = True
		Me.Label2.Location = New System.Drawing.Point(881, 49)
		Me.Label2.Name = "Label2"
		Me.Label2.Size = New System.Drawing.Size(425, 25)
		Me.Label2.TabIndex = 3
		Me.Label2.Text = "Enter resolution of photos that make up the collage:"
		'
		'TextBox1
		'
		Me.TextBox1.Location = New System.Drawing.Point(1312, 12)
		Me.TextBox1.Name = "TextBox1"
		Me.TextBox1.Size = New System.Drawing.Size(150, 31)
		Me.TextBox1.TabIndex = 4
		Me.TextBox1.Text = "20"
		'
		'TextBox2
		'
		Me.TextBox2.Location = New System.Drawing.Point(1312, 49)
		Me.TextBox2.Name = "TextBox2"
		Me.TextBox2.Size = New System.Drawing.Size(150, 31)
		Me.TextBox2.TabIndex = 5
		Me.TextBox2.Text = "300"
		'
		'Button2
		'
		Me.Button2.Location = New System.Drawing.Point(1312, 86)
		Me.Button2.Name = "Button2"
		Me.Button2.Size = New System.Drawing.Size(150, 53)
		Me.Button2.TabIndex = 7
		Me.Button2.Text = "Save"
		Me.Button2.UseVisualStyleBackColor = True
		'
		'Button1
		'
		Me.Button1.Location = New System.Drawing.Point(12, 12)
		Me.Button1.Name = "Button1"
		Me.Button1.Size = New System.Drawing.Size(314, 122)
		Me.Button1.TabIndex = 0
		Me.Button1.Text = "GO!"
		Me.Button1.UseVisualStyleBackColor = True
		'
		'PictureBox2
		'
		Me.PictureBox2.Location = New System.Drawing.Point(469, 12)
		Me.PictureBox2.Name = "PictureBox2"
		Me.PictureBox2.Size = New System.Drawing.Size(207, 122)
		Me.PictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		Me.PictureBox2.TabIndex = 6
		Me.PictureBox2.TabStop = False
		'
		'Button4
		'
		Me.Button4.Location = New System.Drawing.Point(332, 12)
		Me.Button4.Name = "Button4"
		Me.Button4.Size = New System.Drawing.Size(131, 122)
		Me.Button4.TabIndex = 9
		Me.Button4.Text = "Choose a picture"
		Me.Button4.UseVisualStyleBackColor = True
		'
		'Form1
		'
		Me.AutoScaleDimensions = New System.Drawing.SizeF(10.0!, 25.0!)
		Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		Me.ClientSize = New System.Drawing.Size(1468, 1097)
		Me.Controls.Add(Me.PictureBox2)
		Me.Controls.Add(Me.Button1)
		Me.Controls.Add(Me.Button4)
		Me.Controls.Add(Me.Button2)
		Me.Controls.Add(Me.TextBox2)
		Me.Controls.Add(Me.TextBox1)
		Me.Controls.Add(Me.Label2)
		Me.Controls.Add(Me.Label1)
		Me.Controls.Add(Me.PictureBox1)
		Me.Name = "Form1"
		Me.Text = "Collage Maker"
		CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
		CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).EndInit()
		Me.ResumeLayout(False)
		Me.PerformLayout()

	End Sub
	Friend WithEvents PictureBox1 As PictureBox
	Friend WithEvents OpenFileDialog1 As OpenFileDialog
	Friend WithEvents Label1 As Label
	Friend WithEvents Label2 As Label
	Friend WithEvents TextBox1 As TextBox
	Friend WithEvents TextBox2 As TextBox
	Friend WithEvents Button2 As Button
	Friend WithEvents Button1 As Button
	Friend WithEvents PictureBox2 As PictureBox
	Friend WithEvents Button4 As Button
End Class
