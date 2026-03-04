"""
Database Manager - SQLite Veritabanı Yönetimi
Basit SQLite entegrasyonu - DataFrame'leri sakla ve oku
"""

import sqlite3
import pandas as pd
from pathlib import Path
from src.core.logger import get_logger

logger = get_logger()


class DatabaseManager:
    """SQLite veritabanı yöneticisi"""
    
    def __init__(self, db_path="data/database/excel_data.db"):
        """Database Manager'ı başlat"""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None
        
        # Otomatik bağlan
        self.connect()
        logger.info(f"Database Manager başlatıldı: {self.db_path}")
    
    def connect(self):
        """Veritabanına bağlan"""
        try:
            self.conn = sqlite3.connect(str(self.db_path))
            logger.debug(f"SQLite bağlantısı oluşturuldu: {self.db_path}")
            return self.conn
        except Exception as e:
            logger.error(f"SQLite bağlantı hatası: {e}")
            raise
    
    def save_dataframe(self, table_name, df):
        """DataFrame'i SQLite'a kaydet"""
        try:
            if df is None or df.empty:
                logger.warning(f"Boş DataFrame, tablo oluşturulmadı: {table_name}")
                return False
            
            # Tablo adını temizle (sadece alfanumerik ve alt çizgi)
            clean_name = ''.join(c for c in table_name if c.isalnum() or c == '_')
            
            # DataFrame'i kaydet (varsa üzerine yaz)
            df.to_sql(clean_name, self.conn, if_exists='replace', index=False)
            
            logger.info(f"✅ SQLite'a kaydedildi: {clean_name} ({len(df)} satır)")
            return True
            
        except Exception as e:
            logger.error(f"DataFrame kaydetme hatası ({table_name}): {e}")
            return False
    
    def get_table_names(self):
        """Tüm tablo isimlerini al"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
            tables = [row[0] for row in cursor.fetchall()]
            logger.debug(f"Tablolar bulundu: {len(tables)} adet")
            return tables
        except Exception as e:
            logger.error(f"Tablo listesi hatası: {e}")
            return []
    
    def get_table_info(self, table_name):
        """Tablo hakkında bilgi al"""
        try:
            cursor = self.conn.cursor()
            
            # Satır sayısı
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            
            # Sütun bilgileri
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            column_count = len(columns)
            
            # Dosya boyutu
            db_size = self.db_path.stat().st_size / 1024 / 1024  # MB
            
            return {
                'table_name': table_name,
                'rows': row_count,
                'columns': column_count,
                'size_mb': db_size
            }
            
        except Exception as e:
            logger.error(f"Tablo bilgisi hatası ({table_name}): {e}")
            return None
    
    def query_table(self, table_name, limit=100):
        """Tablodan veri oku (DataFrame olarak döndür)"""
        try:
            sql = f"SELECT * FROM {table_name} LIMIT {limit}"
            df = pd.read_sql_query(sql, self.conn)
            logger.debug(f"Sorgu başarılı: {table_name} ({len(df)} satır)")
            return df
        except Exception as e:
            logger.error(f"Sorgu hatası ({table_name}): {e}")
            return pd.DataFrame()
    
    def clear_all_tables(self):
        """Tüm tabloları sil"""
        try:
            tables = self.get_table_names()
            cursor = self.conn.cursor()
            
            for table in tables:
                cursor.execute(f"DROP TABLE IF EXISTS {table}")
                logger.info(f"Tablo silindi: {table}")
            
            self.conn.commit()
            logger.info("Tüm tablolar silindi")
            return True
            
        except Exception as e:
            logger.error(f"Tablo silme hatası: {e}")
            return False
    
    def close(self):
        """Bağlantıyı kapat"""
        if self.conn:
            self.conn.close()
            logger.debug("SQLite bağlantısı kapatıldı")
    
    def __del__(self):
        """Destructor - otomatik kapat"""
        self.close()


# Singleton instance
_db_manager = None

def get_database_manager():
    """Global Database Manager instance al"""
    global _db_manager
    if _db_manager is None:
        _db_manager = DatabaseManager()
    return _db_manager


# Test
if __name__ == "__main__":
    # Test için DataFrame oluştur
    test_df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Test1', 'Test2', 'Test3'],
        'value': [100, 200, 300]
    })
    
    # Database Manager'ı test et
    db = DatabaseManager()
    db.save_dataframe('test_table', test_df)
    
    tables = db.get_table_names()
    print(f"Tablolar: {tables}")
    
    info = db.get_table_info('test_table')
    print(f"Tablo bilgisi: {info}")
    
    result = db.query_table('test_table')
    print(f"Veri:\n{result}")
    
    db.close()
    print("✅ Test başarılı!")