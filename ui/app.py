
from tkinter import *
from ui.canvas_view import CanvasView
from ui.control_panel import ControlPanel
from ui.formula_panel import FormulaPanel
from ui.coordinate_table import CoordinateTable

class GrafikaApp:

    def __init__(self, root):

        root.title("Project Akhir Grafika Komputer")
        root.geometry("1850x980")

        main_paned = PanedWindow(
            root,
            orient=HORIZONTAL,
            sashrelief=RAISED,
            sashwidth=8
        )

        main_paned.pack(fill=BOTH, expand=True)

        left_panel = Frame(main_paned)
        right_panel = Frame(main_paned)

        main_paned.add(left_panel, minsize=350)
        main_paned.add(right_panel, minsize=600)

        top_controls = Frame(left_panel)
        top_controls.pack(fill=X)

        bottom_formula = Frame(left_panel)
        bottom_formula.pack(fill=BOTH, expand=True)

        self.formula = FormulaPanel(bottom_formula)
        self.formula.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.canvas = CanvasView(right_panel)
        self.canvas.pack(fill=BOTH, expand=True)

        self.table = CoordinateTable(root)
        self.table.pack(fill=X, side=BOTTOM)

        self.controls = ControlPanel(
            top_controls,
            self.canvas,
            self.formula,
            self.table
        )

        self.controls.pack(fill=BOTH, expand=True, padx=5, pady=5)
