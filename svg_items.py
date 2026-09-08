# svg_items.py
# Contains 7 dedicated mockups for Section 10 ("What Customer Gets") and custom SVG icons

def get_item_1_svg():
    # Laptop SVG: Main dashboard
    return """<svg viewBox="0 0 500 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 1 Mockup: Dashboard Utama">
  <defs>
    <clipPath id="item1-screen-clip">
      <rect x="40" y="20" width="420" height="240" rx="4"/>
    </clipPath>
  </defs>
  <!-- Laptop lid -->
  <rect x="25" y="10" width="450" height="260" rx="10" fill="#1E293B"/>
  <circle cx="250" cy="15" r="2.5" fill="#38BDF8"/>
  <!-- Screen -->
  <g clip-path="url(#item1-screen-clip)" id="item1-laptop-screen">
    <rect x="40" y="20" width="420" height="240" fill="#F8FAFC"/>
    <!-- Topbar -->
    <rect x="40" y="20" width="420" height="35" fill="#FFFFFF"/>
    <line x1="40" y1="55" x2="460" y2="55" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="42" font-family="'Nunito', sans-serif" font-weight="900" font-size="13" fill="#2563EB">KiddiesSmart<tspan fill="#EF4444">+</tspan></text>
    <rect x="220" y="27" width="95" height="22" rx="11" fill="#EFF6FF"/>
    <text x="267" y="42" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#1E293B" text-anchor="middle">Hai, Aiman! 👋</text>
    <rect x="325" y="27" width="55" height="22" rx="11" fill="#FEF3C7"/>
    <text x="352" y="42" font-family="'Nunito', sans-serif" font-weight="800" font-size="9" fill="#92400E" text-anchor="middle">Tahap 5</text>
    <rect x="385" y="27" width="65" height="22" rx="11" fill="#FEF9C3"/>
    <text x="417" y="42" font-family="'Nunito', sans-serif" font-weight="800" font-size="9" fill="#854D0E" text-anchor="middle">⭐ 120</text>
    <!-- Welcome card -->
    <rect x="55" y="65" width="390" height="42" rx="8" fill="#2563EB"/>
    <text x="70" y="85" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#FFFFFF">Pusat Permainan Interaktif</text>
    <text x="70" y="98" font-family="'Nunito', sans-serif" font-weight="600" font-size="9" fill="#BFDBFE">Semua aktiviti pembelajaran dalam satu akses mudah.</text>
    <!-- Section Title & Tabs -->
    <text x="55" y="125" font-family="'Nunito', sans-serif" font-weight="900" font-size="12" fill="#1E293B">Pilih Permainan</text>
    <rect x="55" y="132" width="45" height="18" rx="9" fill="#2563EB"/>
    <text x="77" y="145" font-family="'Nunito', sans-serif" font-weight="700" font-size="9" fill="#FFFFFF" text-anchor="middle">Semua</text>
    <rect x="105" y="132" width="60" height="18" rx="9" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="135" y="145" font-family="'Nunito', sans-serif" font-weight="700" font-size="9" fill="#64748B" text-anchor="middle">Matematik</text>
    <!-- 3 Mini Cards -->
    <rect x="55" y="160" width="120" height="85" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="55" y="160" width="120" height="40" rx="8" fill="#FEF2F2"/>
    <text x="65" y="215" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#1E293B">Kira &amp; Kumpul</text>
    <rect x="190" y="160" width="120" height="85" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="190" y="160" width="120" height="40" rx="8" fill="#F0FDF4"/>
    <text x="200" y="215" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#1E293B">Cari Huruf</text>
    <rect x="325" y="160" width="120" height="85" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <rect x="325" y="160" width="120" height="40" rx="8" fill="#FAF5FF"/>
    <text x="335" y="215" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#1E293B">Bentuk &amp; Warna</text>
  </g>
  <!-- Laptop base -->
  <path d="M10 270 L490 270 L460 290 L40 290 Z" fill="#64748B"/>
  <rect x="220" y="270" width="60" height="4" rx="2" fill="#334155"/>
</svg>"""

