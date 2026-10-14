# Clon Web Octavio Bikes

Sitio web estático de Octavio Bikes, una tienda de bicicletas y accesorios.

## Estructura

- `index.html` - Página principal (build de producción)
- `favicon.png` - Icono del sitio
- `server.py` - Servidor HTTP simple para preview local (puerto 8080)
- `assets/` - Recursos estáticos (imágenes, CSS, JS)

## Uso

### Preview local

```bash
python server.py 8080
```

Abre http://localhost:8080 en el navegador.

### Despliegue

Cualquier hosting estático (Netlify, Vercel, GitHub Pages, etc.) sirviendo `index.html` como entry point.

## Tecnologías

- HTML5 + CSS3 + JavaScript (React compilado)
- Build de producción con assets inlined/preloaded
- SEO meta tags configurados