"""
Log Görüntüleme Sayfası
Uygulama loglarını görüntüleme, filtreleme ve arama

Özellikler:
- Log dosyalarını listeleme
- Log seviyesine göre filtreleme
- Metin araması
- Otomatik yenileme
- Log temizleme
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                              QTextEdit, QComboBox, QPushButton, QLineEdit,
                              QGroupBox, QCheckBox, QMessageBox, QSpinBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QTextCharFormat, QTextCursor
import sys
import os

# Logger'ı import et
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.logger import get_app_logger


class LogPage(QWidget):
    """Log Görüntüleme Sayfası widget'ı"""
    
    def __init__(self):
        """LogPage'i başlat"""
        super().__init__()
        
        # AppLogger instance
        self.app_logger = get_app_logger()
        self.logger = self.app_logger.get_logger()
        
        # Auto-refresh timer
        self.refresh_timer = None
        
        # Layout oluştur
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Başlık
        title = QLabel("📋 Log Görüntüleme")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Kontrol paneli
        control_panel = self._create_control_panel()
        main_layout.addWidget(control_panel)
        
        # Log metin alanı
        log_group = self._create_log_section()
        main_layout.addWidget(log_group)
        
        # İstatistik label
        self.stats_label = QLabel("Loglar bekleniyor...")
        self.stats_label.setAlignment(Qt.AlignCenter)
        stats_font = QFont()
        stats_font.setPointSize(10)
        self.stats_label.setFont(stats_font)
        self.stats_label.setStyleSheet("color: #888; padding: 5px;")
        main_layout.addWidget(self.stats_label)
        
        self.setLayout(main_layout)
        
        # İlk yükleme
        self._load_logs()
    
    def _create_control_panel(self):
        """Kontrol panelini oluştur"""
        group = QGroupBox("⚙️ Kontroller")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # İlk satır: Seviye ve satır sayısı
        first_row = QHBoxLayout()
        
        # Log seviyesi filtresi
        level_label = QLabel("Seviye:")
        level_label.setFixedWidth(80)
        level_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.level_filter = QComboBox()
        self.level_filter.addItems(["Tümü", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
        self.level_filter.setMinimumHeight(35)
        self.level_filter.currentTextChanged.connect(self._apply_filters)
        
        first_row.addWidget(level_label)
        first_row.addWidget(self.level_filter)
        
        # Satır sayısı
        lines_label = QLabel("Satır:")
        lines_label.setFixedWidth(60)
        lines_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lines_spin = QSpinBox()
        self.lines_spin.setRange(10, 1000)
        self.lines_spin.setValue(100)
        self.lines_spin.setSuffix(" satır")
        self.lines_spin.setMinimumHeight(35)
        self.lines_spin.valueChanged.connect(self._load_logs)
        
        first_row.addWidget(lines_label)
        first_row.addWidget(self.lines_spin)
        first_row.addStretch()
        
        layout.addLayout(first_row)
        
        # İkinci satır: Arama
        second_row = QHBoxLayout()
        
        search_label = QLabel("Ara:")
        search_label.setFixedWidth(80)
        search_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Log içinde ara...")
        self.search_input.setMinimumHeight(35)
        self.search_input.textChanged.connect(self._apply_filters)
        
        second_row.addWidget(search_label)
        second_row.addWidget(self.search_input)
        
        layout.addLayout(second_row)
        
        # Üçüncü satır: Butonlar
        third_row = QHBoxLayout()
        
        # Yenile butonu
        self.refresh_btn = QPushButton("🔄 Yenile")
        self.refresh_btn.setMinimumHeight(35)
        self.refresh_btn.clicked.connect(self._load_logs)
        
        # Otomatik yenileme checkbox
        self.auto_refresh_check = QCheckBox("Otomatik Yenileme (5sn)")
        self.auto_refresh_check.stateChanged.connect(self._toggle_auto_refresh)
        
        # Temizle butonu
        self.clear_btn = QPushButton("🗑️ Logları Temizle")
        self.clear_btn.setMinimumHeight(35)
        self.clear_btn.clicked.connect(self._clear_logs)
        
        third_row.addWidget(self.refresh_btn)
        third_row.addWidget(self.auto_refresh_check)
        third_row.addStretch()
        third_row.addWidget(self.clear_btn)
        
        layout.addLayout(third_row)
        
        group.setLayout(layout)
        return group
    
    def _create_log_section(self):
        """Log metin alanını oluştur"""
        group = QGroupBox("📄 Log Kayıtları")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        
        # Log text edit
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMinimumHeight(400)
        
        # Monospace font
        log_font = QFont("Consolas", 9)
        self.log_text.setFont(log_font)
        
        # Dark theme style
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        
        layout.addWidget(self.log_text)
        
        group.setLayout(layout)
        return group
    
    def _load_logs(self):
        """Log dosyasını yükle"""
        try:
            # Son N satırı oku
            lines = self.lines_spin.value()
            log_lines = self.app_logger.read_log_file(lines=lines)
            
            if not log_lines:
                self.log_text.setPlainText("Henüz log kaydı yok.")
                self.stats_label.setText("⚠️ Log dosyası bulunamadı")
                self.stats_label.setStyleSheet("color: orange; padding: 5px;")
                return
            
            # Ham logları sakla
            self.raw_logs = log_lines
            
            # Filtreleri uygula
            self._apply_filters()
            
            # İstatistik güncelle
            log_files = self.app_logger.get_log_files()
            log_file = log_files[0] if log_files else None
            
            self.stats_label.setText(
                f"✅ {len(log_lines)} satır yüklendi | "
                f"Dosya: {log_file.name if log_file else 'N/A'}"
            )
            self.stats_label.setStyleSheet("color: #4CAF50; padding: 5px;")
            
            # Log spam önleme: Artık logger kullanmıyor (sessiz yükleme)
            # self.logger.debug(f"Loglar yüklendi: {len(log_lines)} satır")
            
        except Exception as e:
            error_msg = f"Log yükleme hatası: {e}"
            self.logger.error(error_msg)
            QMessageBox.critical(self, "Hata", error_msg)
    
    def _apply_filters(self):
        """Filtreleri uygula"""
        if not hasattr(self, 'raw_logs'):
            return
        
        # Filtrelenmiş loglar
        filtered_logs = self.raw_logs.copy()
        
        # Seviye filtresi
        level = self.level_filter.currentText()
        if level != "Tümü":
            filtered_logs = [
                line for line in filtered_logs
                if level in line
            ]
        
        # Arama filtresi
        search_text = self.search_input.text().strip()
        if search_text:
            filtered_logs = [
                line for line in filtered_logs
                if search_text.lower() in line.lower()
            ]
        
        # Metni güncelle
        self.log_text.clear()
        
        for line in filtered_logs:
            # Renklendirme
            if "DEBUG" in line:
                self._append_colored_text(line, QColor("#00BFFF"))  # Cyan
            elif "INFO" in line:
                self._append_colored_text(line, QColor("#32CD32"))  # Green
            elif "WARNING" in line:
                self._append_colored_text(line, QColor("#FFD700"))  # Yellow
            elif "ERROR" in line:
                self._append_colored_text(line, QColor("#FF6347"))  # Red
            elif "CRITICAL" in line:
                self._append_colored_text(line, QColor("#FF1493"))  # Magenta
            else:
                self._append_colored_text(line, QColor("#e0e0e0"))  # Default
        
        # İstatistik
        if len(filtered_logs) == 0:
            self.stats_label.setText("❌ Filtrelere uygun log bulunamadı")
            self.stats_label.setStyleSheet("color: #FF5722; padding: 5px;")
        elif len(filtered_logs) < len(self.raw_logs):
            self.stats_label.setText(
                f"🔍 {len(filtered_logs)} / {len(self.raw_logs)} log gösteriliyor"
            )
            self.stats_label.setStyleSheet("color: #2196F3; padding: 5px;")
    
    def _append_colored_text(self, text, color):
        """Renkli metin ekle"""
        cursor = self.log_text.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        # Format oluştur
        fmt = QTextCharFormat()
        fmt.setForeground(color)
        
        # Metni ekle
        cursor.insertText(text, fmt)
        self.log_text.setTextCursor(cursor)
    
    def _toggle_auto_refresh(self, state):
        """Otomatik yenilemeyi aç/kapat"""
        if state == Qt.Checked:
            # Timer başlat (5 saniyede bir)
            self.refresh_timer = QTimer()
            self.refresh_timer.timeout.connect(self._load_logs)
            self.refresh_timer.start(5000)  # 5000 ms = 5 sn
            self.logger.info("Otomatik yenileme etkinleştirildi (5 saniye)")
        else:
            # Timer durdur
            if self.refresh_timer:
                self.refresh_timer.stop()
                self.refresh_timer = None
            self.logger.info("Otomatik yenileme devre dışı bırakıldı")
    
    def _clear_logs(self):
        """Eski logları temizle"""
        reply = QMessageBox.question(
            self,
            "Log Temizleme",
            "30 günden eski logları temizlemek istiyor musunuz?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                self.app_logger.clear_old_logs(days=30)
                self.logger.info("Eski loglar temizlendi")
                QMessageBox.information(
                    self,
                    "Başarılı",
                    "Eski loglar başarıyla temizlendi!"
                )
                self._load_logs()
            except Exception as e:
                error_msg = f"Log temizleme hatası: {e}"
                self.logger.error(error_msg)
                QMessageBox.critical(self, "Hata", error_msg)


# Test kodu
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    page = LogPage()
    page.setWindowTitle("Log Görüntüleme - Test")
    page.resize(1000, 700)
    page.show()
    sys.exit(app.exec_())