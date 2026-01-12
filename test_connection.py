#!/usr/bin/env python3
"""
Quick test script to verify WordPress connection
Run this before doing a full publish to ensure credentials are correct
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from config import Config
from modules.auth import WordPressAuth

console = Console()


def main():
    """Test WordPress connection"""
    console.print(Panel.fit(
        "[bold cyan]WordPress Connection Test[/bold cyan]\n"
        "[dim]Testing authentication and permissions[/dim]",
        border_style="cyan"
    ))
    
    # Validate config
    try:
        Config.validate()
    except ValueError as e:
        console.print(f"\n[red]Configuration Error:[/red]\n{e}\n")
        sys.exit(1)
    
    console.print(f"\n[cyan]Site URL:[/cyan] {Config.WP_SITE_URL}")
    console.print(f"[cyan]Username:[/cyan] {Config.WP_USERNAME}")
    console.print(f"[cyan]Dry Run:[/cyan] {Config.is_dry_run()}\n")
    
    # Test connection
    console.print("[bold]Testing connection...[/bold]")
    
    auth = WordPressAuth()
    success, message, data = auth.test_connection()
    
    if not success:
        console.print(f"\n[red]❌ Connection Failed:[/red]\n")
        console.print(f"   {message}\n")
        console.print("[yellow]Troubleshooting:[/yellow]")
        console.print("   1. Check WP_SITE_URL in .env (no trailing slash)")
        console.print("   2. Verify WP_USERNAME is correct")
        console.print("   3. Regenerate WP_APP_PASSWORD if needed")
        console.print("   4. Ensure WordPress REST API is enabled\n")
        sys.exit(1)
    
    console.print(f"\n[green]✅ {message}[/green]\n")
    
    # Display site info
    if data:
        info_table = Table(title="Site Information", show_header=False, box=None)
        info_table.add_column("Key", style="cyan")
        info_table.add_column("Value", style="white")
        
        info_table.add_row("Site Name", data.get('site_name', 'Unknown'))
        info_table.add_row("Description", data.get('site_description', 'N/A'))
        info_table.add_row("User", data.get('user_name', 'Unknown'))
        info_table.add_row("User ID", str(data.get('user_id', 'Unknown')))
        
        roles = data.get('user_roles', [])
        info_table.add_row("Roles", ', '.join(roles) if roles else 'Unknown')
        
        console.print(info_table)
        console.print()
    
    # Check permissions
    console.print("[bold]Checking permissions...[/bold]")
    permissions = auth.check_permissions()
    
    perm_table = Table(show_header=True, box=None)
    perm_table.add_column("Permission", style="cyan")
    perm_table.add_column("Status", justify="center")
    
    perm_table.add_row(
        "Publish Posts",
        "[green]✓[/green]" if permissions['can_publish_posts'] else "[red]✗[/red]"
    )
    perm_table.add_row(
        "Publish Pages",
        "[green]✓[/green]" if permissions['can_publish_pages'] else "[red]✗[/red]"
    )
    perm_table.add_row(
        "Upload Files",
        "[green]✓[/green]" if permissions['can_upload_files'] else "[red]✗[/red]"
    )
    perm_table.add_row(
        "Manage Categories",
        "[green]✓[/green]" if permissions['can_manage_categories'] else "[red]✗[/red]"
    )
    
    console.print()
    console.print(perm_table)
    console.print()
    
    # Summary
    all_good = all(permissions.values())
    
    if all_good:
        console.print(Panel(
            "[bold green]✅ All systems ready![/bold green]\n"
            "You're ready to publish content to WordPress.",
            border_style="green"
        ))
    else:
        console.print(Panel(
            "[bold yellow]⚠️  Limited permissions detected[/bold yellow]\n"
            "Some operations may not work. Contact your WordPress admin.",
            border_style="yellow"
        ))
    
    console.print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Test cancelled[/yellow]\n")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
