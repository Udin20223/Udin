# svg_assets.py
# Contains crisp, standard SVG components for KiddiesSmart+

def get_laptop_hero_svg():
    return """<svg viewBox="0 0 1000 600" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Laptop mockup memaparkan Dashboard Utama KiddiesSmart+">
  <defs>
    <filter id="laptop-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="20" stdDeviation="25" flood-color="#0F172A" flood-opacity="0.22"/>
    </filter>
    <linearGradient id="laptop-body-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="laptop-base-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#CBD5E1"/>
      <stop offset="50%" stop-color="#94A3B8"/>
      <stop offset="100%" stop-color="#64748B"/>
    </linearGradient>
    <clipPath id="hero-laptop-screen-clip">
      <rect x="80" y="40" width="840" height="470" rx="6"/>
    </clipPath>
  </defs>

  <!-- Laptop Display Lid -->
  <g filter="url(#laptop-shadow)">
    <rect x="60" y="20" width="880" height="510" rx="20" fill="url(#laptop-body-grad)"/>
    <!-- Webcam -->
    <circle cx="500" cy="30" r="4" fill="#0F172A"/>
    <circle cx="500" cy="30" r="1.5" fill="#38BDF8"/>
  </g>

  <!-- Screen Content Area -->
  <g clip-path="url(#hero-laptop-screen-clip)" id="hero-laptop-screen">
    <!-- Inner Screen Background -->
    <rect x="80" y="40" width="840" height="470" fill="#F8FAFC"/>

    <!-- App Topbar -->
    <rect x="80" y="40" width="840" height="60" fill="#FFFFFF"/>
    <line x1="80" y1="100" x2="920" y2="100" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- App Logo -->
    <text x="110" y="77" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#2563EB">KiddiesSmart<tspan fill="#EF4444">+</tspan></text>

    <!-- User Greeting Badge -->
    <rect x="420" y="52" width="160" height="36" rx="18" fill="#EFF6FF"/>
    <text x="440" y="75" font-family="'Nunito', sans-serif" font-weight="800" font-size="15" fill="#1E293B">Hai, Aiman! 👋</text>

    <!-- Stats Badges -->
    <rect x="680" y="52" width="100" height="36" rx="18" fill="#FEF3C7"/>
    <text x="700" y="75" font-family="'Nunito', sans-serif" font-weight="800" font-size="14" fill="#92400E">Tahap 5</text>

    <rect x="790" y="52" width="115" height="36" rx="18" fill="#FEF9C3"/>
    <text x="805" y="75" font-family="'Nunito', sans-serif" font-weight="800" font-size="14" fill="#854D0E">⭐ 120 Bintang</text>

    <!-- Main Dashboard Body -->
    <!-- Welcome Banner -->
    <rect x="110" y="120" width="780" height="85" rx="14" fill="#2563EB"/>
    <text x="135" y="155" font-family="'Nunito', sans-serif" font-weight="800" font-size="20" fill="#FFFFFF">Selamat Kembali ke KiddiesSmart+!</text>
    <text x="135" y="180" font-family="'Nunito', sans-serif" font-weight="600" font-size="14" fill="#DBEAFE">Selesaikan cabaran hari ini untuk mengumpul lebih banyak bintang.</text>

    <!-- Category Filter Bar -->
    <text x="110" y="235" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#1E293B">Pilih Permainan</text>

    <!-- Tabs -->
    <rect x="110" y="250" width="75" height="32" rx="16" fill="#2563EB"/>
    <text x="130" y="271" font-family="'Nunito', sans-serif" font-weight="700" font-size="13" fill="#FFFFFF">Semua</text>

    <rect x="195" y="250" width="100" height="32" rx="16" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="215" y="271" font-family="'Nunito', sans-serif" font-weight="700" font-size="13" fill="#64748B">Matematik</text>

    <rect x="305" y="250" width="85" height="32" rx="16" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="325" y="271" font-family="'Nunito', sans-serif" font-weight="700" font-size="13" fill="#64748B">Bahasa</text>

    <rect x="400" y="250" width="80" height="32" rx="16" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="420" y="271" font-family="'Nunito', sans-serif" font-weight="700" font-size="13" fill="#64748B">Logik</text>

    <!-- Game Cards Row -->
    <!-- Card 1: Kira & Kumpul -->
    <rect x="110" y="300" width="240" height="180" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="110" y="300" width="240" height="90" rx="14" fill="#FEF2F2"/>
    <!-- Apples in card -->
    <circle cx="190" cy="345" r="18" fill="#EF4444"/>
    <circle cx="230" cy="345" r="18" fill="#EF4444"/>
    <circle cx="270" cy="345" r="18" fill="#EF4444"/>
    <path d="M190 327 Q194 320 200 322" stroke="#15803D" stroke-width="3" fill="none"/>
    <path d="M230 327 Q234 320 240 322" stroke="#15803D" stroke-width="3" fill="none"/>
    <path d="M270 327 Q274 320 280 322" stroke="#15803D" stroke-width="3" fill="none"/>
    <text x="125" y="415" font-family="'Nunito', sans-serif" font-weight="800" font-size="16" fill="#1E293B">Kira &amp; Kumpul</text>
    <text x="125" y="435" font-family="'Nunito', sans-serif" font-weight="600" font-size="12" fill="#64748B">Matematik &bull; Tahap 1</text>
    <rect x="125" y="448" width="80" height="24" rx="12" fill="#2563EB"/>
    <text x="145" y="464" font-family="'Nunito', sans-serif" font-weight="700" font-size="11" fill="#FFFFFF">Mula Main</text>

    <!-- Card 2: Cari Huruf -->
    <rect x="380" y="300" width="240" height="180" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="380" y="300" width="240" height="90" rx="14" fill="#F0FDF4"/>
    <!-- Letters graphic -->
    <text x="460" y="360" font-family="'Nunito', sans-serif" font-weight="900" font-size="44" fill="#10B981">A</text>
    <text x="510" y="355" font-family="'Nunito', sans-serif" font-weight="800" font-size="28" fill="#34D399">B</text>
    <text x="535" y="362" font-family="'Nunito', sans-serif" font-weight="800" font-size="22" fill="#6EE7B7">C</text>
    <text x="395" y="415" font-family="'Nunito', sans-serif" font-weight="800" font-size="16" fill="#1E293B">Cari Huruf</text>
    <text x="395" y="435" font-family="'Nunito', sans-serif" font-weight="600" font-size="12" fill="#64748B">Bahasa &bull; Tahap 2</text>
    <rect x="395" y="448" width="80" height="24" rx="12" fill="#10B981"/>
    <text x="415" y="464" font-family="'Nunito', sans-serif" font-weight="700" font-size="11" fill="#FFFFFF">Mula Main</text>

    <!-- Card 3: Bentuk & Warna -->
    <rect x="650" y="300" width="240" height="180" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="650" y="300" width="240" height="90" rx="14" fill="#FAF5FF"/>
    <!-- Shapes graphic -->
    <circle cx="720" cy="345" r="18" fill="#3B82F6"/>
    <polygon points="770,327 752,363 788,363" fill="#EF4444"/>
    <rect x="805" y="327" width="34" height="34" rx="4" fill="#FACC15"/>
    <text x="665" y="415" font-family="'Nunito', sans-serif" font-weight="800" font-size="16" fill="#1E293B">Bentuk &amp; Warna</text>
    <text x="665" y="435" font-family="'Nunito', sans-serif" font-weight="600" font-size="12" fill="#64748B">Visual &bull; Tahap 1</text>
    <rect x="665" y="448" width="80" height="24" rx="12" fill="#8B5CF6"/>
    <text x="685" y="464" font-family="'Nunito', sans-serif" font-weight="700" font-size="11" fill="#FFFFFF">Mula Main</text>
  </g>

  <!-- Laptop Base & Hinge -->
  <g>
    <!-- Hinge -->
    <rect x="420" y="528" width="160" height="12" rx="4" fill="#475569"/>
    <!-- Base Bottom Plate -->
    <path d="M20 540 L980 540 L930 575 L70 575 Z" fill="url(#laptop-base-grad)"/>
    <!-- Base Opening Notch -->
    <rect x="460" y="540" width="80" height="6" rx="3" fill="#334155"/>
    <!-- Desk Shadow Base -->
    <ellipse cx="500" cy="580" rx="460" ry="12" fill="#0F172A" opacity="0.25"/>
  </g>
</svg>"""

