# Class with ANSI escape codes
class FontModifiers:
    DEFAULT = '\033[0m' # Restore default font
    BOLD = '\033[1m' # Make font bold
    BLACK = '\033[90m' # Change font color to black
    RED = '\033[91m' # Change font color to red
    GREEN = '\033[92m' # Change font color to green
    YELLOW = '\033[93m' # Change font color to yellow
    BLUE = '\033[94m' # Change font color to blue
    MAGENTA = '\033[95m' # Change font color to magenta
    CYAN = '\033[96m' # Change font color to cyan
    WHITE = '\033[97m' # Change font color to white

#####
# Functions printing text with certain font modifications using ANSI escape codes

def font_bold(text):
    print(FontModifiers.BOLD + text + FontModifiers.DEFAULT)

def font_black(text):
    print(FontModifiers.BLACK + text + FontModifiers.DEFAULT)

def font_red(text):
    print(FontModifiers.RED + text + FontModifiers.DEFAULT)

def font_green(text):
    print(FontModifiers.GREEN + text + FontModifiers.DEFAULT)

def font_yellow(text):
    print(FontModifiers.YELLOW + text + FontModifiers.DEFAULT)

def font_blue(text):
    print(FontModifiers.BLUE + text + FontModifiers.DEFAULT)

def font_magenta(text):
    print(FontModifiers.MAGENTA + text + FontModifiers.DEFAULT)

def font_cyan(text):
    print(FontModifiers.CYAN + text + FontModifiers.DEFAULT)

def font_white(text):
    print(FontModifiers.WHITE + text + FontModifiers.DEFAULT)

def font_bold_red(text):
    print(FontModifiers.BOLD + FontModifiers.RED + text + FontModifiers.DEFAULT)

#####

# Test of all font options:
font_bold("BOLD")
font_black("BLACK")
font_red("RED")
font_green("GREEN")
font_yellow("YELLOW")
font_blue("BLUE")
font_magenta("MAGENTA")
font_cyan("CYAN")
font_white("WHITE")
font_bold_red("BOLD RED")