# PrusaSlicer M73 to M117 converter
Converts Prusa `M73` .gcode commands to Marlin `M117`. `M73` command's purpose is to show remaining time on Prusa3D printers.  
Text output is optimised for Ender 3 default 128*64 screen. Tested with default Python 3 and Marlin 2.0.
`M73` command is inserted to gcode by PrusaSlicer itself. My script only replaces this command to Marlin-suitable `M117`. If you need `M73` in your gcode, you simply don't have to run this script.

**Preview:**  
`01:05 left / 34% done`

# Installation
0. If insertion of `M73` commands not enabled yet: tick the `Printer settings` -> `General` -> `Supports remaining time`. After enabling it you will get gcode with `M73` commands.

1. Install Python and remember the installation directory (`[python directory]`)

2. Copy time_converter.py to PrusaSlicer installation folder (to store it safely with slicer itself) or to any other folder (`[script directory]`)

3. Configure the PrusaSlicer: go to `Print settings` > `Output options` > `Post-processing scripts` and add line: `"[python directory]/python.exe"  "[script directory]/script.py";`

