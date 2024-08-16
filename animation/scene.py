from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SimpleTable(Scene):
    def construct(self):
        # Define the table contents
        table_data = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]

        # Create the table
        table = Table(
            table_data,
            row_labels=[Text(f"Row {i+1}") for i in range(3)],
            col_labels=[Text(f"Col {i+1}") for i in range(3)],
            include_outer_lines=True
        )

        # Add the table to the scene
        self.play(Create(table))
        # self.play(Create(table.get_vertical_lines(), run_time=1.5),
        #           Create(table.get_horizontal_lines(), run_time=1.5),)
        # self.play(
        #     Write(table.get_rows()),
        #     Write(table.get_row_labels()),
        #     Write(table.get_col_labels()),
        #     run_time=2
        # )

if __name__ == "__main__":
    scene = SimpleTable()
    scene.render()