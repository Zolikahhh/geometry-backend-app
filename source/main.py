#!/usr/bin/env python3
"""
Szoftverfesztelési folyamatok példaprogram
SZTE TTIK, Informatikai Intézet, Szoftverfejlesztés Tanszék
cc-by-nc-nd
"""

import cowsay
import geometry
import rich

def main():
    l = float(input('A központi sín hossza (méter)? '))
    r = float(input('A kötél hossza (méter)? '))
    h = float(input('A fű magassága (centiméter)? '))
    output = cowsay.get_output_string('cow', f"{geometry.volume(l, r, h):.3f} köbméternyi füvet legeltem!").split('\n')
    words = output[1]
    output[1] = words[:2] + '[green]' + words[2:-2] + '[/green]' + words[-2:]
    rich.print('\n'.join(output))

if __name__ == "__main__":
    main()
