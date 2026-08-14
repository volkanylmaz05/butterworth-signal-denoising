# Butterworth Low-Pass Filter Demo

## 🇹🇷 Amaç
Bu projenin amacı, yapay olarak üretilmiş bir sinüs sinyaline eklenen rastgele gürültüyü (noise), SciPy kütüphanesinin Butterworth alçak geçiren (low-pass) filtresi ile temizleyip orijinal sinyali geri kurtarmaktır.
NOT;

    line(15):  sos = signal.butter(4, 8, fs=fs, btype="low", output="sos");
    İlk İndex= Derece belirtir 
    İkinci İndex= 5*4.derece filtre için çarpan(1.6)alındı.  
    bytpe= Alçak&Yüksek kesim 

Filtre Derecesi  | Eğim Dikliği | Pratik Çarpan Aralığı | 

   1.Derece          Çok yatay          3.00-4.00    
   
   2.Derece          Yumuşak           2.00-2.50 
   
   4.Derece          Dengeli           1.70-1.90 
   
   6.Derece            Dik             1.25-1.35    
   
## 🇬🇧 Purpose
The purpose of this project is to filter out random noise from a synthetic 5 Hz sine wave using a zero-phase Butterworth low-pass filter in Python.

---

## 💻 Çalıştırma / Run

```bash
pip install numpy scipy matplotlib
python main.py
```
<img width="1200" height="800" alt="Figure_1" src="https://github.com/user-attachments/assets/37b13bfb-01b8-4f5f-bb2d-74455d637599" />

