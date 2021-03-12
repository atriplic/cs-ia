import xlrd
import xlwt
from app import app
from flask import render_template, redirect, request
from xlutils.copy import copy

@app.route('/')
@app.route('/index')
def index():
    print('in Index')
    return render_template('landing.html')

@app.route('/first_login')
def first_login():
    print('in First Login')
    return render_template('first_login.html')

@app.route('/sign_up')
def sign_up():
    print('in Sign Up')
    return render_template('sign_up.html')

@app.route('/home_page')
def home_page():
    scores = []
    print('in Home Page')
    wb = xlrd.open_workbook("./points_table.xls")
    sheet = wb.sheet_by_index(0)
    scores.append(sheet.cell_value(1, 15))
    scores.append(sheet.cell_value(2, 15))
    scores.append(sheet.cell_value(3, 15))
    scores.append(sheet.cell_value(4, 15))
    print (scores)
    return render_template('home_page.html', scores=scores)

@app.route('/main_home_page')
def main_home_page():
    scores = []
    print('in Main Home Page')
    wb = xlrd.open_workbook("./points_table.xls")
    sheet = wb.sheet_by_index(0)
    scores.append(sheet.cell_value(1, 15))
    scores.append(sheet.cell_value(2, 15))
    scores.append(sheet.cell_value(3, 15))
    scores.append(sheet.cell_value(4, 15))
    print(scores)
    return render_template('main_home_page.html', scores=scores)

@app.route('/login')
def login():
    print('in Login')
    return render_template('login.html')

@app.route('/update_scores')
def test_update():
    print('in Test Update')
    return render_template('update_scores.html')

