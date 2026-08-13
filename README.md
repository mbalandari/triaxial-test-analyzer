# Triaxial Test Analyzer

A professional desktop application for analyzing triaxial rock mechanics test data.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [Architecture Overview](docs/architecture.md)
- [Data Format Specification](docs/data_format.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Changelog](docs/changelog.md)

---

## ▶️ Running the Application

Run from project root:

```bash
python -m gui.app
```

---

## 📁 Example Data

Example triaxial test files are located in:

```bash
examples/
```

---

## 📊 Features

- Load CSV/XLSX triaxial test files
- Compute peak stress & strain
- Compute σ₁ and σ₃
- Generate Mohr circles (perfectly round)
- Fit Mohr–Coulomb envelope
- Export TXT, PDF, DOCX reports
- Clean PySide6 GUI

---

## 📈 Mohr Circles

- Equal aspect ratio
- Legend outside plot
- Tangent points shown
- Envelope drawn over correct domain
- Exported plots not stretched

---

## 📤 Report Export

Formats:

- .txt
- .pdf
- .docx

PDF/DOCX include embedded Mohr plot.