def get_phone_hero_svg():
    return """<svg viewBox="0 0 300 620" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Phone mockup memaparkan Game Kira & Kumpul">
  <defs>
    <filter id="phone-shadow" x="-10%" y="-5%" width="120%" height="115%">
      <feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#0F172A" flood-opacity="0.3"/>
    </filter>
    <clipPath id="hero-phone-screen-clip">
      <rect x="15" y="15" width="270" height="590" rx="34"/>
    </clipPath>
  </defs>

  <!-- Phone Body Outer Frame -->
  <g filter="url(#phone-shadow)">
    <rect x="10" y="10" width="280" height="600" rx="40" fill="#1E293B" stroke="#475569" stroke-width="4"/>
  </g>

  <!-- Screen Content -->
  <g clip-path="url(#hero-phone-screen-clip)" id="hero-phone-screen">
    <!-- Phone Screen Background -->
    <rect x="15" y="15" width="270" height="590" fill="#FFFFFF"/>

    <!-- Dynamic Island / Speaker Notch -->
    <rect x="105" y="24" width="90" height="20" rx="10" fill="#0F172A"/>
    <circle cx="178" cy="34" r="3" fill="#38BDF8"/>

    <!-- Game Header Inside Phone -->
    <rect x="15" y="55" width="270" height="52" fill="#EFF6FF"/>
    <text x="32" y="86" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#2563EB">Kira &amp; Kumpul</text>
    <rect x="200" y="68" width="70" height="26" rx="13" fill="#FEF3C7"/>
    <text x="210" y="85" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#92400E">⭐ 120</text>

    <!-- Question Title -->
    <rect x="30" y="125" width="240" height="48" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="150" y="156" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#1E293B" text-anchor="middle">Berapa biji epal?</text>

    <!-- Apple Graphics Stage -->
    <rect x="30" y="190" width="240" height="150" rx="16" fill="#FEF2F2" stroke="#FEE2E2"/>
    
    <!-- 3 Apples Graphic -->
    <g transform="translate(48, 230)">
      <!-- Apple 1 -->
      <g transform="translate(0, 0)">
        <circle cx="32" cy="40" r="24" fill="#EF4444"/>
        <circle cx="38" cy="32" r="6" fill="#F87171" opacity="0.6"/>
        <path d="M32 16 Q36 6 46 8" stroke="#16A34A" stroke-width="4" fill="none" stroke-linecap="round"/>
        <ellipse cx="44" cy="10" rx="6" ry="3" fill="#22C55E"/>
      </g>
      <!-- Apple 2 -->
      <g transform="translate(70, 0)">
        <circle cx="32" cy="40" r="24" fill="#EF4444"/>
        <circle cx="38" cy="32" r="6" fill="#F87171" opacity="0.6"/>
        <path d="M32 16 Q36 6 46 8" stroke="#16A34A" stroke-width="4" fill="none" stroke-linecap="round"/>
        <ellipse cx="44" cy="10" rx="6" ry="3" fill="#22C55E"/>
      </g>
      <!-- Apple 3 -->
      <g transform="translate(140, 0)">
        <circle cx="32" cy="40" r="24" fill="#EF4444"/>
        <circle cx="38" cy="32" r="6" fill="#F87171" opacity="0.6"/>
        <path d="M32 16 Q36 6 46 8" stroke="#16A34A" stroke-width="4" fill="none" stroke-linecap="round"/>
        <ellipse cx="44" cy="10" rx="6" ry="3" fill="#22C55E"/>
      </g>
    </g>

    <!-- Answer Choices Grid (2, 3, 4, 5) -->
    <g transform="translate(30, 360)">
      <!-- Choice 2 -->
      <rect x="0" y="0" width="112" height="60" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="56" y="38" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#475569" text-anchor="middle">2</text>

      <!-- Choice 3 (Active / Selected) -->
      <rect x="128" y="0" width="112" height="60" rx="14" fill="#2563EB" stroke="#1D4ED8" stroke-width="2"/>
      <text x="184" y="38" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#FFFFFF" text-anchor="middle">3</text>

      <!-- Choice 4 -->
      <rect x="0" y="74" width="112" height="60" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="56" y="112" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#475569" text-anchor="middle">4</text>

      <!-- Choice 5 -->
      <rect x="128" y="74" width="112" height="60" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="184" y="112" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#475569" text-anchor="middle">5</text>
    </g>

    <!-- Feedback Bar -->
    <rect x="30" y="520" width="240" height="42" rx="12" fill="#DCFCE7"/>
    <text x="150" y="546" font-family="'Nunito', sans-serif" font-weight="800" font-size="14" fill="#15803D" text-anchor="middle">Hebat! Jawapan Betul! +10 Bintang</text>

    <!-- Bottom Indicator -->
    <rect x="110" y="590" width="80" height="4" rx="2" fill="#94A3B8"/>
  </g>
</svg>"""

