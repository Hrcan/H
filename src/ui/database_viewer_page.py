"""
Database/Bellek İçeriği Görüntüleyici
Bellekte yüklü tüm DataFrame'leri ve içeriklerini gösterir

Özellikler:
- Yüklü DataFrame'leri listele
- Satır/sütun sayıları
- Bellek kullanımı
- DataFrame preview
- Gerçek zamanlı güncelleme
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                              QTextEdit, QComboBox, QPushButton, QGroupBox,
                              QTableWidget, QTableWidgetItem, QHeaderView,
                              QAbstractItemView, QScrollArea, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
import sys
import os
import pandas as pd

# Logger'ı başlat
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.logger import get_logger
from core.database_manager import get_database_manager

logger = get_logger()


class DatabaseViewerPage(QWidget):
    """Database/Bellek İçeriği Görüntüleyici"""
    
    def __init__(self, main_window=None):
        """DatabaseViewerPage'i başlat"""
        super().__init__()
        
        # Ana pencereye referans (DataFrame'lere erişmek için)
        self.main_window = main_window
        
        # Layout oluştur
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Başlık
        title = QLabel("🗄️ Database / Bellek İçeriği Görüntüleyici")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Açıklama
        desc = QLabel("Bu sayfa bellekte yüklü tüm DataFrame'leri gösterir. Veri temizleme işleminin çalışıp çalışmadığını kontrol edebilirsiniz.")
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: #888; font-style: italic; padding: 5px;")
        main_layout.addWidget(desc)
        
        # Kontrol paneli
        control_panel = self._create_control_panel()
        main_layout.addWidget(control_panel)
        
        # Özet bilgi
        summary_group = self._create_summary_section()
        main_layout.addWidget(summary_group)
        
        # DataFrame seçici ve görüntüleyici
        viewer_group = self._create_viewer_section()
        main_layout.addWidget(viewer_group)
        
        self.setLayout(main_layout)
        
        # İlk yükleme
        self._refresh_data()
    
    def _create_control_panel(self):
        """Kontrol panelini oluştur"""
        group = QGroupBox("⚙️ Kontroller")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QHBoxLayout()
        
        # Yenile butonu
        self.refresh_btn = QPushButton("🔄 Yenile")
        self.refresh_btn.setMinimumHeight(40)
        self.refresh_btn.setMaximumWidth(150)
        self.refresh_btn.clicked.connect(self._refresh_data)
        
        # Bellek temizle butonu
        self.clear_memory_btn = QPushButton("🗑️ Belleği Temizle")
        self.clear_memory_btn.setMinimumHeight(40)
        self.clear_memory_btn.setMaximumWidth(180)
        self.clear_memory_btn.clicked.connect(self._clear_memory)
        self.clear_memory_btn.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        
        layout.addWidget(self.refresh_btn)
        layout.addStretch()
        layout.addWidget(self.clear_memory_btn)
        
        group.setLayout(layout)
        return group
    
    def _create_summary_section(self):
        """Özet bilgi bölümü"""
        group = QGroupBox("📊 Bellek Özeti")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        
        # Özet metin alanı
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_text.setMinimumHeight(150)
        self.summary_text.setMaximumHeight(200)
        
        # Modern stil
        self.summary_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                padding: 15px;
                font-family: 'Courier New';
                font-size: 12px;
            }
        """)
        
        layout.addWidget(self.summary_text)
        
        group.setLayout(layout)
        return group
    
    def _create_viewer_section(self):
        """DataFrame görüntüleyici bölümü"""
        group = QGroupBox("📋 DataFrame İçeriği")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        
        # DataFrame seçici
        selector_layout = QHBoxLayout()
        
        select_label = QLabel("DataFrame Seç:")
        select_label.setFixedWidth(120)
        
        self.df_selector = QComboBox()
        self.df_selector.setMinimumHeight(35)
        self.df_selector.currentTextChanged.connect(self._show_dataframe)
        
        selector_layout.addWidget(select_label)
        selector_layout.addWidget(self.df_selector)
        
        layout.addLayout(selector_layout)
        
        # DataFrame bilgi label
        self.df_info_label = QLabel("DataFrame seçin...")
        self.df_info_label.setStyleSheet("color: #888; padding: 10px;")
        layout.addWidget(self.df_info_label)
        
        # Tablo widget
        self.df_table = QTableWidget()
        self.df_table.setMinimumHeight(300)
        self.df_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.df_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.df_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.df_table.setAlternatingRowColors(True)
        self.df_table.horizontalHeader().setStretchLastSection(True)
        self.df_table.verticalHeader().setVisible(False)
        
        # Modern dark theme stil
        self.df_table.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
                gridline-color: #3d3d3d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QTableWidget::item:selected {
                background-color: #3498DB;
                color: white;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498DB, stop:1 #2980B9);
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-right: 1px solid #2980B9;
            }
        """)
        
        layout.addWidget(self.df_table)
        
        group.setLayout(layout)
        return group
    
    def _get_dataframes(self):
        """Main window'dan DataFrame'leri al"""
        dataframes = {}
        
        if self.main_window is None:
            return dataframes
        
        try:
            # Hatalı İşler sayfasından DataFrame al
            if hasattr(self.main_window, 'hatali_isler_page'):
                page = self.main_window.hatali_isler_page
                if hasattr(page, 'df') and page.df is not None and not page.df.empty:
                    dataframes['Hatalı İşler'] = page.df
            
            # Uzun İşler sayfasından DataFrame al
            if hasattr(self.main_window, 'uzun_isler_page'):
                page = self.main_window.uzun_isler_page
                if hasattr(page, 'df') and page.df is not None and not page.df.empty:
                    dataframes['Uzun İşler'] = page.df
            
            # Search sayfasından DataFrame al
            if hasattr(self.main_window, 'search_page'):
                page = self.main_window.search_page
                if hasattr(page, 'combined_df') and page.combined_df is not None and not page.combined_df.empty:
                    dataframes['Arama (Combined)'] = page.combined_df
                    
        except Exception as e:
            logger.error(f"DataFrame alma hatası: {e}", exc_info=True)
        
        return dataframes
    
    def _refresh_data(self):
        """Bellek içeriğini yenile ve SQLite'a kaydet"""
        try:
            # 1. Main window'dan DataFrame'leri al
            dataframes = self._get_dataframes()
            
            # 2. DataFrame'leri SQLite'a kaydet
            db = get_database_manager()
            for name, df in dataframes.items():
                # Tablo adını temizle
                table_name = name.replace(' ', '_').replace('(', '').replace(')', '')
                db.save_dataframe(table_name, df)
            
            # 3. SQLite'dan tablo listesini al
            tables = db.get_table_names()
            
            # 4. Özet bilgiyi güncelle (SQLite'dan)
            self._update_summary_from_sqlite(tables)
            
            # 5. DataFrame seçiciyi güncelle (SQLite'dan)
            self._update_selector_from_sqlite(tables)
            
            logger.info(f"Bellek ve SQLite yenilendi: {len(dataframes)} DataFrame → {len(tables)} tablo")
            
        except Exception as e:
            logger.error(f"Bellek yenileme hatası: {e}", exc_info=True)
            self.summary_text.setPlainText(f"❌ Hata: {e}")
    
    def _update_summary(self, dataframes):
        """Özet bilgiyi güncelle"""
        if not dataframes:
            summary = """
╔══════════════════════════════════════════════════════════╗
║                   BELLEK BOŞTA                          ║
╚══════════════════════════════════════════════════════════╝

✅ Bellekte hiçbir DataFrame yüklü değil.
💡 Veri temizleme işlemi başarıyla tamamlandı!

Veri yüklemek için:
  • Ana sayfadan "Excel Yükle" butonuna tıklayın
  • Veya Ctrl+O kısayolunu kullanın
  • Veya Ctrl+1 / Ctrl+2 ile sayfalara gidin
"""
            self.summary_text.setPlainText(summary)
            return
        
        # DataFrame'ler varsa detaylı bilgi
        total_rows = 0
        total_memory = 0
        
        summary_lines = [
            "╔══════════════════════════════════════════════════════════╗",
            "║              BELLEK İÇERİĞİ RAPORU                      ║",
            "╚══════════════════════════════════════════════════════════╝",
            ""
        ]
        
        for name, df in dataframes.items():
            rows = len(df)
            cols = len(df.columns)
            memory = df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
            
            total_rows += rows
            total_memory += memory
            
            summary_lines.append(f"📊 {name}")
            summary_lines.append(f"   ├─ Satır Sayısı: {rows:,}")
            summary_lines.append(f"   ├─ Sütun Sayısı: {cols}")
            summary_lines.append(f"   ├─ Bellek: {memory:.2f} MB")
            summary_lines.append(f"   └─ Durum: ✅ Yüklü")
            summary_lines.append("")
        
        summary_lines.append("─" * 60)
        summary_lines.append(f"📈 TOPLAM: {total_rows:,} satır, {total_memory:.2f} MB bellek")
        summary_lines.append("")
        summary_lines.append("⚠️  Veri temizleme için 'Belleği Temizle' butonuna basın")
        
        self.summary_text.setPlainText("\n".join(summary_lines))
    
    def _update_summary_from_sqlite(self, tables):
        """SQLite'dan özet bilgiyi güncelle"""
        if not tables:
            summary = """
╔══════════════════════════════════════════════════════════╗
║               SQLite VERİTABANI BOŞTA                   ║
╚══════════════════════════════════════════════════════════╝

✅ SQLite veritabanında tablo yok.
💡 Veri yüklemek için Ctrl+1 veya Ctrl+2'ye basın.

Veri yüklemek için:
  • Ctrl+1 → Hatalı İşler yükle
  • Ctrl+2 → Uzun İşler yükle
  • Ctrl+B → Database Viewer'da yenile
"""
            self.summary_text.setPlainText(summary)
            return
        
        # Tablolar varsa detaylı bilgi
        db = get_database_manager()
        total_rows = 0
        total_size = 0
        
        summary_lines = [
            "╔══════════════════════════════════════════════════════════╗",
            "║           SQLite VERİTABANI RAPORU                      ║",
            "╚══════════════════════════════════════════════════════════╝",
            ""
        ]
        
        for table in tables:
            info = db.get_table_info(table)
            if info:
                rows = info['rows']
                cols = info['columns']
                size_mb = info['size_mb']
                
                total_rows += rows
                total_size = size_mb  # Dosya boyutu paylaşımlı
                
                # Tablo adını güzelleştir
                display_name = table.replace('_', ' ').title()
                
                summary_lines.append(f"📊 {display_name}")
                summary_lines.append(f"   ├─ Satır Sayısı: {rows:,}")
                summary_lines.append(f"   ├─ Sütun Sayısı: {cols}")
                summary_lines.append(f"   └─ Durum: ✅ SQLite'da")
                summary_lines.append("")
        
        summary_lines.append("─" * 60)
        summary_lines.append(f"📈 TOPLAM: {total_rows:,} satır, {total_size:.2f} MB (SQLite)")
        summary_lines.append(f"📁 Dosya: data/database/excel_data.db")
        summary_lines.append("")
        summary_lines.append("💡 Veriler SQLite veritabanında kalıcı olarak saklanıyor")
        
        self.summary_text.setPlainText("\n".join(summary_lines))
    
    def _update_selector(self, dataframes):
        """DataFrame seçiciyi güncelle"""
        self.df_selector.clear()
        
        if not dataframes:
            self.df_selector.addItem("(Bellek boş)")
            self.df_selector.setEnabled(False)
            self.df_info_label.setText("❌ Bellekte DataFrame yok")
            self.df_table.setRowCount(0)
            self.df_table.setColumnCount(0)
        else:
            self.df_selector.setEnabled(True)
            for name in dataframes.keys():
                self.df_selector.addItem(name)
    
    def _update_selector_from_sqlite(self, tables):
        """SQLite'dan seçiciyi güncelle"""
        self.df_selector.clear()
        
        if not tables:
            self.df_selector.addItem("(SQLite boş)")
            self.df_selector.setEnabled(False)
            self.df_info_label.setText("❌ SQLite'da tablo yok")
            self.df_table.setRowCount(0)
            self.df_table.setColumnCount(0)
        else:
            self.df_selector.setEnabled(True)
            for table in tables:
                # Tablo adını güzelleştir
                display_name = table.replace('_', ' ').title()
                self.df_selector.addItem(display_name)
    
    def _show_dataframe(self, df_name):
        """Seçilen DataFrame'i göster (SQLite'dan)"""
        if df_name == "(SQLite boş)" or df_name == "(Bellek boş)":
            return
        
        try:
            # Tablo adını geri çevir
            table_name = df_name.replace(' ', '_').lower()
            
            # SQLite'dan oku
            db = get_database_manager()
            df = db.query_table(table_name, limit=100)
            
            if df is None or df.empty:
                self.df_info_label.setText("❌ DataFrame boş veya bulunamadı")
                self.df_table.setRowCount(0)
                self.df_table.setColumnCount(0)
                return
            
            # Bilgi label'ı güncelle
            rows = len(df)
            cols = len(df.columns)
            self.df_info_label.setText(
                f"📊 {df_name}: {rows:,} satır × {cols} sütun | "
                f"İlk 100 satır gösteriliyor"
            )
            self.df_info_label.setStyleSheet("color: #4CAF50; font-weight: bold; padding: 10px;")
            
            # Tabloyu doldur (maksimum 100 satır)
            display_df = df.head(100)
            
            self.df_table.setRowCount(len(display_df))
            self.df_table.setColumnCount(len(display_df.columns))
            self.df_table.setHorizontalHeaderLabels(display_df.columns.tolist())
            
            for i, row in enumerate(display_df.itertuples(index=False)):
                for j, value in enumerate(row):
                    if pd.isna(value):
                        item = QTableWidgetItem("-")
                        item.setForeground(QColor("#888888"))
                    else:
                        item = QTableWidgetItem(str(value))
                        item.setForeground(QColor("#e0e0e0"))
                    
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.df_table.setItem(i, j, item)
            
            # Sütun genişliklerini ayarla
            self.df_table.resizeColumnsToContents()
            
            logger.debug(f"DataFrame gösterildi: {df_name} - {rows} satır")
            
        except Exception as e:
            logger.error(f"DataFrame gösterme hatası: {e}", exc_info=True)
            self.df_info_label.setText(f"❌ Hata: {e}")
    
    def _clear_memory(self):
        """Bellekteki tüm DataFrame'leri temizle"""
        reply = QMessageBox.question(
            self,
            "Bellek Temizleme",
            "Bellekteki TÜM DataFrame'leri silmek istediğinizden emin misiniz?\n\n"
            "⚠️ Bu işlem geri alınamaz!\n"
            "⚠️ Tüm sayfalar yeniden oluşturulacak!",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                # Main window üzerinden temizleme yap
                if self.main_window and hasattr(self.main_window, 'clear_all_data'):
                    success = self.main_window.clear_all_data()
                    
                    if success:
                        logger.info("Bellek başarıyla temizlendi (Database Viewer)")
                        
                        QMessageBox.information(
                            self,
                            "Başarılı",
                            "✅ Bellek başarıyla temizlendi!\n\n"
                            "Tüm DataFrame'ler bellekten silindi ve sayfalar yenilendi."
                        )
                        
                        # Görünümü yenile
                        self._refresh_data()
                    else:
                        QMessageBox.warning(
                            self,
                            "Uyarı",
                            "Bellek temizleme tamamlanamadı.\n"
                            "Detaylar için log dosyasını kontrol edin."
                        )
                else:
                    QMessageBox.critical(
                        self,
                        "Hata",
                        "Ana pencereye erişilemiyor!\n"
                        "Bellek temizleme yapılamadı."
                    )
                
            except Exception as e:
                logger.error(f"Bellek temizleme hatası: {e}", exc_info=True)
                QMessageBox.critical(
                    self,
                    "Hata",
                    f"Bellek temizleme hatası:\n\n{e}"
                )


# Test kodu
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    page = DatabaseViewerPage()
    page.setWindowTitle("Database Viewer - Test")
    page.resize(1200, 800)
    page.show()
    sys.exit(app.exec_())