#!/usr/bin/env python3
"""
Script to replace hardcoded Tailwind amber colors with theme-aware CSS classes
This is SAFE - it only replaces specific, well-defined patterns
"""

import re

# Mapping of Tailwind classes to our theme-aware classes
REPLACEMENTS = {
    # Background colors
    'bg-amber-100': 'bg-primary-light',
    'bg-amber-200': 'bg-primary-light',
    'bg-amber-50': 'bg-primary-light',
    
    # Text colors
    'text-amber-700': 'text-primary-dark',
    'text-amber-800': 'text-primary-darker',
    'text-amber-600': 'text-primary',
    'text-amber-500': 'text-primary',
    
    # Gradients - these are trickier, we'll handle separately
    # Borders
    'border-amber-600': 'border-primary',
    'border-amber-700': 'border-primary-dark',
    
    # Hover states
    'hover:text-amber-700': 'hover:text-primary-dark',
    'hover:text-amber-800': 'hover:text-primary-darker',
    'hover:text-amber-600': 'hover:text-primary',
    'hover:border-amber-600': 'hover:border-primary',
    'hover:bg-amber-50': 'hover:bg-primary-light',
}

# Special gradient replacements
GRADIENT_PATTERNS = [
    # from-amber-600 to-amber-700 → bg-gradient-primary
    (r'bg-gradient-to-r from-amber-600 to-amber-700', 'bg-gradient-primary'),
    (r'bg-gradient-to-br from-amber-600 to-amber-800', 'bg-gradient-primary'),
    (r'bg-gradient-to-br from-amber-50 to-amber-100', 'bg-primary-light'),
    
    # Hover gradients
    (r'hover:from-amber-700 hover:to-amber-800', ''),  # Remove, handled by our class
]

def fix_file(filepath):
    """Replace hardcoded colors in a file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # First, handle gradient patterns (more specific)
    for pattern, replacement in GRADIENT_PATTERNS:
        content = content.replace(pattern, replacement)
    
    # Then handle simple class replacements
    for old_class, new_class in REPLACEMENTS.items():
        content = content.replace(old_class, new_class)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Fixed {filepath}")
        return True
    else:
        print(f"⏭️  No changes needed in {filepath}")
        return False

if __name__ == '__main__':
    files_to_fix = [
        'templates/home.html',
    ]
    
    fixed_count = 0
    for filepath in files_to_fix:
        if fix_file(filepath):
            fixed_count += 1
    
    print(f"\n🎨 Fixed {fixed_count} file(s)")
    print("\n⚠️  IMPORTANT: Review the changes before committing!")
    print("Run: git diff templates/home.html")
