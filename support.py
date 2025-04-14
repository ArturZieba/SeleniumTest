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

# Add a wrapper that returns modified string without having to add the values manually?

# Test of all font options:
print(FontModifiers.BOLD + "BOLD" + FontModifiers.DEFAULT)
print(FontModifiers.BLACK + "BLACK" + FontModifiers.DEFAULT)
print(FontModifiers.RED + "RED" + FontModifiers.DEFAULT)
print(FontModifiers.GREEN + "GREEN" + FontModifiers.DEFAULT)
print(FontModifiers.YELLOW + "YELLOW" + FontModifiers.DEFAULT)
print(FontModifiers.BLUE + "BLUE" + FontModifiers.DEFAULT)
print(FontModifiers.MAGENTA + "MAGENTA" + FontModifiers.DEFAULT)
print(FontModifiers.CYAN + "CYAN" + FontModifiers.DEFAULT)
print(FontModifiers.WHITE + "WHITE" + FontModifiers.DEFAULT)
print(FontModifiers.BOLD + FontModifiers.RED + "BOLD RED" + FontModifiers.DEFAULT)
