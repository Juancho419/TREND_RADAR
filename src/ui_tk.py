"""
Simple Tkinter UI for the Trend Radar MVP.

It shows:
- a main window
- a button to run the analysis
- a status label to show messages to the user
"""

import tkinter as tk
from tkinter import messagebox

from service import run_analysis


def on_run_analysis() -> None:
    """
    Handle the click on the 'Analyze' button.

    It calls run_analysis() and shows a message when finished.
    """
    try:
        status_label.config(text="Running analysis... please wait.")
        # Force UI update so the user sees the message immediately
        root.update_idletasks()

        output_path = run_analysis()

        status_label.config(text="Analysis completed.")
        messagebox.showinfo(
            "Trend Radar",
            f"Analysis completed.\n\nCSV report written to:\n{output_path}",
        )
    except Exception as exc:  # very generic on purpose for the MVP
        status_label.config(text="An error occurred during analysis.")
        messagebox.showerror("Trend Radar - Error", str(exc))


# Create main window
root = tk.Tk()
root.title("Trend Radar - MVP")

# Basic window size (you can adjust if needed)
root.geometry("420x200")

# Title label
title_label = tk.Label(
    root,
    text="Trend Radar - MVP",
    font=("Segoe UI", 14, "bold"),
)
title_label.pack(pady=10)

# (For ahora, sin campos de fecha: solo un botón)
run_button = tk.Button(
    root,
    text="ANALYZE",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=on_run_analysis,
)
run_button.pack(pady=10)

# Status label
status_label = tk.Label(
    root,
    text="Ready.",
    font=("Segoe UI", 10),
)
status_label.pack(pady=10)

# Start Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
