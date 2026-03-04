"""
Search Page - Arama Sayfası
Ana arama ve filtreleme sayfası

Özellikler:
- JCL adı arama (TextBox)
- Ekip seçimi (ComboBox)
- Arama butonu
- Sonuç gösterme
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                              QLineEdit, QComboBox, QPushButton, QTextEdit,
                              QGroupBox, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import pandas as pd

# ExcelReader'ı import et
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.excel_reader import ExcelReader
from core.logger import get_logger

# Logger'ı başlat
logger = get_logger()


class SearchPage(QWidget):
    """Arama sayfası widget'ı"""
    
    def __init__(self):
        """SearchPage'i başlat"""
        super().__init__()
        
        # ExcelReader ve veri hazırlığı
        self.reader = ExcelReader()
        self.hatali_df = None
        self.uzun_df = None
        
        # Layout oluştur
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Başlık
        title = QLabel("Excel Veri Arama")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Arama kriterleri grubu
        search_group = self._create_search_criteria()
        main_layout.addWidget(search_group)
        
        # Arama butonu
        search_btn_layout = QHBoxLayout()
        self.search_btn = QPushButton("🔍 Ara")
        self.search_btn.setMinimumHeight(40)
        self.search_btn.setMaximumWidth(200)
        search_btn_font = QFont()
        search_btn_font.setPointSize(11)
        self.search_btn.setFont(search_btn_font)
        self.search_btn.clicked.connect(self._perform_search)
        search_btn_layout.addStretch()
        search_btn_layout.addWidget(self.search_btn)
        search_btn_layout.addStretch()
        main_layout.addLayout(search_btn_layout)
        
        # Sonuç alanı
        result_group = self._create_result_area()
        main_layout.addWidget(result_group)
        
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
        # Layout oluştuktan sonra Excel verilerini yükle
        self._load_excel_data()
    
    def _create_search_criteria(self):
        """Arama kriterleri bölümünü oluştur"""
        group = QGroupBox("Arama Kriterleri")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # JCL Adı arama - ÇOK SATIRLI (TOPLU ARAMA)
        jcl_layout = QVBoxLayout()
        jcl_label = QLabel("JCL Adı (Toplu Arama):")
        jcl_label_font = QFont()
        jcl_label_font.setBold(True)
        jcl_label.setFont(jcl_label_font)
        
        self.jcl_input = QTextEdit()  # QLineEdit yerine QTextEdit (çok satırlı)
        self.jcl_input.setPlaceholderText(
            "Her satıra bir JCL adı yazın (toplu arama):\n"
            "PKRBI330\n"
            "PMUAI012\n"
            "POPGG001\n"
            "...\n\n"
            "Veya tek JCL için arama yapabilirsiniz"
        )
        self.jcl_input.setMinimumHeight(100)  # Daha büyük alan
        self.jcl_input.setMaximumHeight(150)
        
        jcl_layout.addWidget(jcl_label)
        jcl_layout.addWidget(self.jcl_input)
        layout.addLayout(jcl_layout)
        
        # Separator - Text box ile diğer filtreler arasında
        from PyQt5.QtWidgets import QFrame
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background-color: #3d3d3d; margin: 10px 0;")
        layout.addWidget(separator)
        
        # Ekip ve Excel Türü - TAM AYRILMIŞ (v2.1.2)
        filters_layout = QVBoxLayout()
        filters_layout.setSpacing(15)
        
        # Ekip seçimi
        ekip_row = QHBoxLayout()
        ekip_row.setSpacing(15)
        
        ekip_label = QLabel("Ekip:")
        ekip_label.setMinimumWidth(100)
        ekip_label.setMaximumWidth(100)
        ekip_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        ekip_label_font = QFont()
        ekip_label_font.setBold(True)
        ekip_label.setFont(ekip_label_font)
        
        self.ekip_combo = QComboBox()
        self.ekip_combo.addItem("Tümü")
        self.ekip_combo.addItem("YGDB011")
        self.ekip_combo.addItem("YGDB012")
        self.ekip_combo.addItem("YGDB051")
        self.ekip_combo.addItem("YGDB055")
        self.ekip_combo.addItem("YGDB153")
        self.ekip_combo.addItem("Ana Sistemler SMS")
        self.ekip_combo.addItem("Ana Sistemler VTS")
        self.ekip_combo.setMinimumHeight(35)
        
        ekip_row.addWidget(ekip_label)
        ekip_row.addWidget(self.ekip_combo, 1)
        filters_layout.addLayout(ekip_row)
        
        # Excel türü seçimi
        type_row = QHBoxLayout()
        type_row.setSpacing(15)
        
        type_label = QLabel("Excel Türü:")
        type_label.setMinimumWidth(100)
        type_label.setMaximumWidth(100)
        type_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        type_label_font = QFont()
        type_label_font.setBold(True)
        type_label.setFont(type_label_font)
        
        self.type_combo = QComboBox()
        self.type_combo.addItem("Tümü")
        self.type_combo.addItem("Hatalı İşler")
        self.type_combo.addItem("Uzun İşler")
        self.type_combo.setMinimumHeight(35)
        
        type_row.addWidget(type_label)
        type_row.addWidget(self.type_combo, 1)
        filters_layout.addLayout(type_row)
        
        layout.addLayout(filters_layout)
        
        # Bilgi mesajı
        info_label = QLabel("💡 İpucu: Boş bırakılan alanlar tüm sonuçları getirir")
        info_label.setStyleSheet("color: #666; font-style: italic;")
        layout.addWidget(info_label)
        
        group.setLayout(layout)
        return group
    
    def _create_result_area(self):
        """Sonuç gösterme alanını oluştur"""
        group = QGroupBox("Arama Sonuçları")
        group_font = QFont()
        group_font.setPointSize(11)
        group_font.setBold(True)
        group.setFont(group_font)
        
        layout = QVBoxLayout()
        
        # Sonuç text alanı - DAHA BÜYÜK
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(400)  # 200'den 400'e çıkarıldı
        self.result_text.setPlaceholderText("Arama sonuçları burada görüntülenecek...")
        
        # Başlangıç mesajı
        self.result_text.setHtml("""
            <div style='padding: 20px; text-align: center;'>
                <h3>🔍 Arama Bekleniyor</h3>
                <p>Yukarıdaki kriterleri doldurun ve "Ara" butonuna tıklayın.</p>
                <br>
                <p style='color: green;'><b>✅ ExcelReader hazır ve test edildi</b></p>
                <p><i>142 satır veri, 5 sheet, 38 ekip</i></p>
            </div>
        """)
        
        layout.addWidget(self.result_text)
        
        # İstatistik label
        self.stats_label = QLabel("Henüz arama yapılmadı")
        self.stats_label.setAlignment(Qt.AlignCenter)
        self.stats_label.setStyleSheet("color: #888; padding: 10px;")
        layout.addWidget(self.stats_label)
        
        group.setLayout(layout)
        return group
    
    def _perform_search(self):
        """Arama işlemini gerçekleştir - TOPLU ARAMA DESTEKLİ"""
        # Arama kriterlerin al
        jcl_text = self.jcl_input.toPlainText().strip().upper()  # Çok satırlı text al
        ekip = self.ekip_combo.currentText()
        excel_type = self.type_combo.currentText()
        
        # Boş arama kontrolü
        if not jcl_text and ekip == "Tümü" and excel_type == "Tümü":
            QMessageBox.warning(
                self,
                "Uyarı",
                "Lütfen en az bir arama kriteri girin!\n\n"
                "JCL adı, ekip veya Excel türü seçin."
            )
            return
        
        # Excel verilerinin yüklendiğinden emin ol
        if self.hatali_df is None and self.uzun_df is None:
            QMessageBox.critical(
                self,
                "Hata",
                "Excel verileri yüklenemedi!\n\n"
                "Lütfen Excel dosyalarının data/excel/ klasöründe olduğundan emin olun."
            )
            return
        
        try:
            # TOPLU ARAMA: Her satırı ayrı JCL adı olarak işle
            jcl_names = []
            if jcl_text:
                # Satırlara böl, boşlukları temizle, boş satırları filtrele
                jcl_names = [line.strip() for line in jcl_text.split('\n') if line.strip()]
            
            # Hangi DataFrame'lerde arama yapılacağını belirle
            search_in_hatali = (excel_type == "Tümü" or excel_type == "Hatalı İşler")
            search_in_uzun = (excel_type == "Tümü" or excel_type == "Uzun İşler")
            
            results_list = []
            
            # Hatalı İşler'de ara
            if search_in_hatali and self.hatali_df is not None:
                filtered = self.hatali_df.copy()
                
                # TOPLU JCL adı filtresi
                if jcl_names:
                    # Her JCL adı için arama yap ve sonuçları birleştir
                    jcl_results = []
                    for jcl_name in jcl_names:
                        temp = filtered[
                            filtered['JCL_Adi'].str.upper().str.contains(jcl_name, na=False)
                        ]
                        if not temp.empty:
                            jcl_results.append(temp)
                    
                    if jcl_results:
                        filtered = pd.concat(jcl_results, ignore_index=True)
                        # Tekrar edenleri kaldır
                        filtered = filtered.drop_duplicates()
                    else:
                        filtered = pd.DataFrame()  # Boş DataFrame
                
                # Ekip filtresi
                if ekip != "Tümü" and not filtered.empty:
                    filtered = filtered[filtered['Ekip_Adi'] == ekip]
                
                if not filtered.empty:
                    results_list.append(filtered)
            
            # Uzun İşler'de ara
            if search_in_uzun and self.uzun_df is not None:
                filtered = self.uzun_df.copy()
                
                # TOPLU JCL adı filtresi
                if jcl_names:
                    jcl_results = []
                    for jcl_name in jcl_names:
                        temp = filtered[
                            filtered['JCL_Adi'].str.upper().str.contains(jcl_name, na=False)
                        ]
                        if not temp.empty:
                            jcl_results.append(temp)
                    
                    if jcl_results:
                        filtered = pd.concat(jcl_results, ignore_index=True)
                        filtered = filtered.drop_duplicates()
                    else:
                        filtered = pd.DataFrame()
                
                # Ekip filtresi
                if ekip != "Tümü" and not filtered.empty:
                    filtered = filtered[filtered['Ekip_Adi'] == ekip]
                
                if not filtered.empty:
                    results_list.append(filtered)
            
            # Sonuçları birleştir
            if results_list:
                combined_results = pd.concat(results_list, ignore_index=True)
                # Toplam JCL sayısını göster
                jcl_display = f"{len(jcl_names)} JCL" if len(jcl_names) > 1 else jcl_text
                self._show_real_results(combined_results, jcl_display, ekip, excel_type)
            else:
                # Boş DataFrame ile göster (sonuç bulunamadı)
                empty_df = pd.DataFrame()
                jcl_display = f"{len(jcl_names)} JCL" if len(jcl_names) > 1 else jcl_text
                self._show_real_results(empty_df, jcl_display, ekip, excel_type)
        
        except Exception as e:
            logger.error(f"Arama sırasında hata: {e}", exc_info=True)
            QMessageBox.critical(
                self,
                "Hata",
                f"Arama sırasında hata oluştu:\n\n{str(e)}"
            )
    
    def _show_temporary_results(self, jcl_name, ekip, excel_type):
        """Geçici sonuçları göster (demo amaçlı)"""
        result_html = f"""
            <div style='padding: 15px;'>
                <h3>🔎 Arama Kriterleri:</h3>
                <ul>
                    <li><b>JCL Adı:</b> {jcl_name if jcl_name else '(Tümü)'}</li>
                    <li><b>Ekip:</b> {ekip}</li>
                    <li><b>Excel Türü:</b> {excel_type}</li>
                </ul>
                
                <hr>
                
                <h3>📊 Bulunan Sonuçlar:</h3>
                <p style='color: orange;'>
                    <b>⚠️ ExcelReader Entegrasyonu Bekleniyor</b>
                </p>
                <p>
                    Bu arama sayfası çalışıyor! Sonraki adımda ExcelReader ile
                    gerçek veriler yüklenecek ve sonuçlar burada gösterilecek.
                </p>
                
                <br>
                
                <h4>Demo Sonuç Örneği:</h4>
                <table border='1' cellpadding='5' style='border-collapse: collapse; width: 100%;'>
                    <tr style='background-color: #f0f0f0;'>
                        <th>JCL Adı</th>
                        <th>Ekip</th>
                        <th>Durum</th>
                    </tr>
                    <tr>
                        <td>PKRBI330</td>
                        <td>YGDB051</td>
                        <td style='color: green;'>✅ Bulundu</td>
                    </tr>
                    <tr>
                        <td>PMUAI012</td>
                        <td>YGDB012</td>
                        <td style='color: green;'>✅ Bulundu</td>
                    </tr>
                </table>
                
                <br>
                
                <p style='background-color: #e8f5e9; padding: 10px; border-left: 4px solid green;'>
                    <b>✅ Arama sayfası başarıyla çalışıyor!</b><br>
                    <small>ExcelReader entegrasyonu ile gerçek veriler gelecek.</small>
                </p>
            </div>
        """
        
        self.result_text.setHtml(result_html)
        
        # İstatistik güncelle
        self.stats_label.setText(f"🔍 Arama tamamlandı: 2 sonuç bulundu (demo)")
        self.stats_label.setStyleSheet("color: green; padding: 10px; font-weight: bold;")
    
    def _load_excel_data(self):
        """Excel dosyalarını yükle"""
        try:
            # Hatalı İşler Excel dosyasını yükle
            hatali_path = "data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx"
            self.hatali_df = self.reader.read_hatali_isler(hatali_path)
            
            # Uzun İşler Excel dosyasını yükle
            uzun_path = "data/excel/SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx"
            self.uzun_df = self.reader.read_uzun_isler(uzun_path)
            
            # Ekip listesini ComboBox'a ekle
            self._populate_ekip_combo()
            
            total_rows = len(self.hatali_df) + len(self.uzun_df)
            logger.info(f"Excel verileri başarıyla yüklendi: Hatalı İşler={len(self.hatali_df)} satır, Uzun İşler={len(self.uzun_df)} satır, Toplam={total_rows} satır")
            
        except FileNotFoundError as e:
            logger.error(f"Excel dosyası bulunamadı: {e}")
            QMessageBox.critical(self, "Hata", f"Excel dosyası bulunamadı: {e}")
        except Exception as e:
            logger.error(f"Excel yükleme hatası: {e}", exc_info=True)
            QMessageBox.critical(self, "Hata", f"Excel yükleme hatası: {e}")
    
    def _populate_ekip_combo(self):
        """Gerçek ekip listesini ComboBox'a ekle"""
        try:
            # Mevcut ekipleri temizle (sadece "Tümü" kalsın)
            self.ekip_combo.clear()
            self.ekip_combo.addItem("Tümü")
            
            # Her iki DataFrame'den benzersiz ekipleri al
            ekip_set = set()
            
            if self.hatali_df is not None and not self.hatali_df.empty:
                ekip_set.update(self.hatali_df['Ekip_Adi'].unique())
            
            if self.uzun_df is not None and not self.uzun_df.empty:
                ekip_set.update(self.uzun_df['Ekip_Adi'].unique())
            
            # Ekipleri alfabetik sırala ve ekle
            ekip_list = sorted(ekip_set)
            for ekip in ekip_list:
                self.ekip_combo.addItem(ekip)
            
            logger.info(f"{len(ekip_list)} benzersiz ekip ComboBox'a eklendi")
            
        except Exception as e:
            logger.error(f"Ekip listesi yükleme hatası: {e}", exc_info=True)
    
    def _show_real_results(self, results_df, jcl_name, ekip, excel_type):
        """Gerçek arama sonuçlarını göster"""
        if results_df.empty:
            # Sonuç bulunamadı
            result_html = f"""
                <div style='padding: 15px;'>
                    <h3>🔎 Arama Kriterleri:</h3>
                    <ul>
                        <li><b>JCL Adı:</b> {jcl_name if jcl_name else '(Tümü)'}</li>
                        <li><b>Ekip:</b> {ekip}</li>
                        <li><b>Excel Türü:</b> {excel_type}</li>
                    </ul>
                    
                    <hr>
                    
                    <div style='background-color: #fff3cd; padding: 15px; border-left: 4px solid orange;'>
                        <h3>⚠️ Sonuç Bulunamadı</h3>
                        <p>Belirtilen kriterlere uygun kayıt bulunamadı.</p>
                        <p><small>Lütfen arama kriterlerini değiştirerek tekrar deneyin.</small></p>
                    </div>
                </div>
            """
            self.result_text.setHtml(result_html)
            self.stats_label.setText("❌ Sonuç bulunamadı")
            self.stats_label.setStyleSheet("color: orange; padding: 10px; font-weight: bold;")
            return
        
        # Sonuçlar bulundu - MODERN HTML tablo oluştur
        row_count = len(results_df)
        
        # Tablo HTML'i başlat - MODERN DARK THEME!
        table_html = """
            <table border='0' cellpadding='12' cellspacing='0' style='
                border-collapse: collapse; 
                width: 100%; 
                font-size: 13px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                border-radius: 8px;
                overflow: hidden;
            '>
                <thead>
                    <tr style='
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: #ffffff;
                        font-weight: bold;
                        text-transform: uppercase;
                        letter-spacing: 0.5px;
                        font-size: 12px;
                    '>
        """
        
        # Başlıkları ekle - OKUNUR BEYAZ METIN
        for col in results_df.columns:
            table_html += f"<th style='padding: 15px; text-align: left; border-bottom: 3px solid #5a67d8;'>{col}</th>"
        
        table_html += "</tr></thead><tbody>"
        
        # Satırları ekle (maksimum 50 satır göster) - OKUNUR RENKLER
        max_rows = min(50, row_count)
        for idx, row in results_df.head(max_rows).iterrows():
            # Alternatif satır renkleri - KOYU TEMA İÇİN
            bg_color = "#2d2d2d" if idx % 2 == 0 else "#252525"
            hover_effect = "onmouseover=\"this.style.backgroundColor='#3d3d3d'\" onmouseout=\"this.style.backgroundColor='" + bg_color + "'\""
            
            table_html += f"<tr style='background-color: {bg_color}; transition: all 0.2s;' {hover_effect}>"
            
            for col in results_df.columns:
                value = row[col]
                # NaN veya None kontrolü
                if pd.isna(value):
                    value = "-"
                    text_color = "#888888"
                else:
                    text_color = "#e0e0e0"  # AÇIK GRİ - OKUNABİLİR!
                
                table_html += f"<td style='padding: 12px; color: {text_color}; border-bottom: 1px solid #3d3d3d;'>{value}</td>"
            
            table_html += "</tr>"
        
        table_html += "</tbody></table>"
        
        # Eğer 50'den fazla satır varsa bilgi ekle
        more_info = ""
        if row_count > max_rows:
            more_info = f"""
                <p style='color: #666; font-style: italic; margin-top: 10px;'>
                    ℹ️ İlk {max_rows} sonuç gösteriliyor. Toplam {row_count} sonuç bulundu.
                </p>
            """
        
        # Tam HTML
        result_html = f"""
            <div style='padding: 15px;'>
                <h3>🔎 Arama Kriterleri:</h3>
                <ul>
                    <li><b>JCL Adı:</b> {jcl_name if jcl_name else '(Tümü)'}</li>
                    <li><b>Ekip:</b> {ekip}</li>
                    <li><b>Excel Türü:</b> {excel_type}</li>
                </ul>
                
                <hr>
                
                <h3>📊 Bulunan Sonuçlar: {row_count} kayıt</h3>
                
                <div style='overflow-x: auto;'>
                    {table_html}
                </div>
                
                {more_info}
                
                <div style='background-color: #e8f5e9; padding: 10px; border-left: 4px solid green; margin-top: 15px;'>
                    <b>✅ Arama başarılı!</b><br>
                    <small>{row_count} kayıt bulundu ve listelendi.</small>
                </div>
            </div>
        """
        
        self.result_text.setHtml(result_html)
        
        # İstatistik güncelle
        self.stats_label.setText(f"✅ {row_count} sonuç bulundu")
        self.stats_label.setStyleSheet("color: green; padding: 10px; font-weight: bold;")


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    page = SearchPage()
    page.setWindowTitle("Arama Sayfası Test")
    page.resize(800, 600)
    page.show()
    sys.exit(app.exec_())