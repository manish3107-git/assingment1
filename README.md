# Möbius Strip Modeling in Python

This project models a Möbius strip using parametric equations, computes its surface area and edge length, and visualizes it in 3D.

## Features
- 3D parametric modeling of Möbius strip
- Surface area calculation using numerical integration
- Edge length calculation
- 3D plot with Matplotlib

## Requirements

Install dependencies:
```bash
pip install numpy matplotlib
```

## Usage

Run the project using the Makefile:
```bash
make run
```

Clean up bytecode:
```bash
make clean
```

## Parametric Equations

```math
x(u,v) = (R + v * cos(u/2)) * cos(u)
y(u,v) = (R + v * cos(u/2)) * sin(u)
z(u,v) = v * sin(u/2)
```

Where:
- u ∈ [0, 2π]
- v ∈ [-w/2, w/2]

## Author
Manish Raj

## License
MIT