def get_item_2_svg():
    # Phone SVG: Kira & Kumpul (Matematik)
    return """<svg viewBox="0 0 200 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 2 Mockup: Kira & Kumpul">
  <defs>
    <clipPath id="item2-screen-clip">
      <rect x="10" y="10" width="180" height="300" rx="16"/>
    </clipPath>
  </defs>
  <rect x="5" y="5" width="190" height="310" rx="20" fill="#1E293B"/>
  <g clip-path="url(#item2-screen-clip)" id="item2-phone-screen">
    <rect x="10" y="10" width="180" height="300" fill="#FFFFFF"/>
    <rect x="70" y="15" width="60" height="10" rx="5" fill="#0F172A"/>
    <!-- Game Header -->
    <rect x="10" y="32" width="180" height="28" fill="#FEF2F2"/>
    <text x="20" y="51" font-family="'Nunito', sans-serif" font-weight="900" font-size="11" fill="#EF4444">Kira &amp; Kumpul</text>
    <!-- Question -->
    <rect x="18" y="68" width="164" height="28" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="100" y="86" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#1E293B" text-anchor="middle">Berapa biji epal?</text>
    <!-- 3 Apples -->
    <g transform="translate(35, 105)">
      <circle cx="20" cy="20" r="14" fill="#EF4444"/>
      <path d="M20 6 Q23 0 28 2" stroke="#16A34A" stroke-width="2.5" fill="none"/>
      <circle cx="65" cy="20" r="14" fill="#EF4444"/>
      <path d="M65 6 Q68 0 73 2" stroke="#16A34A" stroke-width="2.5" fill="none"/>
      <circle cx="110" cy="20" r="14" fill="#EF4444"/>
      <path d="M110 6 Q113 0 118 2" stroke="#16A34A" stroke-width="2.5" fill="none"/>
    </g>
    <!-- Choices Grid 2, 3, 4, 5 -->
    <rect x="25" y="155" width="70" height="35" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="60" y="178" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#64748B" text-anchor="middle">2</text>
    <rect x="105" y="155" width="70" height="35" rx="8" fill="#2563EB"/>
    <text x="140" y="178" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#FFFFFF" text-anchor="middle">3</text>
    <rect x="25" y="200" width="70" height="35" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="60" y="223" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#64748B" text-anchor="middle">4</text>
    <rect x="105" y="200" width="70" height="35" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="140" y="223" font-family="'Nunito', sans-serif" font-weight="900" font-size="16" fill="#64748B" text-anchor="middle">5</text>
    <rect x="20" y="255" width="160" height="28" rx="6" fill="#DCFCE7"/>
    <text x="100" y="273" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#15803D" text-anchor="middle">Jawapan Tepat! 🍎</text>
  </g>
</svg>"""

def get_item_3_svg():
    # Phone SVG: Cari Huruf
    return """<svg viewBox="0 0 200 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 3 Mockup: Cari Huruf">
  <defs>
    <clipPath id="item3-screen-clip">
      <rect x="10" y="10" width="180" height="300" rx="16"/>
    </clipPath>
  </defs>
  <rect x="5" y="5" width="190" height="310" rx="20" fill="#1E293B"/>
  <g clip-path="url(#item3-screen-clip)" id="item3-phone-screen">
    <rect x="10" y="10" width="180" height="300" fill="#FFFFFF"/>
    <rect x="70" y="15" width="60" height="10" rx="5" fill="#0F172A"/>
    <!-- Game Header -->
    <rect x="10" y="32" width="180" height="28" fill="#F0FDF4"/>
    <text x="20" y="51" font-family="'Nunito', sans-serif" font-weight="900" font-size="11" fill="#10B981">Cari Huruf</text>
    <!-- Question -->
    <rect x="18" y="68" width="164" height="28" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="100" y="86" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#1E293B" text-anchor="middle">Cari huruf 'A'</text>
    <!-- Choices B C A D E -->
    <rect x="25" y="112" width="68" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="59" y="140" font-family="'Nunito', sans-serif" font-weight="900" font-size="20" fill="#64748B" text-anchor="middle">B</text>
    <rect x="107" y="112" width="68" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="141" y="140" font-family="'Nunito', sans-serif" font-weight="900" font-size="20" fill="#64748B" text-anchor="middle">C</text>
    
    <rect x="66" y="164" width="68" height="42" rx="8" fill="#10B981"/>
    <text x="100" y="192" font-family="'Nunito', sans-serif" font-weight="900" font-size="20" fill="#FFFFFF" text-anchor="middle">A</text>

    <rect x="25" y="216" width="68" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="59" y="244" font-family="'Nunito', sans-serif" font-weight="900" font-size="20" fill="#64748B" text-anchor="middle">D</text>
    <rect x="107" y="216" width="68" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="141" y="244" font-family="'Nunito', sans-serif" font-weight="900" font-size="20" fill="#64748B" text-anchor="middle">E</text>

    <rect x="20" y="270" width="160" height="24" rx="6" fill="#DCFCE7"/>
    <text x="100" y="286" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#15803D" text-anchor="middle">Hebat! Huruf A! ✨</text>
  </g>
</svg>"""

