#!/usr/bin/env python3
import os
import re
import html

# Common English to Spanish translations for website interface
translations = {
    # Navigation
    "GET A DEMO": "OBTENER UNA DEMO",
    "Home": "Inicio",
    "Features": "Características",
    "Pricing": "Precios",
    "Restaurant Types": "Tipos de Restaurantes",
    "POS Hardware": "Hardware de POS",
    "Resource Center": "Centro de Recursos",
    "Blog": "Blog",
    "Contact": "Contacto",
    
    # Hero section
    "SkyTab At Your Service": "SkyTab a Tu Servicio",
    "A SkyTab POS system will transform your restaurant's operations - from front-of-house to back-of-house and everything in between.": 
        "Un sistema POS de SkyTab transformará las operaciones de tu restaurante - desde el frente de casa hasta el atrás de casa y todo lo intermedio.",
    
    # Common buttons/links
    "Explore Lighthouse": "Explorar Faro",
    "Learn More": "Aprender Más",
    "See All Features": "Ver Todas las Características",
    "View Details": "Ver Detalles",
    
    # Common phrases
    "Top-Rated Restaurant POS System": "Sistema POS para Restaurantes Mejor Calificado",
    "Don't take our word for it. Read some reviews from our tens of thousands of happy customers and rest assured that you're in good hands.": 
        "No tomes nuestra palabra por ella. Lee algunas reseñas de nuestros decenas de miles de clientes felices y descansa tranquilo sabiendo que estás en buenas manos.",
        
    # Features section
    "Point of sale software, hardware, and payments.": 
        "Software de punto de venta, hardware y pagos.",
        
    # Footer
    "Privacy Policy": "Política de Privacidad",
    "Terms of Service": "Términos de Servicio",
    "© 2023 SkyTab. All rights reserved.": "© 2023 SkyTab. Todos los derechos reservados.",
}

def translate_text(text):
    """Translate text using dictionary or return original if not found"""
    # Direct lookup
    if text in translations:
        return translations[text]
    
    # Case-insensitive lookup
    for key, value in translations.items():
        if key.lower() == text.lower():
            return value
            
    # If not found, return original
    return text

def extract_translatable_content(html_content):
    """Extract text nodes from HTML that should be translated"""
    # Remove script and style tags content
    cleaned = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r'<style[^>]*>.*?</style>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
    
    # Find all text content between tags
    text_pattern = r'>([^<]+)<'
    matches = re.findall(text_pattern, cleaned)
    
    # Filter out empty or whitespace-only matches
    translatable_texts = []
    for match in matches:
        stripped = match.strip()
        if stripped and len(stripped) > 1:  # Skip single characters and empty
            translatable_texts.append(stripped)
    
    return translatable_texts

def translate_html_file(file_path):
    """Translate an HTML file to Spanish"""
    print(f"Translating: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract translatable text
        translatable_texts = extract_translatable_content(content)
        
        if not translatable_texts:
            print(f"No translatable text found in {file_path}")
            return
        
        # Translate each text
        translated_map = {}
        for text in translatable_texts:
            translated = translate_text(text)
            translated_map[text] = translated
        
        # Replace text in content
        translated_content = content
        for original, translated in translated_map.items():
            # Escape special regex characters in original text
            escaped_original = re.escape(original)
            # Replace the text content between tags
            pattern = f'>{escaped_original}<'
            replacement = f'>{translated}<'
            translated_content = re.sub(pattern, replacement, translated_content)
        
        # Also translate common attributes
        attr_pattern = r'(alt|title|placeholder|aria-label|aria-describedby)\s*=\s*["\']([^"\']*)["\']'
        attr_matches = re.findall(attr_pattern, translated_content, re.IGNORECASE)
        
        for attr_name, attr_value in attr_matches:
            if attr_value.strip():
                translated_attr = translate_text(attr_value)
                # Replace the attribute value (double quotes)
                old_attr = f'{attr_name}="{html.escape(attr_value)}"'
                new_attr = f'{attr_name}="{html.escape(translated_attr)}"'
                translated_content = translated_content.replace(old_attr, new_attr)
                
                # Replace the attribute value (single quotes)
                old_attr_sq = f"{attr_name}='{html.escape(attr_value)}'"
                new_attr_sq = f"{attr_name}='{html.escape(translated_attr)}'"
                translated_content = translated_content.replace(old_attr_sq, new_attr_sq)
        
        # Update html lang attribute
        translated_content = re.sub(r'<html[^>]*lang=["\'][^"\']*["\']', '<html lang="es"', translated_content)
        # If no lang attribute, add it
        if '<html lang=' not in translated_content:
            translated_content = re.sub(r'<html', '<html lang="es"', translated_content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
            
        print(f"Translated {len(translatable_texts)} text segments in {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    # Directory containing the cloned website
    base_dir = "/home/mark/Desktop/skytabmx/www.skytab.com"
    
    # Walk through all HTML files
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files to translate")
    
    # Process each file
    for i, html_file in enumerate(html_files, 1):
        print(f"Progress: {i}/{len(html_files)}")
        translate_html_file(html_file)
    
    print("Translation complete!")

if __name__ == "__main__":
    main()