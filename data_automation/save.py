import openpyxl, os, librosa
import numpy as np
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook('data_automation\data.xlsx')
ex = wb[r'분석 데이터']

sounds = os.listdir('data_automation\sound_files')
#plot graph
y, sr = librosa.load('data_automation\sound_files\\' + sounds[0])
plt.plot(y)
plt.xlim(3000, 3200)
plt.show()

for file in sounds:
    for col in range(2, 50):

        if ex.cell(row=1, column=col).value != None:
            continue

        else:
            y, sr = librosa.load('data_automation\sound_files\\' + file, sr=44100)  
            yf = np.fft.fft(y)
            max_amp = np.max(yf)
            min_amp = np.min(yf)
            frequency = np.fft.fftfreq(yf.size, d=1/sr)
            wavelength = [1/f for f in frequency]
            fre_str = " ".join(str(f) for f in frequency)
            wav_str = " ".join(str(w) for w in wavelength)
            print(fre_str, wav_str)

            ex.cell(row=1, column=col).value = file
            ex.cell(row=2, column=col).value = max_amp
            ex.cell(row=3, column=col).value = min_amp
            ex.cell(row=4, column=col).value = wav_str
            ex.cell(row=5, column=col).value = fre_str
            break

wb.save('data_automation\data.xlsx')