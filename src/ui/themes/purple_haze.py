"""
Purple Haze Theme - Mor Sis Tema
İyileştirilmiş mor ve pembe tonları (mevcut tema)
"""

from .base_theme import BaseTheme


class PurpleHazeTheme(BaseTheme):
    """Purple Haze tema - Mor ve pembe tonları (varsayılan)"""
    
    def __init__(self):
        super().__init__()
        self.name = "Purple Haze"
    
    def _define_colors(self):
        """Purple Haze renk paleti"""
        return {
            # Ana renkler - Mor-pembe gradient
            'primary_start': '#667eea',
            'primary_end': '#9b6bff',
            'accent': '#ff6bff',
            
            # Background - Koyu mor tonları
            'bg_dark': '#1a0f2e',
            'bg_medium': '#2d1f40',
            'bg_light': '#3d2d50',
            
            # Text
            'text_primary': '#f0e8ff',
            'text_secondary': '#c0b0d0',
            'text_disabled': '#8070a0',
            
            # States
            'success': '#4CAF50',
            'warning': '#FF9800',
            'error': '#F44336',
            'info': '#9b6bff',
            
            # Border & Shadow
            'border': '#667eea',
            'shadow': 'rgba(155, 107, 255, 0.3)',
        }