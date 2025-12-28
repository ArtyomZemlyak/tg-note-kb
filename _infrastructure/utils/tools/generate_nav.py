#!/usr/bin/env python3
"""
Скрипт для генерации навигации mkdocs на основе структуры базы знаний
"""

import os
from pathlib import Path

def generate_nav_recursive(current_path, base_path, excluded_dirs=None):
    """
    Рекурсивно генерирует структуру навигации для mkdocs
    """
    if excluded_dirs is None:
        excluded_dirs = {'__pycache__', '.git', '.vscode', '.idea', 'node_modules'}
    
    nav_items = []
    
    # Пройдемся по всем элементам в текущей директории
    for item in sorted(current_path.iterdir()):
        if item.name in excluded_dirs or item.name.startswith('.'):
            continue
            
        if item.is_dir():
            # Обработка подкаталога
            sub_nav = generate_nav_recursive(item, base_path, excluded_dirs)
            if sub_nav:  # Добавляем только если есть содержимое
                dir_name = item.relative_to(base_path).as_posix()
                nav_items.append({item.name: sub_nav})
        elif item.suffix == '.md' and item.name != 'index.md':
            # Обработка markdown файла
            rel_path = item.relative_to(base_path).as_posix()
            nav_items.append(rel_path)
        elif item.name == 'index.md':
            # index.md в подкаталогах - особый случай
            continue  # Он будет включен отдельно
            
    return nav_items

def main():
    # Путь к базе знаний
    base_path = Path('/app/knowledge_base/tg-note-kb/topics')
    
    # Генерация навигации
    nav_structure = generate_nav_recursive(base_path, base_path)
    
    # Создание обновленного содержимого для mkdocs.yml
    mkdocs_content = """site_name: tg-note-kb Documentation
site_description: Knowledge Base Documentation
site_author: Knowledge Base Owner
site_url: https://ArtyomZemlyak.github.io/tg-note-kb/

repo_name: ArtyomZemlyak/tg-note-kb
repo_url: https://github.com/ArtyomZemlyak/tg-note-kb
edit_uri: edit/main/docs/

docs_dir: ../topics  # Изменен путь к базе знаний

theme:
  name: material
  language: en
  palette:
    # Palette toggle for light mode
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Palette toggle for dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.footer
    - search.suggest
    - search.highlight
    - search.share
    - toc.follow
    - content.code.copy
    - content.code.annotate
    - content.tabs.link

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - admonition
  - pymdownx.details
  - pymdownx.tasklist:
      custom_checkbox: true
  - attr_list
  - md_in_html
  - toc:
      permalink: true

plugins:
  - search
  - tags
  - autonav  # Добавлен плагин для автоматической генерации навигации

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/ArtyomZemlyak/tg-note-kb
      name: GitHub Repository

# Автоматически сгенерированная навигация
nav:"""
    
    # Функция для рекурсивного вывода навигации
    def print_nav(items, indent=2):
        result = ""
        for item in items:
            if isinstance(item, dict):
                # Это подкаталог
                for key, value in item.items():
                    result += " " * indent + f"- {key}:\n"
                    result += print_nav(value, indent + 2)
            else:
                # Это файл
                result += " " * indent + f"- {item}\n"
        return result
    
    # Добавляем сгенерированную навигацию к основному содержимому
    nav_content = print_nav(nav_structure)
    full_content = mkdocs_content + "\n" + nav_content
    
    # Сохраняем результат в новый файл
    output_path = base_path / "mkdocs_updated.yml"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    # Также создаем файл nav.md для плагина literate-nav
    nav_output_path = base_path / "nav.md"
    nav_content = "# Навигация по базе знаний\n\n" + print_nav(nav_structure)
    with open(nav_output_path, 'w', encoding='utf-8') as f:
        f.write(nav_content)
    
    print(f"Сгенерированный файл mkdocs сохранен как: {output_path}")
    print(f"Сгенерированный файл навигации сохранен как: {nav_output_path}")
    print("\nСодержимое mkdocs.yml:")
    print(full_content)
    print("\nСодержимое nav.md:")
    print(nav_content)

if __name__ == "__main__":
    main()