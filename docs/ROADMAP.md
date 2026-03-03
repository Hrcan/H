# 🎯 EXCEL VERİ GÖRÜNTÜLEYİCİ - YOL HARİTASI

**Proje Adı:** Excel Veri Görüntüleme Uygulaması  
**Teknoloji:** Python 3.x + PyQt5  
**Hedef:** Masaüstü uygulama (Windows EXE)  
**Başlangıç:** 2026-03-03  

---

## 📊 PROJE GEREKSİNİMLERİ

### Veri Kaynakları
- **Excel Dosyaları:**
  - Hatalı Biten İşler Raporu (Aylık)
  - Uzun Süren İşler Raporu (Aylık)
  
- **TXT Dosyaları:** (İleride eklenecek)
  - AYLIK_HATALI_CALISAN_PROD.TXT
  - AYLIK_UZUN_CALISAN_TUM_GUN.TXT
  - AYLIK_UZUN_CALISAN_GUNICI.TXT

### Veri Yapısı

#### Hatalı İşler Excel (A-E Kolonları):
- **A1:** JCL Adı (Benzersiz Anahtar)
- **B1:** Hatalı Çalışma Sayısı (Aylık)
- **C1:** Son Hatalı Çalışma Tarihi
- **D1:** Hatalı Çalışma Sayısı (Yıllık Toplam)
- **E1:** Sorumlu Ekip (Ekip Adı)

**Sheet'ler:**
- "Hatalı Isler Yazılım PROD"
- "Hatalı Isler AYDB PROD"

#### Uzun İşler Excel (A-D Kolonları):
- **A1:** JCL Adı (Benzersiz Anahtar)
- **B1:** Çalışma Sayısı (Adet)
- **C1:** Çalışma Süresi (Dakika)
- **D1:** Sorumlu Ekip (Ekip Adı)

**Sheet'ler:**
- "Mesai Saatleri"
- "Tüm Gün Yazılım"
- "Tüm Gün AnaSistemler"

---

## 🗺️ GELİŞTİRME FAZLARI

### FAZE 1: ALTYAPI VE TEMEL YAPI ⏳
**Süre:** 1-2 gün  
**Öncelik:** Yüksek

- [ ] **1.1** Proje klasör yapısı oluşturma
  - [ ] docs/, src/, data/, backups/, dist/, assets/, tests/
  - [ ] src/ui/, src/core/, src/utils/ alt klasörleri
  
- [ ] **1.2** Python bağımlılıklarını belirleme
  - [ ] requirements.txt oluşturma
  - [ ] PyQt5, pandas, openpyxl kurulumu
  
- [ ] **1.3** Git repository oluşturma
  - [ ] .gitignore dosyası
  - [ ] İlk commit
  
- [ ] **1.4** Backup mekanizması temeli
  - [ ] src/utils/backup_manager.py
  - [ ] Otomatik backup fonksiyonları

---

### FAZE 2: VERİ OKUMA MODÜLLERİ ⏳
**Süre:** 2-3 gün  
**Öncelik:** Yüksek

- [ ] **2.1** Excel Okuma Modülü
  - [ ] src/core/excel_reader.py
  - [ ] Multi-sheet okuma fonksiyonu
  - [ ] Hatalı İşler okuma (A-E kolonları)
  - [ ] Uzun İşler okuma (A-D kolonları)
  - [ ] Hata yönetimi (dosya bulunamadı, yanlış format vb.)
  
- [ ] **2.2** Veri Modeli Oluşturma
  - [ ] src/core/data_manager.py
  - [ ] JCL sınıfı (benzersiz anahtar)
  - [ ] HataliIsler sınıfı
  - [ ] UzunIsler sınıfı
  - [ ] Veri birleştirme mantığı
  
- [ ] **2.3** Veri Önbellekleme (Cache)
  - [ ] Okunan verileri bellekte tutma
  - [ ] Hızlı erişim için indexleme
  - [ ] JCL adına göre arama optimizasyonu

---

### FAZE 3: ANA PENCERE VE MENÜ SİSTEMİ ⏳
**Süre:** 2 gün  
**Öncelik:** Yüksek

- [ ] **3.1** Ana Pencere Tasarımı
  - [ ] src/ui/main_window.py
  - [ ] PyQt5 QMainWindow oluşturma
  - [ ] Pencere boyutu ve konum ayarları
  - [ ] Uygulama ikonu ekleme
  
