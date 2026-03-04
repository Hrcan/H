# 🔨 EXE DERLEME TALİMATLARI

## Hızlı Başlangıç

```bash
# 1. EXE Derle (tek komut)
pyinstaller build.spec

# 2. Çıktı:
# dist/ExcelViewer.exe
```

## Detaylı Adımlar

### 1️⃣ Gereksinimler Kontrolü
```bash
pip list | findstr pyinstaller
# pyinstaller 6.15.0 olmalı
```

### 2️⃣ Temizlik (İsteğe Bağlı)
```bash
rmdir /s /q build dist
del /q *.spec
```

### 3️⃣ EXE Oluşturma
```bash
pyinstaller build.spec
```

**Süre:** ~2-3 dakika  
**Boyut:** ~150-200 MB (tüm bağımlılıklar dahil)

### 4️⃣ Test
```bash
cd dist
ExcelViewer.exe
```

## 📦 Dağıtım Paketi Oluşturma

### Manuel Paketleme:
```
ExcelViewer_v2.2.0/
├── ExcelViewer.exe          ← Ana program
├── data/
│   ├── excel/               ← Excel dosyaları buraya
│   │   ├── SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx
│   │   └── SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx
│   └── txt/                 ← TXT dosyaları (ileride)
├── logs/                    ← Otomatik oluşur
├── README.txt              ← Kullanım talimatları
└── CHANGELOG.txt           ← Sürüm notları
```

### Otomatik Paketleme:
```bash
# dist/ içeriğini kopyala
xcopy /E /I dist ExcelViewer_v2.2.0
# Excel dosyalarını ekle
xcopy /E /I data\excel ExcelViewer_v2.2.0\data\excel
# Dokümantasyon ekle
copy README.md ExcelViewer_v2.2.0\README.txt
copy docs\CHANGELOG.md ExcelViewer_v2.2.0\CHANGELOG.txt
```

## 🔧 Sorun Giderme

### Hata: "Failed to execute script"
```bash
# Konsol modunda çalıştır (hataları görmek için)
pyinstaller --onefile --console main.py
```

### Hata: "Module not found"
```bash
# build.spec'e hiddenimports ekle
hiddenimports=[
    'PyQt5.QtCore',
    'pandas',
    'openpyxl',
]
```

### Hata: "Data files not found"
```bash
# build.spec'de datas kontrolü
datas=[
    ('data', 'data'),
    ('src', 'src'),
],
```

## 📊 EXE Özellikleri

- **Tip:** Windows GUI Application
- **Konsol:** Kapalı (daha temiz görünüm)
- **UPX:** Aktif (dosya sıkıştırma)
- **Bağımlılıklar:** Dahil (PyQt5, pandas, openpyxl, colorama)
- **Taşınabilirlik:** %100 (Python gerektirmez)

## ✅ Test Checklist

- [ ] EXE çalışıyor
- [ ] Excel dosyaları yükleniyor (46+96=142 satır)
- [ ] Arama sayfası çalışıyor
- [ ] Hatalı İşler (Ctrl+1) çalışıyor
- [ ] Uzun İşler (Ctrl+2) çalışıyor
- [ ] Log sistemi (Ctrl+L) çalışıyor
- [ ] Filtreler çalışıyor
- [ ] Log dosyaları oluşuyor (logs/)

## 🚀 Dağıtım

1. **ZIP Paketi Oluştur:**
   ```bash
   powershell Compress-Archive -Path ExcelViewer_v2.2.0 -DestinationPath ExcelViewer_v2.2.0.zip
   ```

2. **Paylaş:**
   - Network drive'a kopyala
   - Email ile gönder
   - İç portal'a yükle

---

**Not:** İlk çalıştırmada Windows Defender uyarısı çıkabilir. "Daha fazla bilgi → Yine de çalıştır" seçin.