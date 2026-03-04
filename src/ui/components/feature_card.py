"""
Feature Card - Glassmorphism Özellik Kartı
Ana sayfada kullanılacak modern kartlar
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QFont


class FeatureCard(QFrame):
    """Glassmorphism efektli özellik kartı"""
    
    clicked = pyqtSignal()
    
    def __init__(self, icon, title, subtitle, count, parent=None):
        """
        Feature Card oluştur
        
        Args:
            icon: Emoji veya icon
            title: Kart başlığı
            subtitle: Alt başlık
            count: İstatistik sayısı
        """
        super().__init__(parent)
        
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.count = count
        
        self._setup_ui()
        self._setup_animations()
    
    def _setup_ui(self):
        """UI bileşenlerini oluştur"""
        # Ana layout
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)
        
        # Icon
        icon_label = QLabel(self.icon)
        icon_font = QFont()
        icon_font.setPointSize(48)
        icon_label.setFont(icon_font)
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)
        
        # Title
        title_label = QLabel(self.title)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white;")
        layout.addWidget(title_label)
        
        # Subtitle
        subtitle_label = QLabel(self.subtitle)
        subtitle_font = QFont()
        subtitle_font.setPointSize(11)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: rgba(255, 255, 255, 0.8);")
        layout.addWidget(subtitle_label)
        
        # Count (İstatistik)
        count_label = QLabel(f"{self.count} Kayıt")
        count_font = QFont()
        count_font.setPointSize(16)
        count_font.setBold(True)
        count_label.setFont(count_font)
        count_label.setAlignment(Qt.AlignCenter)
        count_label.setStyleSheet("color: #4CAF50;")
        layout.addWidget(count_label)
        
        # Spacer
        layout.addStretch()
        
        # Button
        btn = QPushButton("Görüntüle →")
        btn.setMinimumHeight(40)
        btn.clicked.connect(self.clicked.emit)
        layout.addWidget(btn)
        
        self.setLayout(layout)
        
        # Card styling - Glassmorphism
        self.setStyleSheet("""
            FeatureCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.08),
                    stop:1 rgba(255, 255, 255, 0.05));
                border: 2px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
            }
            FeatureCard:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(255, 255, 255, 0.12),
                    stop:1 rgba(255, 255, 255, 0.08));
                border: 2px solid rgba(255, 255, 255, 0.2);
            }
        """)
        
        # Sabit boyut
        self.setMinimumSize(280, 380)
        self.setMaximumSize(320, 420)
        
        # Mouse tracking
        self.setMouseTracking(True)
    
    def _setup_animations(self):
        """Hover animasyonlarını ayarla"""
        # Yükselme animasyonu
        self.lift_animation = QPropertyAnimation(self, b"pos")
        self.lift_animation.setDuration(200)
        self.lift_animation.setEasingCurve(QEasingCurve.OutCubic)
    
    def enterEvent(self, event):
        """Mouse kartın üzerine geldiğinde"""
        # Yukarı hareket efekti
        current_pos = self.pos()
        self.lift_animation.setStartValue(current_pos)
        self.lift_animation.setEndValue(QPoint(current_pos.x(), current_pos.y() - 5))
        self.lift_animation.start()
        
        # Cursor değiştir
        self.setCursor(Qt.PointingHandCursor)
        
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """Mouse karttan ayrıldığında"""
        # Aşağı hareket efekti
        current_pos = self.pos()
        self.lift_animation.setStartValue(current_pos)
        self.lift_animation.setEndValue(QPoint(current_pos.x(), current_pos.y() + 5))
        self.lift_animation.start()
        
        # Cursor geri al
        self.unsetCursor()
        
        super().leaveEvent(event)
    
    def mousePressEvent(self, event):
        """Karta tıklandığında"""
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)