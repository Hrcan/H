"""
Excel Veri Görüntüleme Uygulaması - Ana Program
Versiyon: 2.0.0
"""

import sys
import os
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow

# Windows console encoding sorununu çöz
if sys.platform == "win32":
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')


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
    print("  [OK] Hatalı İşler Detay (Ctrl+1) - 46 satır")
    print("  [OK] Uzun İşler Detay (Ctrl+2) - 96 satır")
    print("  [OK] Log Sistemi (Ctrl+L)")
    print("  [OK] Modern Dark Theme")
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