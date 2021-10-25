# ghidraScripts

#Ghidra tip:

    argc is the # of args being passed into your program from the cmd line 
    argv is the array of args
    
    # Right-click on main( )func and click on "edit function signature" 
    
        -Change main() from
                 undefined main(int param_1, long param_2)
        -to
                 undefined main(int argc, char ** argv)
   # this will propagate through the rest of the program
   
  Symbol Tree 
      good for finding main(), shows import and exports
      CANT find main(0 look for _start
      
  Function Graph-
      highlight main -> Window -> "function graph"
     
  Converting Data 
      Right-click 0x61 -> select convert -> choose conversion type  "this will propagate through the rest of program"
      
NOTES:
  -Local vars stored on stack, global  vars (0x08 + RIP) cause it's stored in ".data" section of .exe\.elf file 
  -1st 6 params of func are stored in registers RDI, RSI, EDX, RSX, R8, R9 - the rest are stored in Memory
  https://youtu.be/uyWVztMHWtk?t=2448    @ 42:08
  
  -Heap : is for dynamic memory allocation - for global vars, etc...
  https://youtu.be/uyWVztMHWtk?t=2890    @   48:10
  
PE Sections
  -  .text or CODE | contains executable code | permissions are Read-Execute
  -  .data or DATA | typically contains global vars, STRINGS | permissions Read-Write
  -  .rdata | sometimes contains imports & exports | permissions Read-only
  -  .idata | IF present, contains import data. IF NOT present, import data is in .rdata
  -  .edata | IF present, contains export data. IF NOT present, import data is in .rdata
  -  .rsrc  | contains resources used by .exe | icons, dialogs, menus, strings, so on | NOTE: mal-actors may embed another .exe as a dropper, can find w\ Resource Hacker
    
    
