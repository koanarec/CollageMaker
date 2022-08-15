Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim appPath As String = My.Application.Info.DirectoryPath
        Dim path1 As String = appPath.Replace("\Collage\bin\Debug\net6.0-windows", "\")
        Try
            FileSystem.Kill(path1 + "Editcolorofimage\temp_storage\*.*")
        Catch ex As Exception
            ' File is in use.
        End Try


        Dim My_Process As New Process()
        Dim My_Process_Info As New ProcessStartInfo()
        My_Process_Info.FileName = "CMD"
        My_Process_Info.Arguments = "/C cd " + path1 + "Editcolorofimage & collage_maker.py" ' Process arguments
        My_Process.StartInfo = My_Process_Info
        My_Process.Start()

        Do While Not My_Process.HasExited
            Try
                Threading.Thread.Sleep(2000)
                Dim strFileSize As String = ""
                Dim di As New IO.DirectoryInfo(path1 + "Editcolorofimage\temp_storage")
                Dim aryFi As IO.FileInfo() = di.GetFiles("*.png")
                Dim fi As IO.FileInfo

                Dim best As Integer = 0
                Dim temp As String

                For Each fi In aryFi
                    temp = CStr(fi.Name).Substring(0, CStr(fi.Name).Length - 4)

                    temp = temp.Remove(0, 3)

                    If Integer.Parse(temp) > best Then
                        best = Integer.Parse(temp)
                    End If

                Next
                best = best - 1
                If best <> 0 Then
                    PictureBox1.Image = Image.FromFile(path1 + "Editcolorofimage\temp_storage\img" + CStr(best) + ".png")
                    PictureBox1.Refresh()
                End If


            Catch ex As Exception
                '   On ho
            End Try
        Loop
        PictureBox1.Image = Image.FromFile(path1 + "Editcolorofimage\final.png")


    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim appPath As String = My.Application.Info.DirectoryPath
        Dim path1 As String = appPath.Replace("\Collage\bin\Debug\net6.0-windows", "\")

        PictureBox2.ImageLocation = path1 + "Editcolorofimage\decres.png"

        Dim paths As String
        paths = path1 + "Editcolorofimage\setup.txt"
        System.IO.File.WriteAllText(paths, "")
        System.IO.File.AppendAllText(paths, TextBox1.Text & vbCrLf)
        System.IO.File.AppendAllText(paths, TextBox2.Text & vbCrLf)

        Dim My_Process As New Process()
        Dim My_Process_Info As New ProcessStartInfo()

        My_Process_Info.FileName = "CMD"
        My_Process_Info.Arguments = "/C cd " + path1 + "Editcolorofimage & preview.py" ' Process arguments
        My_Process.StartInfo = My_Process_Info
        My_Process.Start() ' Run the process NOW
        My_Process.WaitForExit()
        PictureBox2.ImageLocation = path1 + "Editcolorofimage\decres.png"
        PictureBox2.Refresh()
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim appPath As String = My.Application.Info.DirectoryPath
        Dim path1 As String = appPath.Replace("\Collage\bin\Debug\net6.0-windows", "\")

        PictureBox2.ImageLocation = path1 + "Editcolorofimage\decres.png"

        Try
            FileSystem.Kill(path1 + "Editcolorofimage\temp_storage\*.*")
        Catch ex As Exception
            ' File is in use.
        End Try

    End Sub
    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        Dim appPath As String = My.Application.Info.DirectoryPath
        Dim path1 As String = appPath.Replace("\Collage\bin\Debug\net6.0-windows", "\")

        OpenFileDialog1.ShowDialog()
        Dim FileToCopy As String
        Dim NewCopy As String

        Try
            My.Computer.FileSystem.DeleteFile(path1 + "Editcolorofimage\money.png")
        Catch ex As IO.IOException
            ' File is in use.
        End Try



        FileToCopy = OpenFileDialog1.FileName
        NewCopy = path1 + "Editcolorofimage\money.png"
        System.IO.File.Copy(FileToCopy, NewCopy)
        Me.Button2.PerformClick()

        Dim a As Image
        a = Image.FromFile(OpenFileDialog1.FileName)
        a = Image.FromFile(NewCopy)
        Dim x, y As Integer
        x = 2000 * a.Width / (a.Height + a.Width)
        y = 2000 * (1 - (a.Width / (a.Height + a.Width)))


        PictureBox1.Width = y
        PictureBox1.Height = x
        PictureBox2.ImageLocation = path1 + "Editcolorofimage\decres.png"

    End Sub

End Class
