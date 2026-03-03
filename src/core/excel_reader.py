"""
Excel Reader Module
Excel dosyalarını okuma ve parse etme işlemleri

Desteklenen formatlar:
- Hatalı Biten İşler Raporu (A-E kolonları)
- Uzun Süren İşler Raporu (A-D kolonları)
"""

import pandas as pd
from pathlib import Path
from typing import Optional, List, Dict
import logging

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ExcelReader:
    """Excel dosyalarını okumak için sınıf"""
    
    def __init__(self):
        """ExcelReader sınıfını başlat"""
        self.encoding = 'utf-8'
        self.engine = 'openpyxl'
    
    def read_hatali_isler(self, file_path: str, sheet_name: Optional[str] = None) -> pd.DataFrame:
        """
        Hatalı Biten İşler Excel dosyasını oku
        
        Args:
            file_path: Excel dosyasının yolu
            sheet_name: Okunacak sheet adı (None ise tüm sheet'ler)
        
        Returns:
            pandas DataFrame: Okunan veriler
            
        Kolon Yapısı (A-E):
            A: JCL Adı
            B: Hatalı Çalışma Sayısı (Aylık)
            C: Son Hatalı Çalışma Tarihi
            D: Hatalı Çalışma Sayısı (Yıllık)
            E: Sorumlu Ekip
        """
        try:
            logger.info(f"Hatalı İşler Excel okunuyor: {file_path}")
            
            # Dosya varlığını kontrol et
            if not Path(file_path).exists():
                raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
            
            # Sheet adı verilmediyse tüm sheet'leri oku
            if sheet_name is None:
                excel_file = pd.ExcelFile(file_path, engine=self.engine)
                sheet_names = excel_file.sheet_names
                logger.info(f"Toplam {len(sheet_names)} sheet bulundu: {sheet_names}")
                
                # Tüm sheet'leri oku ve birleştir
                all_data = []
                for sheet in sheet_names:
                    df = self._read_hatali_sheet(file_path, sheet)
                    if df is not None and not df.empty:
                        df['Sheet_Adi'] = sheet  # Sheet adını ekle
                        all_data.append(df)
                
                if all_data:
                    result = pd.concat(all_data, ignore_index=True)
                    logger.info(f"Toplam {len(result)} satır veri okundu")
                    return result
                else:
                    logger.warning("Hiç veri okunamadı")
                    return pd.DataFrame()
            else:
                # Sadece belirtilen sheet'i oku
                return self._read_hatali_sheet(file_path, sheet_name)
                
        except Exception as e:
            logger.error(f"Hatalı İşler Excel okuma hatası: {e}")
            raise
    
    def _read_hatali_sheet(self, file_path: str, sheet_name: str) -> Optional[pd.DataFrame]:
        """
        Hatalı İşler sheet'ini oku ve kolonları düzenle
        
        Args:
            file_path: Excel dosyasının yolu
            sheet_name: Sheet adı
            
        Returns:
            pandas DataFrame veya None
        """
        try:
            # Excel'i oku (A-E kolonları: 0-4)
            df = pd.read_excel(
                file_path,
                sheet_name=sheet_name,
                engine=self.engine,
                usecols="A:E"  # Sadece A-E kolonlarını oku
            )
            
            # Kolon isimlerini standartlaştır
            if len(df.columns) >= 5:
                df.columns = [
                    'JCL_Adi',
                    'Hatali_Calisma_Sayisi_Aylik',
                    'Son_Hatali_Calisma_Tarihi',
                    'Hatali_Calisma_Sayisi_Yillik',
                    'Ekip_Adi'
                ]
            
            # Boş satırları temizle
            df = df.dropna(subset=['JCL_Adi'])
            
            # JCL adını string'e çevir
            df['JCL_Adi'] = df['JCL_Adi'].astype(str).str.strip()
            
            logger.info(f"Sheet '{sheet_name}': {len(df)} satır okundu")
            return df
            
        except Exception as e:
            logger.error(f"Sheet '{sheet_name}' okuma hatası: {e}")
            return None
    
    def read_uzun_isler(self, file_path: str, sheet_name: Optional[str] = None) -> pd.DataFrame:
        """
        Uzun Süren İşler Excel dosyasını oku
        
        Args:
            file_path: Excel dosyasının yolu
            sheet_name: Okunacak sheet adı (None ise tüm sheet'ler)
        
        Returns:
            pandas DataFrame: Okunan veriler
            
        Kolon Yapısı (A-D):
            A: JCL Adı
            B: Çalışma Sayısı (Adet)
            C: Çalışma Süresi (Dakika)
            D: Sorumlu Ekip
        """
        try:
            logger.info(f"Uzun İşler Excel okunuyor: {file_path}")
            
            # Dosya varlığını kontrol et
            if not Path(file_path).exists():
                raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
            
            # Sheet adı verilmediyse tüm sheet'leri oku
            if sheet_name is None:
                excel_file = pd.ExcelFile(file_path, engine=self.engine)
                sheet_names = excel_file.sheet_names
                logger.info(f"Toplam {len(sheet_names)} sheet bulundu: {sheet_names}")
                
                # Tüm sheet'leri oku ve birleştir
                all_data = []
                for sheet in sheet_names:
                    df = self._read_uzun_sheet(file_path, sheet)
                    if df is not None and not df.empty:
                        df['Sheet_Adi'] = sheet  # Sheet adını ekle
                        all_data.append(df)
                
                if all_data:
                    result = pd.concat(all_data, ignore_index=True)
                    logger.info(f"Toplam {len(result)} satır veri okundu")
                    return result
                else:
                    logger.warning("Hiç veri okunamadı")
                    return pd.DataFrame()
            else:
                # Sadece belirtilen sheet'i oku
                return self._read_uzun_sheet(file_path, sheet_name)
                
        except Exception as e:
            logger.error(f"Uzun İşler Excel okuma hatası: {e}")
            raise
    
    def _read_uzun_sheet(self, file_path: str, sheet_name: str) -> Optional[pd.DataFrame]:
        """
        Uzun İşler sheet'ini oku ve kolonları düzenle
        
        Args:
            file_path: Excel dosyasının yolu
            sheet_name: Sheet adı
            
        Returns:
            pandas DataFrame veya None
        """
        try:
            # Excel'i oku (A-D kolonları: 0-3)
            df = pd.read_excel(
                file_path,
                sheet_name=sheet_name,
                engine=self.engine,
                usecols="A:D"  # Sadece A-D kolonlarını oku
            )
            
            # Kolon isimlerini standartlaştır
            if len(df.columns) >= 4:
                df.columns = [
                    'JCL_Adi',
                    'Calisma_Sayisi',
                    'Sure_Dakika',
                    'Ekip_Adi'
                ]
            
            # Boş satırları temizle
            df = df.dropna(subset=['JCL_Adi'])
            
            # JCL adını string'e çevir
            df['JCL_Adi'] = df['JCL_Adi'].astype(str).str.strip()
            
            logger.info(f"Sheet '{sheet_name}': {len(df)} satır okundu")
            return df
            
        except Exception as e:
            logger.error(f"Sheet '{sheet_name}' okuma hatası: {e}")
            return None
    
    def get_excel_info(self, file_path: str) -> Dict[str, any]:
        """
        Excel dosyası hakkında bilgi al
        
        Args:
            file_path: Excel dosyasının yolu
            
        Returns:
            Dict: Dosya bilgileri
        """
        try:
            excel_file = pd.ExcelFile(file_path, engine=self.engine)
            
            info = {
                'dosya_adi': Path(file_path).name,
                'dosya_yolu': str(Path(file_path).absolute()),
                'sheet_sayisi': len(excel_file.sheet_names),
                'sheet_isimleri': excel_file.sheet_names,
                'boyut_mb': Path(file_path).stat().st_size / (1024 * 1024)
            }
            
            return info
            
        except Exception as e:
            logger.error(f"Excel bilgi alma hatası: {e}")
            return {}
    
    def get_unique_ekipler(self, df: pd.DataFrame) -> List[str]:
        """
        DataFrame'den benzersiz ekip adlarını al
        
        Args:
            df: pandas DataFrame
            
        Returns:
            List[str]: Benzersiz ekip adları
        """
        if 'Ekip_Adi' in df.columns:
            ekipler = df['Ekip_Adi'].dropna().unique().tolist()
            ekipler = [str(ekip).strip() for ekip in ekipler]
            ekipler = sorted([e for e in ekipler if e])  # Boş olanları çıkar ve sırala
            return ekipler
        return []


# Örnek kullanım
if __name__ == "__main__":
    reader = ExcelReader()
    
    # Test için
    print("ExcelReader sınıfı hazır!")
    print(f"Engine: {reader.engine}")