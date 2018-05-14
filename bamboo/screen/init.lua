-- 全屏幕显示信息
hs.hotkey.bind({'cmd', 'shift'}, 'h', function() 
	hs.alert('Hello World! 碧峰, 休息一下下.') 
end)


local hyper = {'ctrl', 'alt', 'cmd'}
local hyperShift = {'ctrl', 'alt', 'cmd', 'shift'}
-- hyper + left move the current window to the left monitor
hs.hotkey.bind(hyper, 'left', function()
    local w = hs.window.focusedWindow()
    if not w then
        return
    end
    local s = w:screen():toWest()
    if s then
        w:moveToScreen(s)
    end
end)

-- hyper + right move the current window to the right monitor
hs.hotkey.bind(hyper, 'right', function()
    local w = hs.window.focusedWindow()
    if not w then
        return
    end
    local s = w:screen():toEast()
    if s then
        w:moveToScreen(s)
    end
end)

-- Move Mouse to center of next Monitor
hs.hotkey.bind(hyper, '`', function()
    local screen = hs.mouse.getCurrentScreen()
    local nextScreen = screen:next()
    local rect = nextScreen:fullFrame()
    local center = hs.geometry.rectMidPoint(rect)

    hs.mouse.setAbsolutePosition(center)
    local position = hs.mouse.getAbsolutePosition()
    hs.alert('切了一下下屏幕, (~_~)')
    hs.eventtap.leftClick(position)
end)
