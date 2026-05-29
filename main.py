import questionary
import os
from pathlib import Path
from rich.console import Console

console = Console()

def navigate():

    # console.print("[yellow]Showing directories...[/yellow]")

    # all_files = os.listdir
    # options = []

    # for files in all_files:
    #     options.append(files)

    # answer = questionary.select(
    # "Which directory would you like to go to?",
    # choices=options
    # ).ask()
    return ""

def inspect():

    #using pathlib to get current directory
    current_dir = Path.cwd()
    console.print("[bold cyan]Showing directories...[/bold cyan]")

    items = list(current_dir.iterdir())

    if not items:
        console.print("[italic cyan]This directory is empty.[/italic cyan]")
        return
    
    console.print("[bold underline]Folders:[/bold underline]")
    folders = [item for item in items if item.is_dir()]
    if folders:
        for folder in folders:
            console.print(f"  📁 [bold blue]{folder.name}[/bold blue]")

    else: 
        console.print("  [dim]None[/dim]")

    console.print("\n[bold underline]Files:[/bold underline]")
    files = [item for item in items if item.is_file()]
    if files:
        for file in files:
            console.print(f"  📄 [green]{file.name}[/green]")

    else: 
        console.print("  [dim]None[/dim]")

    #extra line just for clean formatting
    console.print("")



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