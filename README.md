# PrusaSlicer M73 to M117 converter
Converts Prusa `M73` .gcode commands to Marlin `M117`. `M73` command's purpose is to show remaining time on Prusa3D printers.  
Text output is optimised for Ender 3 default 128*64 screen. Tested with default Python 3 and Marlin 2.0

**Preview:**  
`01:05 left / 34% done`

# Installation
1. Install Python and remember the installation directory (`[python directory]`)

2. Copy time_converter.py to PrusaSlicer installation folder (to store it safely with slicer itself) or to any other folder (`[script directory]`)

3. Configure the PrusaSlicer: go to `Print settings` > `Output options` > `Post-processing scripts` and add line: `"[python directory]/python.exe"  "[script directory]/script.py";`
