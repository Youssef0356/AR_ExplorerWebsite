import os
import re

html_path = "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update features grid and card CSS
old_card_css = """    .features-grid {
      display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5px;
      background: var(--card-border); border: 1px solid var(--card-border);
    }
    .feature-card {
      background: var(--bg); padding: 3rem;
      transition: background .25s;
      position: relative; overflow: hidden;
    }"""
new_card_css = """    .features-grid {
      display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem;
    }
    .feature-card {
      background: rgba(30, 40, 60, 0.4); padding: 3rem;
      border: 1px solid var(--card-border);
      border-radius: 16px;
      transition: background .25s, transform .2s, box-shadow .2s;
      position: relative; overflow: hidden;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    .feature-card:hover {
      background: rgba(40, 50, 70, 0.6);
      transform: translateY(-4px);
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), inset 0 0 0 1px var(--cyan);
    }"""

html = html.replace(old_card_css, new_card_css)

# 2. Add extra CSS for the new gallery
gallery_css = """
    /* ── NEW SCREENSHOT GALLERY ── */
    .gallery-container {
      display: flex; flex-direction: column; align-items: center; gap: 2rem;
    }
    .gallery-tabs {
      display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;
      background: rgba(255,255,255,0.03); padding: 0.5rem; border-radius: 100px;
      border: 1px solid var(--card-border);
      backdrop-filter: blur(10px);
    }
    .gallery-tab {
      background: transparent; color: var(--muted); border: none;
      padding: 0.6rem 1.5rem; border-radius: 100px; font-weight: 600;
      font-size: 0.85rem; cursor: pointer; transition: all 0.3s;
      font-family: 'DM Sans', sans-serif;
    }
    .gallery-tab:hover { color: #fff; }
    .gallery-tab.active { background: var(--cyan); color: #000; box-shadow: 0 0 20px rgba(0,229,255,0.4); }

    .gallery-stage {
      position: relative; height: 600px; width: 100%;
      display: flex; align-items: center; justify-content: center;
      perspective: 1000px;
    }
    .gallery-phone {
      position: relative; width: 280px; height: 570px;
      background: #0d1424; border-radius: 36px;
      border: 2px solid rgba(255,255,255,0.1);
      box-shadow: 0 40px 100px rgba(0,0,0,0.8), inset 0 0 10px rgba(255,255,255,0.05);
      overflow: hidden;
      transform: rotateY(0deg); transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
      z-index: 5;
    }
    .gallery-phone:hover { transform: translateY(-5px) scale(1.02); }
    .gallery-notch {
      position: absolute; top: 0; left: 50%; transform: translateX(-50%);
      width: 120px; height: 28px; background: #0d1424; border-radius: 0 0 18px 18px;
      z-index: 10;
    }
    .gallery-screen {
      width: 100%; height: 100%;
      background: #000; display: flex; align-items: center; justify-content: center;
      overflow: hidden; position: relative;
    }
    .gallery-screen img {
      width: 100%; height: 100%; object-fit: cover;
      position: absolute; top: 0; left: 0;
      opacity: 0; transform: scale(1.05);
      transition: opacity 0.5s ease, transform 0.5s ease;
    }
    .gallery-screen img.active { opacity: 1; transform: scale(1); }
"""
html = html.replace('/* ── STATS ── */', gallery_css + '\n    /* ── STATS ── */')

