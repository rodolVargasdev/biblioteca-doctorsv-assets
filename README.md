# Biblioteca DoctorSV: archivos públicos

Imágenes que la Biblioteca DoctorSV necesita servir desde una dirección pública. Apps Script solo acepta el ícono de la pestaña (favicon) como una URL pública terminada en `.png`, y el repositorio de la Biblioteca es privado, así que el ícono vive aquí y se publica con GitHub Pages.

Aquí solo van imágenes públicas. Nada de código de la aplicación, datos, credenciales ni documentos internos.

## Archivos

| archivo | uso |
|---|---|
| `icono-biblioteca-64.png` | ícono de la pestaña del navegador (`setFaviconUrl` en `WebApp.gs` de la Biblioteca) |
| `icono-biblioteca-32.png` | ícono de pestaña en tamaño pequeño |
| `icono-biblioteca-180.png`, `icono-biblioteca-512.png` | tamaños grandes, para accesos directos en el teléfono o materiales |
| `icono-biblioteca.svg` | el original en vector |
| `generar_icono.py` | genera los PNG desde la misma geometría del SVG (Pillow): `python generar_icono.py .` |

URL publicada: `https://rodolvargasdev.github.io/biblioteca-doctorsv-assets/icono-biblioteca-64.png`

El ícono es un libro abierto blanco con un marcador celeste sobre el azul de DoctorSV (`#0b4da2`, `#1f9bcf`), elegido el 2026-11-05.

Cambiar un archivo cambia lo que ve todo el personal en la pestaña de la Biblioteca. Si se renombra, hay que actualizar la URL en `WebApp.gs` y desplegar la Biblioteca.
