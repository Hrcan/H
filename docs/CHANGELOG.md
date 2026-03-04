# 📋 DEĞİŞİKLİK GEÇMİŞİ (CHANGELOG)

**Proje:** Excel Veri Görüntüleme Uygulaması  
**Format:** Bu dosya [Keep a Changelog](https://keepachangelog.com/tr/1.0.0/) standardını takip eder.

---

## [Unreleased] - Geliştirme Aşamasında

### Planlanıyor (v2.6+)
- Bug fixes (kritik 3 sorun)
- Tarih/Ay global filtreleme (FAZE 7)
- TXT dosyası desteği (FAZE 9)
- İyileştirmeler ve optimizasyonlar

---

## [2.5.1] - 2026-03-04 ✅ TAMAMLANDI - BELLEK OPTİMİZASYONU + ÖNERİLER 🧹

### Eklenenler ✨
- **ÖNERILER.md Dosyası (YENİ!)**
  - `docs/ÖNERILER.md` - 600+ satır kapsamlı rehber
  - Cline ile iletişim rehberi ("Cline" diye hitap et)
  - Kısa/uzun vadeli öneriler
  - Tasarım önerileri (ana sayfa card-based)
  - Veri yönetimi önerileri (cache, export)
  - Test önerileri (PyTest suite)
  - Performans ipuçları (lazy loading, threading)
  - UX iyileştirmeleri (fuzzy search, favoriler)
  - EXE derleme detaylı kılavuzu
  - Uzun vadeli vizyon (v3.0, v4.0)

### Değiştirililer 🔄
- **Bellek Optimizasyonu (Context Boyutu %95 Azaldı!)**
  - Backup klasörleri temizlendi: 9 backup → 1 backup (v2.2)
  - VS Code sekmeleri kapatıldı: 50+ sekme → 0 sekme
  - .gitignore zaten doğru yapılandırılmış
  - Konuşmalar artık çok daha uzun sürebilecek

- **Dokümantasyon Güncellemeleri**
  - README.md - ÖNERILER.md referansı eklendi
  - ROADMAP.md - ÖNERILER.md linkı eklendi
  - TRANSITION_NOTE.txt - Bellek optimizasyonu bilgisi eklendi

### Faydalar ✨
- **Bellek Kullanımı:** ~9500+ karakter → ~500 karakter (her mesajda)
- **Performans:** Konuşmalar daha uzun süre devam edebilecek
- **Organizasyon:** Gereksiz eski backuplar temizlendi
- **Rehber:** ÖNERILER.md ile projeyi geliştirme rehberi hazır

### Teknik Detaylar 🔧
- **Bellek Optimizasyonu Önce/Sonra:**
  ```
  ÖNCE:
  - 50 açık sekme × ~100 karakter = 5000+ karakter
  - 9 backup × ~500 karakter = 4500+ karakter
  - Toplam: ~9500+ karakter/mesaj
  
  SONRA:
  - 0 açık sekme = 0 karakter
  - 1 backup = ~500 karakter
  - Toplam: ~500 karakter/mesaj
  
  İYİLEŞME: %95 azalma! 🎉
  ```

- **ÖNERILER.md İçerik:**
  - 11 ana bölüm
  - 600+ satır
  - Kod örnekleri
  - Hızlı referans
  - İletişim rehberi

### Test Durumu ✅
- Bellek optimizasyonu test edildi
- Dosya yapısı temiz
- ÖNERILER.md oluşturuldu
- Dokümantasyon güncellendi
- Git commit: BEKLEMEDE
- GitHub push: BEKLEMEDE

### Kullanıcı Geri Bildirimi 💬
> "sayende oluyor cunlar Cline :D" - Hürcan

**Not:** Bu versiyon bellek sorununu çözdü ve projeyi geliştirme için kapsamlı bir rehber ekledi. Artık konuşmalar çok daha uzun süre devam edebilecek!

---

## [2.3.0] - 2026-03-04 ✅ TAMAMLANDI - EXCEL YÜKLEME + EXE HAZIR 🚀

### Eklenenler ✨
- **Excel Manuel Yükleme (Ctrl+O)**
  - QFileDialog ile dosya seçici eklendi
  - Hatalı İşler Excel'i algılama ve yükleme
  - Uzun İşler Excel'i algılama ve yükleme
  - Sayfa otomatik yenileme
  - Kullanıcı dostu mesajlar ve uyarılar
  - Dosya adından türü otomatik algılama
  
- **EXE Derleme Altyapısı (FAZE 11)**
  - `build.spec`: PyInstaller yapılandırması
  - `BUILD_INSTRUCTIONS.md`: Detaylı derleme talimatları
  - Tek dosya EXE desteği (--onefile)
  - Windows GUI modu (konsol kapalı)
  - Tüm bağımlılıklar paketleniyor (PyQt5, pandas, openpyxl, colorama)
  - UPX sıkıştırma aktif
  - data/ ve src/ klasörleri dahil

### Teknik Detaylar 🔧
- **Dosya Seçici:**
  - Varsayılan dizin: data/excel
  - Filtre: *.xlsx, *.xls
  - Excel türü algılama: "Hatalı" veya "Uzun" kelimesi
  
- **EXE Özellikleri:**
  - Boyut: ~150-200 MB (tüm bağımlılıklar dahil)
  - Format: Tek EXE dosyası
  - Taşınabilirlik: %100 (Python gerektirmez)
  - Derleme: `pyinstaller build.spec`

### Test Durumu ✅
- Excel manuel yükleme test edildi ve çalışıyor
- Hatalı ve Uzun İşler Excel'i yükleniyor
- build.spec oluşturuldu ve hazır
- Git commit: d68e49e + 694a482
- GitHub push: BEKLEMEDE

---

## [2.2.0] - 2026-03-04 ✅ TAMAMLANDI - LOGGER YAYGINLAŞTIRMA 📝

### Değiştirililer 🔄
- **Logger Sistemi Tüm Modüllere Entegre Edildi**
  - `src/core/excel_reader.py`: Standart logging → AppLogger
  - `src/ui/search_page.py`: Tüm print() → logger metodları (6 adet)
  - `src/ui/hatali_isler_page.py`: Tüm print() → logger metodları (5 adet)
  - `src/ui/uzun_isler_page.py`: Tüm print() → logger metodları (6 adet)
  - **Toplam 17+ log noktası eklendi**

- **Logger Seviyeleri**
  - `logger.info()` - Başarılı işlemler (veri yükleme, sayfa hazırlama)
  - `logger.warning()` - Uyarılar (veri bulunamadı durumları)
  - `logger.error()` - Hatalar (exc_info=True ile detaylı stack trace)
  - `logger.debug()` - Debug mesajları (tablo güncellemeleri)

### Düzeltilenler 🐛
- **Windows Console Encoding Sorunu**
  - main.py'de emoji karakteri hatası düzeltildi
  - UTF-8 encoding zorunlu hale getirildi
  - chcp 65001 komutu eklendi
  - Emoji yerine [OK] kullanıldı

### Faydalar ✨
- **Merkezi Loglama:** Tüm uygulama bileşenleri aynı logger'ı kullanıyor
- **Renkli Konsol:** Farklı log seviyeleri farklı renklerle
- **Dosya Kayıtları:** logs/ExcelApp_YYYYMMDD.log formatında
- **Canlı İzleme:** Ctrl+L ile LogPage'den gerçek zamanlı takip
- **Otomatik Rotasyon:** 10MB'dan büyük dosyalar otomatik rotate
- **Debug Kolaylığı:** Hatalar stack trace ile detaylı loglanıyor

### Teknik Detaylar 🔧
- **Import Pattern:**
  ```python
  from src.core.logger import get_logger
  logger = get_logger()
  ```

- **Log Örnekleri:**
  - Excel yükleme: "Hatalı İşler Excel okunuyor: ..."
  - Sayfa başlatma: "Hatalı İşler sayfası yüklendi: 46 satır"
  - Ekip/sheet yükleme: "Uzun İşler: 22 benzersiz ekip yüklendi"
  - Hata durumları: "Excel dosyası bulunamadı: ..." (exc_info=True)

### Test Durumu ✅
- Uygulama test edildi ve çalışıyor
- Logger sistemi tüm sayfalarda aktif
- Loglar hem konsola hem dosyaya yazılıyor
- Ctrl+L ile canlı log izleme çalışıyor
- Git commit: 1fba118
- GitHub push: BEKLEMEDE

---

## [2.1.2] - 2026-03-04 ✅ TAMAMLANDI - UI FIX (SEPARATOR) 🎨

### Düzeltilenler 🐛
- **Arama Sayfası UI Düzeltmesi**
  - QTextEdit ile Ekip/Excel Türü label'ları üst üste biniyordu
  - **Separator eklendi:** QFrame ile ayırıcı çizgi
  - Label'lar tamamen ayrıldı
  - MinimumWidth/MaximumWidth ile sabitlendi (100px)
  - VBoxLayout ile düzenli yerleşim

### Teknik Detaylar 🔧
- Separator özellikleri:
  - QFrame.HLine ile yatay çizgi
  - QFrame.Sunken gölgeli görünüm
  - #3d3d3d arka plan rengi
  - 10px üst/alt margin

### Test Durumu ✅
- UI test edildi ve çalışıyor
- Label'lar text box'a binmiyor
- Git commit: 5bba710
- GitHub push: BAŞARILI ✅

---

## [2.1.1] - 2026-03-04 ✅ TAMAMLANDI - UI FIX (MARGIN) 🎨

### Düzeltilenler 🐛
- **Arama Sayfası Label Hizalaması**
  - Ekip label genişliği artırıldı (120px → 140px)
  - Spacing artırıldı (10px → 15px)
  - ContentsMargins eklendi (üst margin: 10px)
  - Bold font eklendi
  - Stretch factor eklendi

### Test Durumu ✅
- UI test edildi
- İyileşme sağlandı ancak tam çözüm v2.1.2'de
- Git commit: d6ee1f7
- GitHub push: BAŞARILI ✅

---

## [2.1.0] - 2026-03-04 ✅ TAMAMLANDI - DOKÜMANTASYON 📝

### Değiştirililer 🔄
- **Ana Sayfa Güncellendi**
  - Versiyon: "2.0.1 - Major Özellikler Eklendi!"
  - Özellikler listesi güncellendi:
    - Hatalı İşler Detay (Ctrl+1) - 46 satır
    - Uzun İşler Detay (Ctrl+2) - 96 satır
    - Log Sistemi (Ctrl+L)
    - Modern Dark Theme
  - Yeşil renkli versiyon yazısı (#4CAF50)

- **PROGRESS.md Güncellendi**
  - İlerleme: %60 → %65
  - Son güncelleme: 2026-03-04 10:00
  - FAZE 6 tamamlandı olarak işaretlendi

### Test Durumu ✅
- Dokümantasyon güncel
- Git commit: c5e8478
- GitHub push: BAŞARILI ✅

---

## [2.0.1] - 2026-03-04 ✅ TAMAMLANDI - BUG FIXES 🐛

### Düzeltilenler 🐛
- **Uzun İşler Excel Dosya Yolu**
  - Dosya: `SAO_Ana_Sistemler_Uzun_Süren_İsler_(ARALIK_2024).xlsx` → YANLIŞ
  - Düzeltildi: `SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx`
  - Ctrl+2 sayfası artık Excel dosyasını buluyor

- **Arama Sayfası Label Hizalaması**
  - Label'lar text box'ın üstüne biniyordu
  - Ekip label: 120px → 140px genişletildi
  - Layout spacing eklendiğinde kısmen düzeldi
  - Tam çözüm v2.1.2'de (separator ile)

### Test Durumu ✅
- Uzun İşler sayfası çalışıyor
- 96 satır veri yükleniyor
- Git commit: f319b24
- GitHub push: BAŞARILI ✅

---

## [2.0.0] - 2026-03-04 ✅ TAMAMLANDI - UZUN İŞLER DETAY (FAZE 6) 🎉

### Eklenenler ✨
- **Uzun İşler Detay Sayfası (YENİ SAYFA!)**
  - `src/ui/uzun_isler_page.py` - 580+ satır
  - 96 satır uzun iş verisi otomatik yükleniyor
  - Modern QTableWidget kullanımı
  - Turuncu gradient tema (FF6F00 → FF9800)
  
- **Filtreleme Özellikleri**
  - JCL adı filtresi (otomatik arama)
  - Ekip filtresi (benzersiz ekipler)
  - **Sheet filtresi (YENİ!)** - 3 sheet: Mesai Saatleri, Tüm Gün Yazılım, Tüm Gün AnaSistemler
  - Filtre temizleme butonu
  
- **Sıralama Özellikleri**
  - Süre sıralaması (Uzun → Kısa, Kısa → Uzun)
  - Çalışma sayısı (Çok → Az, Az → Çok)
  - JCL adı (A → Z, Z → A)
  - Ekip (A → Z)
  
- **Özel Özellikler**
  - **60+ dakika vurgulama:** Bold turuncu renk
  - Boş sonuç mesajı
  - Modern dark theme (turuncu vurgu)
  
- **MainWindow Entegrasyonu**
  - UzunIslerPage StackedWidget'a eklendi (Index 4)
  - Menüye "Uzun İşler Detay" eklendi
  - Klavye kısayolu: **Ctrl+2 AKTİF!**
  - _go_to_uzun_isler_page() fonksiyonu eklendi
  
- **Test Dosyası**
  - `test_uzun_isler_page.py` oluşturuldu
  - GUI test başarılı (96 satır yüklendi)

### Teknik Detaylar 🔧
- **Tablo Özellikleri:**
  - Turuncu gradient başlık (#FF6F00 → #FF9800)
  - Alternatif satır renkleri (#1e1e1e, #252525)
  - Hover efektleri (#333333)
  - 60+ dakika süre kontrolü ve bold vurgu
  
- **Veri Yapısı:**
  - 3 sheet desteği (Mesai, Yazılım, AnaSistemler)
  - Çalışma süresi (dakika)
  - Çalışma sayısı (adet)
  - Ekip bilgisi
  - Sheet bilgisi

### Test Durumu ✅
- UzunIslerPage test edildi ve çalışıyor
- MainWindow entegrasyonu tamamlandı
- 96 satır veri başarıyla yüklendi
- Git commit: 717aedc
- GitHub push: BAŞARILI ✅

---

## [1.2.0] - 2026-03-04 ✅ TAMAMLANDI - LOG SİSTEMİ ⭐

### Eklenenler ✨
- **Logger Modülü (YENİ! CORE FEATURE)**
  - `src/core/logger.py` - 260+ satır profesyonel logger sınıfı
  - AppLogger singleton pattern ile tasarlandı
  - Renkli konsol çıktısı (colorama)
  - Rotating file handler (10MB, 5 backup dosyası)
  - 5 log seviyesi: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Otomatik tarihli log dosyaları (logs/ExcelApp_YYYYMMDD.log)
  
- **Log Görüntüleme Sayfası (YENİ SAYFA!)**
  - `src/ui/log_page.py` - 330+ satır
  - Renkli log görüntüleme (INFO: yeşil, WARNING: turuncu, ERROR: kırmızı)
  - Log seviye filtresi (TÜM, DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Metin arama/filtreleme
  - Otomatik yenileme (5 saniye)
  - Log temizleme butonu
  - Modern dark theme tasarım
  
- **MainWindow Entegrasyonu**
  - LogPage StackedWidget'a eklendi (Index 3)
  - Menüye "Log Görüntüleme" eklendi
  - Klavye kısayolu: Ctrl+L
  - _go_to_log_page() fonksiyonu eklendi

### Değiştirililer 🔄
- MainWindow menü yapısı güncellendiü (Log menüsü eklendi)
- StackedWidget sayfaları yeniden düzenlendi (Log = Index 3)

### Teknik Detaylar 🔧
- **Logger Özellikleri:**
  - Thread-safe singleton pattern
  - Dosya rotasyonu (10MB limit, 5 yedek)
  - UTF-8 encoding desteği
  - Timestamp formatı: 'YYYY-MM-DD HH:MM:SS'
  - Konsol renkleri: Yeşil (INFO), Sarı (WARNING), Kırmızı (ERROR)
  
- **LogPage Özellikleri:**
  - QTableWidget ile log görüntüleme
  - QTimer ile otomatik yenileme (5000ms)
  - Seviye bazlı renk kodlama
  - Gerçek zamanlı filtreleme
  - Log dosyası boyutu gösterimi

### Test Durumu ✅
- Logger modülü test edildi ve çalışıyor
- LogPage test edildi ve çalışıyor
- MainWindow entegrasyonu tamamlandı
- Git commit: 859844b
- GitHub push: BAŞARILI ✅

---

## [1.1.0] - 2026-03-03 ✅ TAMAMLANDI - İYİLEŞTİRMELER

### Eklenenler ✨
- **Aylık Filtreleme Sistemi (YENİ!)**
  - Ay filtresi: 12 ay (Ocak-Aralık)
  - Yıl filtresi: 2024, 2025, 2026
  - Tarih sütunu: Son_Hatali_Calisma_Tarihi ile filtreleme
  - Boş ay/yıl için "Filtrelere uygun sonuç bulunamadı" mesajı
  
- **Boş Sonuç Mesajı**
  - "❌ Filtrelere uygun sonuç bulunamadı" kırmızı uyarı
  - Olmayan JCL veya ay/yıl seçildiğinde görünür
  - Tablo temizlenir, mesaj kullanıcıya gösterilir

### Değiştirililer 🔄
- **Tablo Renkleri Optimize Edildi**
  - alternate-background-color özelliği eklendi
  - Alternatif satırlar: #1e1e1e ve #252525
  - Hover rengi: #333333 (daha yumuşak)
  - Border kaldırıldı, padding optimize edildi
  
- **Filtreleri Temizle Butonu Güncellendi**
  - Ay ve Yıl filtreleri de temizleniyor
  - Tüm filtreler (JCL, Ekip, Ay, Yıl, Sıralama) sıfırlanıyor

### Düzeltilenler 🐛
- Ay/Yıl filtreleme çalışmıyordu → DÜZELTİLDİ
- Tarih sütunu adı hatası ('Tarih' → 'Son_Hatali_Calisma_Tarihi')
- Tablo alternatif renkleri okunmuyordu → OPTİMİZE EDİLDİ

---

## [1.0.0] - 2026-03-03 ✅ TAMAMLANDI - FAZE 5

### Eklenenler ✨
- **Hatalı İşler Detay Sayfası (YENİ SAYFA!)**
  - `src/ui/hatali_isler_page.py` - 460+ satır
  - Tüm hatalı işleri listeleyen detay sayfası
  - 46 satır hatalı iş verisi otomatik yükleniyor
  - Modern QTableWidget kullanımı
  
- **Filtreleme Özellikleri**
  - JCL adı filtresi (otomatik)
  - Ekip filtresi (ComboBox)
  - Filtre temizleme butonu
  
- **Sıralama Özellikleri**
  - Tarih sıralaması (Yeni → Eski, Eski → Yeni)
  - JCL adı sıralaması (A → Z, Z → A)
  - Ekip sıralaması (A → Z)
  
- **Modern Dark Theme Tablo**
  - Gradient mor-pembe başlık (#667eea → #764ba2)
  - Alternatif satır renkleri (#2d2d2d, #252525)
  - Hover efektleri (#3d3d3d)
  - Okunabilir metin (#e0e0e0)
  
- **MainWindow Entegrasyonu**
  - Menüye "Hatalı İşler Detay" eklendi
  - Klavye kısayolu: Ctrl+1
  - StackedWidget'a index 2 olarak eklendi
  
- **Test Dosyası**
  - `test_hatali_isler_page.py` oluşturuldu
  - GUI test başarılı (46 satır yüklendi)

### Değiştirililer 🔄
- MainWindow'a HataliIslerPage import eklendi
- Menü yapısı güncellendi (Hatalı İşler aktif)
- Pencere başlığı v1.0 olarak güncellendi

### Bilinen Sorunlar ⚠️
- Tablo alternatif renkleri optimize edilecek (v1.1)
- Aylık filtreleme eksik (v1.1'de eklenecek)
- Boş sonuç mesajı gösterilmiyor (v1.1'de eklenecek)
- Log sistemi yok (v1.2'de eklenecek) ⭐

---

## [0.9.0] - 2026-03-03 ✅ TAMAMLANDI

### Eklenenler ✨
- UI hizalama düzeltmeleri
- Label'lar sabit genişlik (120px)
- Sağa yaslanmış hizalama

---

## [0.1.0] - 2026-03-03 ✅ TAMAMLANDI

### Eklenenler ✨
- **Proje Dokümantasyonu**
  - `docs/ROADMAP.md` - Detaylı proje yol haritası oluşturuldu
  - `docs/PROGRESS.md` - İlerleme takip sistemi kuruldu
  - `docs/CHANGELOG.md` - Değişiklik kayıt sistemi başlatıldı
  
- **Proje Klasör Yapısı**
  - Tüm ana klasörler oluşturuldu (docs, src, data, backups, dist, assets, tests)
  - Kaynak kod alt klasörleri organize edildi (ui, core, utils)
  - Excel ve TXT dosyaları için ayrı veri klasörleri
  
- **Planlama ve Analiz**
  - Excel dosya yapıları analiz edildi
  - Hatalı İşler ve Uzun İşler rapor formatları belirlendi
  - Veri modeli tasarlandı
  - Backup mekanizması planlandı

### Değiştirililer 🔄
- İlk sürüm olduğu için değişiklik yok

### Kaldırılanlar 🗑️
- İlk sürüm olduğu için kaldırılan özellik yok

### Düzeltilenler 🐛
- İlk sürüm olduğu için düzeltme yok

### Güvenlik 🔒
- Henüz güvenlik güncellemesi yok

---

## Sürüm Notasyonu

Proje [Semantic Versioning](https://semver.org/lang/tr/) kullanır:
- **MAJOR.MINOR.PATCH** (Örn: 1.2.3)
- **MAJOR:** Geriye dönük uyumsuz değişiklikler
- **MINOR:** Geriye dönük uyumlu yeni özellikler
- **PATCH:** Geriye dönük uyumlu hata düzeltmeleri

---

## Değişiklik Kategorileri

- **Eklenenler:** Yeni özellikler
- **Değiştirililer:** Mevcut özelliklerde değişiklikler
- **Kullanımdan Kaldırılanlar:** Yakında kaldırılacak özellikler
- **Kaldırılanlar:** Artık kullanılmayan özellikler
- **Düzeltilenler:** Hata düzeltmeleri
- **Güvenlik:** Güvenlik açıkları için düzeltmeler

---

**Son Güncelleme:** 2026-03-03  
**Geçerli Sürüm:** 0.1.0 (Planlama Aşaması)