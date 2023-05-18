import openpyxl, os, librosa
import numpy as np
DELTA_T = 0.05

# record_time = (datetime.now().strftime('%H:%M:%S.%f'))[:-3]

wb = openpyxl.load_workbook('data_automation\data.xlsx')
ex = wb[r'분석 데이터']

sounds = os.listdir('data_automation\sound_files')

for file in sounds:
    for ro in range(2, 50):

        if ex.cell(row=ro, column=3).value != None:
            continue

        else:
            file_path = 'data_automation\sound_files\\' + file
            y, sr = librosa.load(file_path, sr=44100)  
            inst_time = ex.cell(row=ro, column=1).value
            
            fund_amp = 
            fund_freq

            
            # ex.cell(row=ro, column=2).value = str(sr) --> parameter of image
            ex.cell(row=ro, column=3).value = str(amp)
            ex.cell(row=ro, column=4).value = fre_str
            break

wb.save('data_automation\saved.xlsx')