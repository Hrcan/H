"""
Base Theme - Temel Tema Sınıfı
Tüm temalar bu sınıftan türetilir
"""


class BaseTheme:
    """Temel tema sınıfı - Tüm temaların parent class'ı"""
    
    def __init__(self):
        """Tema özelliklerini tanımla"""
        self.name = "Base Theme"
        self.colors = self._define_colors()
        self.stylesheet = self._generate_stylesheet()
    
    def _define_colors(self):
        """Renk paletini tanımla (override edilecek)"""
        return {
            # Ana renkler
            'primary_start': '#667eea',
            'primary_end': '#764ba2',
            'accent': '#ff6bff',
            
            # Background
            'bg_dark': '#1e1e1e',
            'bg_medium': '#2d2d2d',
            'bg_light': '#3d3d3d',
            
            # Text
            'text_primary': '#e0e0e0',
            'text_secondary': '#b0b0b0',
            'text_disabled': '#808080',
            
            # States
            'success': '#4CAF50',
            'warning': '#FF9800',
            'error': '#F44336',
            'info': '#2196F3',
            
            # Border & Shadow
            'border': '#3d3d3d',
            'shadow': 'rgba(0, 0, 0, 0.5)',
        }
    
    def _generate_stylesheet(self):
        """QSS stylesheet oluştur"""
        c = self.colors
        
        return f"""
        /* ========================================
           GENEL YAPILAR
           ======================================== */
        
        QMainWindow, QWidget {{
            background-color: {c['bg_dark']};
            color: {c['text_primary']};
            font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
            font-size: 14px;
        }}
        
        /* ========================================
           MENÜ ÇUBUĞU
           ======================================== */
        
        QMenuBar {{
            background-color: {c['bg_medium']};
            color: {c['text_primary']};
            border-bottom: 2px solid {c['primary_start']};
            padding: 6px;
        }}
        
        QMenuBar::item {{
            background-color: transparent;
            padding: 8px 16px;
            margin: 2px;
            border-radius: 6px;
        }}
        
        QMenuBar::item:selected {{
            background-color: {c['bg_light']};
        }}
        
        QMenuBar::item:pressed {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            color: white;
        }}
        
        /* ========================================
           MENÜ DROPDOWN
           ======================================== */
        
        QMenu {{
            background-color: {c['bg_medium']};
            color: {c['text_primary']};
            border: 2px solid {c['border']};
            border-radius: 8px;
            padding: 8px;
        }}
        
        QMenu::item {{
            padding: 10px 30px 10px 16px;
            border-radius: 6px;
            margin: 2px;
        }}
        
        QMenu::item:selected {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            color: white;
        }}
        
        QMenu::separator {{
            height: 2px;
            background-color: {c['border']};
            margin: 8px 16px;
        }}
        
        /* ========================================
           BUTONLAR
           ======================================== */
        
        QPushButton {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            color: white;
            border: none;
            padding: 12px 28px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            min-height: 20px;
        }}
        
        QPushButton:hover {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_end']}, stop:1 {c['primary_start']});
            transform: scale(1.02);
        }}
        
        QPushButton:pressed {{
            background-color: {c['bg_light']};
            padding-top: 14px;
        }}
        
        QPushButton:disabled {{
            background-color: {c['bg_light']};
            color: {c['text_disabled']};
        }}
        
        /* ========================================
           INPUT ALANLARI
           ======================================== */
        
        QLineEdit, QTextEdit {{
            background-color: {c['bg_medium']};
            color: {c['text_primary']};
            border: 2px solid {c['border']};
            border-radius: 8px;
            padding: 10px 14px;
            selection-background-color: {c['primary_start']};
            selection-color: white;
        }}
        
        QLineEdit:focus, QTextEdit:focus {{
            border: 2px solid {c['primary_start']};
            box-shadow: 0 0 10px {c['primary_start']};
        }}
        
        /* ========================================
           COMBOBOX
           ======================================== */
        
        QComboBox {{
            background-color: {c['bg_medium']};
            color: {c['text_primary']};
            border: 2px solid {c['border']};
            border-radius: 8px;
            padding: 8px 14px;
            min-height: 30px;
        }}
        
        QComboBox:hover {{
            border: 2px solid {c['primary_start']};
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 35px;
        }}
        
        QComboBox::down-arrow {{
            image: none;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 8px solid {c['text_primary']};
            margin-right: 10px;
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {c['bg_medium']};
            color: {c['text_primary']};
            selection-background-color: {c['primary_start']};
            border: 2px solid {c['border']};
            border-radius: 8px;
            padding: 4px;
        }}
        
        /* ========================================
           GROUPBOX
           ======================================== */
        
        QGroupBox {{
            background-color: {c['bg_dark']};
            border: 2px solid {c['border']};
            border-radius: 12px;
            margin-top: 16px;
            padding-top: 20px;
            font-weight: 600;
            font-size: 13px;
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 6px 16px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            border-radius: 6px;
            color: white;
            font-weight: 700;
            margin-left: 12px;
        }}
        
        /* ========================================
           TABLO
           ======================================== */
        
        QTableWidget {{
            background-color: {c['bg_dark']};
            alternate-background-color: {c['bg_medium']};
            color: {c['text_primary']};
            gridline-color: {c['border']};
            border: 2px solid {c['border']};
            border-radius: 10px;
            font-size: 13px;
        }}
        
        QTableWidget::item {{
            padding: 12px 10px;
            border: none;
        }}
        
        QTableWidget::item:selected {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            color: white;
        }}
        
        QTableWidget::item:hover {{
            background-color: {c['bg_light']};
        }}
        
        QHeaderView::section {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            color: white;
            font-weight: 700;
            font-size: 12px;
            padding: 14px;
            border: none;
            border-right: 1px solid rgba(255, 255, 255, 0.2);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        QHeaderView::section:first {{
            border-top-left-radius: 10px;
        }}
        
        QHeaderView::section:last {{
            border-top-right-radius: 10px;
            border-right: none;
        }}
        
        QHeaderView::section:hover {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_end']}, stop:1 {c['accent']});
        }}
        
        /* ========================================
           SCROLLBAR
           ======================================== */
        
        QScrollBar:vertical {{
            background-color: {c['bg_dark']};
            width: 14px;
            border-radius: 7px;
            margin: 0px;
        }}
        
        QScrollBar::handle:vertical {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            border-radius: 7px;
            min-height: 30px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background: {c['accent']};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        
        QScrollBar:horizontal {{
            background-color: {c['bg_dark']};
            height: 14px;
            border-radius: 7px;
        }}
        
        QScrollBar::handle:horizontal {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {c['primary_start']}, stop:1 {c['primary_end']});
            border-radius: 7px;
            min-width: 30px;
        }}
        
        /* ========================================
           STATUS BAR
           ======================================== */
        
        QStatusBar {{
            background-color: {c['bg_medium']};
            color: {c['text_primary']};
            border-top: 2px solid {c['primary_start']};
            padding: 6px;
        }}
        
        /* ========================================
           LABEL
           ======================================== */
        
        QLabel {{
            color: {c['text_primary']};
            background-color: transparent;
        }}
        
        /* ========================================
           TOOLTIP
           ======================================== */
        
        QToolTip {{
            background-color: {c['bg_medium']};
            color: white;
            border: 2px solid {c['primary_start']};
            border-radius: 6px;
            padding: 8px;
            font-size: 12px;
        }}
        """
    
    def get_stylesheet(self):
        """Stylesheet'i döndür"""
        return self.stylesheet
    
    def get_colors(self):
        """Renk paletini döndür"""
        return self.colors
    
    def get_gradient(self):
        """Gradient renklerini döndür"""
        return {
            'start': self.colors['primary_start'],
            'end': self.colors['primary_end']
        }