"""
SearchPage Test Script - Gercek Veri ile Test
"""

import sys
from PyQt5.QtWidgets import QApplication

# Import edebilmek icin src'yi path'e ekle
sys.path.insert(0, 'src')

from ui.main_window import MainWindow

if __name__ == "__main__":
    print("=" * 60)
    print("SEARCHPAGE TEST - GERCEK VERI ILE")
    print("=" * 60)
    print()
    print("Test Adimlari:")
    print("1. Ana pencere acilacak")
    print("2. 'Ara' butonuna tiklayin")
    print("3. SearchPage acilacak - Excel verileri yuklenecek")
    print("4. JCL adi girin ve arama yapin (orn: PKRB)")
    print()
    print("Baslatiliyor...")
    print("=" * 60)
    print()
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())