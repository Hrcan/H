"""
Main Window - Ana Pencere
PyQt5 ile oluşturulmuş ana uygulama penceresi

Özellikler:
- Menü sistemi (Dosya, Görünüm, Yardım)
- Durum çubuğu
- Merkezi widget (sayfa geçişleri için)
"""

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                              QMenuBar, QMenu, QAction, QStatusBar,
                              QLabel, QPushButton, QMessageBox, QStackedWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon
import sys

# UI modüllerini import et
from .search_page import SearchPage


class MainWindow(QMainWindow):
    """Ana uygulama penceresi"""
    
    def __init__(self):
        """MainWindow'u başlat"""
        super().__init__()
        
        # Pencere özellikleri
        self.setWindowTitle("Excel Veri Görüntüleme Uygulaması v0.7 - Dark Mode")
        self.setGeometry(100, 100, 1200, 800)  # x, y, genişlik, yükseklik
        self.setMinimumSize(QSize(1000, 600))
        
        # DARK MODE UYGULA! 🎨
        self._apply_dark_theme()
        
        # Sayfa yönetimi için StackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # UI bileşenlerini oluştur
        self._create_menu_bar()
        self._create_status_bar()
        self._create_pages()
        
        # İlk sayfayı göster
        self.stacked_widget.setCurrentIndex(0)
    
    def _apply_dark_theme(self):
        """Modern Dark Mode Teması Uygula 🎨"""
        dark_stylesheet = """
        /* Ana Pencere ve Genel Stil */
        QMainWindow, QWidget {
            background-color: #1e1e1e;
            color: #e0e0e0;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        
        /* Menü Çubuğu */
        QMenuBar {
            background-color: #2d2d2d;
            color: #ffffff;
            border-bottom: 1px solid #3d3d3d;
            padding: 4px;
        }
        
        QMenuBar::item {
            background-color: transparent;
            padding: 6px 12px;
            margin: 2px;
            border-radius: 4px;
        }
        
        QMenuBar::item:selected {
            background-color: #404040;
        }
        
        QMenuBar::item:pressed {
            background-color: #4CAF50;
        }
        
        /* Menü Dropdown */
        QMenu {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #3d3d3d;
            border-radius: 6px;
            padding: 6px;
        }
        
        QMenu::item {
            padding: 8px 24px 8px 12px;
            border-radius: 4px;
            margin: 2px;
        }
        
        QMenu::item:selected {
            background-color: #4CAF50;
            color: #ffffff;
        }
        
        QMenu::separator {
            height: 1px;
            background-color: #3d3d3d;
            margin: 6px 12px;
        }
        
        /* Butonlar */
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #66BB6A;
        }
        
        QPushButton:pressed {
            background-color: #388E3C;
        }
        
        QPushButton:disabled {
            background-color: #3d3d3d;
            color: #808080;
        }
        
        /* Label'lar */
        QLabel {
            color: #e0e0e0;
            background-color: transparent;
        }
        
        /* GroupBox */
        QGroupBox {
            background-color: #252525;
            border: 2px solid #3d3d3d;
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 16px;
            font-weight: bold;
            color: #ffffff;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 4px 12px;
            background-color: #2d2d2d;
            border-radius: 4px;
            color: #4CAF50;
        }
        
        /* TextEdit ve LineEdit */
        QTextEdit, QLineEdit {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 2px solid #3d3d3d;
            border-radius: 6px;
            padding: 8px;
            selection-background-color: #4CAF50;
            selection-color: #ffffff;
        }
        
        QTextEdit:focus, QLineEdit:focus {
            border: 2px solid #4CAF50;
        }
        
        /* ComboBox */
        QComboBox {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 2px solid #3d3d3d;
            border-radius: 6px;
            padding: 6px 12px;
            min-height: 24px;
        }
        
        QComboBox:hover {
            border: 2px solid #4CAF50;
        }
        
        QComboBox::drop-down {
            border: none;
            width: 30px;
        }
        
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 6px solid #e0e0e0;
            margin-right: 8px;
        }
        
        QComboBox QAbstractItemView {
            background-color: #2d2d2d;
            color: #ffffff;
            selection-background-color: #4CAF50;
            border: 1px solid #3d3d3d;
            border-radius: 6px;
        }
        
        /* Scrollbar */
        QScrollBar:vertical {
            background-color: #252525;
            width: 12px;
            border-radius: 6px;
        }
        
        QScrollBar::handle:vertical {
            background-color: #4d4d4d;
            border-radius: 6px;
            min-height: 30px;
        }
        
        QScrollBar::handle:vertical:hover {
            background-color: #5d5d5d;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
        
        QScrollBar:horizontal {
            background-color: #252525;
            height: 12px;
            border-radius: 6px;
        }
        
        QScrollBar::handle:horizontal {
            background-color: #4d4d4d;
            border-radius: 6px;
            min-width: 30px;
        }
        
        QScrollBar::handle:horizontal:hover {
            background-color: #5d5d5d;
        }
        
        /* Status Bar */
        QStatusBar {
            background-color: #2d2d2d;
            color: #e0e0e0;
            border-top: 1px solid #3d3d3d;
        }
        
        /* Tooltips */
        QToolTip {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #4CAF50;
            border-radius: 4px;
            padding: 6px;
        }
        """
        
        self.setStyleSheet(dark_stylesheet)
    
    def _create_menu_bar(self):
        """Menü çubuğunu oluştur"""
        menubar = self.menuBar()
        
        # Dosya Menüsü
        file_menu = menubar.addMenu("&Dosya")
        
        # Excel Yükle
        load_excel_action = QAction("Excel Yükle...", self)
        load_excel_action.setShortcut("Ctrl+O")
        load_excel_action.setStatusTip("Excel dosyası yükle")
        load_excel_action.triggered.connect(self._load_excel)
        file_menu.addAction(load_excel_action)
        
        file_menu.addSeparator()
        
        # Çıkış
        exit_action = QAction("Çıkış", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Uygulamadan çık")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Görünüm Menüsü
        view_menu = menubar.addMenu("&Görünüm")
        
        # Ana Sayfa
        home_action = QAction("Ana Sayfa", self)
        home_action.setShortcut("Ctrl+H")
        home_action.setStatusTip("Ana sayfaya dön")
        home_action.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        view_menu.addAction(home_action)
        
        # Hatalı İşler
        hatali_action = QAction("Hatalı İşler", self)
        hatali_action.setShortcut("Ctrl+1")
        hatali_action.setStatusTip("Hatalı işler sayfası")
        hatali_action.triggered.connect(lambda: self._show_message("Hatalı İşler sayfası henüz hazır değil"))
        view_menu.addAction(hatali_action)
        
        # Uzun İşler
        uzun_action = QAction("Uzun İşler", self)
        uzun_action.setShortcut("Ctrl+2")
        uzun_action.setStatusTip("Uzun işler sayfası")
        uzun_action.triggered.connect(lambda: self._show_message("Uzun İşler sayfası henüz hazır değil"))
        view_menu.addAction(uzun_action)
        
        # Yardım Menüsü
        help_menu = menubar.addMenu("&Yardım")
        
        # Hakkında
        about_action = QAction("Hakkında", self)
        about_action.setStatusTip("Uygulama hakkında bilgi")
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
    
    def _create_status_bar(self):
        """Durum çubuğunu oluştur"""
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Hazır")
    
    def _create_pages(self):
        """Sayfaları oluştur"""
        # Ana Sayfa (Hoş geldiniz ekranı)
        home_page = self._create_home_page()
        self.stacked_widget.addWidget(home_page)  # Index 0
        
        # Arama Sayfası
        self.search_page = SearchPage()
        self.stacked_widget.addWidget(self.search_page)  # Index 1
        
        # Diğer sayfalar gelecekte eklenecek
        # self.stacked_widget.addWidget(hatali_isler_page)  # Index 2
        # self.stacked_widget.addWidget(uzun_isler_page)  # Index 3
    
    def _create_home_page(self):
        """Ana sayfa (hoş geldiniz ekranı) oluştur"""
        page = QWidget()
        layout = QVBoxLayout()
        
        # Başlık
        title = QLabel("Excel Veri Görüntüleme Uygulaması")
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Versiyon
        version = QLabel("Versiyon 0.3 - PyQt5 Arayüz")
        version_font = QFont()
        version_font.setPointSize(12)
        version.setFont(version_font)
        version.setAlignment(Qt.AlignCenter)
        layout.addWidget(version)
        
        # Boşluk
        layout.addStretch(1)
        
        # Bilgi
        info = QLabel("Hoş geldiniz!\n\nBu uygulama Excel verilerini görüntülemek için geliştirilmiştir.\n\n"
                     "📊 Hatalı İşler Analizi\n"
                     "⏱️ Uzun Süren İşler Takibi\n"
                     "🔍 Gelişmiş Arama ve Filtreleme")
        info_font = QFont()
        info_font.setPointSize(11)
        info.setFont(info_font)
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        layout.addStretch(1)
        
        # Başla butonu
        start_btn = QPushButton("Başla")
        start_btn.setMinimumSize(200, 50)
        start_btn_font = QFont()
        start_btn_font.setPointSize(14)
        start_btn.setFont(start_btn_font)
        start_btn.clicked.connect(self._go_to_search_page)
        
        # Butonu ortala
        button_layout = QVBoxLayout()
        button_layout.addWidget(start_btn, alignment=Qt.AlignCenter)
        layout.addLayout(button_layout)
        
        layout.addStretch(2)
        
        # Durum bilgisi
        status = QLabel("✅ ExcelReader hazır | ✅ 142 satır test edildi | ✅ 5 sheet desteği")
        status_font = QFont()
        status_font.setPointSize(9)
        status.setFont(status_font)
        status.setAlignment(Qt.AlignCenter)
        status.setStyleSheet("color: green;")
        layout.addWidget(status)
        
        page.setLayout(layout)
        return page
    
    def _go_to_search_page(self):
        """Arama sayfasına geç"""
        self.stacked_widget.setCurrentIndex(1)  # SearchPage index'i
        self.statusBar.showMessage("Arama sayfası açıldı")
    
    def _load_excel(self):
        """Excel dosyası yükleme (gelecekte implement edilecek)"""
        self._show_message("Excel yükleme özelliği henüz hazır değil.\n\n"
                          "ExcelReader sınıfı hazır, arayüz entegrasyonu devam ediyor.")
        self.statusBar.showMessage("Excel yükleme bekleniyor...")
    
    def _show_about(self):
        """Hakkında dialogunu göster"""
        about_text = """
        <h2>Excel Veri Görüntüleme Uygulaması</h2>
        <p><b>Versiyon:</b> 0.3.0</p>
        <p><b>Tarih:</b> 2026-03-03</p>
        
        <h3>Özellikler:</h3>
        <ul>
            <li>✅ Excel dosya okuma (openpyxl)</li>
            <li>✅ Multi-sheet desteği</li>
            <li>✅ Hatalı İşler analizi</li>
            <li>✅ Uzun İşler takibi</li>
            <li>⏳ Gelişmiş arama (geliştirme aşamasında)</li>
            <li>⏳ Filtreleme (geliştirme aşamasında)</li>
        </ul>
        
        <h3>Teknolojiler:</h3>
        <ul>
            <li>Python 3.13.5</li>
            <li>PyQt5 5.15.11</li>
            <li>pandas 2.3.1</li>
            <li>openpyxl 3.1.5</li>
        </ul>
        
        <p><b>Durum:</b> FAZE 3 - Ana Pencere Tamamlandı</p>
        <p><b>Test Edilen Veri:</b> 142 satır (5 sheet)</p>
        """
        
        QMessageBox.about(self, "Hakkında", about_text)
    
    def _show_message(self, message):
        """Bilgi mesajı göster"""
        QMessageBox.information(self, "Bilgi", message)
        self.statusBar.showMessage(message.split('\n')[0], 3000)  # 3 saniye göster


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())