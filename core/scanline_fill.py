
def scanline_fill(canvas, screen_points, fill_color):
    """
    Algoritma Scan Line Fill untuk mengisi polygon.

    Parameter:
    - canvas: Tkinter Canvas
    - screen_points: list of (px, py) dalam koordinat layar
    - fill_color: warna fill
    """

    if len(screen_points) < 3:
        return

    n = len(screen_points)

    # Cari batas Y minimum dan maksimum
    y_min = int(min(p[1] for p in screen_points))
    y_max = int(max(p[1] for p in screen_points))

    # Bangun Edge Table (ET)
    # Setiap edge disimpan sebagai (y_lower, y_upper, x_at_y_lower, inverse_slope)
    edges = []

    for i in range(n):
        x1, y1 = screen_points[i]
        x2, y2 = screen_points[(i + 1) % n]

        # Abaikan edge horizontal
        if int(y1) == int(y2):
            continue

        # Pastikan y1 < y2 (y1 = bawah/lower)
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        # inverse slope = dx/dy
        inv_slope = (x2 - x1) / (y2 - y1)

        edges.append({
            'y_min': int(y1),
            'y_max': int(y2),
            'x_current': x1,
            'inv_slope': inv_slope
        })

    # Scan dari y_min ke y_max
    for y in range(y_min, y_max + 1):

        # Cari semua edge yang aktif pada scan line y ini
        intersections = []

        for edge in edges:
            if edge['y_min'] <= y < edge['y_max']:
                # Hitung x intersection pada scan line y
                x_intersect = edge['x_current'] + (y - edge['y_min']) * edge['inv_slope']
                intersections.append(x_intersect)

        # Urutkan intersection dari kiri ke kanan
        intersections.sort()

        # Gambar garis antara pasangan intersection
        for i in range(0, len(intersections) - 1, 2):
            x_start = int(intersections[i])
            x_end = int(intersections[i + 1])

            if x_start < x_end:
                canvas.create_line(
                    x_start, y, x_end, y,
                    fill=fill_color,
                    tags="scanline_fill"
                )
