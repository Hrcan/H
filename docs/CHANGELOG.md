# 📋 DEĞİŞİKLİK GEÇMİŞİ (CHANGELOG)

**Proje:** Excel Veri Görüntüleme Uygulaması  
**Format:** Bu dosya [Keep a Changelog](https://keepachangelog.com/tr/1.0.0/) standardını takip eder.

---

## [Unreleased] - Geliştirme Aşamasında

### Planlanıyor (v1.2) - Log Sistemi ⭐ ÖNEMLİ
- Logger modülü (dosya ve konsol)
- Log seviyeleri (DEBUG, INFO, WARNING, ERROR)
- Log görüntüleme ekranı
- Log filtreleme ve arama

### Planlanıyor (v2.0+)
- Uzun İşler Detay Sayfası (FAZE 6)
- Tarih/Ay global filtreleme (FAZE 7)
- TXT dosyası desteği (FAZE 9)
- EXE derleme (FAZE 11)

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