# svg_more_assets.py
# Contains all remaining SVG diagrams, device mockups and demonstration SVGs

def get_adaptive_diagram_svg():
    return """<svg viewBox="0 0 800 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Carta Aliran Mekanisme Adaptive Learning KiddiesSmart+">
  <defs>
    <linearGradient id="adapt-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#1D4ED8"/>
    </linearGradient>
    <filter id="box-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Node 1: ANAK -->
  <g filter="url(#box-shadow)">
    <rect x="310" y="20" width="180" height="55" rx="14" fill="#FFFFFF" stroke="#2563EB" stroke-width="2"/>
    <text x="400" y="55" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#1E293B" text-anchor="middle">1. ANAK MENJAWAB</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <path d="M400 75 L400 108" stroke="#2563EB" stroke-width="3" stroke-linecap="round"/>
  <polygon points="400,116 394,106 406,106" fill="#2563EB"/>

  <!-- Node 2: PRESTASI -->
  <g filter="url(#box-shadow)">
    <rect x="300" y="118" width="200" height="55" rx="14" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
    <text x="400" y="153" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#1E40AF" text-anchor="middle">2. PRESTASI DINILAI</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <path d="M400 173 L400 206" stroke="#2563EB" stroke-width="3" stroke-linecap="round"/>
  <polygon points="400,214 394,204 406,204" fill="#2563EB"/>

  <!-- Node 3: SISTEM ADAPTIF -->
  <g filter="url(#box-shadow)">
    <rect x="270" y="216" width="260" height="60" rx="16" fill="url(#adapt-grad)"/>
    <text x="400" y="253" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#FFFFFF" text-anchor="middle">3. SISTEM BERADAPTASI</text>
  </g>

  <!-- Left Branch: BANTU (Jika sukar) -->
  <path d="M320 276 L200 326" stroke="#EF4444" stroke-width="3" stroke-linecap="round" stroke-dasharray="6,4"/>
  <polygon points="194,328 205,321 200,332" fill="#EF4444"/>

  <g filter="url(#box-shadow)">
    <rect x="70" y="328" width="240" height="60" rx="14" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
    <text x="190" y="353" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#991B1B" text-anchor="middle">BANTU &amp; SOKONG</text>
    <text x="190" y="375" font-family="'Nunito', sans-serif" font-weight="700" font-size="13" fill="#B91C1C" text-anchor="middle">Bimbingan jika soalan sukar</text>
  </g>

  <!-- Right Branch: CABAR (Jika mudah) -->
  <path d="M480 276 L600 326" stroke="#10B981" stroke-width="3" stroke-linecap="round"/>
  <polygon points="606,328 600,321 605,332" fill="#10B981"/>

  <g filter="url(#box-shadow)">
    <rect x="490" y="328" width="240" height="60" rx="14" fill="#F0FDF4" stroke="#10B981" stroke-width="2"/>
    <text x="610" y="353" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#065F46" text-anchor="middle">CABAR KEMAHIRAN</text>
    <text x="610" y="375" font-family="'Nunito', sans-serif" font-weight="700" font-size="13" fill="#047857" text-anchor="middle">Tingkatkan aras jika mudah</text>
  </g>
</svg>"""

