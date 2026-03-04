"""
Theme Manager - Tema Yönetim Sistemi
Temaları yönetir ve değiştirir
"""

from .cyber_blue import CyberBlueTheme
from .neon_green import NeonGreenTheme
from .sunset_orange import SunsetOrangeTheme
from .purple_haze import PurpleHazeTheme


class ThemeManager:
    """Tema yönetim sınıfı - Singleton pattern"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThemeManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Theme Manager'ı başlat"""
        if self._initialized:
            return
        
        self._initialized = True
        self._themes = {}
        self._current_theme = None
        self._register_themes()
        self._set_default_theme()
    
    def _register_themes(self):
        """Mevcut temaları kaydet"""
        self._themes = {
            'purple_haze': PurpleHazeTheme(),
            'cyber_blue': CyberBlueTheme(),
            'neon_green': NeonGreenTheme(),
            'sunset_orange': SunsetOrangeTheme(),
        }
    
    def _set_default_theme(self):
        """Varsayılan temayı ayarla"""
        self._current_theme = self._themes['purple_haze']
    
    def get_theme(self, theme_name=None):
        """Belirtilen temayı döndür"""
        if theme_name is None:
            return self._current_theme
        
        if theme_name in self._themes:
            return self._themes[theme_name]
        
        # Varsayılan temayı döndür
        return self._current_theme
    
    def set_theme(self, theme_name):
        """Aktif temayı değiştir"""
        if theme_name in self._themes:
            self._current_theme = self._themes[theme_name]
            return True
        return False
    
    def get_available_themes(self):
        """Mevcut temaların listesini döndür"""
        return {
            name: theme.name 
            for name, theme in self._themes.items()
        }
    
    def get_stylesheet(self, theme_name=None):
        """Tema stylesheet'ini döndür"""
        theme = self.get_theme(theme_name)
        return theme.get_stylesheet()
    
    def get_colors(self, theme_name=None):
        """Tema renklerini döndür"""
        theme = self.get_theme(theme_name)
        return theme.get_colors()
    
    def get_gradient(self, theme_name=None):
        """Tema gradient renklerini döndür"""
        theme = self.get_theme(theme_name)
        return theme.get_gradient()