# 3. Replace the Screenshots HTML Section
old_screenshots_html = """<!-- SCREENSHOTS -->
<section id="screenshots">
  <div class="container">
    <div class="screenshots-intro reveal">
      <div class="section-label">The app</div>
      <h2 class="section-title">Designed for<br/><em>deep focus</em></h2>
      <p>A dark, focused interface built for learning — not distraction. Every screen is crafted to help you absorb and retain complex AR knowledge.</p>
    </div>
    <div class="phones-stage reveal">
      <!-- Left phone: Learning Roadmap -->
      <div class="phone-frame left">
        <div class="phone-notch"></div>
        <div class="phone-screen">
          <div class="phone-screen-inner">
            <div class="phone-status-bar"><span>9:41</span><span>●●●</span></div>
            <div class="screen-content">
              <div class="screen-module-title">Systems Engineer</div>
              <div class="screen-heading">Developer Roadmap</div>
              <div style="margin-top:8px">
                <div class="screen-roadmap-item">
                  <div class="screen-roadmap-dot" style="background:var(--cyan)"></div>
                  <div class="screen-roadmap-text"><strong>Vuforia Engine</strong>Free · Zone 1</div>
                </div>
                <div class="screen-roadmap-item">
                  <div class="screen-roadmap-dot" style="background:var(--purple)"></div>
                  <div class="screen-roadmap-text"><strong>ARKit / ARCore</strong>Premium · Zone 2</div>
                </div>
                <div class="screen-roadmap-item">
                  <div class="screen-roadmap-dot" style="background:rgba(255,255,255,0.15)"></div>
                  <div class="screen-roadmap-text"><strong>Spatial UI</strong>Locked</div>
                </div>
                <div class="screen-roadmap-item">
                  <div class="screen-roadmap-dot" style="background:rgba(255,255,255,0.15)"></div>
                  <div class="screen-roadmap-text"><strong>Multiplayer AR</strong>Locked</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Center phone: Module content -->
      <div class="phone-frame center">
        <div class="phone-notch"></div>
        <div class="phone-screen">
          <div class="phone-screen-inner">
            <div class="phone-status-bar"><span>9:41</span><span>●●●</span></div>
            <div class="screen-content">
              <div class="screen-module-title">Premium Certificate</div>
              <img src="assets/images/ARexplorerCertif.png" style="width:100%; border-radius:4px; margin: 10px 0; box-shadow: 0 4px 12px rgba(168,85,247,0.3);" />
              <div class="screen-btn" style="background: var(--gold)">Share Achievement ↗</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right phone: Quiz -->
      <div class="phone-frame right">
        <div class="phone-notch"></div>
        <div class="phone-screen">
          <div class="phone-screen-inner">
            <div class="phone-status-bar"><span>9:41</span><span>●●●</span></div>
            <div class="screen-content">
              <div class="screen-module-title">Quiz · Question 3 of 5</div>
              <div class="screen-quiz-q">What does 8th Wall provide that native WebXR does not?</div>
              <div class="screen-option">A proprietary 3D rendering engine</div>
              <div class="screen-option selected">SLAM tracking on any smartphone browser ✓</div>
              <div class="screen-option">Cloud hosting for HTML files</div>
              <div class="screen-option">Access to the phone's battery API</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

new_screenshots_html = """<!-- SCREENSHOTS OVERHAUL -->
<section id="screenshots">
  <div class="container">
    <div class="screenshots-intro reveal">
      <div class="section-label">Real Experience</div>
      <h2 class="section-title">Step inside the<br/><em>AR Workspace</em></h2>
      <p>A beautifully gamified, dark-mode focused environment. Designed to keep you immersed while mastering spatial computing concepts and interactive code challenges.</p>
    </div>
    
    <div class="gallery-container reveal">
      <div class="gallery-tabs">
        <button class="gallery-tab active" data-cat="all">All Features</button>
        <button class="gallery-tab" data-cat="roadmap">Roadmap & Interview</button>
        <button class="gallery-tab" data-cat="games">Modules & Games</button>
        <button class="gallery-tab" data-cat="analytics">Analytics</button>
      </div>

      <div class="gallery-stage">
        <div class="gallery-phone">
          <div class="gallery-notch"></div>
          <div class="gallery-screen" id="gallery-screen">
            <!-- Images will be injected here via Javascript -->
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

html = html.replace(old_screenshots_html, new_screenshots_html)

