import questionary
import os
import time
from rich.progress import track
from rich.table import Table
from pathlib import Path
from rich.console import Console
import organiser

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


#This will have both standard_crispy and developer mode living in here
def make_crispy(current_dir):

    console.print("[bold]You have 2 modes to choose from[/bold]")
    console.print("[green]=======================================================================================[/green]")
    console.print("")
    console.print("[blue]Standard Crispy :     Runs the program normally and will sort all your files[/blue]")
    console.print("[blue]Developer Mode  :     Allows you to choose which file types you would like to organize[/blue]")
    console.print("")
    console.print("[green]=======================================================================================[/green]")

    options = ["Standard Crispy","Developer Mode"]

    answer = questionary.select(
    "Would you like to run standard or developer mode?",
    choices=options
    ).ask()

    if answer == "Standard Crispy":
        standard_crispy(current_dir)

    elif answer == "Developer Mode":
        developer_mode(current_dir)



def standard_crispy(current_dir):

    console.print(f"\n[bold yellow]Preparing to crispify: {current_dir}[/bold yellow]")
    categorised_files, sensitive_files = organiser.scan_directory(str(current_dir))

    total_files = sum(len(files)for files in categorised_files.values())

    if total_files == 0:
        console.print("[bold red]No files found to organise[/bold red]")
        return
    
    console.print("\n[bold green]Busy making crispy...[/bold green]")
    for _ in track(range(total_files), description="[cyan]Processing...[/cyan]"):
        time.sleep(0.1)

    summary = organiser.organise_files(str(current_dir), categorised_files)

    if summary["moved"]:
        console.print("\n[bold green] Made Crispy! Here is what moved:[/bold green]")
        table = Table(title="Crispy File Movement Summary", title_style="bold magenta")
        table.add_column("File Name", style="green")
        table.add_column("Destination Folder", style="bold blue")

        for filename, category in summary["moved"]:
            table.add_row(filename, f"{category}/")

        console.print(table)

    if summary["errors"]:
        console.print("\n[bold red]Some errors occurred during organizing:[/bold red]")
        for filename, error in summary["errors"]:
            console.print(f"  [red]• {filename}: {error}[/red]")

    
        

def developer_mode():
    return ""


#This will have make_cripsy, exit, inspect and navigate living in here
def main_menu():

    current_dir = Path.home()
    options = ["Navigate", "Inspect", "Make Crispy", "Exit App"]

    while True:

        answer = questionary.select(
        "What would you like to do?",
        choices=options
        ).ask()

        if answer == "Navigate":
            current_dir = navigate(current_dir)
        
        elif answer == "Inspect":
            inspect(current_dir)
        
        elif answer == "Make Crispy":
            make_crispy(current_dir)
        
        elif answer == "Exit App":
            console.print("[bold red]Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main_menu()