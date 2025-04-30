if application "Firefox" is running then
    tell application "System Events"
        tell process "Firefox"
            set frontmost to true
            click menu item "New Window" of menu "File" of menu bar 1
        end tell
    end tell
else
    tell application "Firefox" to activate
end if
