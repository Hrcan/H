"""
Neon Green Theme - Neon Yeşil Tema
Matrix tarzı yeşil neon görünüm
"""

from .base_theme import BaseTheme


class NeonGreenTheme(BaseTheme):
    """Neon Green tema - Matrix yeşili"""
    
    def __init__(self):
        super().__init__()
        self.name = "Neon Green"
    
    def _define_colors(self):
        """Neon Green renk paleti"""
        return {
            # Ana renkler - Yeşil gradient
            'primary_start': '#00ff88',
            'primary_end': '#00cc6a',
            'accent': '#39ff14',
            
            # Background - Koyu yeşil tonları
            'bg_dark': '#001a0f',
            'bg_medium': '#002618',
            'bg_light': '#003320',
            
            # Text
            'text_primary': '#e0ffe0',
            'text_secondary': '#b0e0b0',
            'text_disabled': '#608060',
            
            # States
            'success': '#00ff88',
            'warning': '#ffcc00',
            'error': '#ff4444',
            'info': '#00ccff',
            
            # Border & Shadow
            'border': '#00cc6a',
            'shadow': 'rgba(0, 255, 136, 0.3)',
        }