def get_item_4_svg():
    # Memory & Logic Game Interface
    return """<svg viewBox="0 0 500 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 4 Mockup: Memory & Logic Games">
  <defs>
    <clipPath id="item4-screen-clip">
      <rect x="40" y="20" width="420" height="240" rx="4"/>
    </clipPath>
  </defs>
  <rect x="25" y="10" width="450" height="260" rx="10" fill="#1E293B"/>
  <circle cx="250" cy="15" r="2.5" fill="#38BDF8"/>
  <g clip-path="url(#item4-screen-clip)" id="item4-laptop-screen">
    <rect x="40" y="20" width="420" height="240" fill="#F8FAFC"/>
    <!-- Topbar -->
    <rect x="40" y="20" width="420" height="35" fill="#FFFFFF"/>
    <line x1="40" y1="55" x2="460" y2="55" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="42" font-family="'Nunito', sans-serif" font-weight="900" font-size="13" fill="#8B5CF6">Padanan Memori &amp; Corak Logik</text>
    <text x="430" y="42" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#64748B" text-anchor="end">Logik &bull; Tahap 1</text>
    <!-- Instructions -->
    <rect x="55" y="65" width="390" height="30" rx="6" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="250" y="84" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#7C3AED" text-anchor="middle">Buka kad dan cari pasangan simbol yang sepadan</text>
    <!-- Cards Grid 2x3 -->
    <!-- Row 1 -->
    <rect x="75" y="108" width="85" height="60" rx="8" fill="#8B5CF6"/>
    <text x="117" y="145" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#FFFFFF" text-anchor="middle">⭐</text>
    <rect x="180" y="108" width="85" height="60" rx="8" fill="#8B5CF6"/>
    <text x="222" y="145" font-family="'Nunito', sans-serif" font-weight="900" font-size="24" fill="#FFFFFF" text-anchor="middle">⭐</text>
    <rect x="285" y="108" width="85" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="327" y="145" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#94A3B8" text-anchor="middle">?</text>
    <!-- Row 2 -->
    <rect x="75" y="180" width="85" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="117" y="217" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#94A3B8" text-anchor="middle">?</text>
    <rect x="180" y="180" width="85" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="222" y="217" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#94A3B8" text-anchor="middle">?</text>
    <rect x="285" y="180" width="85" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="327" y="217" font-family="'Nunito', sans-serif" font-weight="900" font-size="22" fill="#94A3B8" text-anchor="middle">?</text>
  </g>
  <path d="M10 270 L490 270 L460 290 L40 290 Z" fill="#64748B"/>
  <rect x="220" y="270" width="60" height="4" rx="2" fill="#334155"/>
</svg>"""

