"""Render a shaded ASCII donut in a fixed-size character canvas."""

from __future__ import annotations

import math


WIDTH = 40
HEIGHT = 40
SHADES = ".,-~:;=!*#$@"


def render_donut(width: int = WIDTH, height: int = HEIGHT) -> str:
    """Return an ASCII donut centered in a ``width`` by ``height`` canvas.

    The character buffer has exactly ``height`` rows and each row has exactly
    ``width`` columns.  Characters in ``SHADES`` encode surface brightness.
    """
    if width < 1 or height < 1:
        raise ValueError("width and height must be positive")

    canvas = [[" "] * width for _ in range(height)]
    depth = [[0.0] * width for _ in range(height)]

    # A torus is sampled in polar coordinates and projected with a perspective
    # transform.  Halving the vertical scale compensates for terminal character
    # cells, which are usually about twice as tall as they are wide.
    for theta_index in range(0, 628, 4):
        theta = theta_index / 100
        cos_theta, sin_theta = math.cos(theta), math.sin(theta)
        for phi_index in range(0, 628, 2):
            phi = phi_index / 100
            cos_phi, sin_phi = math.cos(phi), math.sin(phi)

            # theta travels around the large ring; phi travels around the tube.
            ring_radius = 2 + cos_phi
            x = ring_radius * cos_theta
            y = ring_radius * sin_theta
            z = 5 + sin_phi
            inverse_z = 1 / z

            column = int(width / 2 + width * 0.52 * inverse_z * x)
            row = int(height / 2 - height * 0.26 * inverse_z * y)
            brightness = -0.3 * cos_phi * cos_theta - 0.6 * cos_phi * sin_theta + 0.7 * sin_phi

            if 0 <= column < width and 0 <= row < height and inverse_z > depth[row][column]:
                depth[row][column] = inverse_z
                shade = max(0, min(len(SHADES) - 1, int(brightness * 8 + 5)))
                canvas[row][column] = SHADES[shade]

    return "\n".join("".join(row) for row in canvas)


def main() -> None:
    """Print a 40×40 ASCII donut."""
    print(render_donut())


if __name__ == "__main__":
    main()
