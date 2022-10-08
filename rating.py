import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

# GLOBALS
# Global lists
review_items = ["Food Score", "Wine Score", "Atmosphere Score"]
restaurant_items = ["Romantika", "El Mundo", "Pony", "Curry House", "Camellia"]

# Create empty lists to store ratings
scores_list = []
food_score_list = []
wine_score_list = []
atmosphere_score_list = []

# Set default on_click value to None
on_click = None
file = "ratings.txt"

# ----------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------Methods/Functions--------------------------------------------------------#


# Method to set rating for each aspect
def SetRating():
    global scores_list

    if len(scores_list) == 1 and scores_list[0] == "NA":
        stringOutputRating = display_selected("") + ", Food:" + "NA"
        addNewScore(stringOutputRating)
        read_score_data()
    elif len(scores_list) == 1:
        stringOutputRating = display_selected("") + ", Food:" + str(scores_list[0])
        addNewScore(stringOutputRating)
    elif len(scores_list) == 2:
        stringOutputRating = display_selected("") + ", Wine:" + str(scores_list[1])
        addNewScore(stringOutputRating)
    elif len(scores_list) == 2 and scores_list[1] == "NA":
        stringOutputRating = display_selected("") + ", Wine:" + "NA"
        addNewScore(stringOutputRating)
    elif len(scores_list) == 3:
        stringOutputRating = display_selected("") + ", Atmosphere:" + str(scores_list[2])
        addNewScore(stringOutputRating)
    elif len(scores_list) == 3 and scores_list[2] == "NA":
        stringOutputRating = display_selected("") + ", Atmosphere:" + "NA"
        addNewScore(stringOutputRating)
    elif len(scores_list) > 3:
        scores_list = []
        foodFrame()
    else:
        print("Missing rating for aspect. Reset scores")


# Method to read the ratings file and create a list of each line elements
def read_score_data():
    file_name = os.path.abspath(file)

    # Check if file path exists & handle errors
    if os.path.exists(file_name):

        ratings_list = []
        ratings_list_format = []
        # Loop each line in ratings.txt and append to a list
        with open(file_name, "r") as f:
            ratings_list = f.readlines()

            for element in ratings_list:
                ratings_list_format.append(element.strip())
            return ratings_list_format
    else:
        print("Error reading file path, check file is in the working directory")


#Method to calculate the average food score
def calculateFoodAvg():
    data_list = read_score_data()

    food_string = display_selected("") + ", Food:"
    food_avg = []

    for i in range(len(data_list)):
        if food_string in data_list[i]:
            food_avg.append(int(data_list[i][-1]))

        if len(food_avg) > 0:
            food_avg_output = sum(food_avg) / len(food_avg)
            food_avg_output_round = str(round(food_avg_output, 2))
            return food_avg_output_round


#Method to calculate the average wine score
def calculateWineAvg():
    data_list = read_score_data()

    wine_string = display_selected("") + ", Wine:"
    wine_avg = []
    for i in range(len(data_list)):
        if wine_string in data_list[i]:
            wine_avg.append(int(data_list[i][-1]))

    if len(wine_avg) > 0:
        wine_avg_output = sum(wine_avg) / len(wine_avg)
        wine_avg_output_round = str(round(wine_avg_output, 3))

        return wine_avg_output_round


#Method to calculate the average Atmosphere score
def calculateAtmoAvg():
    data_list = read_score_data()

    atmo_string = display_selected("") + ", Atmosphere:"
    atmo_avg = []

    for i in range(len(data_list)):
        if atmo_string in data_list[i]:
            atmo_avg.append(int(data_list[i][-1]))

    if len(atmo_avg) > 0:
        atmo_avg_output = sum(atmo_avg) / len(atmo_avg)
        atmo_avg_output_round = str(round(atmo_avg_output, 2))

        return atmo_avg_output_round


#-------------------------------------------SCORE BUTTON FUNCTIONS-----------------------------------------------------#
#Methods to store and return an integer value for the scoring buttons and NA value
def setBtnNA_Val():
    global on_click
    on_click = "NA"
    scores_list.append(on_click)

#Conditional statements to switch to the next scoring panel/frame
    if len(scores_list) > 0:
        wineFrame()

        if len(scores_list) > 1:
            atmoFrame()

            if len(scores_list) == 3:
                popUp()

# Call the setRating() method to store the ratings
    SetRating()
    return scores_list


def setBtn1_Val():
    global on_click
    global scores_list
    on_click = 1
    scores_list.append(on_click)

    if len(scores_list) > 0:
        wineFrame()

        if len(scores_list) > 1:
            atmoFrame()

            if len(scores_list) == 3:
                popUp()

    SetRating()
    return scores_list


def setBtn2_Val():
    global on_click
    global scores_list
    on_click = 2
    scores_list.append(on_click)

    if len(scores_list) > 0:
        wineFrame()

        if len(scores_list) > 1:
            atmoFrame()

            if len(scores_list) == 3:
                popUp()

    SetRating()
    return scores_list


