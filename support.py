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

    # Modify to return string instead of printing/make additional functions

    def font_bold(text):
        print(f"{FontModifiers.BOLD}{text}{FontModifiers.DEFAULT}")

    def font_black(text):
        print(f"{FontModifiers.BLACK}{text}{FontModifiers.DEFAULT}")

    def font_red(text):
        print(f"{FontModifiers.RED}{text}{FontModifiers.DEFAULT}")

    def font_green(text):
        print(f"{FontModifiers.GREEN}{text}{FontModifiers.DEFAULT}")

    def font_yellow(text):
        print(f"{FontModifiers.YELLOW}{text}{FontModifiers.DEFAULT}")

    def font_blue(text):
        print(f"{FontModifiers.BLUE}{text}{FontModifiers.DEFAULT}")

    def font_magenta(text):
        print(f"{FontModifiers.MAGENTA}{text}{FontModifiers.DEFAULT}")

    def font_cyan(text):
        print(f"{FontModifiers.CYAN}{text}{FontModifiers.DEFAULT}") 

    def font_white(text):
        print(f"{FontModifiers.WHITE}{text}{FontModifiers.DEFAULT}") 

    def font_bold_red(text):
        print(f"{FontModifiers.BOLD}{FontModifiers.RED}{text}{FontModifiers.DEFAULT}")

    #####

# Test of all font options:
if __name__ == '__main__':
    FontModifiers.font_bold("BOLD")
    FontModifiers.font_black("BLACK")
    FontModifiers.font_red("RED")
    FontModifiers.font_green("GREEN")
    FontModifiers.font_yellow("YELLOW")
    FontModifiers.font_blue("BLUE")
    FontModifiers.font_magenta("MAGENTA")
    FontModifiers.font_cyan("CYAN")
    FontModifiers.font_white("WHITE")
    FontModifiers.font_bold_red("BOLD RED")