def get_demo_laptop_selection_svg():
    return """<svg viewBox="0 0 700 450" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visual A: Skrin Pilih Permainan">
  <defs>
    <clipPath id="game-selection-screen-clip">
      <rect x="50" y="30" width="600" height="360" rx="8"/>
    </clipPath>
  </defs>

  <!-- Laptop Frame -->
  <rect x="35" y="15" width="630" height="390" rx="16" fill="#1E293B"/>
  <circle cx="350" cy="22" r="3" fill="#38BDF8"/>

  <!-- Screen Content -->
  <g clip-path="url(#game-selection-screen-clip)" id="game-selection-screen">
    <rect x="50" y="30" width="600" height="360" fill="#F8FAFC"/>
    
    <!-- Top Header -->
    <rect x="50" y="30" width="600" height="50" fill="#FFFFFF"/>
    <line x1="50" y1="80" x2="650" y2="80" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="75" y="62" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#2563EB">KiddiesSmart<tspan fill="#EF4444">+</tspan></text>
    <text x="480" y="62" font-family="'Nunito', sans-serif" font-weight="800" font-size="14" fill="#1E293B">Aiman (Tahap 5)</text>

    <!-- Title -->
    <text x="75" y="115" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#1E293B">Pilih Permainan</text>

    <!-- Grid 2x2 Games -->
    <!-- Game 1: Kira & Kumpul -->
    <rect x="75" y="135" width="245" height="110" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="75" y="135" width="6" height="110" rx="3" fill="#EF4444"/>
    <text x="95" y="165" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#1E293B">Kira &amp; Kumpul</text>
    <text x="95" y="188" font-family="'Nunito', sans-serif" font-weight="600" font-size="13" fill="#64748B">Matematik Asas &bull; Tahap 1</text>
    <rect x="95" y="200" width="90" height="24" rx="6" fill="#FEF2F2"/>
    <text x="140" y="216" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#DC2626" text-anchor="middle">Permainan Aktif</text>

    <!-- Game 2: Tambah & Tolak Duit -->
    <rect x="340" y="135" width="245" height="110" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="340" y="135" width="6" height="110" rx="3" fill="#F59E0B"/>
    <text x="360" y="165" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#1E293B">Tambah &amp; Tolak Duit</text>
    <text x="360" y="188" font-family="'Nunito', sans-serif" font-weight="600" font-size="13" fill="#64748B">Kemahiran Wang &bull; Tahap 2</text>
    <rect x="360" y="200" width="70" height="24" rx="6" fill="#FEF3C7"/>
    <text x="395" y="216" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#D97706" text-anchor="middle">Sedia Main</text>

    <!-- Game 3: Cari Huruf -->
    <rect x="75" y="260" width="245" height="110" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="75" y="260" width="6" height="110" rx="3" fill="#10B981"/>
    <text x="95" y="290" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#1E293B">Cari Huruf</text>
    <text x="95" y="313" font-family="'Nunito', sans-serif" font-weight="600" font-size="13" fill="#64748B">Kosa Kata &bull; Tahap 1</text>
    <rect x="95" y="325" width="70" height="24" rx="6" fill="#DCFCE7"/>
    <text x="130" y="341" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#16A34A" text-anchor="middle">Sedia Main</text>

    <!-- Game 4: Bentuk & Warna -->
    <rect x="340" y="260" width="245" height="110" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="340" y="260" width="6" height="110" rx="3" fill="#8B5CF6"/>
    <text x="360" y="290" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#1E293B">Bentuk &amp; Warna</text>
    <text x="360" y="313" font-family="'Nunito', sans-serif" font-weight="600" font-size="13" fill="#64748B">Diskriminasi Visual &bull; Tahap 1</text>
    <rect x="360" y="325" width="70" height="24" rx="6" fill="#F3E8FF"/>
    <text x="395" y="341" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#7C3AED" text-anchor="middle">Sedia Main</text>
  </g>

  <!-- Base -->
  <path d="M10 405 L690 405 L650 435 L50 435 Z" fill="#64748B"/>
  <rect x="310" y="405" width="80" height="6" rx="3" fill="#334155"/>
</svg>"""

