#!/usr/bin/env python3
"""
Quick script to update Aura Intelligence color palette
From: Warm Amber Gold → To: Minimal Luxury Champagne
"""

import re

def update_home_colors():
    with open('templates/home.html', 'r') as f:
        content = f.read()
    
    # Update CSS variables in <style> section
    old_css = '''    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
        }
        
        .font-serif {
            font-family: 'Cormorant Garamond', serif;
        }
        
        .gradient-text {
            background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero-gradient {
            background: linear-gradient(135deg, #fafaf9 0%, #f5f5f4 50%, #fafaf9 100%);
        }
        
        .gold-border {
            border-color: #d97706;
        }
        
        .hover-lift {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .hover-lift:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
    </style>'''
    
    new_css = '''    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'champagne': {
                            50: '#FEFDFB',
                            100: '#F8F6F3',
                            200: '#E8E0D5',
                            300: '#D4C7B5',
                            400: '#C9B896',
                            500: '#B5A585',
                            600: '#A18F71',
                            700: '#7D6F56',
                            800: '#5A503D',
                            900: '#3A3327',
                        },
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');
        
        :root {
            /* Minimal Luxury Champagne Palette */
            --accent: #C9B896;
            --accent-hover: #B5A585;
            --accent-light: #E8E0D5;
            
            --background: #FEFEFE;
            --surface: #F8F8F7;
            --border: #E8E8E6;
            
            --text-primary: #1A1A1A;
            --text-secondary: #6B6B6B;
            --text-muted: #9B9B9B;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--background) !important;
            color: var(--text-primary) !important;
        }
        
        .font-serif {
            font-family: 'Cormorant Garamond', serif;
        }
        
        .gradient-text {
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero-gradient {
            background: linear-gradient(135deg, var(--background) 0%, var(--surface) 50%, var(--background) 100%);
        }
        
        .hover-lift {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .hover-lift:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
        }
    </style>'''
    
    content = content.replace(old_css, new_css)
    
    # Replace Tailwind classes with champagne equivalents
    replacements = [
        ('bg-stone-50', 'bg-white'),
        ('bg-stone-100', 'bg-champagne-100'),
        ('text-stone-900', 'text-gray-900'),
        ('text-stone-800', 'text-gray-800'),
        ('text-stone-700', 'text-gray-700'),
        ('text-stone-600', 'text-gray-600'),
        ('text-stone-500', 'text-gray-500'),
        ('border-stone-200', 'border-gray-200'),
        ('border-stone-300', 'border-gray-300'),
        
        # Amber to Champagne
        ('from-amber-600 to-amber-700', 'from-champagne-400 to-champagne-500'),
        ('hover:from-amber-700 hover:to-amber-800', 'hover:from-champagne-500 hover:to-champagne-600'),
        ('bg-amber-100', 'bg-champagne-200'),
        ('text-amber-800', 'text-champagne-700'),
        ('text-amber-700', 'text-champagne-600'),
        ('bg-amber-50', 'bg-champagne-100'),
        ('border-amber-600', 'border-champagne-500'),
        ('hover:border-amber-600', 'hover:border-champagne-500'),
        ('hover:text-amber-700', 'hover:text-champagne-600'),
        ('gold-border', 'border-champagne-500'),
        ('bg-gradient-to-br from-amber-50 to-amber-100', 'bg-champagne-100'),
        ('bg-amber-200', 'bg-champagne-300'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open('templates/home.html', 'w') as f:
        f.write(content)
    
    print("✅ Updated home.html colors")

def update_app_colors():
    with open('templates/app.html', 'r') as f:
        content = f.read()
    
    # Update CSS variables
    css_replacements = {
        '--primary-gold: #d97706;': '--primary: #C9B896;',
        '--primary-gold-dark: #b45309;': '--primary-dark: #B5A585;',
        '--primary-gold-darker: #92400e;': '--primary-darker: #A18F71;',
        '--gold-light: #fbbf24;': '--accent-light: #E8E0D5;',
        
        '--stone-50: #fafaf9;': '--stone-50: #FEFEFE;',
        '--stone-100: #f5f5f4;': '--stone-100: #F8F8F7;',
        '--stone-200: #e7e5e4;': '--stone-200: #E8E8E6;',
        '--stone-600: #78716c;': '--stone-600: #6B6B6B;',
        '--stone-800: #292524;': '--stone-800: #1A1A1A;',
        '--stone-900: #1c1917;': '--stone-900: #1A1A1A;',
        
        '--gold: #d97706;': '--gold: #C9B896;',
    }
    
    for old, new in css_replacements.items():
        content = content.replace(old, new)
    
    # NOW UPDATE HTML TAILWIND CLASSES (this was missing!)
    tailwind_replacements = [
        # Stone to Gray/White
        ('bg-stone-50', 'bg-white'),
        ('text-stone-900', 'text-gray-900'),
        ('text-stone-800', 'text-gray-800'),
        ('text-stone-700', 'text-gray-700'),
        ('text-stone-600', 'text-gray-600'),
        ('text-stone-500', 'text-gray-500'),
        ('text-stone-400', 'text-gray-400'),
        ('border-stone-200', 'border-gray-200'),
        ('border-stone-300', 'border-gray-300'),
        ('hover:text-stone-900', 'hover:text-gray-900'),
        ('hover:text-stone-800', 'hover:text-gray-800'),
        
        # Amber to Champagne (for any remaining amber classes)
        ('bg-amber-600', 'bg-champagne-400'),
        ('bg-amber-700', 'bg-champagne-500'),
        ('bg-amber-100', 'bg-champagne-200'),
        ('bg-amber-50', 'bg-champagne-100'),
        ('text-amber-700', 'text-champagne-600'),
        ('text-amber-600', 'text-champagne-500'),
        ('text-amber-800', 'text-champagne-700'),
        ('border-amber-600', 'border-champagne-500'),
        ('from-amber-600 to-amber-700', 'from-champagne-400 to-champagne-500'),
        ('from-amber-700 to-amber-800', 'from-champagne-500 to-champagne-600'),
        ('hover:from-amber-700', 'hover:from-champagne-500'),
        ('hover:to-amber-800', 'hover:to-champagne-600'),
    ]
    
    for old, new in tailwind_replacements:
        content = content.replace(old, new)
    
    with open('templates/app.html', 'w') as f:
        f.write(content)
    
    print("✅ Updated app.html CSS variables + Tailwind classes")

if __name__ == '__main__':
    print("🎨 Updating Aura Intelligence color palette...")
    print("   From: Warm Amber Gold (#d97706)")
    print("   To: Minimal Luxury Champagne (#C9B896)")
    print()
    
    update_home_colors()
    update_app_colors()
    
    print()
    print("✅ All done! New champagne gold palette applied.")
    print("   Run the app to see the changes: python app.py")
