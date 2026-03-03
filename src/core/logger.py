"""
Logger Modülü
Uygulama genelinde kullanılacak merkezi loglama sistemi

Özellikler:
- Dosya ve konsol logları
- Log seviyeleri: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Otomatik log dosyası rotasyonu
- Renkli konsol çıktısı
- Thread-safe loglama
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from logging.handlers import RotatingFileHandler


class ColoredFormatter(logging.Formatter):
    """Konsol için renkli log formatter"""
    
    # ANSI renk kodları
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[35m',   # Magenta
        'RESET': '\033[0m'        # Reset
    }
    
    def format(self, record):
        """Log kaydını renklendir"""
        # Renk kodunu ekle
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{self.COLORS['RESET']}"
        
        # Format uygula
        return super().format(record)


class AppLogger:
    """Uygulama Logger Sınıfı"""
    
    def __init__(self, name='ExcelApp', log_dir='logs'):
        """
        Logger'ı başlat
        
        Args:
            name: Logger adı
            log_dir: Log dosyalarının kaydedileceği klasör
        """
        self.name = name
        self.log_dir = Path(log_dir)
        self.logger = None
        
        # Log dizinini oluştur
        self.log_dir.mkdir(exist_ok=True)
        
        # Logger'ı kur
        self._setup_logger()
    
    def _setup_logger(self):
        """Logger'ı yapılandır"""
        # Logger oluştur
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        
        # Mevcut handler'ları temizle
        self.logger.handlers.clear()
        
        # Dosya handler (Rotating - max 10MB, 5 backup)
        log_file = self.log_dir / f"{self.name}_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # Konsol handler (Renkli)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = ColoredFormatter(
            '%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # İlk log kaydı
        self.logger.info(f"Logger başlatıldı: {self.name}")
        self.logger.debug(f"Log dosyası: {log_file}")
    
    def get_logger(self):
        """Logger instance'ını döndür"""
        return self.logger
    
    def set_console_level(self, level):
        """
        Konsol log seviyesini ayarla
        
        Args:
            level: Log seviyesi (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        
        if level.upper() in level_map:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.StreamHandler):
                    handler.setLevel(level_map[level.upper()])
                    self.logger.info(f"Konsol log seviyesi değiştirildi: {level.upper()}")
    
    def set_file_level(self, level):
        """
        Dosya log seviyesini ayarla
        
        Args:
            level: Log seviyesi (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        
        if level.upper() in level_map:
            for handler in self.logger.handlers:
                if isinstance(handler, RotatingFileHandler):
                    handler.setLevel(level_map[level.upper()])
                    self.logger.info(f"Dosya log seviyesi değiştirildi: {level.upper()}")
    
    def get_log_files(self):
        """Mevcut log dosyalarını listele"""
        return sorted(self.log_dir.glob('*.log'), reverse=True)
    
    def read_log_file(self, log_file=None, lines=100):
        """
        Log dosyasını oku
        
        Args:
            log_file: Okunacak log dosyası (None ise son dosya)
            lines: Okunacak satır sayısı (None ise tümü)
        
        Returns:
            list: Log satırları
        """
        if log_file is None:
            log_files = self.get_log_files()
            if not log_files:
                return []
            log_file = log_files[0]
        
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                if lines:
                    # Son N satırı oku
                    all_lines = f.readlines()
                    return all_lines[-lines:]
                else:
                    # Tüm dosyayı oku
                    return f.readlines()
        except Exception as e:
            self.logger.error(f"Log dosyası okunamadı: {e}")
            return []
    
    def clear_old_logs(self, days=30):
        """
        Eski log dosyalarını temizle
        
        Args:
            days: Silinecek log dosyalarının yaşı (gün)
        """
        from datetime import timedelta
        
        cutoff = datetime.now() - timedelta(days=days)
        deleted_count = 0
        
        for log_file in self.log_dir.glob('*.log*'):
            # Dosya oluşturma tarihini kontrol et
            file_time = datetime.fromtimestamp(log_file.stat().st_ctime)
            if file_time < cutoff:
                try:
                    log_file.unlink()
                    deleted_count += 1
                except Exception as e:
                    self.logger.error(f"Log dosyası silinemedi {log_file}: {e}")
        
        if deleted_count > 0:
            self.logger.info(f"{deleted_count} eski log dosyası temizlendi")


# Global logger instance
_app_logger = None


def get_logger(name='ExcelApp'):
    """
    Global logger instance'ını döndür
    
    Args:
        name: Logger adı
    
    Returns:
        logging.Logger: Logger instance
    """
    global _app_logger
    
    if _app_logger is None:
        _app_logger = AppLogger(name)
    
    return _app_logger.get_logger()


def get_app_logger():
    """
    AppLogger instance'ını döndür
    
    Returns:
        AppLogger: AppLogger instance
    """
    global _app_logger
    
    if _app_logger is None:
        _app_logger = AppLogger()
    
    return _app_logger


# Test kodu
if __name__ == "__main__":
    # Logger'ı test et
    logger = get_logger()
    
    logger.debug("Bu bir DEBUG mesajıdır")
    logger.info("Bu bir INFO mesajıdır")
    logger.warning("Bu bir WARNING mesajıdır")
    logger.error("Bu bir ERROR mesajıdır")
    logger.critical("Bu bir CRITICAL mesajıdır")
    
    # Log dosyalarını listele
    app_logger = get_app_logger()
    log_files = app_logger.get_log_files()
    print(f"\n[LOG FILES] {len(log_files)} log dosyasi bulundu:")
    for lf in log_files:
        print(f"  - {lf.name}")
    
    # Son 5 satırı oku
    print("\n[LAST LOGS] Son 5 log satiri:")
    last_logs = app_logger.read_log_file(lines=5)
    for line in last_logs:
        print(f"  {line.strip()}")
    
    print("\n[OK] Logger testi tamamlandi!")