def get_demo_achievement_svg():
    return """<svg viewBox="0 0 700 450" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visual B: Skrin Pencapaian Anda">
  <defs>
    <clipPath id="achievement-screen-clip">
      <rect x="50" y="30" width="600" height="360" rx="8"/>
    </clipPath>
  </defs>

  <!-- Laptop Frame -->
  <rect x="35" y="15" width="630" height="390" rx="16" fill="#1E293B"/>
  <circle cx="350" cy="22" r="3" fill="#38BDF8"/>

  <!-- Screen Content -->
  <g clip-path="url(#achievement-screen-clip)" id="achievement-screen">
    <rect x="50" y="30" width="600" height="360" fill="#F8FAFC"/>
    
    <!-- Header -->
    <rect x="50" y="30" width="600" height="50" fill="#FFFFFF"/>
    <line x1="50" y1="80" x2="650" y2="80" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="75" y="62" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#2563EB">KiddiesSmart<tspan fill="#EF4444">+</tspan></text>
    <rect x="490" y="42" width="140" height="28" rx="14" fill="#FEF3C7"/>
    <text x="560" y="61" font-family="'Nunito', sans-serif" font-weight="800" font-size="13" fill="#92400E" text-anchor="middle">⭐ 120 Bintang</text>

    <!-- Title -->
    <text x="75" y="118" font-family="'Nunito', sans-serif" font-weight="900" font-size="20" fill="#1E293B">Pencapaian Anda</text>
    <text x="75" y="138" font-family="'Nunito', sans-serif" font-weight="600" font-size="14" fill="#64748B">Ganjaran lencana kejayaan anak selepas menyelesaikan aktiviti pembelajaran.</text>

    <!-- Cards Grid -->
    <!-- Achievement 1: Super Learner (DIBUKA) -->
    <rect x="75" y="160" width="250" height="190" rx="16" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
    <circle cx="200" cy="215" r="32" fill="#DCFCE7"/>
    <!-- Trophy Icon -->
    <path d="M190 205 L210 205 L206 222 Q200 230 194 222 Z" fill="#10B981"/>
    <circle cx="200" cy="205" r="6" fill="#10B981"/>
    <rect x="196" y="228" width="8" height="10" fill="#10B981"/>
    <rect x="190" y="238" width="20" height="4" rx="2" fill="#10B981"/>
    
    <text x="200" y="275" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#1E293B" text-anchor="middle">Super Learner</text>
    <text x="200" y="295" font-family="'Nunito', sans-serif" font-weight="600" font-size="13" fill="#64748B" text-anchor="middle">Selesaikan 10 Aktiviti</text>
    
    <rect x="145" y="310" width="110" height="28" rx="14" fill="#10B981"/>
    <text x="200" y="329" font-family="'Nunito', sans-serif" font-weight="900" font-size="12" fill="#FFFFFF" text-anchor="middle">✓ DIBUKA</text>

    <!-- Achievement 2: Genius Math (TERKUNCI) -->
    <rect x="350" y="160" width="250" height="190" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <circle cx="475" cy="215" r="32" fill="#F1F5F9"/>
    <!-- Lock Icon -->
    <rect x="465" y="210" width="20" height="18" rx="4" fill="#94A3B8"/>
    <path d="M470 210 V202 Q475 196 480 202 V210" stroke="#94A3B8" stroke-width="3" fill="none"/>

    <text x="475" y="275" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#64748B" text-anchor="middle">Genius Math</text>
    <text x="475" y="295" font-family="'Nunito', sans-serif" font-weight="600" font-size="13" fill="#94A3B8" text-anchor="middle">Capai 200 Bintang</text>

    <rect x="420" y="310" width="110" height="28" rx="14" fill="#E2E8F0"/>
    <text x="475" y="329" font-family="'Nunito', sans-serif" font-weight="900" font-size="12" fill="#64748B" text-anchor="middle">🔒 TERKUNCI</text>
  </g>

  <!-- Base -->
  <path d="M10 405 L690 405 L650 435 L50 435 Z" fill="#64748B"/>
</svg>"""

def get_demo_phone_letters_svg():
    return """<svg viewBox="0 0 300 520" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visual C: Phone Skrin Cari Huruf">
  <defs>
    <clipPath id="lang-phone-screen-clip">
      <rect x="15" y="15" width="270" height="490" rx="28"/>
    </clipPath>
  </defs>

  <!-- Phone Body -->
  <rect x="10" y="10" width="280" height="500" rx="32" fill="#1E293B"/>

  <!-- Screen Content -->
  <g clip-path="url(#lang-phone-screen-clip)" id="lang-phone-screen">
    <rect x="15" y="15" width="270" height="490" fill="#FFFFFF"/>
    <rect x="105" y="22" width="90" height="16" rx="8" fill="#0F172A"/>

    <!-- Header -->
    <rect x="15" y="48" width="270" height="48" fill="#F0FDF4"/>
    <text x="32" y="77" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#10B981">Cari Huruf</text>
    <rect x="210" y="60" width="60" height="24" rx="12" fill="#DCFCE7"/>
    <text x="240" y="76" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#16A34A" text-anchor="middle">Bahasa</text>

    <!-- Question -->
    <rect x="30" y="115" width="240" height="50" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="150" y="146" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#1E293B" text-anchor="middle">Cari huruf 'A'</text>

    <!-- Letter Choices: B, C, A, D, E -->
    <g transform="translate(30, 190)">
      <!-- Row 1: B, C -->
      <rect x="10" y="0" width="95" height="75" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="57" y="48" font-family="'Nunito', sans-serif" font-weight="900" font-size="34" fill="#64748B" text-anchor="middle">B</text>

      <rect x="135" y="0" width="95" height="75" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="182" y="48" font-family="'Nunito', sans-serif" font-weight="900" font-size="34" fill="#64748B" text-anchor="middle">C</text>

      <!-- Row 2: A (Selected/Active Answer) -->
      <rect x="72" y="95" width="95" height="75" rx="16" fill="#10B981" stroke="#059669" stroke-width="2"/>
      <text x="119" y="143" font-family="'Nunito', sans-serif" font-weight="900" font-size="34" fill="#FFFFFF" text-anchor="middle">A</text>

      <!-- Row 3: D, E -->
      <rect x="10" y="190" width="95" height="75" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="57" y="238" font-family="'Nunito', sans-serif" font-weight="900" font-size="34" fill="#64748B" text-anchor="middle">D</text>

      <rect x="135" y="190" width="95" height="75" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
      <text x="182" y="238" font-family="'Nunito', sans-serif" font-weight="900" font-size="34" fill="#64748B" text-anchor="middle">E</text>
    </g>

    <!-- Success Message -->
    <rect x="30" y="465" width="240" height="30" rx="8" fill="#DCFCE7"/>
    <text x="150" y="485" font-family="'Nunito', sans-serif" font-weight="800" font-size="13" fill="#15803D" text-anchor="middle">Syabas! Ini huruf A! +10 Mata</text>
  </g>
</svg>"""