def get_item_5_svg():
    # Phone SVG: Bentuk & Warna
    return """<svg viewBox="0 0 200 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 5 Mockup: Bentuk & Warna">
  <defs>
    <clipPath id="item5-screen-clip">
      <rect x="10" y="10" width="180" height="300" rx="16"/>
    </clipPath>
  </defs>
  <rect x="5" y="5" width="190" height="310" rx="20" fill="#1E293B"/>
  <g clip-path="url(#item5-screen-clip)" id="item5-phone-screen">
    <rect x="10" y="10" width="180" height="300" fill="#FFFFFF"/>
    <rect x="70" y="15" width="60" height="10" rx="5" fill="#0F172A"/>
    <!-- Game Header -->
    <rect x="10" y="32" width="180" height="28" fill="#FAF5FF"/>
    <text x="20" y="51" font-family="'Nunito', sans-serif" font-weight="900" font-size="11" fill="#8B5CF6">Bentuk &amp; Warna</text>
    <!-- Question -->
    <rect x="18" y="68" width="164" height="28" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="100" y="86" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#1E293B" text-anchor="middle">Pilih Segi Tiga Merah</text>
    
    <!-- Circle -->
    <rect x="20" y="108" width="160" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <circle cx="45" cy="129" r="14" fill="#3B82F6"/>
    <text x="75" y="134" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#475569">Circle (Bulatan)</text>

    <!-- Triangle (Target) -->
    <rect x="20" y="158" width="160" height="42" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
    <polygon points="45,118 31,142 59,142" fill="#EF4444" transform="translate(0, 52)"/>
    <text x="75" y="184" font-family="'Nunito', sans-serif" font-weight="900" font-size="12" fill="#DC2626">Triangle (Segi Tiga)</text>

    <!-- Square -->
    <rect x="20" y="208" width="160" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
    <rect x="32" y="216" width="26" height="26" rx="4" fill="#FACC15"/>
    <text x="75" y="234" font-family="'Nunito', sans-serif" font-weight="800" font-size="12" fill="#475569">Square (Segi Empat)</text>

    <rect x="20" y="262" width="160" height="26" rx="6" fill="#DCFCE7"/>
    <text x="100" y="279" font-family="'Nunito', sans-serif" font-weight="800" font-size="10" fill="#15803D" text-anchor="middle">Tepat Sekali! 🔺</text>
  </g>
</svg>"""

def get_item_6_svg():
    # Adaptive Learning Experience Diagram
    return """<svg viewBox="0 0 500 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 6 Mockup: Adaptive Learning Experience Diagram">
  <rect x="10" y="10" width="480" height="300" rx="16" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <!-- Flow Node: ANAK -->
  <rect x="175" y="25" width="150" height="42" rx="10" fill="#FFFFFF" stroke="#2563EB" stroke-width="2"/>
  <text x="250" y="51" font-family="'Nunito', sans-serif" font-weight="900" font-size="13" fill="#1E293B" text-anchor="middle">ANAK</text>
  
  <path d="M250 67 L250 92" stroke="#2563EB" stroke-width="2.5"/>
  <polygon points="250,98 245,90 255,90" fill="#2563EB"/>

  <!-- Flow Node: PRESTASI -->
  <rect x="165" y="100" width="170" height="42" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
  <text x="250" y="126" font-family="'Nunito', sans-serif" font-weight="900" font-size="13" fill="#1E40AF" text-anchor="middle">PRESTASI</text>

  <path d="M250 142 L250 167" stroke="#2563EB" stroke-width="2.5"/>
  <polygon points="250,173 245,165 255,165" fill="#2563EB"/>

  <!-- Flow Node: SISTEM ADAPTIF -->
  <rect x="145" y="175" width="210" height="44" rx="12" fill="#2563EB"/>
  <text x="250" y="202" font-family="'Nunito', sans-serif" font-weight="900" font-size="13" fill="#FFFFFF" text-anchor="middle">SISTEM ADAPTIF</text>

  <!-- Branches -->
  <path d="M190 219 L110 248" stroke="#EF4444" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="105,250 114,244 110,254" fill="#EF4444"/>

  <path d="M310 219 L390 248" stroke="#10B981" stroke-width="2"/>
  <polygon points="395,250 390,254 386,244" fill="#10B981"/>

  <!-- BANTU -->
  <rect x="35" y="250" width="150" height="45" rx="8" fill="#FEF2F2" stroke="#EF4444"/>
  <text x="110" y="272" font-family="'Nunito', sans-serif" font-weight="900" font-size="12" fill="#991B1B" text-anchor="middle">BANTU</text>
  <text x="110" y="287" font-family="'Nunito', sans-serif" font-weight="700" font-size="9" fill="#DC2626" text-anchor="middle">Sokong jika sukar</text>

  <!-- CABAR -->
  <rect x="315" y="250" width="150" height="45" rx="8" fill="#F0FDF4" stroke="#10B981"/>
  <text x="390" y="272" font-family="'Nunito', sans-serif" font-weight="900" font-size="12" fill="#065F46" text-anchor="middle">CABAR</text>
  <text x="390" y="287" font-family="'Nunito', sans-serif" font-weight="700" font-size="9" fill="#16A34A" text-anchor="middle">Aras tinggi jika mahir</text>
</svg>"""

