#!/usr/bin/env python3
"""
Auto-add "Back to Top" buttons after each Markdown table in README.md
"""
import re

def add_back_to_top_buttons(filename='README.md'):
    """
    Read README.md, find all tables, and insert [⬆ Back to Top](#readme) after each.
    Prevents duplicate insertion.
    """
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines for easier processing
    lines = content.split('\n')
    result = []
    in_table = False
    i = 0
    
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        # Detect if we're in a table (lines with | characters)
        if '|' in line and line.strip().startswith('|'):
            in_table = True
        elif in_table and line.strip() == '':
            # Empty line after table, check if next line is already back-to-top
            if i + 1 < len(lines) and '[⬆ Back to Top]' not in lines[i + 1]:
                # Insert back to top button
                result.append('')
                result.append('[⬆ Back to Top](#readme)')
            in_table = False
        elif in_table and not ('|' in line or line.strip().startswith(':---')):
            # Table ended (no more | characters)
            in_table = False
            # Check if we need to add button
            if '[⬆ Back to Top]' not in line:
                result.append('')
                result.append('[⬆ Back to Top](#readme)')
        
        i += 1
    
    # Write back to file
    new_content = '\n'.join(result)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Added 'Back to Top' buttons to {filename}")
    print("📝 Run this script again if you add more tables in the future!")

if __name__ == '__main__':
    add_back_to_top_buttons('README.md')