@app.route('/update_scores', methods=['GET', 'POST'])
def update_scores():
    print("In Update Scores")
    blue_basketball  = request.form['blue_basketball']
    blue_football = request.form['blue_football']
    blue_swimming = request.form['blue_swimming']
    blue_tennis = request.form['blue_tennis']
    red_basketball = request.form['red_basketball']
    red_football = request.form['red_football']
    red_swimming = request.form['red_swimming']
    red_tennis = request.form['red_tennis']
    green_basketball = request.form['green_basketball']
    green_football = request.form['green_football']
    green_swimming = request.form['green_swimming']
    green_tennis = request.form['green_tennis']
    yellow_basketball = request.form['yellow_basketball']
    yellow_football = request.form['yellow_football']
    yellow_swimming = request.form['yellow_swimming']
    yellow_tennis = request.form['yellow_tennis']
    print("The Blue House Basketball Score is", blue_basketball)
    print("The Blue House Football Score is", blue_football)
    print("The Blue House Swimming Score is", blue_swimming)
    print("The Blue House Tennis Score is", blue_tennis)
    print("The Red House Basketball Score is", red_basketball)
    print("The Red House Football Score is", red_football)
    print("The Red House Swimming Score is", red_swimming)
    print("The Red House Tennis Score is", red_tennis)
    print("The Green House Basketball Score is", green_basketball)
    print("The Green House Football Score is", green_football)
    print("The Green House Swimming Score is", green_swimming)
    print("The Green House Tennis Score is", green_tennis)
    print("The Yellow House Basketball Score is", yellow_basketball)
    print("The Yellow House Football Score is", yellow_football)
    print("The Yellow House Swimming Score is", yellow_swimming)
    print("The Yellow House Tennis Score is", yellow_tennis)
    wb = xlrd.open_workbook("./points_table.xls")
    read_sheet = wb.sheet_by_index(0)
    write_wb = copy(wb)
    write_sheet = write_wb.get_sheet(0)
    cur_blue_basketball = read_sheet.cell_value(1, 3)
    cur_blue_football = read_sheet.cell_value(1, 4)
    cur_blue_swimming = read_sheet.cell_value(1, 14)
    cur_blue_tennis = read_sheet.cell_value(1, 13)
    cur_red_basketball = read_sheet.cell_value(2, 3)
    cur_red_football = read_sheet.cell_value(2, 4)
    cur_red_swimming = read_sheet.cell_value(2, 14)
    cur_red_tennis = read_sheet.cell_value(2, 13)
    cur_green_basketball = read_sheet.cell_value(3, 3)
    cur_green_football = read_sheet.cell_value(3, 4)
    cur_green_swimming = read_sheet.cell_value(3, 14)
    cur_green_tennis = read_sheet.cell_value(3, 13)
    cur_yellow_basketball = read_sheet.cell_value(4, 3)
    cur_yellow_football = read_sheet.cell_value(4, 4)
    cur_yellow_swimming = read_sheet.cell_value(4, 14)
    cur_yellow_tennis = read_sheet.cell_value(4, 13)


    print("Current Blue Basketball", cur_blue_basketball)
    print("Blue basketball from form", blue_basketball)
    new_blue_basketball = int(blue_basketball) + int(cur_blue_basketball)
    new_blue_football = int(blue_football) + int(cur_blue_football)
    new_blue_swimming = int(blue_swimming) + int(cur_blue_swimming)
    new_blue_tennis = int(blue_tennis) + int(cur_blue_tennis)
    new_red_basketball = int(red_basketball) + int(cur_red_basketball)
    new_red_football = int(red_football) + int(cur_red_football)
    new_red_swimming = int(red_swimming) + int(cur_red_swimming)
    new_red_tennis = int(red_tennis) + int(cur_red_tennis)
    new_green_basketball = int(green_basketball) + int(cur_green_basketball)
    new_green_football = int(green_football) + int(cur_green_football)
    new_green_swimming = int(green_swimming) + int(cur_green_swimming)
    new_green_tennis = int(green_tennis) + int(cur_green_tennis)
    new_yellow_basketball = int(yellow_basketball) + int(cur_yellow_basketball)
    new_yellow_football = int(yellow_football) + int(cur_yellow_football)
    new_yellow_swimming = int(yellow_swimming) + int(cur_yellow_swimming)
    new_yellow_tennis = int(yellow_tennis) + int(cur_yellow_tennis)


    print("Blue Basketball + current blue bball", new_blue_basketball)
    write_sheet.write(1, 3, blue_basketball)
    write_sheet.write(1, 4, blue_football)
    write_sheet.write(1, 14, blue_swimming)
    write_sheet.write(1, 13, blue_tennis)
    write_sheet.write(2, 3, red_basketball)
    write_sheet.write(2, 4, red_football)
    write_sheet.write(2, 14, red_swimming)
    write_sheet.write(2, 13, red_tennis)
    write_sheet.write(3, 3, green_basketball)
    write_sheet.write(3, 4, green_football)
    write_sheet.write(3, 14, green_swimming)
    write_sheet.write(3, 13, green_tennis)
    write_sheet.write(4, 3, yellow_basketball)
    write_sheet.write(4, 4, yellow_football)
    write_sheet.write(4, 14, yellow_swimming)
    write_sheet.write(4, 13, yellow_tennis)
    blue_total = int(new_blue_basketball) + int(new_blue_football) + int(new_blue_swimming) + int(new_blue_tennis)
    red_total = int(new_red_basketball) + int(new_red_football) + int(new_red_swimming) + int(new_red_tennis)
    green_total = int(new_green_basketball) + int(new_green_football) + int(new_green_swimming) + int(new_green_tennis)
    yellow_total = int(new_yellow_basketball) + int(new_yellow_football) + int(new_yellow_swimming) + int(new_yellow_tennis)
    print('Blue total is', blue_total)
    print('Red total is', red_total)
    print('Green total is', green_total)
    print('Yellow total is', yellow_total)
    write_sheet.write(1, 15, (blue_total))
    write_sheet.write(2, 15, (red_total))
    write_sheet.write(3, 15, (green_total))
    write_sheet.write(4, 15, (yellow_total))
    write_wb.save('./points_table.xls')
    read_sheet = wb.sheet_by_index(0)
    print('Totals')
    print(read_sheet.cell_value(1, 15))
    print(read_sheet.cell_value(2, 15))
    print(read_sheet.cell_value(3, 15))
    print(read_sheet.cell_value(4, 15))
    return redirect('main_home_page')
