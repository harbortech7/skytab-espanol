#!/usr/bin/env python3
import os
import re
import html
from googletrans import Translator
import time

def translate_text(text, translator, dest='es'):
    """Translate text to Spanish"""
    if not text.strip():
        return text
    
    try:
        # Add delay to avoid rate limiting
        time.sleep(0.1)
        result = translator.translate(text, dest=dest)
        return result.text
    except Exception as e:
        print(f"Translation error for '{text[:50]}...': {e}")
        return text

def extract_translatable_content(html_content):
    """Extract text nodes from HTML that should be translated"""
    # Pattern to match text content outside of tags
    # This is a simplified approach - for production, consider using BeautifulSoup
    # But we'll use regex for simplicity here
    
    # Remove script and style tags content
    cleaned = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r'<style[^>]*>.*?</style>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
    
    # Find all text content between tags
    # This matches content between > and < that's not just whitespace
    text_pattern = r'>([^<]+)<'
    matches = re.findall(text_pattern, cleaned)
    
    # Filter out empty or whitespace-only matches
    translatable_texts = []
    for match in matches:
        stripped = match.strip()
        if stripped and not stripped.isdigit():  # Skip pure numbers
            translatable_texts.append(stripped)
    
    return translatable_texts

def translate_html_file(file_path, translator):
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
            translated = translate_text(text, translator)
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
        
        # Also translate attributes like alt, title, placeholder, etc.
        # Pattern for attribute values that might need translation
        attr_pattern = r'(alt|title|placeholder|aria-label|aria-describedby)\s*=\s*["\']([^"\']*)["\']'
        attr_matches = re.findall(attr_pattern, translated_content, re.IGNORECASE)
        
        for attr_name, attr_value in attr_matches:
            if attr_value.strip() and not attr_value.isdigit():
                translated_attr = translate_text(attr_value, translator)
                # Replace the attribute value
                old_attr = f'{attr_name}="{html.escape(attr_value)}"'
                new_attr = f'{attr_name}="{html.escape(translated_attr)}"'
                translated_content = translated_content.replace(old_attr, new_attr)
                
                # Also handle single quotes
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
    # Initialize translator
    translator = Translator()
    
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
        translate_html_file(html_file, translator)
    
    print("Translation complete!")

if __name__ == "__main__":
    main()