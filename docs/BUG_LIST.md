# 🐛 BİLİNEN SORUNLAR VE HATA LİSTESİ

**Proje:** Excel Veri Görüntüleme Uygulaması  
**Son Güncelleme:** 2026-03-04 12:57  
**Versiyon:** v2.5.0 (Modern Design)

---

## 🔴 KRİTİK SORUNLAR (Acil Düzeltilmeli)

### 1. Veri Yönetimi - Veri Temizleme Çalışmıyor ❌
**Dosya:** `src/ui/data_manager_page.py`  
**Sorun:** "Tüm Veriyi Temizle" butonuna basıldığında veriler temizlenmiyor.  
**Beklenen:** Tüm yüklü Excel verileri bellekten silinmeli ve tablolar boş görünmeli.  
**Gerçekte:** Veriler duruyor, temizlenmiyor.  
**Öncelik:** 🔴 Yüksek  
**Etkilenen Kullanıcılar:** Tüm kullanıcılar  

**Çözüm Önerisi:**
- `data_manager_page.py` içinde `_clear_all_data()` fonksiyonunu kontrol et
- DataFrame'lerin gerçekten temizlendiğinden emin ol
- Tablo widget'larını güncelle
- Diğer sayfalara da temizlik sinyali gönder

---

### 2. Excel Yükleme - Çoklu Dosya Yükleme Hatası ⚠️
**Dosya:** `src/ui/main_window.py` - `_load_excel()` fonksiyonu  
**Sorun:** Birden fazla Excel dosyası seçildiğinde bazı dosyalar "Yüklenmedi" uyarısı veriyor.  
**Beklenen:** Tüm seçilen Excel dosyaları başarıyla yüklenmeli.  
**Gerçekte:** 
- Hatalı İşler Excel'i yükleniyor
- Uzun İşler Excel'i yükleniyor
- Ek dosyalar (KASIM, EKİM vb.) "Yüklenmedi" diyor

**Öncelik:** 🔴 Yüksek  
**Etkilenen Kullanıcılar:** Çoklu ay verisi yüklemek isteyenler  

**Çözüm Önerisi:**
```python
# Sorun: Dosya adı algılama mantığı sadece tek dosya için çalışıyor
# Çözüm: Her dosya için yeni bir reader instance oluştur
# Mevcut sayfaları yenile, yeni instance oluşturma
```

**Detay:**
- Dosya kategorize mantığı çalışıyor (Hatalı/Uzun ayrımı)
- Ama her dosya için ayrı DataFrame merge edilmiyor
- Sadece son yüklenen dosya görünüyor

---

### 3. Log Sayfası - Sürekli "Loglar yüklendi" Mesajı 🔁
**Dosya:** `src/ui/log_page.py`  
**Sorun:** Log sayfası açıldığında sürekli "Loglar yüklendi: 100 satır" mesajı basılıyor.  
**Beklenen:** Log yükleme işlemi bir kez yapılmalı, sessizce.  
**Gerçekte:** Her refresh'te log dosyasına "Loglar yüklendi" yazılıyor.  

**Öncelik:** 🟡 Orta  
**Etkilenen Kullanıcılar:** Log sayfasını kullananlar  

**Log Çıktısı:**
```
12:56:08 | INFO | Loglar yüklendi: 100 satır
12:56:09 | INFO | Loglar yüklendi: 100 satır
12:56:10 | INFO | Loglar yüklendi: 100 satır
... (20+ kez tekrar ediyor)
```

**Çözüm Önerisi:**
- `log_page.py` içinde `_load_logs()` fonksiyonunda logger kullanma
- Veya log level'ı DEBUG'a düşür
- Veya log mesajını kaldır (silent loading)

---

## 🟡 ORTA ÖNCELİKLİ SORUNLAR

### 4. ComboBox Görünüm Problemi 🎨
**Dosyalar:** 
- `src/ui/hatali_isler_page.py`
- `src/ui/uzun_isler_page.py`

**Sorun:** Açılır menülerde (ComboBox) görünüm sorunları var.  
**Detaylar:**
- Dropdown ok işareti görünmüyor veya küçük
- Seçenekler listesi koyu arka plan ile okunmuyor
- Hover efekti tutarsız

**Öncelik:** 🟡 Orta  
**Etkilenen Kullanıcılar:** Filtreleme kullananlar  

**Gözlemler (Ekran Görüntüsünden):**
- ✅ Filtreleme çalışıyor (46 satır gösteriliyor)
- ⚠️ ComboBox styling eksik
- ⚠️ Dropdown arrow görünmüyor

**Çözüm Önerisi:**
```css
/* Theme'de ComboBox::down-arrow için SVG icon ekle */
/* Veya border-based arrow'u büyüt */
QComboBox::down-arrow {
    width: 12px;
    height: 8px;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid #e0e0e0;
}
```

---

### 5. Modern UI - Ana Sayfa Eski Tasarım 🏠
**Dosya:** `src/ui/main_window.py` - `_create_home_page()`  
**Sorun:** Ana sayfa card-based tasarıma geçmedi, eski tasarım duruyor.  
**Beklenen:** Modern glassmorphism kartlar, gradient background.  
**Gerçekte:** Liste bazlı eski tasarım.  

**Öncelik:** 🟢 Düşük (Görsel)  
**Etkilenen Kullanıcılar:** İlk açılış deneyimi  

**Not:** Kod yazıldı ama uygulanmadı. Sadece entegrasyon gerekiyor.

---

## 🟢 DÜŞÜK ÖNCELİKLİ / İYİLEŞTİRME

