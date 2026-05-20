
from tkinter import *
from ui.canvas_view import CanvasView
from ui.control_panel import ControlPanel
from ui.formula_panel import FormulaPanel
from ui.coordinate_table import CoordinateTable
from ui.navigation_panel import NavigationPanel

class GrafikaApp:
    def __init__(self,root):
        root.title("Project Akhir Grafika Komputer")
        root.geometry("1850x980")

        top = Frame(root)
        top.pack(fill="x", pady=5)

        toolbar = Frame(root)
        toolbar.pack(fill="x")

        main_frame = Frame(root)
        main_frame.pack(fill="both", expand=True)

        left_frame = Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = Frame(main_frame, width=350)
        right_frame.pack(side="right", fill="y", padx=10)

        self.canvas = CanvasView(left_frame)
        self.canvas.pack(padx=10, pady=10)

        self.formula = FormulaPanel(right_frame)
        self.formula.pack(fill="both", expand=True, pady=10)

        Button(
            toolbar,
            text="Tampilkan Navigasi",
            bg="lightblue",
            command=self.show_navigation
        ).pack(side="right", padx=10)

        bottom = Frame(root)
        bottom.pack(fill="x")

        self.table = CoordinateTable(bottom)
        self.table.pack(fill="x")

        self.controls = ControlPanel(
            top,
            self.canvas,
            self.formula,
            self.table
        )
        self.controls.pack(fill="x", padx=10)

        self.nav_window = None

    def show_navigation(self):
        if self.nav_window is None or not self.nav_window.winfo_exists():
            self.nav_window = NavigationPanel(
                self.canvas.master,
                self.canvas
            )
