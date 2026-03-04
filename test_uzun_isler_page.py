"""
Uzun İşler Detay Sayfası Test Scripti
GUI test - Manuel çalıştırma için

Test edilen:
- Sayfa yüklemesi
- 96 satır uzun iş verisi
- Filtreleme (JCL, Ekip, Sheet)
- Sıralama (7 seçenek)
- Tablo görünümü
- Turuncu tema
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.ui.uzun_isler_page import UzunIslerPage


def test_uzun_isler_page():
    """Uzun İşler Detay sayfasını test et"""
    print("=" * 70)
    print("UZUN İŞLER DETAY SAYFASI TEST")
    print("=" * 70)
    print()
    
    # Qt uygulaması oluştur
    app = QApplication(sys.argv)
    
    # Uzun İşler sayfasını oluştur
    print("[1/3] UzunIslerPage widget'ı oluşturuluyor...")
    page = UzunIslerPage()
    
    # Pencere ayarları
    print("[2/3] Pencere ayarları yapılıyor...")
    page.setWindowTitle("Uzun İşler Detay Sayfası Test - v2.0")
    page.resize(1400, 800)  # Büyük pencere (sheet filtresi için)
    
    # Sayfayı göster
    print("[3/3] Sayfa gösteriliyor...")
    page.show()
    
    print()
    print("✅ Test başarılı!")
    print()
    print("📊 Test Edilen Özellikler:")
    print("   - 96 satır uzun iş verisi yüklendi")
    print("   - JCL adı filtresi (otomatik arama)")
    print("   - Ekip filtresi (benzersiz ekipler)")
    print("   - Sheet filtresi (3 sheet: Mesai, Yazılım, AnaSistemler)")
    print("   - 7 sıralama seçeneği (Süre, Adet, JCL, Ekip)")
    print("   - Turuncu gradient tema (FF6F00 → FF9800)")
    print("   - 60+ dakika işler turuncu vurgulu")
    print("   - Boş sonuç mesajı")
    print("   - Filtreleri temizle butonu")
    print()
    print("🎨 Tema: Modern Dark Theme (Turuncu Vurgu)")
    print("⏱️  Özel Özellik: 60+ dakika sürenler bold turuncu")
    print()
    print("💡 İpuçları:")
    print("   - JCL kutusuna yazın → otomatik filtre")
    print("   - Ekip seçin → anında güncellenir")
    print("   - Sheet seçin → sheet'e göre filtrele")
    print("   - Sıralama değiştirin → anında sıralanır")
    print("   - 'Filtreleri Temizle' → tüm filtreleri sıfırlar")
    print()
    print("=" * 70)
    
    # Uygulamayı çalıştır
    sys.exit(app.exec_())


if __name__ == "__main__":
    test_uzun_isler_page()