### 6. Otomatik Yenileme - Log Sayfası ♻️
**Sorun:** Otomatik yenileme çok sık tetikleniyor olabilir.  
**Öneriler:**
- Refresh interval'ı 5 saniyeden 10 saniyeye çıkar
- Veya manuel refresh butonu ekle
- Otomatik yenilemeyi kapatma seçeneği

---

### 7. Tema Sistemi - Henüz Kullanılmıyor 🎨
**Durum:** 4 tema hazır ama kullanıcı seçemiyor.  
**Öneriler:**
- Ayarlar menüsü ekle
- Tema seçici dropdown
- Canlı tema değiştirme (uygulama yeniden başlatmadan)

---

## 📋 SORUN ÖZETİ

| # | Sorun | Öncelik | Dosya | Durum |
|---|-------|---------|-------|-------|
| 1 | Veri Temizleme Çalışmıyor | 🔴 Yüksek | data_manager_page.py | Açık |
| 2 | Çoklu Excel Yükleme Hatası | 🔴 Yüksek | main_window.py | Açık |
| 3 | Log Spam Problemi | 🟡 Orta | log_page.py | Açık |
| 4 | ComboBox Görünümü | 🟡 Orta | hatali/uzun_isler_page.py | Açık |
| 5 | Ana Sayfa Eski Tasarım | 🟢 Düşük | main_window.py | Açık |
| 6 | Log Auto-Refresh | 🟢 Düşük | log_page.py | İyileştirme |
| 7 | Tema Seçici Yok | 🟢 Düşük | Genel | İyileştirme |

---

## 🔧 ÖNERİLEN DÜZELTME SIRASI

### Sprint 1: Kritik Hatalar (1-2 saat)
1. **Veri Temizleme Fix** (30 dk)
   - `data_manager_page.py` düzelt
   - Test et: Temizle → Yenile → Kontrol

2. **Excel Yükleme Fix** (45 dk)
   - Multi-file handling mantığını düzelt
   - DataFrame merge/append ekle
   - Test: 3-4 dosya birden yükle

3. **Log Spam Fix** (15 dk)
   - Logger.info çağrısını kaldır veya DEBUG yap
   - Test: Log sayfası aç → kontrol et

### Sprint 2: UI İyileştirmeler (1 saat)
4. **ComboBox Styling** (30 dk)
   - Theme dosyalarında QComboBox CSS düzelt
   - Dropdown arrow ekle/büyüt
   - Test: Tüm sayfalarda ComboBox'ları kontrol et

5. **Ana Sayfa Modern Tasarım** (30 dk)
   - `_create_home_page()` fonksiyonunu değiştir
   - Card sistemini entegre et
   - Test: Ana sayfayı aç

### Sprint 3: İyileştirmeler (1 saat)
6. **Log Optimizasyonu** (20 dk)
7. **Tema Seçici** (40 dk)

---

## 🧪 TEST PLANI

### Her Düzeltme İçin:
```
1. Lokal test yap
2. Ana fonksiyonları kontrol et
3. Edge case'leri dene
4. Performans kontrolü
5. Git commit (açıklayıcı mesaj)
6. Backup al
```

### Tam Test Checklist:
- [ ] Excel yükleme (tek dosya)
- [ ] Excel yükleme (çoklu dosya)
- [ ] Veri temizleme
- [ ] Veri yeniden yükleme
- [ ] Hatalı İşler filtreleme
- [ ] Uzun İşler filtreleme
- [ ] Log görüntüleme
- [ ] Sayfa geçişleri (Ctrl+1, Ctrl+2, Ctrl+L)
- [ ] ComboBox'ları aç/kapat
- [ ] Tabloları scroll et

---

## 📝 NOTLAR

### Genel Gözlemler:
- ✅ Uygulama çalışıyor, crash yok
- ✅ Excel okuma başarılı
- ✅ Filtreleme mantığı çalışıyor
- ✅ Logger sistemi aktif
- ⚠️ UI polish gerekiyor
- ⚠️ Veri yönetimi iyileştirme gerekiyor

### Kullanıcı Deneyimi:
- 🙂 Modern dark theme hoş
- 🙂 Menüler çalışıyor
- 😐 ComboBox'lar okunmuyor
- 😐 Veri temizleme çalışmıyor
- 😕 Çoklu dosya yüklenmiyor

---

**Sonraki Güncelleme:** Sorunlar düzeltildikçe bu dosya güncellenecek.  
**Durum Takibi:** PROGRESS.md ve CHANGELOG.md ile senkronize.

---

## 🆘 HIZLI FIX NOTLARI

```python
# 1. Veri Temizleme Fix
def _clear_all_data(self):
    # DataFrame'leri None yap
    self.hatali_df = None
    self.uzun_df = None
    # Tablo widget'larını temizle
    self.table.clear()
    # Diğer sayfalara sinyal gönder
    self.search_page.clear_data()
    ...

# 2. Excel Yükleme Fix
for file_path in file_paths:
    # Her dosya için ayrı işle
    if "Hatalı" in file_name:
        new_df = reader.read_hatali_isler(file_path)
        if existing_df is not None:
            existing_df = pd.concat([existing_df, new_df])
        else:
            existing_df = new_df

# 3. Log Spam Fix
# logger.info("Loglar yüklendi: {len(logs)} satır")  # KALDIR
# Veya
logger.debug("Loglar yüklendi: {len(logs)} satır")  # DEBUG'a çevir
```

---

**Hazırlayan:** Claude (AI Assistant)  
**Tarih:** 2026-03-04  
**Durum:** 📋 Aktif Takip