def get_demo_phone_shapes_svg():
    return """<svg viewBox="0 0 300 520" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visual D: Phone Skrin Bentuk & Warna">
  <defs>
    <clipPath id="visual-phone-screen-clip">
      <rect x="15" y="15" width="270" height="490" rx="28"/>
    </clipPath>
  </defs>

  <!-- Phone Frame -->
  <rect x="10" y="10" width="280" height="500" rx="32" fill="#1E293B"/>

  <!-- Screen Content -->
  <g clip-path="url(#visual-phone-screen-clip)" id="visual-phone-screen">
    <rect x="15" y="15" width="270" height="490" fill="#FFFFFF"/>
    <rect x="105" y="22" width="90" height="16" rx="8" fill="#0F172A"/>

    <!-- Header -->
    <rect x="15" y="48" width="270" height="48" fill="#FAF5FF"/>
    <text x="32" y="77" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#8B5CF6">Bentuk &amp; Warna</text>
    <rect x="210" y="60" width="60" height="24" rx="12" fill="#F3E8FF"/>
    <text x="240" y="76" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#7C3AED" text-anchor="middle">Visual</text>

    <!-- Question Card -->
    <rect x="30" y="115" width="240" height="50" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="150" y="146" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#1E293B" text-anchor="middle">Pilih Segi Tiga Merah</text>

    <!-- Shapes Choices: Circle, Triangle, Square -->
    <!-- Choice 1: Circle (Blue) -->
    <rect x="30" y="185" width="240" height="75" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
    <circle cx="75" cy="222" r="24" fill="#3B82F6"/>
    <text x="130" y="228" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#475569">Circle (Bulatan)</text>

    <!-- Choice 2: Triangle (Red - Active/Target) -->
    <rect x="30" y="275" width="240" height="75" rx="14" fill="#FEF2F2" stroke="#EF4444" stroke-width="2.5"/>
    <polygon points="75,200 50,244 100,244" fill="#EF4444" transform="translate(0, 90)"/>
    <text x="130" y="318" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#DC2626">Triangle (Segi Tiga)</text>
    <text x="130" y="336" font-family="'Nunito', sans-serif" font-weight="700" font-size="12" fill="#EF4444">Warna Merah</text>

    <!-- Choice 3: Square (Yellow) -->
    <rect x="30" y="365" width="240" height="75" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2"/>
    <rect x="52" y="380" width="46" height="46" rx="6" fill="#FACC15"/>
    <text x="130" y="408" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#475569">Square (Segi Empat)</text>

    <!-- Feedback -->
    <rect x="30" y="460" width="240" height="32" rx="8" fill="#DCFCE7"/>
    <text x="150" y="481" font-family="'Nunito', sans-serif" font-weight="800" font-size="13" fill="#15803D" text-anchor="middle">Tepat Sekali! Segi Tiga Merah!</text>
  </g>
</svg>"""

