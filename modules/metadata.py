"""
Metadata and Schema Module
Handles SEO metadata and schema markup
"""

import json
from typing import Dict, Optional


class MetadataHandler:
    """Handle SEO metadata and schema markup"""
    
    def __init__(self):
        self.schema_templates = {}
    
    def generate_article_schema(self, post: Dict, site_info: Dict) -> str:
        """
        Generate Article schema (JSON-LD) for blog post
        
        Args:
            post: Post data with title, excerpt, author, etc.
            site_info: Site information
        
        Returns:
            JSON-LD schema as string
        """
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": post.get('title', ''),
            "description": post.get('excerpt', ''),
        }
        
        # Add author if provided
        if post.get('author_name'):
            schema["author"] = {
                "@type": "Person",
                "name": post['author_name']
            }
        
        # Add publisher if provided
        if site_info.get('site_name'):
            schema["publisher"] = {
                "@type": "Organization",
                "name": site_info['site_name']
            }
        
        # Add image if provided
        if post.get('featured_image_url'):
            schema["image"] = post['featured_image_url']
        
        # Add dates if provided
        if post.get('date_published'):
            schema["datePublished"] = post['date_published']
        
        if post.get('date_modified'):
            schema["dateModified"] = post['date_modified']
        
        return json.dumps(schema, indent=2)
    
    def generate_local_business_schema(self, business_info: Dict) -> str:
        """
        Generate LocalBusiness schema for Camp Lakota
        
        Args:
            business_info: Dict with business details
        
        Returns:
            JSON-LD schema as string
        """
        schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": business_info.get('name', 'Camp Lakota'),
            "description": business_info.get('description', ''),
        }
        
        # Add address if provided
        if business_info.get('address'):
            addr = business_info['address']
            schema["address"] = {
                "@type": "PostalAddress",
                "streetAddress": addr.get('street', ''),
                "addressLocality": addr.get('city', ''),
                "addressRegion": addr.get('state', ''),
                "postalCode": addr.get('zip', ''),
                "addressCountry": addr.get('country', 'US')
            }
        
        # Add contact info
        if business_info.get('phone'):
            schema["telephone"] = business_info['phone']
        
        if business_info.get('email'):
            schema["email"] = business_info['email']
        
        if business_info.get('website'):
            schema["url"] = business_info['website']
        
        # Add logo
        if business_info.get('logo'):
            schema["logo"] = business_info['logo']
        
        # Add image
        if business_info.get('image'):
            schema["image"] = business_info['image']
        
        # Add opening hours if provided
        if business_info.get('opening_hours'):
            schema["openingHours"] = business_info['opening_hours']
        
        # Add price range if provided
        if business_info.get('price_range'):
            schema["priceRange"] = business_info['price_range']
        
        return json.dumps(schema, indent=2)
    
    def generate_organization_schema(self, org_info: Dict) -> str:
        """
        Generate Organization schema
        
        Args:
            org_info: Organization details
        
        Returns:
            JSON-LD schema as string
        """
        schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": org_info.get('name', 'Camp Lakota'),
            "url": org_info.get('url', ''),
        }
        
        if org_info.get('logo'):
            schema["logo"] = org_info['logo']
        
        if org_info.get('description'):
            schema["description"] = org_info['description']
        
        # Social media profiles
        if org_info.get('social_profiles'):
            schema["sameAs"] = org_info['social_profiles']
        
        return json.dumps(schema, indent=2)
    
    def inject_schema_into_content(self, content: str, schema_json: str) -> str:
        """
        Inject schema markup into HTML content
        
        Args:
            content: HTML content
            schema_json: JSON-LD schema string
        
        Returns:
            Content with schema injected
        """
        schema_script = f'<script type="application/ld+json">\n{schema_json}\n</script>\n\n'
        return schema_script + content
    
    def prepare_yoast_meta(self, content: Dict) -> Dict:
        """
        Prepare meta fields for Yoast SEO plugin
        
        Args:
            content: Content dict with meta information
        
        Returns:
            Dict with Yoast meta fields
        """
        meta = {}
        
        if content.get('meta_title'):
            meta['yoast_wpseo_title'] = content['meta_title']
        
        if content.get('meta_description'):
            meta['yoast_wpseo_metadesc'] = content['meta_description']
        
        if content.get('focus_keyword'):
            meta['yoast_wpseo_focuskw'] = content['focus_keyword']
        
        return meta
    
    def prepare_rankmath_meta(self, content: Dict) -> Dict:
        """
        Prepare meta fields for Rank Math plugin
        
        Args:
            content: Content dict with meta information
        
        Returns:
            Dict with Rank Math meta fields
        """
        meta = {}
        
        if content.get('meta_title'):
            meta['rank_math_title'] = content['meta_title']
        
        if content.get('meta_description'):
            meta['rank_math_description'] = content['meta_description']
        
        if content.get('focus_keyword'):
            meta['rank_math_focus_keyword'] = content['focus_keyword']
        
        return meta
