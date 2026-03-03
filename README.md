# 📊 Excel Veri Görüntüleme Uygulaması

**Versiyon:** 0.1.0 (Geliştirme Aşaması)  
**Son Güncelleme:** 2026-03-03  
**Durum:** 🟡 Aktif Geliştirme

Modern ve kullanıcı dostu bir masaüstü uygulaması ile Excel ve TXT dosyalarındaki JCL (Job Control Language) verilerini görüntüleyin, filtreleyin ve analiz edin.

---

## 🎯 Proje Hakkında

Bu uygulama, sistem operasyon raporlarındaki (Hatalı İşler ve Uzun Süren İşler) verileri kolayca görüntülemek, aramak ve filtrelemek için geliştirilmiştir. PyQt5 ile oluşturulan modern arayüzü sayesinde karmaşık Excel verilerini basit ve hızlı bir şekilde analiz edebilirsiniz.

### Temel Özellikler

- ✅ **Excel Dosyası Desteği:** Hatalı İşler ve Uzun Süren İşler raporlarını okuma
- ✅ **Multi-Sheet Okuma:** Tek Excel'de birden fazla sayfa desteği
- ✅ **Akıllı Arama:** JCL adı ve ekip bazlı filtreleme
- ✅ **Tarih/Ay Seçimi:** Checkbox ile esnek tarih filtreleme
- ✅ **Detaylı Görünüm:** Hem hatalı hem uzun işleri yan yana görüntüleme
- 🚧 **TXT Dosyası Desteği:** (Yakında)
- 🚧 **Ekip Atama:** TXT'den okunan verilere ekip bilgisi ekleme (Yakında)

---

## 📋 İçindekiler

- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Veri Formatları](#-veri-formatları)
- [Proje Yapısı](#-proje-yapısı)
- [Geliştirme](#-geliştirme)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🚀 Kurulum

### Gereksinimler

- **Python:** 3.8 veya üzeri
- **İşletim Sistemi:** Windows 10/11
- **RAM:** Minimum 4GB (8GB önerilir)

### Adım 1: Python Bağımlılıklarını Yükleme

```bash
pip install -r requirements.txt
```

### Adım 2: Veri Klasörlerini Hazırlama

Excel ve TXT dosyalarınızı ilgili klasörlere yerleştirin:

```
data/
├── excel/        # Excel dosyalarını buraya
└── txt/          # TXT dosyalarını buraya
```

### Adım 3: Uygulamayı Çalıştırma

```bash
python src/main.py
```

---

## 💻 Kullanım

### 1. Excel Dosyası Yükleme

- Menüden **Dosya → Excel Yükle** seçeneğini tıklayın
- `data/excel/` klasöründen rapor dosyasını seçin
- Veriler otomatik olarak yüklenecek ve son ay verileri gösterilecektir

### 2. JCL Arama

- Ana arama sayfasında **JCL Adı** kutusuna aranacak JCL'i yazın
- **Ara** butonuna tıklayın
- Sonuçlar tabloda listelenecektir

### 3. Ekip Bazlı Filtreleme

- **Ekip Adı** açılır menüsünden ekip seçin
- Sadece o ekibe ait JCL'ler gösterilecektir

### 4. Tarih/Ay Filtreleme

- **Ay Seçici** bölümünden istediğiniz ayları işaretleyin
- **Filtrele** butonuna tıklayın
- Seçili aylar için veriler getirilebilir

### 5. Detay Görüntüleme

- Tabloda bir JCL'e çift tıklayın
- Hem hatalı hem uzun iş verileri yan yana gösterilecektir
- Veri yoksa "Veri bulunamadı" mesajı görünür

---

## 📊 Veri Formatları

### Hatalı İşler Excel Formatı

**Dosya Adı:** `SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(AY_YILI).xlsx`

**Okunacak Kolonlar (A-E):**

| Kolon | Başlık | Açıklama |
|-------|--------|----------|
| A | JCL Adı | İş adı (Benzersiz anahtar) |
| B | Hatalı Çalışma Sayısı (Aylık) | O ayki toplam hata sayısı |
| C | Son Hatalı Çalışma Tarihi | En son hata tarihi |
| D | Hatalı Çalışma Sayısı (Yıllık) | Yıl içi toplam hata sayısı |
| E | Sorumlu Ekip | Ekip adı bilgisi |

**Sheet'ler:**
- "Hatalı Isler Yazılım PROD"
- "Hatalı Isler AYDB PROD"

### Uzun İşler Excel Formatı

**Dosya Adı:** `SAO_Sistem_Operasyon_Uzun_Süren_İşler(AY_YILI).xlsx`

**Okunacak Kolonlar (A-D):**

| Kolon | Başlık | Açıklama |
|-------|--------|----------|
| A | JCL Adı | İş adı (Benzersiz anahtar) |
| B | Çalışma Sayısı (Adet) | Toplam çalışma sayısı |
| C | Çalışma Süresi (Dakika) | Toplam süre |
| D | Sorumlu Ekip | Ekip adı bilgisi |

**Sheet'ler:**
- "Mesai Saatleri"
- "Tüm Gün Yazılım"
- "Tüm Gün AnaSistemler"

---

## 📁 Proje Yapısı

```
d:/H/
├── 📂 docs/                    # Dökümantasyon
│   ├── ROADMAP.md             # Proje yol haritası
│   ├── PROGRESS.md            # İlerleme takibi
│   └── CHANGELOG.md           # Değişiklik geçmişi
│
├── 📂 src/                     # Kaynak kodlar
│   ├── main.py                # Ana program
│   ├── ui/                    # Arayüz dosyaları
│   ├── core/                  # İş mantığı
│   └── utils/                 # Yardımcı fonksiyonlar
│
├── 📂 data/                    # Veri dosyaları
│   ├── excel/                 # Excel dosyaları
│   └── txt/                   # TXT dosyaları
│
├── 📂 backups/                 # Otomatik yedekler
├── 📂 dist/                    # EXE çıktıları
├── 📂 assets/                  # Görseller ve ikonlar
├── 📂 tests/                   # Test dosyaları
│
├── README.md                   # Bu dosya
└── requirements.txt            # Python bağımlılıkları
```

---

## 🛠️ Geliştirme

### Geliştirme Ortamı Kurulumu

1. Repository'yi klonlayın veya indirin
2. Sanal ortam oluşturun (opsiyonel):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

### Backup Sistemi

Proje otomatik backup mekanizması ile çalışır:

- Her önemli değişiklik öncesi otomatik backup alınır
- Backup'lar `backups/` klasöründe tarih-saat damgası ile saklanır
- Her backup'ta `BACKUP_NOTE.txt` ile değişiklik açıklaması yer alır

### Test Etme

```bash
python -m pytest tests/
```

### EXE Olarak Derleme

```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico src/main.py
```

Derlenmiş EXE `dist/` klasöründe oluşturulacaktır.

---

## 📖 Dokümantasyon

Detaylı dokümantasyon için `docs/` klasörüne bakın:

- **[ROADMAP.md](docs/ROADMAP.md)** - Proje yol haritası ve geliştirme fazları
- **[PROGRESS.md](docs/PROGRESS.md)** - Güncel ilerleme durumu ve tamamlanan işler
- **[CHANGELOG.md](docs/CHANGELOG.md)** - Sürüm geçmişi ve değişiklikler

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları takip edin:

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'i push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

### Kod Standartları

- PEP 8 Python kod standartlarını takip edin
- Anlamlı commit mesajları yazın
- Her fonksiyon için docstring ekleyin
- Yeni özellikler için test yazın

---

## 🐛 Hata Bildirimi

Bir hata bulduysanız lütfen şunları yapın:

1. Hatanın daha önce bildirilip bildirilmediğini kontrol edin
2. Detaylı açıklama ile yeni bir issue oluşturun
3. Hata mesajlarını ve ekran görüntülerini ekleyin
4. Sisteminizin özelliklerini belirtin (OS, Python versiyonu vb.)

---

## 📝 Lisans

Bu proje şu anda geliştirme aşamasındadır. Lisans bilgileri yakında eklenecektir.

---

## 👥 İletişim

Sorularınız veya önerileriniz için:

- **Proje Sahibi:** [İsim]
- **E-posta:** [E-posta adresi]
- **GitHub:** [GitHub profili]

---

## 🙏 Teşekkürler

Bu projeyi geliştirmede yardımcı olan herkese teşekkürler!

---

**Son Güncelleme:** 2026-03-03  
**Versiyon:** 0.1.0  
**Durum:** Aktif Geliştirme 🚀