def setBtn3_Val():
    global on_click
    global scores_list
    on_click = 3
    scores_list.append(on_click)

    if len(scores_list) > 0:
        wineFrame()

        if len(scores_list) > 1:
            atmoFrame()

            if len(scores_list) == 3:
                popUp()

    SetRating()
    return scores_list


def setBtn4_Val():
    global on_click
    global scores_list
    on_click = 4
    scores_list.append(on_click)

    if len(scores_list) > 0:
        wineFrame()

        if len(scores_list) > 1:
            atmoFrame()

            if len(scores_list) == 3:
                popUp()

    SetRating()
    return scores_list


def setBtn5_Val():
    global on_click
    global scores_list
    on_click = 5
    scores_list.append(on_click)

    if len(scores_list) > 0:
        wineFrame()

        if len(scores_list) > 1:
            atmoFrame()

            if len(scores_list) == 3:
                popUp()

    SetRating()
    return scores_list
#-------------------------------------------END SCORE BUTTON FUNCTIONS-------------------------------------------------#


# Method to add new score to text file - Pass as a string
def addNewScore(score_string):
    text_file = open("ratings.txt", "a")
    text_file.write(score_string + "\n")
    text_file.close()


# Method to discplay which restaurant has been selected from the drop-down and change label text
def display_selected(choice):
    selected_rest = rest_clicked.get()
    header_label1.config(text="RESTAURANT: " + selected_rest)
    return selected_rest


# Methods to run the calculation method and set values
def setAvgFoodValues():
    setFoodVal = calculateFoodAvg()
    avgScoreLabel.config(text="AVG SCORE: " + str(setFoodVal))
    return setFoodVal


def setAvgWineValues():
    setWineVal = calculateWineAvg()
    avgScoreLabel.config(text="AVG SCORE: " + str(setWineVal))
    return setWineVal


def setAvgAtmoValues():
    setAtmoVal = calculateAtmoAvg()
    avgScoreLabel.config(text="AVG SCORE: " + str(setAtmoVal))
    return setAtmoVal


# Method to reset the current ratings
def resetAction():
    global scores_list
    line_count = len(scores_list)

    with open("ratings.txt", "r") as file:
        lines = file.readlines()

    with open("ratings.txt", "w") as file_new:
        file_new.writelines(lines[:-line_count])

    scores_list = []
    foodFrame()


#Method to display pop up at end of ratings selections
def popUp():
    global popWindow
    popWindow = Toplevel(mainframe)
    popWindow.title("Confirm Ratings")
    popWindow.geometry("300x120")

    pop_label = Label(popWindow, text="Thank you for your ratings! \nDo you want to submit your scores or start again?")
    pop_label.pack(pady=10)

    popUp_frame = Frame(popWindow)
    popUp_frame.pack(pady=5)

    SubmitBtnPopUp = Button(popUp_frame, text="Submit", command=lambda: foodFrame())
    SubmitBtnPopUp.grid(column=2, row=3, padx=10, pady=10)
    ResetBtnPopUp = Button(popUp_frame, text="Reset", command=lambda: resetAction())
    ResetBtnPopUp.grid(column=3, row=3, padx=10, pady=10)

# ---------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------GUI Set-up----------------------------------------------------------#
root = Tk()
root.title("ReviewMe - The Restaurant Review App!")

style = Style()

# Creating a photo image object to use image
photo1 = PhotoImage(file=r"resources\1.png").subsample(4, 4)
photo2 = PhotoImage(file=r"resources\2.png").subsample(4, 4)
photo3 = PhotoImage(file=r"resources\3.png").subsample(4, 4)
photo4 = PhotoImage(file=r"resources\4.png").subsample(4, 4)
photo5 = PhotoImage(file=r"resources\5.png").subsample(4, 4)
photoNA = PhotoImage(file=r"resources\NA.png").subsample(4, 4)
photoStart = PhotoImage(file=r"resources\start.png").subsample(1, 1)
photoBack = PhotoImage(file=r"resources\back.png").subsample(6, 6)
photoReset = PhotoImage(file=r"resources\reset.png").subsample(6, 6)
photoSubmit = PhotoImage(file=r"resources\submit.png").subsample(6, 6)

# Main window setup
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
root.geometry("980x550")

mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)


