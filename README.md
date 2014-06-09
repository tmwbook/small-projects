small-projects
==============

A collection of smaller projects I work on

Projects that have been deployed as EXE's:

   MultipleMovieTimer

Movie Timer
===========
Download of the zip file for this program can be found at:                      
https://www.mediafire.com/?ybb8k3xfjbr4vsq

Steps to set up the program:
    
    1.  If you do not have PyQt4 and Python 2.7 installed and would like to use this program,
        download the zip file from the link above.
    
    2.  If you are launching this with Python, just launch the script by right clicking it 
        and selecting 'Open with.." and then Python.  You could also run it from the command 
        line.
        
        If you downloaded the file above and are trying to launch the program, continue 
        reading the instructions below.
        
    3.  Move the .zip file that you downloaded into the folder(directory) that you want to 
        keep the program in.
    
    4.  Right click the ziped folderd and press 'Extract All'
    
    5.  Here you can choose the location that you want the file to be extracted to, but the
        default is the location of the file that you are currently extracting.
        
        5a.  IE: If I had 'MultipleMovieTimer.zip' on my desktop, Windows would try to 
             extract this folder to '~/Desktop/MultipleMovieTimer'
    
    6.  To launch the program, double click the file named "Movie Timer.exe", or "Move Timer".
    
Using the Movie Timer:
    
    + Pessing the 'Start/Stop' button will start or stop the timer next to it.
    
    + Pressing 'Save' will save all of the current times to Settings.ini
    
    + Currently the only way to manually change times is to change the times in Settings.ini,
      they are formatted in 'hh:mm:ss'.  If you're feeling adventurous, give it a try.
    
    + Pressing 'Reset Timers' will reset ALL of your timers.  If you press this by mistake, 
      stop all of the running timers, close the program and reopen the program.  This will 
      load the times from the last time you saved.
    
    + If you can, try to NOT PRESS RESET WHILE TIMERS ARE RUNNNING.  I have not tested how
      this could mess up the threads, I have not added a conditional to check if timers are
      running, and I don't have a dialogue to check if you are 'Sure that you want to do this?'
      
    + If you accidentall change the timers by highlighting the time and pushing a button, 
      don't panic, you can press 'ctrl + z' to undo the change that you made.  The timer 
      should fix itself if the timer was running while you made this change.