# 4. Add the Javascript for the Interactive Gallery
gallery_js = """
// ── SCREENSHOT GALLERY LOGIC ──
const screenshotsList = [
  // Roadmap & Interview mapped first!
  { src: 'Screenshot_2026-04-12-21-35-53-333_com.the356company.arexplorer.jpg', cat: 'roadmap' }, // Roadmap (02)
  { src: 'Screenshot_2026-04-12-21-36-10-172_com.the356company.arexplorer.jpg', cat: 'roadmap' }, // Interview (05)
  { src: 'Screenshot_2026-04-12-21-36-13-192_com.the356company.arexplorer.jpg', cat: 'roadmap' }, // Interview (06)
  { src: 'Screenshot_2026-04-12-21-36-18-388_com.the356company.arexplorer.jpg', cat: 'roadmap' }, // Interview (07)
  { src: 'Screenshot_2026-04-12-21-36-25-375_com.the356company.arexplorer.jpg', cat: 'roadmap' }, // Interview (08)
  
  // Games & Modules
  { src: 'Screenshot_2026-04-12-21-35-57-227_com.the356company.arexplorer.jpg', cat: 'games' }, // Systems Eng (03)
  { src: 'Screenshot_2026-04-12-21-36-59-275_com.the356company.arexplorer.jpg', cat: 'games' }, // Bug Debugger (12)
  { src: 'Screenshot_2026-04-12-21-37-07-402_com.the356company.arexplorer.jpg', cat: 'games' }, // Pipeline (13)
  { src: 'Screenshot_2026-04-12-21-37-19-999_com.the356company.arexplorer.jpg', cat: 'games' }, // XR Builder (14)
  { src: 'Screenshot_2026-04-12-21-37-28-886_com.the356company.arexplorer.jpg', cat: 'games' }, // Scene Details (15)
  { src: 'Screenshot_2026-04-12-21-37-32-628_com.the356company.arexplorer.jpg', cat: 'games' }, // Code Game (16)

  // Analytics & Dashboard & Rewards
  { src: 'Screenshot_2026-04-12-21-35-46-612_com.the356company.arexplorer.jpg', cat: 'analytics' }, // Dashboard (01)
  { src: 'Screenshot_2026-04-12-21-36-04-678_com.the356company.arexplorer.jpg', cat: 'analytics' }, // Stats (04)
  { src: 'Screenshot_2026-04-12-21-36-34-529_com.the356company.arexplorer.jpg', cat: 'analytics' }, // Analytics Graph (09)
  { src: 'Screenshot_2026-04-12-21-36-37-186_com.the356company.arexplorer.jpg', cat: 'analytics' }, // Certificate (10)
  { src: 'Screenshot_2026-04-12-21-36-45-986_com.the356company.arexplorer.jpg', cat: 'analytics' }, // Modules Grid (11)
  { src: 'Screenshot_2026-04-12-21-37-39-549_com.the356company.arexplorer.jpg', cat: 'analytics' }  // Setting/Summary (17)
];

const screenContainer = document.getElementById('gallery-screen');
const tabs = document.querySelectorAll('.gallery-tab');
let currentIndex = 0;
let filteredScreenshots = screenshotsList;
let intervalId = null;

// Preload and create img elements
const imgElements = screenshotsList.map((item, idx) => {
  const img = document.createElement('img');
  img.src = `assets/images/screenshots/${item.src}`;
  img.dataset.cat = item.cat;
  img.dataset.index = idx;
  screenContainer.appendChild(img);
  return img;
});

function showScreenshot(index) {
  imgElements.forEach(img => img.classList.remove('active'));
  if (filteredScreenshots.length > 0) {
    const targetObj = filteredScreenshots[index];
    const actualImg = imgElements.find(img => img.src.includes(targetObj.src));
    if(actualImg) actualImg.classList.add('active');
  }
}

function nextScreenshot() {
  if (filteredScreenshots.length === 0) return;
  currentIndex = (currentIndex + 1) % filteredScreenshots.length;
  showScreenshot(currentIndex);
}

function startAutoCycle() {
  stopAutoCycle();
  intervalId = setInterval(nextScreenshot, 3000);
}
function stopAutoCycle() {
  if (intervalId) clearInterval(intervalId);
}

// Interactivity for tabs
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    
    const cat = tab.dataset.cat;
    if (cat === 'all') {
      filteredScreenshots = screenshotsList;
    } else {
      filteredScreenshots = screenshotsList.filter(s => s.cat === cat);
    }
    
    currentIndex = 0; // Reset index when switching categories
    showScreenshot(currentIndex);
    startAutoCycle(); // Restart cycle with new category
  });
});

// Initialize
showScreenshot(0);
startAutoCycle();
"""
html = html.replace('// ── SCROLL REVEAL ──', gallery_js + '\n// ── SCROLL REVEAL ──')


