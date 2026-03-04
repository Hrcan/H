"""
Sunset Orange Theme - Gün Batımı Turuncu Tema
Sıcak turuncu ve altın tonları
"""

from .base_theme import BaseTheme


class SunsetOrangeTheme(BaseTheme):
    """Sunset Orange tema - Gün batımı renkleri"""
    
    def __init__(self):
        super().__init__()
        self.name = "Sunset Orange"
    
    def _define_colors(self):
        """Sunset Orange renk paleti"""
        return {
            # Ana renkler - Turuncu gradient
            'primary_start': '#ff6b35',
            'primary_end': '#ff4500',
            'accent': '#ffd700',
            
            # Background - Koyu turuncu tonları
            'bg_dark': '#1a0f00',
            'bg_medium': '#2a1600',
            'bg_light': '#3a1e00',
            
            # Text
            'text_primary': '#ffe8d0',
            'text_secondary': '#d0b090',
            'text_disabled': '#907050',
            
            # States
            'success': '#90ee90',
            'warning': '#ffaa00',
            'error': '#ff3333',
            'info': '#66ccff',
            
            # Border & Shadow
            'border': '#ff6b35',
            'shadow': 'rgba(255, 107, 53, 0.3)',
        }