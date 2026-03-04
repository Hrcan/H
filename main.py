"""
Excel Veri Görüntüleme Uygulaması - Ana Program
Versiyon: 2.0.0
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow


def main():
    """Ana uygulama fonksiyonu"""
    print("=" * 70)
    print("EXCEL VERİ GÖRÜNTÜLEME UYGULAMASI")
    print("=" * 70)
    print()
    print("Versiyon: 2.0.0")
    print("Durum: Aktif - Major Özellikler Eklendi!")
    print()
    print("Özellikler:")
    print("  ✅ Hatalı İşler Detay (Ctrl+1) - 46 satır")
    print("  ✅ Uzun İşler Detay (Ctrl+2) - 96 satır")
    print("  ✅ Log Sistemi (Ctrl+L)")
    print("  ✅ Modern Dark Theme")
    print()
    print("Uygulama başlatılıyor...")
    print("=" * 70)
    print()
    
    # Qt uygulaması oluştur
    app = QApplication(sys.argv)
    
    # Ana pencereyi oluştur ve göster
    window = MainWindow()
    window.show()
    
    # Uygulamayı çalıştır
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()