# Method to change scores to food aspect
def foodFrame():
    food_frame = tkinter.Frame(mainframe, height=100, bg='green')
    food_frame.grid(row=4, column=1, columnspan=8, sticky=EW, padx=10, pady=10)
    header_label2.config(text="ASPECT: Food")

    # Rating Buttons
    btn_NA = ttk.Button(food_frame, image=photoNA, command=setBtnNA_Val)
    btn_NA.grid(column=1, row=4, padx=10, pady=10)

    btn_1 = ttk.Button(food_frame, image=photo1, command=setBtn1_Val)
    btn_1.grid(column=2, row=4, padx=10, pady=10)

    btn_2 = ttk.Button(food_frame, image=photo2, command=setBtn2_Val)
    btn_2.grid(column=3, row=4, padx=10, pady=10)

    btn_3 = ttk.Button(food_frame, image=photo3, command=setBtn3_Val)
    btn_3.grid(column=4, row=4, padx=10, pady=10)

    btn_4 = ttk.Button(food_frame, image=photo4, command=setBtn4_Val)
    btn_4.grid(column=5, row=4, padx=10, pady=10)

    btn_5 = ttk.Button(food_frame, image=photo5, command=setBtn5_Val)
    btn_5.grid(column=6, row=4, padx=10, pady=10)


# Method to change scores to wine aspect
def wineFrame():
    wine_frame = tkinter.Frame(mainframe, height=100, bg='red')
    wine_frame.grid(row=4, column=1, columnspan=8, sticky=EW, padx=10, pady=10)
    header_label2.config(text="ASPECT: Wine")
    calculateFoodAvg()
    setAvgWineValues()

    # Rating Buttons
    btn_NA = ttk.Button(wine_frame, image=photoNA, command=setBtnNA_Val)
    btn_NA.grid(column=1, row=4, padx=10, pady=10)

    btn_1 = ttk.Button(wine_frame, image=photo1, command=setBtn1_Val)
    btn_1.grid(column=2, row=4, padx=10, pady=10)

    btn_2 = ttk.Button(wine_frame, image=photo2, command=setBtn2_Val)
    btn_2.grid(column=3, row=4, padx=10, pady=10)

    btn_3 = ttk.Button(wine_frame, image=photo3, command=setBtn3_Val)
    btn_3.grid(column=4, row=4, padx=10, pady=10)

    btn_4 = ttk.Button(wine_frame, image=photo4, command=setBtn4_Val)
    btn_4.grid(column=5, row=4, padx=10, pady=10)

    btn_5 = ttk.Button(wine_frame, image=photo5, command=setBtn5_Val)
    btn_5.grid(column=6, row=4, padx=10, pady=10)


# Method to change scores to atmosphere aspect
def atmoFrame():
    atmo_frame = tkinter.Frame(mainframe, height=100, bg='blue')
    atmo_frame.grid(row=4, column=1, columnspan=8, sticky=EW, padx=10, pady=10)
    header_label2.config(text="ASPECT: Atmosphere")
    calculateFoodAvg()
    setAvgAtmoValues()

    # Rating Buttons
    btn_NA = ttk.Button(atmo_frame, image=photoNA, command=setBtnNA_Val)
    btn_NA.grid(column=1, row=4, padx=10, pady=10)

    btn_1 = ttk.Button(atmo_frame, image=photo1, command=setBtn1_Val)
    btn_1.grid(column=2, row=4, padx=10, pady=10)
    btn_1.setvar(value="1")

    btn_2 = ttk.Button(atmo_frame, image=photo2, command=setBtn2_Val)
    btn_2.grid(column=3, row=4, padx=10, pady=10)

    btn_3 = ttk.Button(atmo_frame, image=photo3, command=setBtn3_Val)
    btn_3.grid(column=4, row=4, padx=10, pady=10)

    btn_4 = ttk.Button(atmo_frame, image=photo4, command=setBtn4_Val)
    btn_4.grid(column=5, row=4, padx=10, pady=10)

    btn_5 = ttk.Button(atmo_frame, image=photo5, command=setBtn5_Val)
    btn_5.grid(column=6, row=4, padx=10, pady=10)


# Button Layouts
ttk.Button(mainframe, image=photoReset, command=resetAction).grid(column=1, columnspan=1, row=10, sticky=W)

# Text Layouts
header_label1 = ttk.Label(mainframe, text="RESTAURANT: Romantika")
header_label1.grid(column=1, columnspan=2, row=5, sticky=W,  pady=10)
header_label2 = ttk.Label(mainframe, text="ASPECT: ")
header_label2.grid(column=1, columnspan=1, row=6, sticky=EW, pady=10)

avgScoreLabel = ttk.Label(mainframe, text="AVG SCORE: ")
avgScoreLabel.grid(column=1, columnspan=1, row=9, pady=25, sticky=EW)

# Rating general notes
note = ttk.Label(mainframe, text="*Rating is scored between 1 & 5. 5 being the highest rating for the item being rated,"
                                 " 1 being the lowest rating for the item being rated. Enter NA for not-assessed")
note.grid(column=1, columnspan=8, row=16, pady=45, sticky=EW)

# Drop-down restaurant list
rest_clicked = StringVar()
rest_clicked.set(restaurant_items[0])
rest_options_list = OptionMenu(mainframe, rest_clicked, *restaurant_items, command=display_selected)
rest_options_list.grid(column=1, row=1, sticky=W)

# Initialise food frame at start-up
foodFrame()

mainframe.pack()
root.mainloop()
