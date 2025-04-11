import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from fpdf import FPDF

# Full metric names and options
metrics = {
    "Attack Vector": ["Network", "Adjacent", "Local", "Physical"],
    "Attack Complexity": ["Low", "High"],
    "Privileges Required": ["None", "Low", "High"],
    "User Interaction": ["None", "Required"],
    "Scope": ["Unchanged", "Changed"],
    "Confidentiality": ["None", "Low", "High"],
    "Integrity": ["None", "Low", "High"],
    "Availability": ["None", "Low", "High"]
}

tooltips = {
    "Attack Vector": "Where the attacker needs to be located to exploit the vulnerability.",
    "Attack Complexity": "Conditions beyond the attacker's control required for exploitation.",
    "Privileges Required": "Level of access needed before an attacker can exploit the vulnerability.",
    "User Interaction": "Whether a user needs to click or open something.",
    "Scope": "Does the vulnerability impact other components beyond its scope?",
    "Confidentiality": "Impact on the disclosure of information.",
    "Integrity": "Impact on the trustworthiness and accuracy of data.",
    "Availability": "Impact on the availability of the impacted component."
}

# CVSS Score calculator stub
def calculate_score():
    # Simplified example logic
    score = 9.8  # Just a placeholder value
    result.set(f"CVSS Vector: [Generated Vector]\nBase Score: {score}\nSeverity: Critical")

def export_txt():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if filepath:
        with open(filepath, "w") as f:
            f.write(result.get())

def export_pdf():
    filepath = filedialog.asksaveasfilename(defaultextension=".pdf")
    if filepath:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in result.get().split("\n"):
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(filepath)

def toggle_dark_mode():
    current_bg = root.cget("bg")
    new_bg = "black" if current_bg == "SystemButtonFace" else "SystemButtonFace"
    new_fg = "white" if new_bg == "black" else "black"
    root.configure(bg=new_bg)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=new_bg, fg=new_fg)
        except:
            pass

root = tk.Tk()
root.title("CVSS v3.1 Calculator")

entries = {}
row = 0
for metric, options in metrics.items():
    label = tk.Label(root, text=metric)
    label.grid(row=row, column=0, sticky='w', padx=5, pady=2)
    combo = ttk.Combobox(root, values=options, state="readonly")
    combo.current(0)
    combo.grid(row=row, column=1, padx=5, pady=2)
    entries[metric] = combo

    # Tooltip binding
    def create_tooltip(widget, text):
        tooltip = tk.Toplevel(widget)
        tooltip.withdraw()
        tooltip.wm_overrideredirect(True)
        label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1)
        label.pack()
        def enter(event):
            tooltip.deiconify()
            tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")
        def leave(event):
            tooltip.withdraw()
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)
    create_tooltip(label, tooltips[metric])
    row += 1

# Result display
result = tk.StringVar()
output = tk.Label(root, textvariable=result, justify="left")
output.grid(row=row, column=0, columnspan=2, padx=5, pady=10)

# Action buttons
tk.Button(root, text="✅ Calculate", command=calculate_score).grid(row=row+1, column=0, pady=5)
tk.Button(root, text="📝 Export as TXT", command=export_txt).grid(row=row+2, column=0, pady=5)
tk.Button(root, text="📄 Export as PDF", command=export_pdf).grid(row=row+2, column=1, pady=5)
tk.Button(root, text="🌒 Toggle Dark Mode", command=toggle_dark_mode).grid(row=row+1, column=1, pady=5)

root.mainloop()
