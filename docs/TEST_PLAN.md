# 🧪 TEST PLANI

**Proje:** Excel Veri Görüntüleme Uygulaması  
**Versiyon:** 0.1.0  
**Test Başlangıcı:** 2026-03-03  
**Son Güncelleme:** 2026-03-03 16:22

---

## 📋 TEST STRATEJİSİ

### Test Seviyeleri
1. **Birim Testleri (Unit Tests)** - Her modül ayrı test edilir
2. **Entegrasyon Testleri** - Modüller arası etkileşim testi
3. **Sistem Testleri** - Tüm sistemin bütünsel testi
4. **Kullanıcı Kabul Testleri (UAT)** - Son kullanıcı senaryoları

### Test Ortamı
- **Python:** 3.13
- **İşletim Sistemi:** Windows 11
- **Test Framework:** pytest
- **Excel Dosyaları:** data/excel/ klasöründeki gerçek veriler

---

## 🎯 TEST FAZLARI

### FAZE 1: ALTYAPI TESTLERİ (v0.1) ✅

#### Test 1.1: Klasör Yapısı Kontrolü
**Amaç:** Tüm gerekli klasörlerin oluşturulduğunu doğrula

**Kontrol Listesi:**
- [ ] docs/ klasörü var mı?
- [ ] src/ui/ klasörü var mı?
- [ ] src/core/ klasörü var mı?
- [ ] src/utils/ klasörü var mı?
- [ ] data/excel/ klasörü var mı?
- [ ] data/txt/ klasörü var mı?
- [ ] backups/ klasörü var mı?
- [ ] dist/ klasörü var mı?
- [ ] assets/ klasörü var mı?
- [ ] tests/ klasörü var mı?

**Beklenen Sonuç:** Tüm klasörler mevcut olmalı

---

#### Test 1.2: Dokümantasyon Dosyaları Kontrolü
**Amaç:** Tüm dokümantasyon dosyalarının eksiksiz olduğunu doğrula

**Kontrol Listesi:**
- [ ] README.md var ve içerik dolu mu?
- [ ] docs/ROADMAP.md var ve 11 faz tanımlı mı?
- [ ] docs/PROGRESS.md var ve güncel mi?
- [ ] docs/CHANGELOG.md var ve v0.1.0 kaydı var mı?
- [ ] requirements.txt var ve bağımlılıklar listelendi mi?
- [ ] .gitignore var mı?

**Beklenen Sonuç:** Tüm dosyalar eksiksiz olmalı

---

#### Test 1.3: Backup Sistemi Kontrolü
**Amaç:** İlk backup'ın düzgün oluşturulduğunu doğrula

**Kontrol Listesi:**
- [ ] backups/backup_v0.1_2026-03-03_16-20/ var mı?
- [ ] BACKUP_NOTE.txt var ve detaylı mı?
- [ ] Backup notu v0.1 bilgilerini içeriyor mu?

**Beklenen Sonuç:** Backup klasörü ve notu eksiksiz olmalı

---

### FAZE 2: EXCEL OKUMA TESTLERİ (v0.2) 🔜

#### Test 2.1: Pandas Kurulum Testi
**Dosya:** `tests/test_dependencies.py`

```python
def test_pandas_import():
    """Pandas'ın doğru kurulduğunu test et"""
    import pandas as pd
    assert pd.__version__ >= "2.3.0"

def test_openpyxl_import():
    """Openpyxl'in doğru kurulduğunu test et"""
    import openpyxl
    assert openpyxl.__version__ >= "3.1.0"
```

**Çalıştırma:**
```bash
pytest tests/test_dependencies.py -v
```

**Beklenen Sonuç:** 2/2 test geçmeli

---

#### Test 2.2: Hatalı İşler Excel Okuma
**Dosya:** `tests/test_excel_reader.py`

```python
def test_read_hatali_isler_excel():
    """Hatalı İşler Excel dosyasını oku ve doğrula"""
    from src.core.excel_reader import ExcelReader
    
    reader = ExcelReader()
    data = reader.read_hatali_isler(
        "data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx"
    )
    
    # Testler
    assert data is not None
    assert len(data) > 0
    assert 'JCL_Adi' in data.columns
    assert 'Ekip_Adi' in data.columns
    
def test_hatali_isler_columns():
    """A-E kolonlarının doğru okunduğunu test et"""
    # A: JCL Adı
    # B: Hatalı Çalışma Sayısı (Aylık)
    # C: Son Hatalı Çalışma Tarihi  
    # D: Hatalı Çalışma Sayısı (Yıllık)
    # E: Sorumlu Ekip
    pass
```

