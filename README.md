# CVSS v3.1 Calculator GUI

A simple and intuitive graphical user interface (GUI) tool to calculate CVSS (Common Vulnerability Scoring System) v3.1 base scores. This tool is designed to help security analysts, students, and professionals assess vulnerabilities easily using descriptive labels, tooltips, and export options.

---

## Features

- Full metric names (no abbreviations)
- Hover tooltips for every metric explaining its purpose
- Toggle between light and dark themes
- Export results as `.txt` or `.pdf`
- Displays vector string, base score, and severity rating (simplified logic)

---

## Screenshot (Dark Mode)

![CVSS GUI Screenshot - Dark Mode](screenshot_dark.png)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cvss-calculator-gui.git
cd cvss-calculator-gui
```

2. **Install the required package**
```bash
pip install fpdf
```

---

## Usage

Run the application using:

```bash
python cvss_calculator_gui.py
```

Then:

- Select values from each dropdown menu
- Hover over metric labels to view explanations
- Click "Calculate" to view the CVSS score and vector
- Use the export buttons to save results as text or PDF
- Toggle dark mode using the provided switch

---

## Export Options

- **TXT**: Plain text summary of your results
- **PDF**: Formatted report with CVSS vector and score

---

## Technologies Used

- Python 3.x
- Tkinter (standard GUI library)
- fpdf (for PDF generation)

---

## Roadmap

- Implement full CVSS vector logic
- Add support for Temporal and Environmental metrics
- Extend to web version (Flask or React frontend)

---

## License

This project is licensed under the MIT License.

---

## Author

**Athul M**  
[LinkedIn](https://www.linkedin.com/in/athul-m-zeous/)  
[GitHub](https://github.com/Zeousultra)
