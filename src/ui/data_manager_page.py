"""
Data Manager Page - Veri Yönetimi Sayfası
Yüklü Excel verilerini görüntüleme ve temizleme

Özellikler:
- Yüklü dosyaların listesi
- Satır sayıları
- Veri temizleme
- Yeniden yükleme
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                              QPushButton, QTableWidget, QTableWidgetItem,
                              QHeaderView, QMessageBox, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from src.core.excel_reader import ExcelReader
from src.core.logger import get_logger
import os

logger = get_logger()


class DataManagerPage(QWidget):
    """Veri yönetimi sayfası"""
    
    def __init__(self):
        """DataManagerPage'i başlat"""
        super().__init__()
        
        # Excel okuyucu
        self.reader = ExcelReader()
        
        # Veri durumu bayrağı (temizlendiyse True)
        self.data_cleared = False
        
        # UI oluştur
        self._create_ui()
        
        # İlk yükleme
        self._load_data_info()
        
        logger.info("Veri Yönetimi sayfası yüklendi")
    
    def _create_ui(self):
        """UI bileşenlerini oluştur"""
        layout = QVBoxLayout()
        
        # Başlık
        title = QLabel("📊 Veri Yönetimi")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #4CAF50; padding: 10px;")
        layout.addWidget(title)
        
        # Özet bilgiler
        summary_group = QGroupBox("📈 Özet Bilgiler")
        summary_layout = QVBoxLayout()
        
        self.summary_label = QLabel("Yükleniyor...")
        self.summary_label.setStyleSheet("font-size: 13px; padding: 10px;")
        summary_layout.addWidget(self.summary_label)
        
        summary_group.setLayout(summary_layout)
        layout.addWidget(summary_group)
        
        # Yüklü dosyalar tablosu
        files_group = QGroupBox("📁 Yüklü Excel Dosyaları")
        files_layout = QVBoxLayout()
        
        # Tablo
        self.files_table = QTableWidget()
        self.files_table.setColumnCount(4)
        self.files_table.setHorizontalHeaderLabels([
            "Dosya Türü", "Dosya Adı", "Satır Sayısı", "Durum"
        ])
        
        # Tablo stilini ayarla
        header = self.files_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        self.files_table.setAlternatingRowColors(True)
        self.files_table.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                gridline-color: #3d3d3d;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 6px;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QTableWidget::item:hover {
                background-color: #333333;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #2196F3, stop:1 #64B5F6);
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
                font-size: 12px;
            }
        """)
        
        files_layout.addWidget(self.files_table)
        files_group.setLayout(files_layout)
        layout.addWidget(files_group)
        
        # Butonlar
        button_layout = QHBoxLayout()
        
        # Yenile butonu
        refresh_btn = QPushButton("🔄 Yenile")
        refresh_btn.clicked.connect(self._load_data_info)
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #42A5F5;
            }
        """)
        button_layout.addWidget(refresh_btn)
        
        button_layout.addStretch()
        
        # Veriyi temizle butonu
        clear_btn = QPushButton("🗑️ Tüm Veriyi Temizle")
        clear_btn.clicked.connect(self._clear_all_data)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
        """)
        button_layout.addWidget(clear_btn)
        
        # Yeniden yükle butonu
        reload_btn = QPushButton("📥 Yeniden Yükle")
        reload_btn.clicked.connect(self._reload_all_data)
        reload_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #66BB6A;
            }
        """)
        button_layout.addWidget(reload_btn)
        
        layout.addLayout(button_layout)
        
        # Ana layout'u ayarla
        self.setLayout(layout)
    
    def _load_data_info(self):
        """Yüklü veri bilgilerini getir"""
        try:
            # Tablo temizle
            self.files_table.setRowCount(0)
            
            total_rows = 0
            file_count = 0
            
            # Hatalı İşler
            hatali_excel = "data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx"
            if os.path.exists(hatali_excel):
                hatali_data = self.reader.read_hatali_isler(hatali_excel)
                if hatali_data is not None and not hatali_data.empty:
                    row = self.files_table.rowCount()
                    self.files_table.insertRow(row)
                    
                    self.files_table.setItem(row, 0, QTableWidgetItem("📋 Hatalı İşler"))
                    self.files_table.setItem(row, 1, QTableWidgetItem(os.path.basename(hatali_excel)))
                    self.files_table.setItem(row, 2, QTableWidgetItem(str(len(hatali_data))))
                    
                    status_item = QTableWidgetItem("✅ Yüklü")
                    status_item.setForeground(Qt.green)
                    self.files_table.setItem(row, 3, status_item)
                    
                    total_rows += len(hatali_data)
                    file_count += 1
            
            # Uzun İşler
            uzun_excel = "data/excel/SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx"
            if os.path.exists(uzun_excel):
                uzun_data = self.reader.read_uzun_isler(uzun_excel)
                if uzun_data is not None and not uzun_data.empty:
                    row = self.files_table.rowCount()
                    self.files_table.insertRow(row)
                    
                    self.files_table.setItem(row, 0, QTableWidgetItem("⏱️ Uzun İşler"))
                    self.files_table.setItem(row, 1, QTableWidgetItem(os.path.basename(uzun_excel)))
                    self.files_table.setItem(row, 2, QTableWidgetItem(str(len(uzun_data))))
                    
                    status_item = QTableWidgetItem("✅ Yüklü")
                    status_item.setForeground(Qt.green)
                    self.files_table.setItem(row, 3, status_item)
                    
                    total_rows += len(uzun_data)
                    file_count += 1
            
            # Diğer Excel dosyalarını kontrol et
            excel_dir = "data/excel"
            if os.path.exists(excel_dir):
                for filename in os.listdir(excel_dir):
                    if filename.endswith(('.xlsx', '.xls')) and filename not in [
                        os.path.basename(hatali_excel),
                        os.path.basename(uzun_excel)
                    ]:
                        row = self.files_table.rowCount()
                        self.files_table.insertRow(row)
                        
                        self.files_table.setItem(row, 0, QTableWidgetItem("📄 Diğer"))
                        self.files_table.setItem(row, 1, QTableWidgetItem(filename))
                        self.files_table.setItem(row, 2, QTableWidgetItem("-"))
                        
                        status_item = QTableWidgetItem("⚠️ Yüklenmedi")
                        status_item.setForeground(Qt.yellow)
                        self.files_table.setItem(row, 3, status_item)
            
            # Özet güncelle
            summary_text = f"""
            <b>Toplam Dosya:</b> {file_count} adet yüklü<br>
            <b>Toplam Satır:</b> {total_rows:,} satır<br>
            <b>Hafıza Durumu:</b> {'✅ Veri yüklü' if total_rows > 0 else '❌ Veri yok'}
            """
            self.summary_label.setText(summary_text)
            
            logger.info(f"Veri yönetimi yenilendi: {file_count} dosya, {total_rows} satır")
            
        except Exception as e:
            logger.error(f"Veri bilgileri yüklenirken hata: {e}", exc_info=True)
            QMessageBox.critical(self, "Hata", f"Veri bilgileri yüklenemedi:\n{str(e)}")
    
    def _clear_all_data(self):
        """Tüm veriyi temizle"""
        # Onay mesajı
        reply = QMessageBox.question(
            self,
            "Onay",
            "⚠️ Tüm yüklü veriler temizlenecek!\n\n"
            "Sayfalar boş kalacak ve yeniden Excel yüklemeniz gerekecek.\n\n"
            "Devam etmek istediğinizden emin misiniz?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                # Ana pencereyi bul ve clear_all_data çağır
                from PyQt5.QtWidgets import QApplication
                main_window = None
                for widget in QApplication.topLevelWidgets():
                    if widget.__class__.__name__ == 'MainWindow':
                        main_window = widget
                        break
                
                if main_window and hasattr(main_window, 'clear_all_data'):
                    # MainWindow'daki global clear metodunu kullan
                    success = main_window.clear_all_data()
                    if success:
                        logger.info("Tüm veriler temizlendi (MainWindow üzerinden)")
                        QMessageBox.information(
                            self,
                            "Başarılı",
                            "✅ Tüm veriler temizlendi!\n\n"
                            "Ana sayfaya yönlendiriliyorsunuz.\n\n"
                            "Yeni Excel dosyaları yüklemek için:\n"
                            "Dosya → Excel Yükle (Ctrl+O)"
                        )
                    else:
                        raise Exception("MainWindow.clear_all_data() false döndü")
                else:
                    # Fallback: Sadece bu sayfanın reader'ını temizle
                    self.reader = ExcelReader()
                    self._load_data_info()
                    logger.warning("MainWindow bulunamadı, sadece local reader temizlendi")
                    QMessageBox.warning(
                        self,
                        "Kısmi Temizlik",
                        "⚠️ Sadece bu sayfanın verileri temizlendi.\n\n"
                        "Diğer sayfaları temizlemek için uygulamayı yeniden başlatın."
                    )
                
            except Exception as e:
                logger.error(f"Veri temizleme hatası: {e}", exc_info=True)
                QMessageBox.critical(self, "Hata", f"Veri temizlenemedi:\n{str(e)}")
    
    def _reload_all_data(self):
        """Tüm veriyi yeniden yükle"""
        try:
            # Yeni ExcelReader oluştur
            self.reader = ExcelReader()
            
            loaded_count = 0
            
            # Hatalı İşler
            hatali_excel = "data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx"
            if os.path.exists(hatali_excel):
                hatali_data = self.reader.read_hatali_isler(hatali_excel)
                if hatali_data is not None and not hatali_data.empty:
                    loaded_count += 1
            
            # Uzun İşler
            uzun_excel = "data/excel/SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx"
            if os.path.exists(uzun_excel):
                uzun_data = self.reader.read_uzun_isler(uzun_excel)
                if uzun_data is not None and not uzun_data.empty:
                    loaded_count += 1
            
            # Tabloyu güncelle
            self._load_data_info()
            
            logger.info(f"Veriler yeniden yüklendi: {loaded_count} dosya")
            QMessageBox.information(
                self,
                "Başarılı",
                f"✅ {loaded_count} Excel dosyası yeniden yüklendi!\n\n"
                "Sayfalar güncellendi."
            )
            
        except Exception as e:
            logger.error(f"Veri yeniden yükleme hatası: {e}", exc_info=True)
            QMessageBox.critical(self, "Hata", f"Veriler yeniden yüklenemedi:\n{str(e)}")


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    page = DataManagerPage()
    page.show()
    sys.exit(app.exec_())