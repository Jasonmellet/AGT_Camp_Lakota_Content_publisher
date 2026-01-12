"""
Internal Linking Module
Handles internal link mapping and insertion
"""

import re
from typing import Dict, List, Optional


class InternalLinkManager:
    """Manage internal links between pages and posts"""
    
    def __init__(self, session):
        """
        Initialize link manager
        Args:
            session: Authenticated requests session
        """
        self.session = session
        self.slug_to_url = {}  # Map slugs to full URLs
        self.slug_to_id = {}   # Map slugs to WordPress IDs
    
    def register_published_content(self, slug: str, url: str, wp_id: int):
        """
        Register published content for linking
        
        Args:
            slug: Content slug
            url: Full URL to content
            wp_id: WordPress post/page ID
        """
        self.slug_to_url[slug] = url
        self.slug_to_id[slug] = wp_id
        print(f"📌 Registered: {slug} → {url}")
    
    def replace_link_placeholders(self, content: str, link_map: Optional[Dict] = None) -> str:
        """
        Replace link placeholders with actual URLs
        
        Supports formats:
        - {{link:slug}} → full URL
        - {{link:slug|anchor text}} → <a href="url">anchor text</a>
        
        Args:
            content: HTML content with placeholders
            link_map: Optional custom link mapping
        
        Returns:
            Content with placeholders replaced
        """
        if link_map is None:
            link_map = self.slug_to_url
        
        # Pattern: {{link:slug}} or {{link:slug|anchor text}}
        pattern = r'\{\{link:([^|}]+)(?:\|([^}]+))?\}\}'
        
        def replace_match(match):
            slug = match.group(1).strip()
            anchor_text = match.group(2).strip() if match.group(2) else None
            
            # Get URL for slug
            url = link_map.get(slug)
            
            if not url:
                print(f"⚠️  Link placeholder not found: {{{{link:{slug}}}}}")
                return match.group(0)  # Return unchanged
            
            # If anchor text provided, create full link
            if anchor_text:
                return f'<a href="{url}">{anchor_text}</a>'
            else:
                return url
        
        updated_content = re.sub(pattern, replace_match, content)
        return updated_content
    
    def find_link_placeholders(self, content: str) -> List[str]:
        """
        Find all link placeholders in content
        
        Args:
            content: HTML content
        
        Returns:
            List of slugs referenced in placeholders
        """
        pattern = r'\{\{link:([^|}]+)(?:\|[^}]+)?\}\}'
        matches = re.findall(pattern, content)
        return [slug.strip() for slug in matches]
    
    def update_content_links(self, wp_id: int, content_type: str, updated_content: str) -> bool:
        """
        Update WordPress content with resolved links
        
        Args:
            wp_id: WordPress post/page ID
            content_type: 'posts' or 'pages'
            updated_content: Content with resolved links
        
        Returns:
            True if successful
        """
        from config import Config
        
        try:
            response = self.session.post(
                Config.get_api_url(f'{content_type}/{wp_id}'),
                json={'content': updated_content},
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ Updated links for {content_type[:-1]} ID: {wp_id}")
                return True
            else:
                print(f"⚠️  Failed to update links for {content_type[:-1]} ID {wp_id}: {response.status_code}")
                return False
        
        except Exception as e:
            print(f"❌ Error updating links for {content_type[:-1]} ID {wp_id}: {e}")
            return False
    
    def process_content_links(self, content_items: List[Dict], content_type: str):
        """
        Process and update internal links for all content
        
        Args:
            content_items: List of dicts with 'id', 'slug', 'content'
            content_type: 'posts' or 'pages'
        """
        print(f"\n🔗 Processing internal links for {content_type}...")
        
        for item in content_items:
            wp_id = item.get('id')
            content = item.get('content', '')
            
            if not wp_id or not content:
                continue
            
            # Find placeholders
            placeholders = self.find_link_placeholders(content)
            
            if not placeholders:
                continue
            
            print(f"\n📝 Processing {item.get('slug', 'unknown')}...")
            print(f"   Found {len(placeholders)} link placeholder(s)")
            
            # Replace placeholders
            updated_content = self.replace_link_placeholders(content)
            
            # Update if content changed
            if updated_content != content:
                self.update_content_links(wp_id, content_type, updated_content)
            else:
                print(f"   No changes needed")
    
    def get_url_for_slug(self, slug: str) -> Optional[str]:
        """Get URL for a given slug"""
        return self.slug_to_url.get(slug)
    
    def get_id_for_slug(self, slug: str) -> Optional[int]:
        """Get WordPress ID for a given slug"""
        return self.slug_to_id.get(slug)