def get_trust_secure_payment_svg():
    return """<svg viewBox="0 0 32 32" width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ikon Pembayaran Selamat">
  <path d="M16 3L5 7.5V14.5C5 21.8 9.7 28.5 16 30C22.3 28.5 27 21.8 27 14.5V7.5L16 3Z" fill="#EFF6FF" stroke="#2563EB" stroke-width="2.2" stroke-linejoin="round"/>
  <rect x="11.5" y="14.5" width="9" height="7.5" rx="1.8" fill="#2563EB"/>
  <path d="M13.5 14.5V12C13.5 10.62 14.62 9.5 16 9.5C17.38 9.5 18.5 10.62 18.5 12V14.5" stroke="#2563EB" stroke-width="2" stroke-linecap="round"/>
  <circle cx="16" cy="18" r="1" fill="#FFFFFF"/>
</svg>"""

def get_trust_instant_access_svg():
    return """<svg viewBox="0 0 32 32" width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ikon Akses Serta-Merta">
  <circle cx="16" cy="16" r="13" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
  <path d="M17.5 7L9.5 17H16L14.5 25L22.5 15H16L17.5 7Z" fill="#F59E0B" stroke="#D97706" stroke-width="1.8" stroke-linejoin="round"/>
</svg>"""

def get_trust_privacy_first_svg():
    return """<svg viewBox="0 0 32 32" width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ikon Privasi Terpelihara">
  <path d="M16 3L5 7.5V14.5C5 21.8 9.7 28.5 16 30C22.3 28.5 27 21.8 27 14.5V7.5L16 3Z" fill="#ECFDF5" stroke="#10B981" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M11 15.5L14.5 19L21 12" stroke="#059669" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

print("Hero & Trust SVGs ready")
