import questionary
import os
from pathlib import Path
from rich.console import Console

console = Console()

def navigate(current_dir):

    console.print(f"[yellow]Current Location: {current_dir}[/yellow]")

    sub_folders = [item for item in current_dir.iterdir() if item.is_dir()]
    options = ["Stay in current directory","Previous Directory","Home Directory"]

    for folder in sub_folders:
        options.append(folder.name)

    if not sub_folders:
        console.print("[dim]No subfolders found in this directory.[/dim]")

    answer = questionary.select(
    "Which directory would you like to go to?",
    choices=options
    ).ask()

    if answer == "Stay in current directory":
        console.print(f"[cyan]Stayed in current directory: {current_dir}[/cyan]")
        return current_dir
    
    elif answer == "Previous Directory":
        if current_dir == Path.home():
            console.print("[yellow]Already at home directory.[/yellow]")
            return current_dir
        else:
            new_dir = current_dir.parent
            console.print(f"[green]Moving into: {answer} [/green]")
            return new_dir
    
    elif answer == "Home Directory":
        new_dir = Path.home()
        console.print(f"[green]Moving to Home Directory: {answer} [/green]")
        return new_dir
    
    else:
        new_dir = current_dir / answer
        console.print(f"[green]Moving into: {answer} [/green]")
        return new_dir


def inspect(current_dir):

    console.print("[bold cyan]Showing folders and files ...[/bold cyan]")

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

    #using pathlib to make the user always start in the home directory
    #remember this, this may not live right here, just keeping it here for my thinking
    current_dir = Path.home #<< only for my reference
    options = ["Navigate", "Inspect", "Make Crispy", "Exit App"]

    while True:

        answer = questionary.select(
        "What would you like to do?",
        choices=options
        ).ask()

        if answer == "Navigate":
            navigate(current_dir)
        
        elif answer == "Inspect":
            inspect(current_dir)
        
        elif answer == "Make Crispy":
            make_cripsy()
        
        elif answer == "Exit App":
            console.print("[bold red]Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main_menu()