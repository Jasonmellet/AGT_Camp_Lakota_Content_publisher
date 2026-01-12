# Camp Lakota - WordPress Content Publisher

A streamlined tool to publish landing pages and blog posts to WordPress via the REST API.

## Project Overview

This project publishes pre-created content for Camp Lakota to WordPress, including:
- **4 Landing Pages** with full metadata and schema
- **6 Blog Posts** with images, internal links, and SEO optimization

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your WordPress credentials
```

3. Add your content to the `/content` directory

4. Run the publisher:
```bash
python publish.py
```

## Project Structure

```
AGT_Camp_Lakota/
├── README.md                 # This file
├── ROADMAP.md               # Development roadmap
├── TECH_SPEC.md             # Technical specifications
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your credentials (git-ignored)
├── config.py               # Configuration handler
├── publish.py              # Main publishing script
├── content/
│   ├── pages/             # Landing pages (JSON/Markdown)
│   ├── posts/             # Blog posts (JSON/Markdown)
│   └── images/            # Image files
├── modules/
│   ├── auth.py            # WordPress authentication
│   ├── content.py         # Content processor
│   ├── images.py          # Image uploader
│   ├── metadata.py        # Meta & schema handler
│   └── links.py           # Internal linking
└── logs/                   # Execution logs

```

## Status Tracking

- [x] Project setup complete ✅
- [x] Git repository initialized and pushed to GitHub ✅
- [x] Documentation complete ✅
- [x] Core application built ✅
- [x] All modules implemented ✅
- [ ] **Next: Configure WordPress credentials** 👈 Start here!
- [ ] Content files added
- [ ] Test connection to WordPress
- [ ] Landing pages published
- [ ] Blog posts published
- [ ] Internal links verified
- [ ] Schema markup validated

## Documentation

### Core Documentation
- [ROADMAP.md](ROADMAP.md) - Development phases and timeline
- [TECH_SPEC.md](TECH_SPEC.md) - Technical specifications and requirements
- [CONTENT_REQUIREMENTS.md](CONTENT_REQUIREMENTS.md) - What we need from you

### Security & Git
- [SECURITY.md](SECURITY.md) - Security guide and authentication setup
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Git branching strategy and workflow

### Backup & Management
- [BACKUP_RESTORE.md](BACKUP_RESTORE.md) - Complete backup and recovery guide
- [CHANGELOG.md](CHANGELOG.md) - Version history and changes
- [GITHUB_SETUP.md](GITHUB_SETUP.md) - Repository configuration guide

## Git Repository

**GitHub:** [AGT_Camp_Lakota_Content_publisher](https://github.com/Jasonmellet/AGT_Camp_Lakota_Content_publisher)

**Current Version:** v0.1.0  
**Current Branch:** `develop`  
**Branches:** `main` (stable), `develop` (active development)

## Support

For issues or questions, refer to the documentation files above.
