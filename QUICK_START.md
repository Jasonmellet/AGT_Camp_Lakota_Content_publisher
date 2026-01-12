# Quick Start Guide

Get up and running with the Camp Lakota WordPress Publisher in 5 minutes.

---

## 🚀 Prerequisites

- Python 3.8 or higher
- WordPress site with REST API enabled
- WordPress admin access

---

## 📋 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Jasonmellet/AGT_Camp_Lakota_Content_publisher.git
cd AGT_Camp_Lakota_Content_publisher
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Credentials

```bash
# Copy the template
cp env.example .env

# Edit .env with your details
nano .env  # or use your preferred editor
```

**Required settings in `.env`:**
```bash
WP_SITE_URL=https://your-site.com
WP_USERNAME=your_admin_username
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx
```

**How to get Application Password:**
1. Log into WordPress Admin
2. Go to Users → Your Profile
3. Scroll to "Application Passwords"
4. Name it: "Camp Lakota Publisher"
5. Click "Add New Application Password"
6. Copy the generated password

### 4. Prepare Your Content

Add your content files to the appropriate directories:

```bash
content/
├── pages/          # Your 4 landing pages (JSON)
├── posts/          # Your 6 blog posts (JSON)
└── images/         # All images
```

**Content format:** See [CONTENT_REQUIREMENTS.md](CONTENT_REQUIREMENTS.md) for details.

### 5. Test Connection

```bash
# Set DRY_RUN=true in .env first!
python publish.py
```

This will validate:
- ✅ WordPress connection
- ✅ Authentication
- ✅ Content files
- ✅ Images
- ❌ **Won't publish anything** (dry run mode)

### 6. Publish Content

```bash
# Set DRY_RUN=false in .env
python publish.py
```

---

## 🆘 Common Issues

### "401 Unauthorized"
**Fix:** Check your username and application password in `.env`

### "404 Not Found"
**Fix:** Verify `WP_SITE_URL` is correct (no trailing slash)

### "Application Passwords option missing"
**Fix:** 
- Ensure WordPress 5.6+
- Check with hosting provider (some disable it)
- Try JWT authentication (advanced)

### "Module not found"
**Fix:** Reinstall dependencies
```bash
pip install -r requirements.txt
```

---

## 📚 Next Steps

- Read [SECURITY.md](SECURITY.md) for security best practices
- Check [ROADMAP.md](ROADMAP.md) for development phases
- Review [BACKUP_RESTORE.md](BACKUP_RESTORE.md) for backup strategies
- See [GITHUB_SETUP.md](GITHUB_SETUP.md) for repository management

---

## 🎯 Project Structure Overview

```
AGT_Camp_Lakota/
├── publish.py              # Main script - run this!
├── config.py               # Configuration loader
├── requirements.txt        # Python dependencies
├── .env                    # Your credentials (git-ignored)
├── modules/               # Core functionality
│   ├── auth.py            # WordPress authentication
│   ├── content.py         # Content processing
│   ├── images.py          # Image upload
│   ├── metadata.py        # Meta & schema
│   └── links.py           # Internal linking
├── content/               # Your content goes here
│   ├── pages/
│   ├── posts/
│   └── images/
└── logs/                  # Execution logs
```

---

## ✅ Quick Checklist

Before running:
- [ ] Cloned repository
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Created `.env` from `env.example`
- [ ] Generated WordPress Application Password
- [ ] Added credentials to `.env`
- [ ] Prepared content files
- [ ] Tested with `DRY_RUN=true`
- [ ] Ready to publish!

---

## 📞 Need Help?

- **Security questions:** See [SECURITY.md](SECURITY.md)
- **Content format:** See [CONTENT_REQUIREMENTS.md](CONTENT_REQUIREMENTS.md)
- **Technical specs:** See [TECH_SPEC.md](TECH_SPEC.md)
- **Backup issues:** See [BACKUP_RESTORE.md](BACKUP_RESTORE.md)
- **GitHub issues:** [Report a bug](https://github.com/Jasonmellet/AGT_Camp_Lakota_Content_publisher/issues)

---

**Time to complete:** ~5-10 minutes  
**Difficulty:** Easy  
**Result:** All Camp Lakota content published to WordPress! 🎉
