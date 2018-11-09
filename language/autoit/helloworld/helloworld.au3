#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.5
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here
Run("C:\Program Files (x86)\Notepad++\notepad++.exe") ; 启动notepad++, 注意路径

; Local $titleRegex = StringRegExp(".* - Notepad++")  ; 正则
Local $nodepadEdit = WinWaitActive("[CLASS:Notepad++; REGEXPTITLE:.* - Notepad++]")  ; 等待notepad++启动或者变为活动窗口
MsgBox(64, "校验", "你好, 已经成功启动notepad++并获得焦点")
Send("I am a auto send text")  ; 自动发送文本到当前窗口中
WinClose("[CLASS:Notepad++]")  ; 自动关闭窗口