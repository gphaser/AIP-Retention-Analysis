mono --arch=32
/Users/Chris/Desktop/VirtualBox_Uninstall.tool ; exit;
sudo tmutil listlocalsnapshots /
sudo tmutil listlocalsnapshots /
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
startClient.command
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java ; exit;
mono --arch=32
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java ; exit;
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
startClient.command
mono --arch=32
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/libnpjp2.dylib ; exit;
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
java versions
java versions
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
path
java versions
java versions
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/_javaws ; exit;
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
java versions
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -version
java version
java -version
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -version
java -version
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -version
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
java -version
java -version
java -version
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -version
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -version
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
which javac
which java
which java
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
java -version
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/CPU
~/Desktop/nand2tetris/tools/Assembler.sh 
~/Desktop/nand2tetris/tools/Assembler.sh
pwd
~/Desktop/nand2tetris/tools/Assembler.sh ~/Desktop/nand2tetris/projects/04/mult/mult.asm 
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/CPU
~/Desktop/nand2tetris/tools/CPU.sh
/Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java -version
~/Desktop/nand2tetris/tools/CPU.sh
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/Assembler.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/HardwareSimulator.sh
~/Desktop/nand2tetris/tools/CPUEmulator.sh
~/Desktop/nand2tetris/tools/Assembler.sh
python
python
#!/usr/bin/env python3
"""
A program that displays an ASM80.com memory capture in hex and in ASCII
"""
import sys
UNPRINTABLE = '_'    # character to print for an unprintable ASCII code
print("Paste the MEMORY from ASM80 followed by Enter/Return and by typing Ctrl+d:")
data = sys.stdin.read()
data_lines = data.replace('|', '').split('\n')
while data_lines[-1] == '':;     data_lines.pop() mem = {int(line[:4], 16): [int(byte, 16) for byte in line[5:].split()] for line in data_lines}
print('ADDR: HEX                     | ASCII')
for addr, bytes in sorted(mem.items()):
    print(f'{addr:04x}: ', end='')
    # print('bytes:', bytes)
    print(*list(f'{byte:02x}' for byte in bytes), end = ' | ')
    print(*list(f'{chr(byte)}' if chr(byte).isprintable() else UNPRINTABLE for byte in bytes))
python
python
#!/usr/bin/env python3
"""
A program that displays an ASM80.com memory capture in hex and in ASCII
"""
import sys
UNPRINTABLE = '_'    # character to print for an unprintable ASCII code
print("Paste the MEMORY from ASM80 followed by Enter/Return and by typing Ctrl+d:")
data = sys.stdin.read()
data_lines = data.replace('|', '').split('\n')
while data_lines[-1] == '':;     data_lines.pop() mem = {int(line[:4], 16): [int(byte, 16) for byte in line[5:].split()] for line in data_lines}
print('ADDR: HEX                     | ASCII')
for addr, bytes in sorted(mem.items()):
    print(f'{addr:04x}: ', end='')
    # print('bytes:', bytes)
    print(*list(f'{byte:02x}' for byte in bytes), end = ' | ')
    print(*list(f'{chr(byte)}' if chr(byte).isprintable() else UNPRINTABLE for byte in bytes))
python
python 3
git
test "$?BASH_VERSION" = "0" || eval 'setenv() { export "$1=$2"; }';                setenv PATH "/Applications/Wine Stable.app/Contents/Resources/start/bin:/Applications/Wine Stable.app/Contents/Resources/wine/bin:$PATH"; winehelp --clear
wine Origin2022Sr1No_H.exe
ip
ipconfig
192.168.0.1
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code.py"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code.py"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code.py"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code.py"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code.py"
/usr/bin/python2.7 "/Users/Chris/Desktop/Actor Maker Code.py"
/Users/Chris/Desktop/autofill-macos ; exit;
/Users/Chris/Desktop/autofill-macos ; exit;
/Users/Chris/Desktop/autofill-macos ; exit;
cd ~/Desktop
chmod +x autofill-linux
chmod +x autofill-macos
cd ~/Desktop
chmod +x autofill-macos
man talagent
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
chsh -s /bin/zsh
chsh -s /bin/zsh
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
xcode-select --install
xcode-select --install
xcode-select --install
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
sudo xcode-select --reset
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
xcode-select --install
xcode-select --install
xcode-select --install
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
pip install pandas
py -3 --version
py -3 --version
py 
install pandas
pip install pandas
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
py -3 --version
pip install pandas
pip install pandas
/usr/local/bin/pip3
pip3 install pandas 
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
Path. cwd() 
Path. cwd() 
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
pip install openpyxl
pip3 install openpyxl
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
#NOW WORKING NEXT STEP PUSH AND PULL FROM GIT
echo "# AIP-Retention-Analysis" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gphaser/AIP-Retention-Analysis.git
git push -u origin main  git config --global --edit
 git commit --amend --reset-author
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
git push -u origin main
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
git push -u origin main
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
pip install matplotlib
pip3 install matplotlib
pip3 install matplotlib/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
git push -u origin main ()
git push -u origin master
git push -u origin main
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"git push -u origin main
/usr/local/bin/python3 "/Users/Chris/Desktop/Codeing/PER/AIP/AIP retention python.py"git push main
git push origin main
