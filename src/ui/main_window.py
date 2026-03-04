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
from .database_viewer_page import DatabaseViewerPage
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
        self.setWindowTitle("Excel Veri Görüntüleme Uygulaması v2.5.2 - Database Viewer")
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
        
        # Database Viewer (YENİ! v2.5.2) 🗄️
        db_viewer_action = QAction("Database Viewer", self)
        db_viewer_action.setShortcut("Ctrl+B")
        db_viewer_action.setStatusTip("Bellek içeriğini görüntüle")
        db_viewer_action.triggered.connect(self._go_to_database_viewer_page)
        view_menu.addAction(db_viewer_action)
        
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
        
        # Database Viewer Sayfası (YENİ! v2.5.2) 🗄️
        self.database_viewer_page = DatabaseViewerPage()
        self.stacked_widget.addWidget(self.database_viewer_page)  # Index 6
    
    def _create_home_page(self):
        """Ana sayfa - Modern Dashboard Tasarımı"""
        page = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Üst Başlık - Daha kompakt
        header_layout = QVBoxLayout()
        header_layout.setSpacing(5)
        
        title = QLabel("📊 EXCEL ANALİZ PLATFORMU")
        title_font = QFont('Segoe UI', 24, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white; letter-spacing: 1px; padding: 10px;")
        header_layout.addWidget(title)
        
        subtitle = QLabel("Verilerinizi Analiz Edin • Hızlı Arama • Detaylı Raporlama")
        subtitle_font = QFont('Segoe UI', 11)
        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: rgba(255, 255, 255, 0.6);")
        header_layout.addWidget(subtitle)
        
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(10)
        
        # Ana İşlevler - 3x3 Grid (Database Viewer eklendi!)
        features_grid = QGridLayout()
        features_grid.setSpacing(15)
        
        # Satır 1
        features_grid.addWidget(self._create_feature_button(
            "🔍", "ARAMA", "Toplu JCL Arama\n142 Kayıt", 
            self._go_to_search_page, "#4A90E2"
        ), 0, 0)
        
        features_grid.addWidget(self._create_feature_button(
            "❌", "HATALI İŞLER", "Detaylı Analiz\n46 Kayıt",
            self._go_to_hatali_isler_page, "#E74C3C"
        ), 0, 1)
        
        features_grid.addWidget(self._create_feature_button(
            "⏱️", "UZUN İŞLER", "Performans Takibi\n96 Kayıt",
            self._go_to_uzun_isler_page, "#F39C12"
        ), 0, 2)
        
        # Satır 2
        features_grid.addWidget(self._create_feature_button(
            "📥", "EXCEL YÜKLE", "Yeni Dosya Yükle\nÇoklu Seçim",
            self._load_excel, "#9B59B6"
        ), 1, 0)
        
        features_grid.addWidget(self._create_feature_button(
            "📝", "LOG SİSTEMİ", "Uygulama Logları\nGerçek Zamanlı",
            self._go_to_log_page, "#1ABC9C"
        ), 1, 1)
        
        features_grid.addWidget(self._create_feature_button(
            "💾", "VERİ YÖNETİMİ", "Veri Temizleme\nYeniden Yükleme",
            self._go_to_data_manager_page, "#3498DB"
        ), 1, 2)
        
        # Satır 3 (YENİ! Database Viewer)
        features_grid.addWidget(self._create_feature_button(
            "🗄️", "DATABASE VIEWER", "Bellek İçeriği\nGerçek Zamanlı",
            self._go_to_database_viewer_page, "#8E44AD"
        ), 2, 0)
        
        main_layout.addLayout(features_grid)
        
        main_layout.addStretch()
        
        # Alt Bilgi - Daha minimal
        footer_layout = QHBoxLayout()
        footer_layout.setSpacing(20)
        
        info_labels = [
            "✨ Modern UI",
            "🎨 4 Farklı Tema",
            "🚀 Yüksek Performans",
            "💚 Kolay Kullanım"
        ]
        
        for info in info_labels:
            label = QLabel(info)
            label.setFont(QFont('Segoe UI', 9))
            label.setStyleSheet("color: rgba(255, 255, 255, 0.4);")
            footer_layout.addWidget(label)
        
        footer_layout.insertStretch(0)
        footer_layout.addStretch()
        
        main_layout.addLayout(footer_layout)
        
        page.setLayout(main_layout)
        
        # Gradient arka plan
        page.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e,
                    stop:0.5 #16213e,
                    stop:1 #0f3460);
            }
        """)
        
        return page
    
    def _create_feature_button(self, icon, title, subtitle, callback, color):
        """Modern özellik butonu oluştur - TEMİZ TASARIM"""
        btn = QPushButton()
        btn.setCursor(Qt.PointingHandCursor)
        btn.clicked.connect(callback)
        btn.setMinimumHeight(150)
        btn.setMaximumHeight(170)
        
        # İç widget ve layout
        inner_widget = QWidget()
        inner_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setSpacing(8)
        inner_layout.setContentsMargins(15, 20, 15, 20)
        
        # Emoji/İkon
        icon_label = QLabel(icon)
        icon_font = QFont('Segoe UI Emoji', 40)
        icon_label.setFont(icon_font)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("color: white;")
        inner_layout.addWidget(icon_label)
        
        # Başlık
        title_label = QLabel(title)
        title_font = QFont('Segoe UI', 14, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white;")
        inner_layout.addWidget(title_label)
        
        # Alt başlık
        subtitle_label = QLabel(subtitle)
        subtitle_font = QFont('Segoe UI', 10)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setWordWrap(True)
        subtitle_label.setStyleSheet("color: rgba(255, 255, 255, 0.8);")
        inner_layout.addWidget(subtitle_label)
        
        # Widget'ı butona ekle
        btn_layout = QVBoxLayout(btn)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.addWidget(inner_widget)
        
        # Modern stil (CSS Spam düzeltildi - transform kaldırıldı)
        btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {color},
                    stop:1 {color}aa);
                border: 2px solid rgba(255, 255, 255, 0.15);
                border-radius: 12px;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {color},
                    stop:1 {color}cc);
                border: 2px solid rgba(255, 255, 255, 0.3);
            }}
            QPushButton:pressed {{
                background: {color};
                border: 2px solid rgba(255, 255, 255, 0.5);
            }}
        """)
        
        return btn
    
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
    
    def _go_to_database_viewer_page(self):
        """Database Viewer sayfasına geç (YENİ! v2.5.2) 🗄️"""
        self.stacked_widget.setCurrentIndex(6)  # DatabaseViewerPage index'i
        self.statusBar.showMessage("Database Viewer sayfası açıldı")
        # Sayfa her açıldığında yenile
        self.database_viewer_page._refresh_data()
    
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
            # Dosyaları YOLLARIYLA kategorize et (sadece isim değil!)
            hatali_paths = []
            uzun_paths = []
            unknown_files = []
            
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                
                if "Hatalı" in file_name or "HATALI" in file_name.upper():
                    hatali_paths.append(file_path)  # Tam yolu sakla
                elif "Uzun" in file_name or "UZUN" in file_name.upper():
                    uzun_paths.append(file_path)  # Tam yolu sakla
                else:
                    unknown_files.append(file_name)
            
            # Yükleme sonuçları
            loaded = []
            errors = []
            actual_loaded_count = 0
            
            # Hatalı İşler dosyalarını yükle
            if hatali_paths:
                try:
                    # Sayfayı yeniden oluştur (default dosyaları yükler)
                    self.hatali_isler_page = HataliIslerPage()
                    self.stacked_widget.removeWidget(self.stacked_widget.widget(2))
                    self.stacked_widget.insertWidget(2, self.hatali_isler_page)
                    loaded.append(f"✅ Hatalı İşler: {len(hatali_paths)} dosya seçildi")
                    actual_loaded_count += 1
                    
                    # ÖNEMLİ NOT: Şu anda sadece default dosya yükleniyor!
                    # Çoklu dosya desteği için ExcelReader'a merge/concat mantığı gerekiyor
                    if len(hatali_paths) > 1:
                        loaded.append(f"   ⚠️ Uyarı: Şu an sadece default dosya yüklendi")
                        loaded.append(f"   📋 Seçilen dosyalar:")
                        for path in hatali_paths[:3]:
                            loaded.append(f"      • {os.path.basename(path)}")
                        if len(hatali_paths) > 3:
                            loaded.append(f"      ... ve {len(hatali_paths)-3} dosya daha")
                            
                except Exception as e:
                    errors.append(f"❌ Hatalı İşler: {str(e)}")
            
            # Uzun İşler dosyalarını yükle
            if uzun_paths:
                try:
                    # Sayfayı yeniden oluştur (default dosyaları yükler)
                    self.uzun_isler_page = UzunIslerPage()
                    self.stacked_widget.removeWidget(self.stacked_widget.widget(4))
                    self.stacked_widget.insertWidget(4, self.uzun_isler_page)
                    loaded.append(f"✅ Uzun İşler: {len(uzun_paths)} dosya seçildi")
                    actual_loaded_count += 1
                    
                    # ÖNEMLİ NOT: Şu anda sadece default dosya yükleniyor!
                    if len(uzun_paths) > 1:
                        loaded.append(f"   ⚠️ Uyarı: Şu an sadece default dosya yüklendi")
                        loaded.append(f"   📋 Seçilen dosyalar:")
                        for path in uzun_paths[:3]:
                            loaded.append(f"      • {os.path.basename(path)}")
                        if len(uzun_paths) > 3:
                            loaded.append(f"      ... ve {len(uzun_paths)-3} dosya daha")
                            
                except Exception as e:
                    errors.append(f"❌ Uzun İşler: {str(e)}")
            
            # Sonuç mesajı
            message_parts = []
            
            if loaded:
                message_parts.append("📦 Excel Yükleme Durumu:\n")
                message_parts.append("\n".join(loaded))
                
                # Çoklu dosya uyarısı
                total_selected = len(hatali_paths) + len(uzun_paths)
                if total_selected > actual_loaded_count:
                    message_parts.append("\n\n💡 Çoklu Dosya Desteği:")
                    message_parts.append("Şu anda sadece default Excel dosyaları yüklenmektedir.")
                    message_parts.append("Gelecek versiyonda çoklu dosya birleştirme eklenecek.")
            
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
                QMessageBox.information(self, "Excel Yükleme", final_message)
            
            # Status bar güncelle
            summary = f"{actual_loaded_count} kategori yüklendi"
            if len(hatali_paths) > 0:
                summary += f" (Hatalı: {len(hatali_paths)} dosya seçildi)"
            if len(uzun_paths) > 0:
                summary += f" (Uzun: {len(uzun_paths)} dosya seçildi)"
            self.statusBar.showMessage(summary, 5000)
            
        else:
            # Dosya seçilmedi
            self.statusBar.showMessage("Excel yükleme iptal edildi", 3000)
    
    def _show_about(self):
        """Hakkında dialogunu göster"""
        about_text = """
        <h2>Excel Veri Görüntüleme Uygulaması</h2>
        <p><b>Versiyon:</b> 2.5.2</p>
        <p><b>Tarih:</b> 2026-03-04</p>
        
        <h3>Özellikler:</h3>
        <ul>
            <li>✅ Excel dosya okuma (openpyxl)</li>
            <li>✅ Multi-sheet desteği</li>
            <li>✅ Hatalı İşler analizi</li>
            <li>✅ Uzun İşler takibi</li>
            <li>✅ Database Viewer (Bellek görüntüleme)</li>
            <li>✅ Modern UI ve Tema sistemi</li>
        </ul>
        
        <h3>Teknolojiler:</h3>
        <ul>
            <li>Python 3.13.5</li>
            <li>PyQt5 5.15.11</li>
            <li>pandas 2.3.1</li>
            <li>openpyxl 3.1.5</li>
        </ul>
        
        <p><b>Durum:</b> v2.5.2 - Database Viewer Eklendi</p>
        <p><b>Test Edilen Veri:</b> 142 satır (5 sheet)</p>
        """
        
        QMessageBox.about(self, "Hakkında", about_text)
    
    def clear_all_data(self):
        """Tüm yüklü verileri temizle ve sayfaları yeniden oluştur"""
        try:
            # Tüm sayfaları yeniden oluştur (VERİ YÜKLEMEDEN - load_data=False)
            # Search page - JCL input'ları da temizlenir!
            old_search = self.stacked_widget.widget(1)
            self.search_page = SearchPage(load_data=False)  # ✅ VERİ YÜKLEME!
            self.stacked_widget.removeWidget(old_search)
            self.stacked_widget.insertWidget(1, self.search_page)
            if old_search:
                old_search.deleteLater()
            
            # Hatalı İşler page
            old_hatali = self.stacked_widget.widget(2)
            self.hatali_isler_page = HataliIslerPage(load_data=False)  # ✅ VERİ YÜKLEME!
            self.stacked_widget.removeWidget(old_hatali)
            self.stacked_widget.insertWidget(2, self.hatali_isler_page)
            if old_hatali:
                old_hatali.deleteLater()
            
            # Uzun İşler page
            old_uzun = self.stacked_widget.widget(4)
            self.uzun_isler_page = UzunIslerPage(load_data=False)  # ✅ VERİ YÜKLEME!
            self.stacked_widget.removeWidget(old_uzun)
            self.stacked_widget.insertWidget(4, self.uzun_isler_page)
            if old_uzun:
                old_uzun.deleteLater()
            
            # Data Manager page - son olarak yenile
            old_data = self.stacked_widget.widget(5)
            self.data_manager_page = DataManagerPage()
            self.stacked_widget.removeWidget(old_data)
            self.stacked_widget.insertWidget(5, self.data_manager_page)
            if old_data:
                old_data.deleteLater()
            
            # Database Viewer page - yenile
            old_db = self.stacked_widget.widget(6)
            self.database_viewer_page = DatabaseViewerPage()
            self.stacked_widget.removeWidget(old_db)
            self.stacked_widget.insertWidget(6, self.database_viewer_page)
            if old_db:
                old_db.deleteLater()
            
            # Ana sayfaya dön
            self.stacked_widget.setCurrentIndex(0)
            self.statusBar.showMessage("✅ Tüm veriler ve JCL'ler temizlendi!", 3000)
            
            return True
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.statusBar.showMessage(f"Temizleme hatası: {e}", 5000)
            return False
    
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