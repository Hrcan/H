"""
Main Window - Ana Pencere
PyQt5 ile oluşturulmuş ana uygulama penceresi

Özellikler:
- Menü sistemi (Dosya, Görünüm, Yardım)
- Durum çubuğu
- Merkezi widget (sayfa geçişleri için)
"""

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                              QMenuBar, QMenu, QAction, QStatusBar,
                              QLabel, QPushButton, QMessageBox, QStackedWidget,
                              QFileDialog, QFrame)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon
import sys
import os

# UI modüllerini import et
from .search_page import SearchPage
from .hatali_isler_page import HataliIslerPage
from .uzun_isler_page import UzunIslerPage
from .log_page import LogPage
from .data_manager_page import DataManagerPage
from .components.feature_card import FeatureCard
from .themes.theme_manager import ThemeManager


class MainWindow(QMainWindow):
    """Ana uygulama penceresi"""
    
    def __init__(self):
        """MainWindow'u başlat"""
        super().__init__()
        
        # Theme Manager
        self.theme_manager = ThemeManager()
        
        # Pencere özellikleri
        self.setWindowTitle("Excel Veri Görüntüleme Uygulaması v2.5.0 - Modern Design")
        self.setGeometry(100, 100, 1280, 850)  # x, y, genişlik, yükseklik
        self.setMinimumSize(QSize(1100, 700))
        
        # MODERN THEME UYGULA! 🎨
        self._apply_theme()
        
        # Sayfa yönetimi için StackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # UI bileşenlerini oluştur
        self._create_menu_bar()
        self._create_status_bar()
        self._create_pages()
        
        # İlk sayfayı göster
        self.stacked_widget.setCurrentIndex(0)
    
    def _apply_theme(self, theme_name=None):
        """Modern Tema Uygula 🎨"""
        # Theme Manager'dan stylesheet al
        stylesheet = self.theme_manager.get_stylesheet(theme_name)
        self.setStyleSheet(stylesheet)
    
    def _apply_dark_theme_OLD(self):
        """ESKİ Modern Dark Mode Teması - KULLANILMIYOR"""
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
        # Bu fonksiyon artık kullanılmıyor - theme_manager kullanılıyor
        pass
    
    def _create_menu_bar(self):
        """Menü çubuğunu oluştur"""
        menubar = self.menuBar()
        
        # Dosya Menüsü
        file_menu = menubar.addMenu("&Dosya")
        
        # Excel Yükle (AKTİF - v2.1.4)
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
        
        # Hatalı İşler (YENİ! v1.0 - AKTİF)
        hatali_action = QAction("Hatalı İşler Detay", self)
        hatali_action.setShortcut("Ctrl+1")
        hatali_action.setStatusTip("Hatalı işler detay sayfası")
        hatali_action.triggered.connect(self._go_to_hatali_isler_page)
        view_menu.addAction(hatali_action)
        
        # Uzun İşler (YENİ! v2.0 - AKTİF!)
        uzun_action = QAction("Uzun İşler Detay", self)
        uzun_action.setShortcut("Ctrl+2")
        uzun_action.setStatusTip("Uzun işler detay sayfası")
        uzun_action.triggered.connect(self._go_to_uzun_isler_page)
        view_menu.addAction(uzun_action)
        
        view_menu.addSeparator()
        
        # Veri Yönetimi (YENİ! v2.4 - AKTİF!) 🆕
        data_manager_action = QAction("Veri Yönetimi", self)
        data_manager_action.setShortcut("Ctrl+D")
        data_manager_action.setStatusTip("Yüklü verileri görüntüle ve yönet")
        data_manager_action.triggered.connect(self._go_to_data_manager_page)
        view_menu.addAction(data_manager_action)
        
        # Log Görüntüleme (YENİ! v1.2)
        log_action = QAction("Log Görüntüleme", self)
        log_action.setShortcut("Ctrl+L")
        log_action.setStatusTip("Uygulama loglarını görüntüle")
        log_action.triggered.connect(self._go_to_log_page)
        view_menu.addAction(log_action)
        
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
        
        # Hatalı İşler Detay Sayfası (YENİ! v1.0)
        self.hatali_isler_page = HataliIslerPage()
        self.stacked_widget.addWidget(self.hatali_isler_page)  # Index 2
        
        # Log Görüntüleme Sayfası (YENİ! v1.2)
        self.log_page = LogPage()
        self.stacked_widget.addWidget(self.log_page)  # Index 3
        
        # Uzun İşler Detay Sayfası (YENİ! v2.0)
        self.uzun_isler_page = UzunIslerPage()
        self.stacked_widget.addWidget(self.uzun_isler_page)  # Index 4
        
        # Veri Yönetimi Sayfası (YENİ! v2.4) 🆕
        self.data_manager_page = DataManagerPage()
        self.stacked_widget.addWidget(self.data_manager_page)  # Index 5
    
    def _create_home_page(self):
        """Ana sayfa (modern card-based) oluştur"""
        page = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setSpacing(30)
        main_layout.setContentsMargins(40, 40, 40, 40)
        
        # Başlık bölümü
        header_layout = QVBoxLayout()
        header_layout.setSpacing(10)
        
        # Ana başlık
        title = QLabel("🎨 EXCEL VERİ GÖRÜNTÜLEYİCİ")
        title_font = QFont('Inter', 32, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white; letter-spacing: -1px;")
        header_layout.addWidget(title)
        
        # Versiyon
        version = QLabel("v2.5.0 Design Refresh - Modern Glassmorphism")
        version_font = QFont('Inter', 13)
        version.setFont(version_font)
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet("color: rgba(255, 255, 255, 0.7); font-weight: 500;")
        header_layout.addWidget(version)
        
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(20)
        
        # Feature Cards - Grid Layout
        cards_layout = QGridLayout()
        cards_layout.setSpacing(25)
        
        # Arama Kartı
        search_card = FeatureCard(
            icon="🔍",
            title="Arama",
            subtitle="Toplu JCL Arama",
            count=142
        )
        search_card.clicked.connect(self._go_to_search_page)
        cards_layout.addWidget(search_card, 0, 0)
        
        # Hatalı İşler Kartı
        hatali_card = FeatureCard(
            icon="❌",
            title="Hatalı İşler",
            subtitle="Detaylı Analiz",
            count=46
        )
        hatali_card.clicked.connect(self._go_to_hatali_isler_page)
        cards_layout.addWidget(hatali_card, 0, 1)
        
        # Uzun İşler Kartı
        uzun_card = FeatureCard(
            icon="⏱️",
            title="Uzun İşler",
            subtitle="Performans Takibi",
            count=96
        )
        uzun_card.clicked.connect(self._go_to_uzun_isler_page)
        cards_layout.addWidget(uzun_card, 0, 2)
        
        main_layout.addLayout(cards_layout)
        main_layout.addSpacing(15)
        
        # Quick Access Buttons
        quick_layout = QVBoxLayout()
        quick_layout.setSpacing(12)
        
        # Log button
        log_btn = self._create_quick_button("📝 Log Sistemi", "CTRL+L")
        log_btn.clicked.connect(self._go_to_log_page)
        quick_layout.addWidget(log_btn)
        
        # Veri Yönetimi button
        data_btn = self._create_quick_button("💾 Veri Yönetimi", "CTRL+D")
        data_btn.clicked.connect(self._go_to_data_manager_page)
        quick_layout.addWidget(data_btn)
        
        main_layout.addLayout(quick_layout)
        
        main_layout.addStretch()
        
        # Footer bilgisi
        footer = QLabel("✨ Modern UI • 🎨 4 Tema • 🚀 Yüksek Performans • 💚 Kullanıcı Dostu")
        footer_font = QFont('Inter', 10)
        footer.setFont(footer_font)
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: rgba(255, 255, 255, 0.5); padding: 20px;")
        main_layout.addWidget(footer)
        
        page.setLayout(main_layout)
        
        # Sayfa arka plan gradient
        page.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a0f2e,
                    stop:1 #0f0a1a);
            }
        """)
        
        return page
    
    def _create_quick_button(self, text, shortcut):
        """Hızlı erişim butonu oluştur"""
        btn = QPushButton(f"{text}          {shortcut}")
        btn.setMinimumHeight(50)
        btn.setMaximumHeight(60)
        btn_font = QFont('Inter', 12, QFont.Medium)
        btn.setFont(btn_font)
        btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.05);
                border: 2px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 12px 24px;
                text-align: left;
                color: rgba(255, 255, 255, 0.9);
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.08);
                border: 2px solid rgba(255, 255, 255, 0.2);
            }
            QPushButton:pressed {
                background: rgba(255, 255, 255, 0.12);
            }
        """)
        return btn
    
    def _go_to_search_page(self):
        """Arama sayfasına geç"""
        self.stacked_widget.setCurrentIndex(1)  # SearchPage index'i
        self.statusBar.showMessage("Arama sayfası açıldı")
    
    def _go_to_hatali_isler_page(self):
        """Hatalı İşler Detay sayfasına geç (YENİ! v1.0)"""
        self.stacked_widget.setCurrentIndex(2)  # HataliIslerPage index'i
        self.statusBar.showMessage("Hatalı İşler Detay sayfası açıldı")
    
    def _go_to_log_page(self):
        """Log sayfasına geç (YENİ! v1.2)"""
        self.stacked_widget.setCurrentIndex(3)  # LogPage index'i
        self.statusBar.showMessage("Log sayfası açıldı")
    
    def _go_to_uzun_isler_page(self):
        """Uzun İşler Detay sayfasına geç (YENİ! v2.0)"""
        self.stacked_widget.setCurrentIndex(4)  # UzunIslerPage index'i
        self.statusBar.showMessage("Uzun İşler Detay sayfası açıldı")
    
    def _go_to_data_manager_page(self):
        """Veri Yönetimi sayfasına geç (YENİ! v2.4) 🆕"""
        self.stacked_widget.setCurrentIndex(5)  # DataManagerPage index'i
        self.statusBar.showMessage("Veri Yönetimi sayfası açıldı")
        # Sayfa her açıldığında yenile
        self.data_manager_page._load_data_info()
    
    def _load_excel(self):
        """Excel dosyası yükleme (toplu yükleme destekli)"""
        # ÇOKLU dosya seçici aç
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Excel Dosyaları Seç (Birden fazla seçilebilir)",
            "data/excel",  # Varsayılan dizin
            "Excel Dosyaları (*.xlsx *.xls);;Tüm Dosyalar (*.*)"
        )
        
        if file_paths:
            # Dosyalar kategorize et
            hatali_files = []
            uzun_files = []
            unknown_files = []
            
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                
                if "Hatalı" in file_name or "HATALI" in file_name.upper():
                    hatali_files.append(file_name)
                elif "Uzun" in file_name or "UZUN" in file_name.upper():
                    uzun_files.append(file_name)
                else:
                    unknown_files.append(file_name)
            
            # Yükleme sonuçları
            loaded = []
            errors = []
            
            # Hatalı İşler dosyalarını yükle
            if hatali_files:
                try:
                    self.hatali_isler_page = HataliIslerPage()
                    self.stacked_widget.removeWidget(self.stacked_widget.widget(2))
                    self.stacked_widget.insertWidget(2, self.hatali_isler_page)
                    loaded.append(f"✅ Hatalı İşler: {len(hatali_files)} dosya")
                except Exception as e:
                    errors.append(f"❌ Hatalı İşler: {str(e)}")
            
            # Uzun İşler dosyalarını yükle
            if uzun_files:
                try:
                    self.uzun_isler_page = UzunIslerPage()
                    self.stacked_widget.removeWidget(self.stacked_widget.widget(4))
                    self.stacked_widget.insertWidget(4, self.uzun_isler_page)
                    loaded.append(f"✅ Uzun İşler: {len(uzun_files)} dosya")
                except Exception as e:
                    errors.append(f"❌ Uzun İşler: {str(e)}")
            
            # Sonuç mesajı
            message_parts = []
            
            if loaded:
                message_parts.append("📦 Yüklenen Excel Dosyaları:\n")
                message_parts.append("\n".join(loaded))
            
            if unknown_files:
                message_parts.append(f"\n\n⚠️ Tanınmayan dosyalar ({len(unknown_files)}):")
                for f in unknown_files[:3]:  # İlk 3'ünü göster
                    message_parts.append(f"  • {f}")
                if len(unknown_files) > 3:
                    message_parts.append(f"  ... ve {len(unknown_files)-3} dosya daha")
            
            if errors:
                message_parts.append("\n\n❌ Hatalar:")
                message_parts.append("\n".join(errors))
            
            # Mesajı göster
            final_message = "\n".join(message_parts)
            if errors:
                QMessageBox.warning(self, "Yükleme Tamamlandı (Hatalarla)", final_message)
            else:
                QMessageBox.information(self, "Yükleme Başarılı", final_message)
            
            # Status bar güncelle
            summary = f"{len(hatali_files)} Hatalı + {len(uzun_files)} Uzun İşler Excel yüklendi"
            if unknown_files:
                summary += f" ({len(unknown_files)} tanınmayan)"
            self.statusBar.showMessage(summary, 5000)
            
        else:
            # Dosya seçilmedi
            self.statusBar.showMessage("Excel yükleme iptal edildi", 3000)
    
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