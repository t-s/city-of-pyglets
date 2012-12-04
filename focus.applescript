on run argv
	set pid to item 1 of argv as integer
	get pid
	tell application "System Events"
    	set theprocs to every process whose unix id is pid
    	repeat with proc in theprocs
        	set the frontmost of proc to true
   		end repeat
	end tell
end run