# 5. Fix the fallback gradient issue
old_fallback = """setTimeout(() => {
  if (!framesReady) {
    ctx.fillStyle = 'linear-gradient';
    const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
    grad.addColorStop(0, '#050c1a');
    grad.addColorStop(1, '#0d1a30');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    // Show text hint
    ctx.fillStyle = 'rgba(0,229,255,0.3)';
    ctx.font = '14px monospace';
    ctx.textAlign = 'center';
    ctx.fillText('[ Place 280 frames in /frames/Videoframes/ folder as frame__00000_00000.jpg → frame__00000_00279.jpg ]', canvas.width/2, canvas.height/2);
  }
}, 2000);"""

new_fallback = """setTimeout(() => {
  if (!framesReady) {
    // Brand-aligned fallback aesthetic instead of blank black or missing sequence
    
    // We add an animated CSS background to the parent to make it beautiful
    const section = document.getElementById('sequence-section');
    const overlay = document.querySelector('.sequence-overlay');
    if(overlay) {
      overlay.style.background = 'linear-gradient(135deg, rgba(0,229,255,0.1) 0%, rgba(168,85,247,0.1) 50%, rgba(255,60,172,0.1) 100%)';
      overlay.style.animation = 'pulseGradient 8s ease infinite alternate';
    }
    
    // Insert CSS Keyframes
    const style = document.createElement('style');
    style.innerHTML = `
      @keyframes pulseGradient { 
        0% { background-position: 0% 50%; opacity: 0.8; }
        100% { background-position: 100% 50%; opacity: 1; filter: saturate(1.5) hue-rotate(20deg); }
      }
    `;
    document.head.appendChild(style);

    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
}, 2000);"""

# Wait, `ctx.fillStyle = grad;` in new_fallback will fail because `grad` is undefined! Let fixed!
new_fallback_fixed = """setTimeout(() => {
  if (!framesReady) {
    // Brand-aligned fallback aesthetic instead of blank black or missing sequence
    
    // We add an animated CSS background to the parent to make it beautiful
    const section = document.getElementById('sequence-section');
    const overlay = document.querySelector('.sequence-overlay');
    if(overlay) {
      overlay.style.background = 'linear-gradient(135deg, #050c1a 0%, #0a1128 30%, #160a28 70%, #1a0a1a 100%)';
      overlay.style.backgroundSize = '400% 400%';
      overlay.style.animation = 'pulseGradient 8s ease infinite alternate';
    }
    
    // Insert CSS Keyframes
    const style = document.createElement('style');
    style.innerHTML = `
      @keyframes pulseGradient { 
        0% { background-position: 0% 50%; box-shadow: inset 0 0 100px rgba(0,229,255,0.2); }
        50% { background-position: 100% 50%; box-shadow: inset 0 0 100px rgba(168,85,247,0.2); }
        100% { background-position: 0% 50%; box-shadow: inset 0 0 100px rgba(255,60,172,0.2); }
      }
    `;
    document.head.appendChild(style);

    // Dark fill on canvas
    ctx.fillStyle = '#050c1a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
}, 2000);"""

html = html.replace(old_fallback, new_fallback_fixed)

# 6. Update the Features Text to mention the newly added games explicitly
# Find "<div class="feature-card reveal" style="--accent-color: var(--cyan)">
old_feat1 = """<div class="feature-name">Systems Engineer</div>
        <div class="feature-desc">Solve real engineering scripts in our Code Challenges. Fill in missing logic for Vuforia, ARKit, and ARCore. Zone 1 is completely free to start your journey.</div>"""
new_feat1 = """<div class="feature-name">Systems Engineer & XR Builder</div>
        <div class="feature-desc">Assemble spatial UI via the new XR Builder and write production code for Vuforia/ARKit features. Advanced gamification tests your logic directly.</div>"""
html = html.replace(old_feat1, new_feat1)

old_feat2 = """<div class="feature-name">Pipeline & Debugger</div>
        <div class="feature-desc">Exclusive Pro-simulations. Connect complex logic pipelines and hunt for rendering glitches in the AR Debugger. Advanced tools for advanced engineers.</div>"""
new_feat2 = """<div class="feature-name">Pipeline Sandbox & Debugger</div>
        <div class="feature-desc">Hunt for spatial tracking glitches inside the 3D-visualized AR Debugger and architect complex rendering logic inside the interactive Pipeline Sandbox.</div>"""
html = html.replace(old_feat2, new_feat2)

# Write back to index.html
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html successfully.")