**Beklenen Sonuç:** Tüm testler geçmeli, veri doğru şekilde okunmalı

---

#### Test 2.3: Uzun İşler Excel Okuma
**Dosya:** `tests/test_excel_reader.py`

```python
def test_read_uzun_isler_excel():
    """Uzun İşler Excel dosyasını oku ve doğrula"""
    from src.core.excel_reader import ExcelReader
    
    reader = ExcelReader()
    data = reader.read_uzun_isler(
        "data/excel/SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx"
    )
    
    # Testler
    assert data is not None
    assert len(data) > 0
    assert 'JCL_Adi' in data.columns
    assert 'Ekip_Adi' in data.columns

def test_uzun_isler_multi_sheet():
    """3 sheet'in de okunduğunu test et"""
    # Mesai Saatleri, Tüm Gün Yazılım, Tüm Gün AnaSistemler
    pass
```

**Beklenen Sonuç:** Tüm sheet'ler okunmalı, veriler birleştirilmeli

---

#### Test 2.4: Veri Modeli Testi
**Dosya:** `tests/test_data_manager.py`

```python
def test_jcl_unique_key():
    """JCL adının benzersiz anahtar olduğunu test et"""
    pass

def test_data_merge():
    """Farklı aylardaki verilerin birleştirilmesini test et"""
    pass

def test_ekip_change_tracking():
    """Ekip değişikliklerinin takip edildiğini test et"""
    pass
```

---

### FAZE 3: PYQT5 ARAYÜZ TESTLERİ (v0.3) 🔜

#### Test 3.1: Ana Pencere Testi
**Dosya:** `tests/test_main_window.py`

```python
def test_main_window_creation(qtbot):
    """Ana pencerenin oluşturulduğunu test et"""
    from src.ui.main_window import MainWindow
    
    window = MainWindow()
    qtbot.addWidget(window)
    
    assert window.isVisible()
    assert window.windowTitle() == "Excel Veri Görüntüleyici"

def test_menu_bar():
    """Menü çubuğunun doğru oluşturulduğunu test et"""
    pass
```

---

#### Test 3.2: Sayfa Geçişleri Testi
**Dosya:** `tests/test_navigation.py`

```python
def test_navigate_to_search():
    """Arama sayfasına geçişi test et"""
    pass

def test_navigate_to_hatali():
    """Hatalı işler sayfasına geçişi test et"""
    pass

def test_navigate_to_uzun():
    """Uzun işler sayfasına geçişi test et"""
    pass
```

---

### FAZE 4: ARAMA VE FİLTRELEME TESTLERİ (v0.4) 🔜

#### Test 4.1: JCL Arama Testi
**Dosya:** `tests/test_search.py`

```python
def test_search_by_jcl_name():
    """JCL adına göre arama"""
    pass

def test_search_case_insensitive():
    """Büyük/küçük harf duyarsız arama"""
    pass

def test_search_partial_match():
    """Kısmi eşleşme desteği"""
    pass
```

---

#### Test 4.2: Ekip Filtreleme Testi
**Dosya:** `tests/test_filtering.py`

```python
def test_filter_by_ekip():
    """Ekip adına göre filtreleme"""
    pass

def test_combobox_population():
    """ComboBox'ın ekiplerle doldurulması"""
    pass
```

---

#### Test 4.3: Tarih Filtreleme Testi
**Dosya:** `tests/test_date_filtering.py`

```python
def test_filter_single_month():
    """Tek ay seçimi"""
    pass

def test_filter_multiple_months():
    """Birden fazla ay seçimi"""
    pass

def test_filter_no_data_message():
    """Veri yoksa mesaj gösterimi"""
    pass

def test_ekip_change_across_months():
    """Aylar arası ekip değişikliği takibi"""
    pass
```

---

### FAZE 5-8: DETAY SAYFALAR TESTLERİ 🔜

#### Test 5.1: Hatalı İşler Detay Görünümü
- Tablo doğru oluşturuldu mu?
- Kolonlar eksiksiz mi?
- Sıralama çalışıyor mu?
- Veri yoksa mesaj gösteriliyor mu?

