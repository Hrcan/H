"""
Uzun İşler Detay Sayfası
Tüm uzun süren işleri detaylı listeleyen sayfa

Özellikler:
- Tüm uzun işleri listeleme (96 satır)
- Filtreleme: Ekip, JCL adı, sheet
- Sıralama özellikleri
- Modern tablo tasarımı (Dark Theme)
- Detaylı görünüm
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                              QLineEdit, QComboBox, QPushButton, QTextEdit,
                              QGroupBox, QMessageBox, QTableWidget, QTableWidgetItem,
                              QHeaderView, QAbstractItemView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
import pandas as pd

# ExcelReader'ı import et
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.excel_reader import ExcelReader
from core.logger import get_logger

# Logger'ı başlat
logger = get_logger()


class UzunIslerPage(QWidget):
    """Uzun İşler Detay Sayfası widget'ı"""
    
    def __init__(self):
        """UzunIslerPage'i başlat"""
        super().__init__()
        
        # ExcelReader ve veri hazırlığı
        self.reader = ExcelReader()
        self.uzun_df = None
        self.filtered_df = None
        
        # Layout oluştur
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Başlık
        title = QLabel("⏱️ Uzun Süren İşler Detay Listesi")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Filtre grubu
        filter_group = self._create_filter_section()
        main_layout.addWidget(filter_group)
        
        # İstatistik label
        self.stats_label = QLabel("Veriler yükleniyor...")
        self.stats_label.setAlignment(Qt.AlignCenter)
        stats_font = QFont()
        stats_font.setPointSize(11)
        stats_font.setBold(True)
        self.stats_label.setFont(stats_font)
        self.stats_label.setStyleSheet("color: #FF9800; padding: 10px;")
        main_layout.addWidget(self.stats_label)
        
        # Tablo grubu
        table_group = self._create_table_section()
        main_layout.addWidget(table_group)
        
        self.setLayout(main_layout)
        
        # Excel verilerini yükle
        self._load_excel_data()
    
    def _create_filter_section(self):
        """Filtreleme bölümünü oluştur"""
        group = QGroupBox("🔍 Filtreleme")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # İlk satır: JCL adı ve Ekip
        first_row = QHBoxLayout()
        
        # JCL adı filtresi
        jcl_label = QLabel("JCL Adı:")
        jcl_label.setFixedWidth(100)
        jcl_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.jcl_filter = QLineEdit()
        self.jcl_filter.setPlaceholderText("JCL adı ile filtrele (örn: PKRBI)")
        self.jcl_filter.setMinimumHeight(35)
        self.jcl_filter.textChanged.connect(self._apply_filters)
        
        first_row.addWidget(jcl_label)
        first_row.addWidget(self.jcl_filter)
        
        # Ekip filtresi
        ekip_label = QLabel("Ekip:")
        ekip_label.setFixedWidth(80)
        ekip_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.ekip_filter = QComboBox()
        self.ekip_filter.addItem("Tümü")
        self.ekip_filter.setMinimumHeight(35)
        self.ekip_filter.setMinimumWidth(200)
        self.ekip_filter.currentTextChanged.connect(self._apply_filters)
        
        first_row.addWidget(ekip_label)
        first_row.addWidget(self.ekip_filter)
        
        layout.addLayout(first_row)
        
        # İkinci satır: Sheet filtresi
        second_row = QHBoxLayout()
        
        # Sheet filtresi (YENİ!)
        sheet_label = QLabel("Sheet:")
        sheet_label.setFixedWidth(100)
        sheet_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.sheet_filter = QComboBox()
        self.sheet_filter.addItem("Tümü")
        self.sheet_filter.setMinimumHeight(35)
        self.sheet_filter.setMinimumWidth(300)
        self.sheet_filter.currentTextChanged.connect(self._apply_filters)
        
        second_row.addWidget(sheet_label)
        second_row.addWidget(self.sheet_filter)
        second_row.addStretch()
        
        layout.addLayout(second_row)
        
        # Üçüncü satır: Sıralama ve butonlar
        third_row = QHBoxLayout()
        
        # Sıralama
        sort_label = QLabel("Sırala:")
        sort_label.setFixedWidth(100)
        sort_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.sort_combo = QComboBox()
        self.sort_combo.addItem("Süre (Uzun → Kısa)")
        self.sort_combo.addItem("Süre (Kısa → Uzun)")
        self.sort_combo.addItem("Çalışma Sayısı (Çok → Az)")
        self.sort_combo.addItem("Çalışma Sayısı (Az → Çok)")
        self.sort_combo.addItem("JCL Adı (A → Z)")
        self.sort_combo.addItem("JCL Adı (Z → A)")
        self.sort_combo.addItem("Ekip (A → Z)")
        self.sort_combo.setMinimumHeight(35)
        self.sort_combo.currentTextChanged.connect(self._apply_filters)
        
        third_row.addWidget(sort_label)
        third_row.addWidget(self.sort_combo)
        
        # Filtreleri temizle butonu
        self.clear_btn = QPushButton("🔄 Filtreleri Temizle")
        self.clear_btn.setMinimumHeight(35)
        self.clear_btn.setMaximumWidth(180)
        self.clear_btn.clicked.connect(self._clear_filters)
        
        third_row.addWidget(self.clear_btn)
        third_row.addStretch()
        
        layout.addLayout(third_row)
        
        # Bilgi mesajı
        info_label = QLabel("💡 İpucu: Filtreler otomatik olarak uygulanır")
        info_label.setStyleSheet("color: #888; font-style: italic; padding-top: 5px;")
        layout.addWidget(info_label)
        
        group.setLayout(layout)
        return group
    
    def _create_table_section(self):
        """Tablo bölümünü oluştur"""
        group = QGroupBox("📊 Uzun İşler Listesi")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        
        # Tablo widget'ı
        self.table = QTableWidget()
        self.table.setMinimumHeight(400)
        
        # Tablo ayarları
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Read-only
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # Satır seçimi
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # Tek satır
        self.table.setAlternatingRowColors(True)  # Alternatif renkler
        self.table.horizontalHeader().setStretchLastSection(True)  # Son sütunu genişlet
        self.table.verticalHeader().setVisible(False)  # Satır numaralarını gizle
        
        # Modern Dark Theme Stil (Turuncu Tema - Uzun İşler)
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
                gridline-color: #3d3d3d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                font-size: 13px;
            }
            QTableWidget::item {
                padding: 10px 8px;
                border: none;
            }
            QTableWidget::item:alternate {
                background-color: #252525;
            }
            QTableWidget::item:selected {
                background-color: #FF9800;
                color: white;
            }
            QTableWidget::item:hover {
                background-color: #333333;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #FF6F00, stop:1 #FF9800);
                color: white;
                font-weight: bold;
                font-size: 12px;
                padding: 12px;
                border: none;
                border-right: 1px solid #F57C00;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            QHeaderView::section:first {
                border-top-left-radius: 8px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 8px;
                border-right: none;
            }
        """)
        
        layout.addWidget(self.table)
        
        group.setLayout(layout)
        return group
    
    def _load_excel_data(self):
        """Excel dosyasından uzun işleri yükle"""
        try:
            # Uzun İşler Excel dosyasını yükle (Dosya adı düzeltildi - v2.0.1)
            uzun_path = "data/excel/SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx"
            self.uzun_df = self.reader.read_uzun_isler(uzun_path)
            
            if self.uzun_df is not None and not self.uzun_df.empty:
                # Ekip listesini doldur
                self._populate_ekip_filter()
                
                # Sheet listesini doldur (YENİ!)
                self._populate_sheet_filter()
                
                # Filtrelenmiş DataFrame başlangıçta tüm veriyi göster
                self.filtered_df = self.uzun_df.copy()
                
                # Tabloyu doldur
                self._populate_table()
                
                # İstatistik güncelle
                row_count = len(self.uzun_df)
                self.stats_label.setText(f"✅ Toplam {row_count} uzun iş yüklendi")
                self.stats_label.setStyleSheet("color: #FF9800; padding: 10px; font-weight: bold;")
                
                logger.info(f"Uzun İşler sayfası yüklendi: {row_count} satır")
            else:
                logger.warning("Uzun İşler verisi bulunamadı")
                self.stats_label.setText("⚠️ Veri bulunamadı")
                self.stats_label.setStyleSheet("color: orange; padding: 10px;")
                
        except FileNotFoundError as e:
            logger.error(f"Uzun İşler Excel dosyası bulunamadı: {e}")
            QMessageBox.critical(self, "Hata", f"Excel dosyası bulunamadı:\n{e}")
            self.stats_label.setText("❌ Dosya bulunamadı")
            self.stats_label.setStyleSheet("color: red; padding: 10px;")
            
        except Exception as e:
            logger.error(f"Uzun İşler veri yükleme hatası: {e}", exc_info=True)
            QMessageBox.critical(self, "Hata", f"Veri yükleme hatası:\n{e}")
            self.stats_label.setText("❌ Yükleme hatası")
            self.stats_label.setStyleSheet("color: red; padding: 10px;")
    
    def _populate_ekip_filter(self):
        """Ekip filtresini doldur"""
        if self.uzun_df is not None and not self.uzun_df.empty:
            # Benzersiz ekipleri al ve sırala
            ekip_list = sorted(self.uzun_df['Ekip_Adi'].unique())
            
            # ComboBox'ı temizle ve doldur
            self.ekip_filter.clear()
            self.ekip_filter.addItem("Tümü")
            for ekip in ekip_list:
                self.ekip_filter.addItem(ekip)
            
            logger.info(f"Uzun İşler: {len(ekip_list)} benzersiz ekip yüklendi")
    
    def _populate_sheet_filter(self):
        """Sheet filtresini doldur (YENİ!)"""
        if self.uzun_df is not None and not self.uzun_df.empty and 'Sheet_Adi' in self.uzun_df.columns:
            # Benzersiz sheet'leri al ve sırala
            sheet_list = sorted(self.uzun_df['Sheet_Adi'].unique())
            
            # ComboBox'ı temizle ve doldur
            self.sheet_filter.clear()
            self.sheet_filter.addItem("Tümü")
            for sheet in sheet_list:
                self.sheet_filter.addItem(sheet)
            
            logger.info(f"Uzun İşler: {len(sheet_list)} benzersiz sheet yüklendi")
    
    def _populate_table(self):
        """Tabloyu verilerle doldur"""
        if self.filtered_df is None or self.filtered_df.empty:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            return
        
        # Tablo yapısını ayarla
        row_count = len(self.filtered_df)
        col_count = len(self.filtered_df.columns)
        
        self.table.setRowCount(row_count)
        self.table.setColumnCount(col_count)
        
        # Sütun başlıklarını ayarla
        self.table.setHorizontalHeaderLabels(self.filtered_df.columns.tolist())
        
        # Verileri tabloya ekle
        for i, row in enumerate(self.filtered_df.itertuples(index=False)):
            for j, value in enumerate(row):
                # NaN veya None kontrolü
                if pd.isna(value):
                    item = QTableWidgetItem("-")
                    item.setForeground(QColor("#888888"))
                else:
                    # Sayısal değerleri formatla
                    if isinstance(value, (int, float)) and not pd.isna(value):
                        item = QTableWidgetItem(str(int(value)))
                    else:
                        item = QTableWidgetItem(str(value))
                    
                    # Uzun süre vurgusu (60 dakika üzeri turuncu)
                    col_name = self.filtered_df.columns[j]
                    if col_name == 'Calisma_Suresi_Dakika' and isinstance(value, (int, float)):
                        if value >= 60:
                            item.setForeground(QColor("#FF9800"))  # Turuncu
                            item.setFont(QFont("", -1, QFont.Bold))
                        else:
                            item.setForeground(QColor("#e0e0e0"))
                    else:
                        item.setForeground(QColor("#e0e0e0"))
                
                # Hizalama
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                
                self.table.setItem(i, j, item)
        
        # Sütun genişliklerini ayarla
        self.table.resizeColumnsToContents()
        
        # Minimum genişlikler
        for i in range(col_count):
            if self.table.columnWidth(i) < 100:
                self.table.setColumnWidth(i, 100)
        
        logger.debug(f"Uzun İşler tablosu güncellendi: {row_count} satır, {col_count} sütun")
    
    def _apply_filters(self):
        """Filtreleri uygula"""
        if self.uzun_df is None or self.uzun_df.empty:
            return
        
        # Filtrelenmemiş veriyle başla
        filtered = self.uzun_df.copy()
        
        # JCL adı filtresi
        jcl_text = self.jcl_filter.text().strip().upper()
        if jcl_text:
            filtered = filtered[
                filtered['JCL_Adi'].str.upper().str.contains(jcl_text, na=False)
            ]
        
        # Ekip filtresi
        ekip = self.ekip_filter.currentText()
        if ekip != "Tümü":
            filtered = filtered[filtered['Ekip_Adi'] == ekip]
        
        # Sheet filtresi (YENİ!)
        sheet = self.sheet_filter.currentText()
        if sheet != "Tümü" and 'Sheet_Adi' in filtered.columns:
            filtered = filtered[filtered['Sheet_Adi'] == sheet]
        
        # Sıralama
        sort_option = self.sort_combo.currentText()
        if "Süre (Uzun → Kısa)" in sort_option:
            if 'Calisma_Suresi_Dakika' in filtered.columns:
                filtered = filtered.sort_values('Calisma_Suresi_Dakika', ascending=False)
        elif "Süre (Kısa → Uzun)" in sort_option:
            if 'Calisma_Suresi_Dakika' in filtered.columns:
                filtered = filtered.sort_values('Calisma_Suresi_Dakika', ascending=True)
        elif "Çalışma Sayısı (Çok → Az)" in sort_option:
            if 'Calisma_Sayisi_Adet' in filtered.columns:
                filtered = filtered.sort_values('Calisma_Sayisi_Adet', ascending=False)
        elif "Çalışma Sayısı (Az → Çok)" in sort_option:
            if 'Calisma_Sayisi_Adet' in filtered.columns:
                filtered = filtered.sort_values('Calisma_Sayisi_Adet', ascending=True)
        elif "JCL Adı (A → Z)" in sort_option:
            filtered = filtered.sort_values('JCL_Adi', ascending=True)
        elif "JCL Adı (Z → A)" in sort_option:
            filtered = filtered.sort_values('JCL_Adi', ascending=False)
        elif "Ekip (A → Z)" in sort_option:
            filtered = filtered.sort_values('Ekip_Adi', ascending=True)
        
        # Filtrelenmiş veriyi güncelle
        self.filtered_df = filtered
        
        # Tabloyu güncelle
        self._populate_table()
        
        # İstatistik güncelle
        total_count = len(self.uzun_df)
        filtered_count = len(filtered)
        
        if filtered_count == 0:
            # BOŞ SONUÇ MESAJI
            self.stats_label.setText("❌ Filtrelere uygun sonuç bulunamadı")
            self.stats_label.setStyleSheet("color: #FF5722; padding: 10px; font-weight: bold;")
        elif filtered_count == total_count:
            self.stats_label.setText(f"✅ Toplam {total_count} uzun iş")
            self.stats_label.setStyleSheet("color: #FF9800; padding: 10px; font-weight: bold;")
        else:
            self.stats_label.setText(
                f"🔍 {filtered_count} / {total_count} uzun iş gösteriliyor"
            )
            self.stats_label.setStyleSheet("color: #2196F3; padding: 10px; font-weight: bold;")
    
    def _clear_filters(self):
        """Tüm filtreleri temizle"""
        # Filtreleri sıfırla
        self.jcl_filter.clear()
        self.ekip_filter.setCurrentIndex(0)  # "Tümü"
        self.sheet_filter.setCurrentIndex(0) # "Tümü" (YENİ!)
        self.sort_combo.setCurrentIndex(0)   # İlk seçenek
        
        # Filtreleri uygula (otomatik olarak uygulanacak)
        self._apply_filters()
        
        logger.info("Uzun İşler: Tüm filtreler temizlendi")


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    page = UzunIslerPage()
    page.setWindowTitle("Uzun İşler Detay Sayfası Test")
    page.resize(1200, 700)
    page.show()
    sys.exit(app.exec_())