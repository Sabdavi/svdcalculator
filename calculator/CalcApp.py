import tkinter as tk
from tkinter import messagebox, font
from enum import Enum
from calculator import Calculator


# an enum class that will enumerate the operations by numbers
class Operations(Enum):
    addition = 0
    multiplication = 1
    subtraction = 2
    determinant = 3
    transpose = 4
    power = 5
    eigenvalue = 6


class CalcApp:
    def __init__(self):
        # initializing our instance variable which are the main building block for our GUI
        # we will reference these variables throughout the GUI code
        # the main window of our app
        self.root = tk.Tk()
        self.root.geometry("800x500")
        # the window can't be resized for design convenience
        self.root.resizable(False, False)
        self.root.title("Matrix Calculator")
        # the main frame that will hold our operation buttons
        self.opFrame = tk.Frame(self.root, highlightbackground="black", highlightthickness=2, padx=10, pady=10)
        self.opFrame.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=20, pady=20)
        # a list that will hold our operation button object which will be referenced throughout the code
        self.opButtons = []
        # the main frame that will show the content and the changes of the app
        self.contentframe = tk.Frame(self.root, highlightbackground="black", highlightthickness=2)
        self.contentframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20), pady=20)

        self.chooseOP = tk.Label(self.contentframe, text="Choose Operation", font=15)
        self.chooseOP.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.defaultFont = font.Font(family="Helvetica", size=9, weight="normal")
        self.clickedFont = font.Font(family="Helvetica", size=10, weight="bold")

        opLabel = tk.Label(self.opFrame, text="OPERATIONS", font=("Helvetica", 12, "bold"))
        opLabel.pack(pady=5)

        additionBu = tk.Button(self.opFrame, text="ADDITION", width=20, pady=5, font=self.defaultFont,
                               command=lambda: self.initialize_operation(Operations.addition))
        additionBu.pack(pady=5)
        self.opButtons.append(additionBu)

        multyBu = tk.Button(self.opFrame, text="MULTIPLICATION", width=20, pady=5, font=self.defaultFont,
                            command=lambda: self.initialize_operation(Operations.multiplication))
        multyBu.pack(pady=5)
        self.opButtons.append(multyBu)

        subtBu = tk.Button(self.opFrame, text="SUBTRACTION", width=20, pady=5, font=self.defaultFont,
                           command=lambda: self.initialize_operation(Operations.subtraction))
        subtBu.pack(pady=5)
        self.opButtons.append(subtBu)

        deterBu = tk.Button(self.opFrame, text="DETERMINANT", width=20, pady=5, font=self.defaultFont,
                            command=lambda: self.initialize_operation(Operations.determinant))
        deterBu.pack(pady=5)
        self.opButtons.append(deterBu)

        transposeBu = tk.Button(self.opFrame, text="TRANSPOSE", width=20, pady=5, font=self.defaultFont,
                                command=lambda: self.initialize_operation(Operations.transpose))
        transposeBu.pack(pady=5)
        self.opButtons.append(transposeBu)

        powBu = tk.Button(self.opFrame, text="POWER", width=20, pady=5, font=self.defaultFont,
                          command=lambda: self.initialize_operation(Operations.power))
        powBu.pack(pady=5)
        self.opButtons.append(powBu)

        eigenValuesBu = tk.Button(self.opFrame, text="EIGENVALUES", width=20, pady=5, font=self.defaultFont,
                                  command=lambda: self.initialize_operation(Operations.eigenvalue))
        eigenValuesBu.pack(pady=5)
        self.opButtons.append(eigenValuesBu)

    def run(self):
        self.root.mainloop()

    def initialize_operation(self, operation):
        # getting the currently pressed button from the list of buttons
        pressedButton = self.opButtons[operation.value]
        # if button in not pressed already (not highlighted ie:bg!=orange) then initialize operation else do nothing
        if pressedButton.cget("bg") != "orange":
            # remove highlight from all operation buttons
            for button in self.opButtons:
                button.config(bg="#f0f0f0", fg="black", relief="raised", font=self.defaultFont)
                # highlight the pressed operation button
            pressedButton.config(bg="orange", fg="white", relief="sunken", font=self.clickedFont)
            # remove the "choose operation" label that appears on start of application
            if self.chooseOP:
                self.chooseOP.destroy()
            # clear what is already on the screen
            self.clearScreen()
            # initialize the dimension input screen and get the tuple of chosen dimensions returned
            dimTuple = self.dimension_input(operation)
            # a fill in matrix button that switches to a screen where the user can fill in the entries of the matrix
            button = tk.Button(self.contentframe, text="FILL IN MATRIX",
                               command=lambda: self.input_matrix_screen(operation, dimTuple))
            button.place(anchor=tk.CENTER, relx=0.5, rely=0.9)

    def clearScreen(self):
        previous_screen = self.contentframe.winfo_children()
        for child in previous_screen:
            child.destroy()

    def dimension_input(self, operation):
        # a label showing the title of the screen content
        dimlabel = tk.Label(self.contentframe, text="SET DIMENSION", font=30)
        dimlabel.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        # a main frame that will contain the dimension Widgets
        dimframe = tk.Frame(self.contentframe)
        dimframe.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        # a frame that will contain the dimension drop down box for the first matrix
        innerDimFrame = tk.LabelFrame(dimframe, text="MATRIX A", padx=10, pady=10)
        innerDimFrame.grid(columnspan=2, row=0, column=0, pady=(0, 20))
        # tkinter dynamic variable that will contain the dimension values selected
        row = tk.IntVar()
        col = tk.IntVar()
        # row and columns default values set to 2
        row.set(2)
        col.set(2)
        # matrices are of maximum size of 5 now just to fit on our ugly GUI but our calculator methods work on nxn
        # a dropdown box to select the number of rows
        rowLabel = tk.Label(innerDimFrame, text="row: ", font=30)
        rowBox = tk.OptionMenu(innerDimFrame, row, 2, 3, 4, 5)
        # put the row dropdown box on the screen
        rowLabel.grid(column=0, row=0)
        rowBox.grid(column=1, row=0)
        # if the operation requires a square matrix set the row=col and limit the user to choose only rows(=columns)
        if operation == Operations.determinant or operation == Operations.power or operation == Operations.eigenvalue:
            rowLabel.config(text="dim: ")
            col = row
            # if selected operation is power operation then give the user the option to chose the power
            if operation == Operations.power:
                pow = tk.IntVar()
                pow.set(2)
                powLabel = tk.Label(innerDimFrame, text="pow: ", font=30)
                powBox = tk.OptionMenu(innerDimFrame, pow, 2, 3, 4, 5)
                # put it on the screen
                powLabel.grid(column=0, row=1)
                powBox.grid(column=1, row=1)
                # return the dimension and power of the square matrix
                return row, col, pow
            # if the square matrix operation is not a power operation then only return the dimension
            return row, col
        # if the operation accepts nxm matrix give the user the option to choose columns too
        else:
            # create the column dropdown box
            colLabel = tk.Label(innerDimFrame, text="col: ", font=30)
            colBox = tk.OptionMenu(innerDimFrame, col, 2, 3, 4, 5)
            # put it on the screen
            colLabel.grid(column=0, row=1)
            colBox.grid(column=1, row=1)

        # if the operation can take 2 matrices of different sizes (multiplication)
        # then create a second frame letting the user select 2nd matrix dimension (same as first matrix)
        if operation == Operations.multiplication:
            innerDimFrame2 = tk.LabelFrame(dimframe, text="MATRIX B", padx=10, pady=10)
            innerDimFrame2.grid(columnspan=2, row=1, column=0)
            colLabel2 = tk.Label(innerDimFrame2, text="col: ", font=30)
            colLabel2.grid(column=0, row=0)
            colMatrixB = tk.IntVar()
            colMatrixB.set(1)
            colBox_mult = tk.OptionMenu(innerDimFrame2, colMatrixB, 2, 3, 4, 5)
            colBox_mult.grid(column=1, row=0)
            # if the operation is multiplication return the dimensions (rows and columns of the 1st matrix and the
            # columns of 2nd matrix) in the tuple
            return row, col, colMatrixB
        else:
            # else just return the dimensions of the single matrix as a tuple
            return row, col

    def input_matrix_screen(self, operation, dimension):
        # clear screen
        self.clearScreen()
        # get the dimensions of the first matrix from the dimension tuple
        rows = dimension[0].get()
        columns = dimension[1].get()
        # a label showing the title of the current screen i.e: filling the input
        fillLabel = tk.Label(self.contentframe, text="FILL IN DATA", font=30)
        fillLabel.pack(side=tk.TOP, pady=20)
        # a main frame that will hold the actual matrix GUI's
        mainFrame = tk.Frame(self.contentframe)
        mainFrame.place(anchor=tk.CENTER, relx=0.45, rely=0.5)
        # a frame that will hold the GUI of the first matrix
        matrix1Frame = tk.Frame(mainFrame)
        matrix1Frame.grid(column=0, row=0, pady=(0, 30))
        # calling the fill_matrix() method that will create a matrix GUI and put it inside frame 1
        # fill_matrix() will return a list of entries (tkinter entry objects) containing the input data
        matrix1 = self.create_input_matrix(rows, columns, matrix1Frame, "A")

        matrix2 = None
        if operation == Operations.addition or operation == Operations.multiplication or operation == Operations.subtraction:
            matrix2Frame = tk.Frame(mainFrame)
            matrix2Frame.grid(column=0, row=1)
            # if the operation is multiplication then the rows of 1st matrix must be equal to columns of 1st matrix
            if operation == Operations.multiplication:
                rows = columns
                # get the columns of 2nd matrix which will be the 3rd element in the dimension tuple
                columns = dimension[2].get()
                matrix2 = self.create_input_matrix(rows, columns, matrix2Frame, "B")
            # if operation is addition or subtraction then the 2nd matrix must be the same size as the 1st matrix
            else:
                matrix2 = self.create_input_matrix(rows, columns, matrix2Frame, "B")
        # if the operation is the power operation get the power selected and returned as the 3rd element in the
        # dimension tuple
        power = None
        if operation == Operations.power:
            power = dimension[2].get()

        # when "CALCULATE" button is clicked call the validate function to check that the filled entries are valid
        # the power argument is just passed for future use and has no role in the validation method
        button = tk.Button(self.contentframe, text="CALCULATE",
                           command=lambda: self.validate(operation, matrix1, matrix2, power))
        button.place(anchor=tk.CENTER, relx=0.5, rely=0.9)

    # method to create a matrix GUI and show in on the screen
    def create_input_matrix(self, r, c, parent, name):
        # a label that shows the name of the matrix
        namelabel = tk.Label(parent, text=name + " = ", font=("Arial", 25))
        namelabel.pack(side=tk.LEFT)
        # a frame that will hold the whole matrix
        matrixFrame = tk.Frame(parent, bg="black")
        matrixFrame.pack(side=tk.LEFT)
        # empty list to store all the entry objects of the matrix
        entries = []
        # creating a cell for each entry and adding it to the appropriate position on the matrixFrame using a grid
        for row in range(r):
            entries.append([])
            for col in range(c):
                # create a frame to hold the current cell
                cellframe = tk.Frame(matrixFrame, bg="white", width=25, height=25)
                # add the cell frame to the matrix frame
                cellframe.grid(row=row, column=col, padx=0.5, pady=0.5)
                # create an entry widget for the current position
                entry = tk.Entry(cellframe, width=5, bg="white", bd=0, justify="center")
                # adding an event to the entry that will highlight it in orange when selected
                entry.bind("<FocusIn>", self.highlight_entry)
                # an event that will call unhighlight_entry() and remove highlight from the entry when not in focus
                entry.bind("<FocusOut>", self.unhighlight_entry)
                # add the entry to the current cell frame
                entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                # store the current entry object in the entry list
                entries[row].append(entry)
        # return the list of entries which will be our matrix
        return entries

    # a function to highlight a matrix entry cell
    def highlight_entry(self, event):
        entry = event.widget
        entry.configure(bg="orange")
        entry.master.configure(bg="orange")

    # a function to unhighlight a matrix entry cell
    def unhighlight_entry(self, event):
        entry = event.widget
        entry.configure(bg="white")
        entry.master.configure(bg="white")

    # a function that takes the input matrices and validate the input data
    def validate(self, operation, m1, m2, power=None):
        # a try except block that will try extract the data as number
        try:
            matrix1 = self.extractMatrix(m1)
            matrix2 = m2
            if m2:
                matrix2 = self.extractMatrix(m2)
            self.show_result(operation, matrix1, matrix2, power)
        # if the any of the input data is not a number raise an exception
        except ValueError:
            # show a warning message box if input data is not numbers
            messagebox.showwarning("Value error", "Only numerical values accepted! ")

    # a method that will take a matrix (2d  list) of entry objects and return a matrix of actual values (numbers)
    def extractMatrix(self, entries):
        # use of list comprehension to get the actual value from every entry object as a 2d List
        # notice that if an entry is left empty the value will be taken as 0
        matrix = [[0 if entry.get() == '' else float(entry.get()) for entry in row] for row in entries]
        return matrix

    def show_result(self, operation, matrix1, matrix2, power=None):
        # clear previous screen
        self.clearScreen()
        # a label to show the title of the current screen
        resultLabel = tk.Label(self.contentframe, text="RESULT:", font=30)
        resultLabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        # a variable the will store the result calculated
        result = None
        # a string that will store the name of the result eg: det(A)
        resultName = ""
        # a match-case statement that will call the appropriate operation function
        match operation:
            case Operations.multiplication:
                # calling the multiply function from our Calculator back-end class code
                result = Calculator.multiply(matrix1, matrix2)
                # setting the appropriate result label (multiplication)
                resultName = "A x B"
            case Operations.subtraction:
                result = Calculator.subtract(matrix1, matrix2)
                resultName = "A - B"
            case Operations.determinant:
                result = Calculator.calculate_determinant(matrix1)
                resultName = "det(A)"
            case Operations.power:
                result = Calculator.power(matrix1, power)
                resultName = "pow(A," + str(power) + ")"
            case Operations.transpose:
                result = Calculator.transpose(matrix1)
                resultName = "transpose(A)"
            case Operations.eigenvalue:
                result = Calculator.eigenvalues_m(matrix1)
                resultName = "eigenvalues(A)"
            case _:
                result = None
        # show the result matrix on the screen by calling the create_result_matrix() method
        self.create_result_matrix(result, resultName)

    # a method that creates a matrix gui from the 2d list result and show it on the screen
    def create_result_matrix(self, matrix, name):
        # a frame that will hold the GUI of the result matrix and put it on the center of the screen
        resultFrame = tk.Frame(self.contentframe)
        resultFrame.place(anchor=tk.CENTER, relx=0.45, rely=0.5)
        # a label to show the name of the result
        namelabel = tk.Label(resultFrame, text=name + " = ", font=("Arial", 15))
        namelabel.pack(side=tk.LEFT)
        matrixFrame = tk.Frame(resultFrame, bg="black")
        matrixFrame.pack(side=tk.LEFT)
        # if the result is not a list (eg: a number for determinant) then set row and column of result matrix to 1
        if not isinstance(matrix, list):
            r = c = 1
            # create a 2d list with only it list[0][0] value set the result
            # for the case of operations that only result in a number (eg: determinant)
            result = [[matrix]]
        else:
            r = len(matrix)
            c = len(matrix[0])
            result = matrix
        # create a matrix of result entries
        for row in range(r):
            for col in range(c):
                # a frame to hold the current result cell
                cellframe = tk.Frame(matrixFrame, bg="white", width=40, height=40)
                cellframe.grid(row=row, column=col, padx=0.5, pady=0.5)
                # a label that will show the result value for the current position
                entry = tk.Label(cellframe, text=str(result[row][col]), width=40, height=40, justify="center")
                entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    app = CalcApp()
    app.run()