#### Test 6.1: Uzun İşler Detay Görünümü
- Tablo doğru oluşturuldu mu?
- Sheet bilgisi gösteriliyor mu?
- Renklendirme doğru mu?

#### Test 8.1: Yan Yana Görünüm
- Her iki tablo da görünüyor mu?
- Bağımsız çalışıyorlar mı?
- Veri yoksa mesajlar doğru mu?

---

### FAZE 10: PERFORMANS TESTLERİ 🔜

#### Test 10.1: Büyük Dosya Testi
```python
def test_large_excel_file():
    """10,000+ satırlık Excel'i oku"""
    import time
    start = time.time()
    # Excel oku
    duration = time.time() - start
    assert duration < 5  # 5 saniyeden kısa olmalı
```

#### Test 10.2: Bellek Kullanımı
```python
def test_memory_usage():
    """Bellek kullanımını ölç"""
    import psutil
    import os
    process = psutil.Process(os.getpid())
    # İşlemleri yap
    mem = process.memory_info().rss / 1024 / 1024  # MB
    assert mem < 500  # 500 MB'dan az olmalı
```

---

### FAZE 11: EXE DERLEME TESTLERİ 🔜

#### Test 11.1: EXE Oluşturma
**Komut:**
```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico src/main.py
```

**Kontrol:**
- [ ] dist/main.exe oluşturuldu mu?
- [ ] Boyut makul mü? (<100MB)
- [ ] Bağımlılıklar dahil mi?

#### Test 11.2: EXE Çalıştırma Testi
**Test Senaryosu:**
1. EXE'yi Python yüklü OLMAYAN bir PC'ye kopyala
2. data/ klasörünü kopyala
3. EXE'yi çalıştır
4. Excel dosyası yükle
5. Arama yap
6. Sonuçları görüntüle

**Beklenen:** Sorunsuz çalışmalı

---

## 📊 TEST KAPSAMI HEDEFLERİ

| Modül | Hedef Kapsam | Durum |
|-------|--------------|-------|
| excel_reader.py | %95 | 🔜 Bekliyor |
| data_manager.py | %90 | 🔜 Bekliyor |
| filter_manager.py | %90 | 🔜 Bekliyor |
| main_window.py | %80 | 🔜 Bekliyor |
| search_page.py | %85 | 🔜 Bekliyor |
| backup_manager.py | %100 | 🔜 Bekliyor |

**Genel Hedef:** %85+ test kapsamı

---

## 🐛 HATA RAPORLAMA

Her test hatası için şunları kaydet:
1. **Hata Açıklaması:** Ne oldu?
2. **Adımlar:** Hatayı tekrar üretme adımları
3. **Beklenen:** Ne olmalıydı?
4. **Gerçekleşen:** Ne oldu?
5. **Ekran Görüntüsü:** Varsa ekle
6. **Log:** Hata mesajları

---

## ✅ TEST ONAY LİSTESİ

### v0.1 Test Onayı (Altyapı)
- [x] Klasör yapısı tam
- [x] Dokümantasyon eksiksiz
- [x] Backup oluşturuldu
- [ ] Git repository başlatıldı

### v0.2 Test Onayı (Excel Okuma)
- [ ] Excel dosyaları okunuyor
- [ ] Kolonlar doğru eşleştiriliyor
- [ ] Multi-sheet okuma çalışıyor
- [ ] Hata yönetimi var

### v0.3 Test Onayı (Ana Pencere)
- [ ] PyQt5 çalışıyor
- [ ] Pencere açılıyor
- [ ] Menüler çalışıyor
- [ ] Sayfa geçişleri var

---

## 📝 TEST RAPORU ŞABLONU

```
═══════════════════════════════════════════
TEST RAPORU - vX.X
═══════════════════════════════════════════
Tarih: YYYY-MM-DD
Test Eden: [İsim]
Versiyon: X.X.X

ÖZET:
- Toplam Test: XX
- Başarılı: XX
- Başarısız: XX
- Atlanan: XX

DETAYLAR:
[Test detayları buraya]

SORUNLAR:
[Bulunan hatalar]

SONRAKİ ADIMLAR:
[Yapılacaklar]
═══════════════════════════════════════════
```

---

**Son Güncelleme:** 2026-03-03 16:22  
**Durum:** Test planı hazır, testlere başlanabilir  
**Sonraki:** Python bağımlılıkları yükle ve test yaz