import questionary
from rich.console import Console

console = Console()

def navigate():
    return ""

def inspect():
    return ""

def exit_app():
    return ""

#This will have both standard_crispy and developer mode living in here
def make_cripsy():
    return ""

def standard_cripsy():
    return ""

def developer_mode():
    return ""

#Perameter needed
def loading_bar():
    return ""

#This will have make_cripsy, exit, inspect and navigate living in here
def main_menu():

    options = ["Navigate", "Inspect", "Make Crispy", "Exit App"]

    while True:

        answer = questionary.select(
        "What would you like to do?",
        choices=options
        ).ask()

        if answer == "Navigate":
            navigate()
        
        elif answer == "Inspect":
            inspect()
        
        elif answer == "Make Crispy":
            make_cripsy()
        
        elif answer == "Exit App":
            console.print("[bold red]Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main_menu()