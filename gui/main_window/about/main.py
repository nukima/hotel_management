from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox, Tk, ttk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    About()


class About(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        notebook = ttk.Notebook(self)
        tab1 = self.create_tab(notebook, "Income")
        tab2 = self.create_tab_2(notebook, "Check In/Out")
        tab3 = self.create_tab_3(notebook, "Room Type Income")
        tab4 = self.create_tab_4(notebook, "Service Type Income")

        # Add the tabs to the Notebook
        notebook.add(tab1, text="Income")
        notebook.add(tab2, text="Check In/Out")
        notebook.add(tab3, text="Room Type Income")
        notebook.add(tab4, text="Service Type Income")

        # Pack the Notebook widget
        notebook.pack()


    def create_tab(self, parent, title):
        tab_frame = Frame(parent)
        tab_frame.configure(bg="#FFFFFF")

        canvas = Canvas(
            tab_frame,
            bg="#FFFFFF",
            height=500,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        # Fetch data from the database
        months, total_bills = get_bill_value_group_by_month()

        # Create the bar chart
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(
            months,
            total_bills,
            color="#5E95FF",
            width=0.5,
            edgecolor="#5E95FF",
            linewidth=1,
        )
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Bill Value')
        ax.set_title('Time Series Bar Chart of Total Bill Value')
        ax.set_xticklabels(months, rotation=45)

        # Create a FigureCanvasTkAgg object to display the chart in the Canvas widget
        canvas_widget = FigureCanvasTkAgg(fig, master=tab_frame)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()

        # Place the FigureCanvasTkAgg object within the Canvas widget
        canvas.create_window(0, 0, anchor='nw', window=canvas_widget.get_tk_widget())
        canvas.pack()

        return tab_frame

    def create_tab_2(self, parent, title):
        tab_frame = Frame(parent)
        tab_frame.configure(bg="#FFFFFF")

        canvas = Canvas(
            tab_frame,
            bg="#FFFFFF",
            height=500,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        # Fetch data from the database
        months, total_check_ins, total_check_outs = get_total_check_in_check_out_group_by_month()
        # Create the multi-line chart
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(months, total_check_ins, color="#5E95FF", linewidth=1, label="Check In")
        ax.plot(months, total_check_outs, color="#FFA500", linewidth=1, label="Check Out")
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Check In/Out')
        ax.set_title('Time Series Line Chart of Total Check In/Out')
        ax.set_xticklabels(months, rotation=45)
        ax.legend()

        # Create a FigureCanvasTkAgg object to display the chart in the Canvas widget
        canvas_widget = FigureCanvasTkAgg(fig, master=tab_frame)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()

        # Place the FigureCanvasTkAgg object within the Canvas widget
        canvas.create_window(0, 0, anchor='nw', window=canvas_widget.get_tk_widget())
        canvas.pack()

        return tab_frame

    def create_tab_3(self, parent, title):
        tab_frame = Frame(parent)
        tab_frame.configure(bg="#FFFFFF")

        canvas = Canvas(
            tab_frame,
            bg="#FFFFFF",
            height=500,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        # Fetch data from the database
        months, deluxe_bills, normal_bills = get_total_bill_value_each_room_type_group_by_month()
        # create mullti-bar chart
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(
            months,
            deluxe_bills,
            color="#5E95FF",
            width=0.5,
            edgecolor="#5E95FF",
            linewidth=1,
            label="Deluxe",
        )
        ax.bar(
            months,
            normal_bills,
            color="#FFA500",
            width=0.5,
            edgecolor="#FFA500",
            linewidth=1,
            label="Normal",
        )
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Bill Value')
        ax.set_title('Time Series Bar Chart of Total Bill Value Each Room Type')
        ax.set_xticklabels(months, rotation=45)
        ax.legend()

        # Create a FigureCanvasTkAgg object to display the chart in the Canvas widget
        canvas_widget = FigureCanvasTkAgg(fig, master=tab_frame)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()

        # Place the FigureCanvasTkAgg object within the Canvas widget
        canvas.create_window(0, 0, anchor='nw', window=canvas_widget.get_tk_widget())
        canvas.pack()

        return tab_frame

    def create_tab_4(self, parent, title):
        tab_frame = Frame(parent)
        tab_frame.configure(bg="#FFFFFF")

        canvas = Canvas(
            tab_frame,
            bg="#FFFFFF",
            height=500,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        # Fetch data from the database
        months, service_values = get_total_service_value_each_type_group_by_month()
        # create stacked area chart
        fig, ax = plt.subplots(figsize=(7, 4))
        service_names = list(service_values.keys())
        list_of_values = list(service_values.values())
        ax.stackplot(months, *list_of_values, labels=service_names)
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Service Value')
        ax.set_title('Time Series Stacked Area Chart of Total Service Value Each Type')
        ax.set_xticklabels(months, rotation=45)
        ax.legend()

        # Create a FigureCanvasTkAgg object to display the chart in the Canvas widget
        canvas_widget = FigureCanvasTkAgg(fig, master=tab_frame)
        canvas_widget.draw()
        canvas_widget.get_tk_widget().pack()

        # Place the FigureCanvasTkAgg object within the Canvas widget
        canvas.create_window(0, 0, anchor='nw', window=canvas_widget.get_tk_widget())
        canvas.pack()

        return tab_frame