- [ ] **3.2** Menü Sistemi
  - [ ] Dosya Menüsü
    - [ ] Excel Yükle
    - [ ] TXT Yükle (ileride)
    - [ ] Çıkış
  - [ ] Görünüm Menüsü
    - [ ] Ana Arama
    - [ ] Hatalı İşler
    - [ ] Uzun İşler
  - [ ] Yardım Menüsü
    - [ ] Hakkında
    - [ ] Kullanım Kılavuzu
  
- [ ] **3.3** Sayfa Geçiş Mekanizması
  - [ ] QStackedWidget kullanımı
  - [ ] Sayfalar arası geçiş fonksiyonları

---

### FAZE 4: ANA ARAMA SAYFASI ⏳
**Süre:** 3-4 gün  
**Öncelik:** Yüksek

- [ ] **4.1** Arayüz Tasarımı
  - [ ] src/ui/search_page.py
  - [ ] JCL Adı TextBox (arama kutusu)
  - [ ] Ekip Adı ComboBox (filtreleme)
  - [ ] Ay/Yıl Seçici (CheckBox'lar)
  - [ ] Ara butonu
  
- [ ] **4.2** Sonuç Tablosu
  - [ ] QTableWidget oluşturma
  - [ ] Kolonlar: JCL Adı, Excel Adı, Ay, Yıl, Ekip
  - [ ] Çift tıklama ile detay sayfasına gitme
  
- [ ] **4.3** Filtreleme Mantığı
  - [ ] src/core/filter_manager.py
  - [ ] JCL adına göre arama (case-insensitive)
  - [ ] Ekip adına göre filtreleme
  - [ ] Tarih/ay aralığına göre filtreleme
  - [ ] Birden fazla ay seçimi desteği
  
- [ ] **4.4** Varsayılan Davranış
  - [ ] Uygulama açılınca en son ay verisi gösterme
  - [ ] Tüm ekipleri ComboBox'a doldurma
  - [ ] "Veri bulunamadı" mesajı gösterme

---

### FAZE 5: HATALI İŞLER DETAY SAYFASI ⏳
**Süre:** 2-3 gün  
**Öncelik:** Orta

- [ ] **5.1** Sayfa Tasarımı
  - [ ] src/ui/hatali_isler_page.py
  - [ ] Detaylı tablo görünümü
  - [ ] Başlık: "Hatalı İşler Detayı"
  
- [ ] **5.2** Tablo Kolonları
  - [ ] JCL Adı
  - [ ] Hatalı Çalışma Sayısı (Aylık)
  - [ ] Son Hatalı Çalışma Tarihi
  - [ ] Hatalı Çalışma Sayısı (Yıllık)
  - [ ] Ekip Adı
  - [ ] Ay/Yıl Bilgisi
  
- [ ] **5.3** Özel Özellikler
  - [ ] Satır renklendirme (yüksek hata sayısı için kırmızı)
  - [ ] Sıralama (her kolona tıklayarak)
  - [ ] Excel'e export butonu
  
- [ ] **5.4** Veri Yoksa Mesajı
  - [ ] "Bu JCL için hatalı iş verisi bulunamadı"
  - [ ] Geri dön butonu

---

### FAZE 6: UZUN İŞLER DETAY SAYFASI ⏳
**Süre:** 2-3 gün  
**Öncelik:** Orta

- [ ] **6.1** Sayfa Tasarımı
  - [ ] src/ui/uzun_isler_page.py
  - [ ] Detaylı tablo görünümü
  - [ ] Başlık: "Uzun İşler Detayı"
  
- [ ] **6.2** Tablo Kolonları
  - [ ] JCL Adı
  - [ ] Çalışma Sayısı (Adet)
  - [ ] Çalışma Süresi (Dakika)
  - [ ] Ekip Adı
  - [ ] Sheet Adı
  - [ ] Ay/Yıl Bilgisi
  
- [ ] **6.3** Özel Özellikler
  - [ ] Satır renklendirme (uzun süre için turuncu)
  - [ ] Sıralama özelliği
  - [ ] Excel'e export butonu
  
- [ ] **6.4** Veri Yoksa Mesajı
  - [ ] "Bu JCL için uzun iş verisi bulunamadı"
  - [ ] Geri dön butonu

---

### FAZE 7: TARİH/AY FİLTRELEME SİSTEMİ ⏳
**Süre:** 2-3 gün  
**Öncelik:** Yüksek

- [ ] **7.1** Ay Seçici Arayüzü
  - [ ] 12 aylık CheckBox grid'i
  - [ ] "Tümünü Seç" / "Hiçbirini Seçme" butonları
  - [ ] Yıl seçici ComboBox
  
- [ ] **7.2** Filtreleme Mantığı
  - [ ] Seçili aylar için veri getirme
  - [ ] Veri yoksa "Veri bulunamadı" gösterme
  - [ ] Her ay için ekip değişikliğini takip etme
  
- [ ] **7.3** Varsayılan Davranış
  - [ ] Uygulama açılınca sadece son ay seçili
  - [ ] Kullanıcı filtreleme yaptıkça güncelleme

---

### FAZE 8: DETAY GÖRÜNÜMÜ (YAN YANA) ⏳
**Süre:** 2 gün  
**Öncelik:** Orta

- [ ] **8.1** Kombine Detay Sayfası
  - [ ] Hem Hatalı hem Uzun İşler yan yana
  - [ ] Sol taraf: Hatalı İşler
  - [ ] Sağ taraf: Uzun İşler
  
- [ ] **8.2** Veri Yoksa Durumu
  - [ ] Sol tarafta veri yoksa: "Hatalı iş verisi yok"
  - [ ] Sağ tarafta veri yoksa: "Uzun iş verisi yok"
  - [ ] Her iki taraf bağımsız çalışır

---

### FAZE 9: TXT DOSYASI OKUMA (İLERİDE) 📅
**Süre:** 3-4 gün  
**Öncelik:** Düşük

- [ ] **9.1** TXT Okuma Modülü
  - [ ] src/core/txt_reader.py
  - [ ] Pipe-separated (|) format okuma
  - [ ] Başlık satırı algılama
  
- [ ] **9.2** Ekip Adı Girişi Arayüzü
  - [ ] TXT'den okunan JCL'ler için ekip atama
  - [ ] Toplu düzenleme özelliği
  - [ ] ComboBox ile ekip seçimi
  
- [ ] **9.3** Veri Kaydetme
  - [ ] Güncellenmiş verileri yeni Excel'e yazma
  - [ ] Veya SQLite veritabanına kaydetme

---

### FAZE 10: TEST VE OPTİMİZASYON ⏳
**Süre:** 2-3 gün  
**Öncelik:** Yüksek

- [ ] **10.1** Birim Testleri
  - [ ] tests/test_excel_reader.py
  - [ ] tests/test_data_manager.py
  - [ ] tests/test_filter_manager.py
  
- [ ] **10.2** Performans Optimizasyonu
  - [ ] Büyük Excel dosyaları için hız testi
  - [ ] Bellek kullanımı optimizasyonu
  - [ ] Lazy loading (gerektiğinde yükleme)
  
- [ ] **10.3** Hata Yönetimi
  - [ ] Try-except blokları
  - [ ] Kullanıcı dostu hata mesajları
  - [ ] Log sistemi

---

### FAZE 11: EXE DERLEME VE DAĞITIM 🎯
**Süre:** 1-2 gün  
**Öncelik:** Yüksek

- [ ] **11.1** PyInstaller Konfigürasyonu
  - [ ] build.spec dosyası oluşturma
  - [ ] İkon ekleme
  - [ ] Bağımlılıkları dahil etme
  
- [ ] **11.2** EXE Oluşturma
  - [ ] `pyinstaller --onefile --windowed` komutu
  - [ ] data/ klasörü ile paketleme
  - [ ] dist/ klasörüne çıktı alma
  
- [ ] **11.3** Test
  - [ ] Farklı Windows PC'lerde test
  - [ ] Python yüklü olmayan sistemde test
  - [ ] Taşınabilirlik kontrolü
  
- [ ] **11.4** Dağıtım Paketi
  - [ ] README.txt (kullanım talimatları)
  - [ ] data/excel/ ve data/txt/ klasörleri
  - [ ] ExcelDataViewer.exe

---

## 📦 BAĞIMLILIKLAR

```
PyQt5==5.15.10
pandas==2.3.1
openpyxl==3.1.2
pyinstaller==6.3.0
```

---

## 🎨 TASARIM PRENSİPLERİ

1. **Kullanıcı Dostu:** Sade ve anlaşılır arayüz
2. **Hızlı:** Önbellekleme ile hızlı erişim
3. **Güvenli:** Otomatik backup sistemi
4. **Taşınabilir:** Tek EXE dosyası
5. **Ölçeklenebilir:** İleride yeni özellikler eklenebilir

---

## 📝 NOTLAR

- Her faz tamamlandıkça PROGRESS.md güncellenecek
- Her büyük değişiklik öncesi backup alınacak
- Kod kalitesi için PEP 8 standartları uygulanacak
- Git commit'leri düzenli ve açıklayıcı olacak

---

**Son Güncelleme:** 2026-03-03  
**Durum:** Planlama Tamamlandı ✅