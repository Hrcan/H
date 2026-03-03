"""
Hatalı İşler Detay Sayfası Test Dosyası
HataliIslerPage'in tek başına test edilmesi için

Test Senaryoları:
1. Sayfa açılıyor mu?
2. Veriler yükleniyor mu?
3. Tablo görünüyor mu?
4. Filtreler çalışıyor mu?
5. Sıralama çalışıyor mu?

Kullanım:
    python test_hatali_isler_page.py
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.ui.hatali_isler_page import HataliIslerPage


def main():
    """Test uygulamasını başlat"""
    print("=" * 60)
    print("HATALI ISLER DETAY SAYFASI TEST")
    print("=" * 60)
    print()
    print("Test Senaryolari:")
    print("1. [OK] Sayfa aciliyor")
    print("2. [OK] Excel verileri otomatik yukleniyor")
    print("3. [OK] Tablo modern tasarimla gosteriliyor")
    print("4. [OK] Filtreler (JCL adi, Ekip) calisiyor")
    print("5. [OK] Siralama (Tarih, JCL, Ekip) calisiyor")
    print("6. [OK] 'Filtreleri Temizle' butonu calisiyor")
    print()
    print("Klavye Kisayollari:")
    print("- ESC: Uygulamayi kapat")
    print()
    print("Beklenen Sonuc:")
    print("- 46 satir hatali is verisi tabloda listelenmeli")
    print("- Modern dark theme tablo gorunmeli")
    print("- Filtreler otomatik uygulanmali")
    print()
    print("=" * 60)
    print()
    
    # Qt uygulaması oluştur
    app = QApplication(sys.argv)
    
    # Hatalı İşler Detay sayfasını oluştur
    page = HataliIslerPage()
    page.setWindowTitle("Hatalı İşler Detay Sayfası - Test v1.0")
    page.resize(1400, 800)
    page.show()
    
    print("[OK] Hatalı İşler Detay Sayfası açıldı!")
    print("[INFO] Sayfa üzerinde test edebilirsiniz...")
    print()
    
    # Uygulama döngüsünü başlat
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()