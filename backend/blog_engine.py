import os
import frontmatter
import markdown
from datetime import datetime

POSTS_DIR = "posts"

def get_posts():
    """
    Lee todos los archivos .md de la carpeta posts, extrae metadatos
    y los devuelve ordenados por fecha (descendente).
    """
    posts = []
    if not os.path.exists(POSTS_DIR):
        print(f"Warning: {POSTS_DIR} directory not found.")
        return []

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
                
                # Crear objeto Post
                post_data = {
                    "slug": filename.replace(".md", ""),
                    "title": post.get("title", "Sin Título"),
                    "date": post.get("date", "1970-01-01"),
                    "author": post.get("author", "Anonimo"),
                    "image": post.get("image", ""),
                    "summary": post.get("summary", ""),
                    "content": post.content # Markdown raw, not needed for list
                }
                posts.append(post_data)
    
    # Ordenar por fecha (más reciente primero)
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts

def get_post_by_slug(slug):
    """
    Busca un post por slug, convierte su contenido a HTML y devuelve los datos.
    Retorna None si no existe.
    """
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, "r", encoding="utf-8") as f:
        post = frontmatter.load(f)
        
        # Convertir Markdown a HTML
        # Se activa la extensión 'tables' para soportar tablas y 'fenced_code' para bloques de código
        html_content = markdown.markdown(post.content, extensions=['tables', 'fenced_code'])
        
        return {
            "slug": slug,
            "title": post.get("title", "Sin Título"),
            "date": post.get("date", "1970-01-01"),
            "author": post.get("author", "Anonimo"),
            "image": post.get("image", ""),
            "content": html_content
        }
