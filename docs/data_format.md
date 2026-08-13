# Data Format Specification

This document explains the required format for triaxial test input files.

---

## 1. Required Columns

Each CSV/XLSX file must contain:

- axial_strain
- axial_stress
- confining_pressure

Column names are case-insensitive.

---

## 2. Example

axial_strain,axial_stress,confining_pressure

0.0000,0.00,5

0.0020,12.50,5

0.0040,25.10,5

...

---

## 3. Units

- Axial strain: decimal (e.g., 0.012)
- Axial stress: MPa
- Confining pressure: MPa

---

## 4. Multiple Specimens

You may load multiple files at once.

Each file represents one specimen.

---

## 5. Common Errors

- Missing columns
- Empty files
- Non-numeric values
- Wrong delimiter (use comma)

---