def get_item_7_svg():
    # Laptop SVG: Ruangan Ibubapa Perkembangan Anak
    return """<svg viewBox="0 0 500 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Item 7 Mockup: Parent Progress Dashboard">
  <defs>
    <clipPath id="item7-screen-clip">
      <rect x="40" y="20" width="420" height="240" rx="4"/>
    </clipPath>
  </defs>
  <rect x="25" y="10" width="450" height="260" rx="10" fill="#1E293B"/>
  <circle cx="250" cy="15" r="2.5" fill="#38BDF8"/>
  <g clip-path="url(#item7-screen-clip)" id="item7-laptop-screen">
    <rect x="40" y="20" width="420" height="240" fill="#F8FAFC"/>
    <!-- Topbar -->
    <rect x="40" y="20" width="420" height="35" fill="#FFFFFF"/>
    <line x1="40" y1="55" x2="460" y2="55" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="42" font-family="'Nunito', sans-serif" font-weight="900" font-size="13" fill="#2563EB">Ruangan Ibubapa</text>
    <text x="445" y="42" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#64748B" text-anchor="end">Pantau Prestasi</text>
    <!-- Child Overview -->
    <text x="55" y="78" font-family="'Nunito', sans-serif" font-weight="900" font-size="14" fill="#1E293B">Perkembangan Anak</text>
    <text x="55" y="94" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#2563EB">Aiman (Tahap 5)</text>

    <!-- Matematik 80% -->
    <rect x="55" y="108" width="390" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="68" y="127" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#1E293B">Matematik</text>
    <text x="430" y="127" font-family="'Nunito', sans-serif" font-weight="900" font-size="11" fill="#2563EB" text-anchor="end">80%</text>
    <rect x="68" y="133" width="360" height="8" rx="4" fill="#F1F5F9"/>
    <rect x="68" y="133" width="288" height="8" rx="4" fill="#2563EB"/>

    <!-- Bahasa 60% -->
    <rect x="55" y="156" width="390" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="68" y="175" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#1E293B">Bahasa</text>
    <text x="430" y="175" font-family="'Nunito', sans-serif" font-weight="900" font-size="11" fill="#10B981" text-anchor="end">60%</text>
    <rect x="68" y="181" width="360" height="8" rx="4" fill="#F1F5F9"/>
    <rect x="68" y="181" width="216" height="8" rx="4" fill="#10B981"/>

    <!-- Logik 40% -->
    <rect x="55" y="204" width="390" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="68" y="223" font-family="'Nunito', sans-serif" font-weight="800" font-size="11" fill="#1E293B">Logik</text>
    <text x="430" y="223" font-family="'Nunito', sans-serif" font-weight="900" font-size="11" fill="#8B5CF6" text-anchor="end">40%</text>
    <rect x="68" y="229" width="360" height="8" rx="4" fill="#F1F5F9"/>
    <rect x="68" y="229" width="144" height="8" rx="4" fill="#8B5CF6"/>
  </g>
  <path d="M10 270 L490 270 L460 290 L40 290 Z" fill="#64748B"/>
  <rect x="220" y="270" width="60" height="4" rx="2" fill="#334155"/>
</svg>"""

print("Items SVGs ready")
