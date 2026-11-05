# Renders option A (open book) from the same geometry as icono-biblioteca.svg.
import os, sys
from PIL import Image, ImageDraw

OUT = sys.argv[1]
S = 2048                      # draw big, then downscale for clean edges
k = S / 64.0
BLUE, WHITE, CELESTE = (11, 77, 162, 255), (255, 255, 255, 255), (31, 155, 207, 255)

def P(x, y): return (x * k, y * k)

def cubic(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        pts.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                    u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    return pts

def page(sign):
    x = lambda v: 32 + sign * (32 - v)   # mirror around the spine
    top = cubic((32, 19.5), (x(26.5), 15.6), (x(19.5), 14.6), (x(11.5), 15.6))
    bottom = cubic((x(11.5), 46.4), (x(19.5), 45.5), (x(26.5), 46.6), (32, 50.5))
    return [P(*p) for p in top + bottom]

img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.rounded_rectangle((0, 0, S - 1, S - 1), radius=14 * k, fill=BLUE)
d.polygon(page(1), fill=WHITE)
d.polygon(page(-1), fill=WHITE)
w = 2.4 * k
d.line([P(32, 21), P(32, 49)], fill=BLUE, width=int(w))
for y in (21, 49): d.ellipse((P(32, y)[0] - w / 2, P(32, y)[1] - w / 2, P(32, y)[0] + w / 2, P(32, y)[1] + w / 2), fill=BLUE)
d.polygon([P(40.5, 15.2), P(40.5, 29.5), P(44, 26.6), P(47.5, 29.5), P(47.5, 15.1)], fill=CELESTE)

os.makedirs(OUT, exist_ok=True)
for s in (32, 64, 180, 512):
    img.resize((s, s), Image.LANCZOS).save(os.path.join(OUT, f'icono-biblioteca-{s}.png'), optimize=True)
print(sorted((f, os.path.getsize(os.path.join(OUT, f))) for f in os.listdir(OUT) if f.endswith('.png')))