def get_parent_dashboard_laptop_svg():
    return """<svg viewBox="0 0 1000 600" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Laptop mockup memaparkan Ruangan Ibubapa Perkembangan Anak">
  <defs>
    <filter id="parent-laptop-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="20" stdDeviation="25" flood-color="#0F172A" flood-opacity="0.22"/>
    </filter>
    <linearGradient id="parent-base-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#CBD5E1"/>
      <stop offset="50%" stop-color="#94A3B8"/>
      <stop offset="100%" stop-color="#64748B"/>
    </linearGradient>
    <clipPath id="parent-dashboard-screen-clip">
      <rect x="80" y="40" width="840" height="470" rx="6"/>
    </clipPath>
  </defs>

  <!-- Laptop Body -->
  <g filter="url(#parent-laptop-shadow)">
    <rect x="60" y="20" width="880" height="510" rx="20" fill="#1E293B"/>
    <circle cx="500" cy="30" r="4" fill="#0F172A"/>
    <circle cx="500" cy="30" r="1.5" fill="#38BDF8"/>
  </g>

  <!-- Screen Content -->
  <g clip-path="url(#parent-dashboard-screen-clip)" id="parent-dashboard-screen">
    <rect x="80" y="40" width="840" height="470" fill="#F8FAFC"/>

    <!-- Header -->
    <rect x="80" y="40" width="840" height="60" fill="#FFFFFF"/>
    <line x1="80" y1="100" x2="920" y2="100" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="110" y="77" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#2563EB">KiddiesSmart<tspan fill="#EF4444">+</tspan></text>
    
    <rect x="740" y="52" width="150" height="36" rx="18" fill="#EFF6FF"/>
    <text x="815" y="75" font-family="'Nunito', sans-serif" font-weight="800" font-size="14" fill="#2563EB" text-anchor="middle">Ruangan Ibubapa</text>

    <!-- Main Section Header -->
    <text x="110" y="145" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#1E293B">Perkembangan Anak</text>
    <text x="110" y="170" font-family="'Nunito', sans-serif" font-weight="700" font-size="15" fill="#2563EB">Aiman (Tahap 5)</text>

    <!-- 3 Metric Progress Cards -->
    <!-- Metric 1: Matematik 80% -->
    <rect x="110" y="195" width="760" height="85" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="135" y="232" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#1E293B">Matematik</text>
    <text x="830" y="232" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#2563EB" text-anchor="end">80%</text>
    <!-- Progress Track -->
    <rect x="135" y="248" width="700" height="12" rx="6" fill="#F1F5F9"/>
    <!-- Progress Fill: 80% of 700 = 560 -->
    <rect x="135" y="248" width="560" height="12" rx="6" fill="#2563EB"/>

    <!-- Metric 2: Bahasa 60% -->
    <rect x="110" y="295" width="760" height="85" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="135" y="332" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#1E293B">Bahasa</text>
    <text x="830" y="332" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#10B981" text-anchor="end">60%</text>
    <!-- Progress Track -->
    <rect x="135" y="348" width="700" height="12" rx="6" fill="#F1F5F9"/>
    <!-- Progress Fill: 60% of 700 = 420 -->
    <rect x="135" y="348" width="420" height="12" rx="6" fill="#10B981"/>

    <!-- Metric 3: Logik 40% -->
    <rect x="110" y="395" width="760" height="85" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="135" y="432" font-family="'Nunito', sans-serif" font-weight="900" font-size="17" fill="#1E293B">Logik</text>
    <text x="830" y="432" font-family="'Nunito', sans-serif" font-weight="900" font-size="18" fill="#8B5CF6" text-anchor="end">40%</text>
    <!-- Progress Track -->
    <rect x="135" y="448" width="700" height="12" rx="6" fill="#F1F5F9"/>
    <!-- Progress Fill: 40% of 700 = 280 -->
    <rect x="135" y="448" width="280" height="12" rx="6" fill="#8B5CF6"/>
  </g>

  <!-- Laptop Base -->
  <g>
    <rect x="420" y="528" width="160" height="12" rx="4" fill="#475569"/>
    <path d="M20 540 L980 540 L930 575 L70 575 Z" fill="url(#parent-base-grad)"/>
    <rect x="460" y="540" width="80" height="6" rx="3" fill="#334155"/>
    <ellipse cx="500" cy="580" rx="460" ry="12" fill="#0F172A" opacity="0.25"/>
  </g>
</svg>"""

print("More SVGs ready")
