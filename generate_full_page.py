# generate_full_page.py
import os
from build_page import get_head_and_styles
from svg_assets import (
    get_laptop_hero_svg,
    get_phone_hero_svg,
    get_trust_secure_payment_svg,
    get_trust_instant_access_svg,
    get_trust_privacy_first_svg
)
from svg_more_assets import (
    get_adaptive_diagram_svg,
    get_demo_laptop_selection_svg,
    get_demo_achievement_svg,
    get_demo_phone_letters_svg,
    get_demo_phone_shapes_svg,
    get_parent_dashboard_laptop_svg
)
from svg_items import (
    get_item_1_svg,
    get_item_2_svg,
    get_item_3_svg,
    get_item_4_svg,
    get_item_5_svg,
    get_item_6_svg,
    get_item_7_svg
)

def build_full_html():
    head = get_head_and_styles()
    
    html = [head]
    
    # 1. Top Brand Mark & Audience Badge & Hero
    html.append("""
    <!-- BRAND HEADER (NO MENU / NO NAVBAR) -->
    <header class="brand-header">
        <div class="container">
            <a href="#" class="brand-logo" aria-label="KiddiesSmart+ Beranda">
                KiddiesSmart<span class="plus">+</span>
            </a>
        </div>
    </header>

    <!-- SECTION 1: HERO -->
    <section class="hero">
        <div class="container">
            <span class="audience-badge">UNTUK IBU BAPA ANAK 4–12 TAHUN</span>
            <h1>Untuk Ibu Bapa Yang Mahu Anak Belajar Dengan Lebih Seronok — Bukan Dipaksa</h1>
            <p class="subheadline">
                KiddiesSmart+ ialah Education Game dengan Adaptive Learning yang membantu anak belajar mengikut tahap, kemahiran dan kemajuan mereka.
            </p>

            <!-- REAL LAPTOP + PHONE SVG MOCKUP -->
            <div class="hero-mockup-wrapper">
                <div class="hero-laptop-box">
                    """ + get_laptop_hero_svg() + """
                </div>
                <div class="hero-phone-box">
                    """ + get_phone_hero_svg() + """
                </div>
            </div>
        </div>
    </section>
    """)

    # TRUST SIGNALS SECTION (CREDIBILITY & REASSURANCE)
    html.append("""
    <section class="trust-signals-section" aria-label="Jaminan & Kredibiliti Platform">
        <div class="container">
            <div class="trust-signals-wrapper">
                <div class="trust-signals-grid">
                    <!-- Trust 1: Secure Payment -->
                    <div class="trust-signal-card" id="trust-signal-payment">
                        <div class="trust-icon-box secure" aria-hidden="true">
                            """ + get_trust_secure_payment_svg() + """
                        </div>
                        <div class="trust-signal-text">
                            <h3>Pembayaran Selamat</h3>
                            <p>Transaksi dilindungi penyulitan SSL 256-bit yang selamat & telus.</p>
                        </div>
                    </div>

                    <!-- Trust 2: Instant Access -->
                    <div class="trust-signal-card" id="trust-signal-access">
                        <div class="trust-icon-box instant" aria-hidden="true">
                            """ + get_trust_instant_access_svg() + """
                        </div>
                        <div class="trust-signal-text">
                            <h3>Akses Serta-Merta</h3>
                            <p>Akses platform diaktifkan terus sejurus pengesahan pembayaran.</p>
                        </div>
                    </div>

                    <!-- Trust 3: Privacy-First -->
                    <div class="trust-signal-card" id="trust-signal-privacy">
                        <div class="trust-icon-box privacy" aria-hidden="true">
                            """ + get_trust_privacy_first_svg() + """
                        </div>
                        <div class="trust-signal-text">
                            <h3>Privasi Terpelihara</h3>
                            <p>Persekitaran 100% selamat kanak-kanak tanpa iklan pihak ketiga.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 2: PROBLEM
    html.append("""
    <section class="problem-section">
        <div class="container">
            <div class="section-header">
                <h2>Anak Suka Main. Tapi Boleh Tak Masa Skrin Itu Jadi Masa Belajar?</h2>
                <p class="problem-intro">“Sebagai ibu bapa, kita semua berhadapan dengan situasi yang sama…”</p>
            </div>

            <div class="problem-grid">
                <!-- Card 1 -->
                <div class="problem-card">
                    <div class="problem-icon-wrap">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#EF4444" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"/>
                            <path d="M8 15h8"/>
                            <line x1="9" y1="9" x2="9.01" y2="9"/>
                            <line x1="15" y1="9" x2="15.01" y2="9"/>
                        </svg>
                    </div>
                    <h3>Cepat Bosan</h3>
                    <p>Aktiviti belajar biasa susah mengekalkan perhatian anak.</p>
                </div>

                <!-- Card 2 -->
                <div class="problem-card">
                    <div class="problem-icon-wrap">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#EF4444" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="12 6 12 12 14 14"/>
                            <path d="M4.93 4.93l4.24 4.24"/>
                        </svg>
                    </div>
                    <h3>Susah Fokus</h3>
                    <p>Anak cepat hilang minat apabila belajar terasa seperti tugasan.</p>
                </div>

                <!-- Card 3 -->
                <div class="problem-card">
                    <div class="problem-icon-wrap">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#EF4444" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="3" width="20" height="14" rx="2"/>
                            <line x1="8" y1="21" x2="16" y2="21"/>
                            <line x1="12" y1="17" x2="12" y2="21"/>
                            <line x1="2" y1="3" x2="22" y2="17"/>
                        </svg>
                    </div>
                    <h3>Screen Time Pasif</h3>
                    <p>Masa skrin boleh menjadi lebih bermakna apabila anak turut berfikir dan menyelesaikan cabaran.</p>
                </div>

                <!-- Card 4 -->
                <div class="problem-card">
                    <div class="problem-icon-wrap">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#EF4444" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="18" y1="20" x2="18" y2="10"/>
                            <line x1="12" y1="20" x2="12" y2="4"/>
                            <line x1="6" y1="20" x2="6" y2="14"/>
                            <path d="M2 18l6-4 4 4 8-10"/>
                        </svg>
                    </div>
                    <h3>Tahap Tak Sesuai</h3>
                    <p>Aktiviti yang terlalu mudah atau terlalu sukar boleh mengurangkan minat anak.</p>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 3: DESIRE
    html.append("""
    <section class="desire-section">
        <div class="container">
            <div class="desire-box">
                <h2>Bayangkan Kalau Anak Mula Minta Untuk “Main Belajar”...</h2>
                <p class="desire-quote">“Kini masa skrin boleh menjadi sebahagian daripada rutin pembelajaran yang lebih interaktif.”</p>
                <p class="desire-copy">
                    Anak bermain. Mereka menyelesaikan cabaran. Ibu bapa pula boleh melihat perkembangan secara telus dan tenang.
                </p>
                <div class="desire-pills">
                    <span class="desire-pill">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                        Anak Suka Main
                    </span>
                    <span class="desire-pill">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                        Selesaikan Cabaran
                    </span>
                    <span class="desire-pill">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                        Ibu Bapa Pantau Kemajuan
                    </span>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 4: UNIQUE MECHANISM
    html.append("""
    <section class="mechanism-section">
        <div class="container">
            <div class="section-header">
                <h2>Rahsianya: Adaptive Learning</h2>
                <p>KiddiesSmart+ bukan sekadar game biasa. Konsep Adaptive Learning membantu pengalaman pembelajaran disesuaikan berdasarkan prestasi anak.</p>
            </div>

            <div class="diagram-container">
                """ + get_adaptive_diagram_svg() + """
            </div>

            <div class="steps-grid">
                <div class="step-item">
                    <div class="step-number">01</div>
                    <h4>Anak Menjawab</h4>
                    <p>Anak menyelesaikan aktiviti interaktif mengikut minat mereka.</p>
                </div>
                <div class="step-item">
                    <div class="step-number">02</div>
                    <h4>Prestasi Dinilai</h4>
                    <p>Sistem menganalisis ketepatan dan kelancaran jawapan anak.</p>
                </div>
                <div class="step-item">
                    <div class="step-number">03</div>
                    <h4>Sistem Beradaptasi</h4>
                    <p>Modul melaraskan tahap cabaran dan bimbingan secara dinamik.</p>
                </div>
                <div class="step-item">
                    <div class="step-number">04</div>
                    <h4>Berlatih Tahap Sesuai</h4>
                    <p>Anak terus berlatih pada aras yang membina keyakinan diri.</p>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 5: PRODUCT ECOSYSTEM
    html.append("""
    <section class="ecosystem-section">
        <div class="container">
            <div class="section-header">
                <h2>Bukan Sekadar Satu Game. Ia Sebuah Ekosistem Pembelajaran.</h2>
                <p>Enam tunjang perkembangan kognitif menyeluruh yang dibina khusus untuk anak-anak umur 4 hingga 12 tahun.</p>
            </div>

            <div class="categories-grid">
                <!-- 1. Matematik -->
                <div class="category-card cat-math">
                    <div class="category-icon-box">
                        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="12" y1="5" x2="12" y2="19"/>
                            <line x1="5" y1="12" x2="19" y2="12"/>
                        </svg>
                    </div>
                    <h3>Matematik</h3>
                    <p>Pengiraan asas, nombor, operasi tambah tolak dan kemahiran wang interaktif.</p>
                </div>

                <!-- 2. Bahasa -->
                <div class="category-card cat-lang">
                    <div class="category-icon-box">
                        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#10B981" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                        </svg>
                    </div>
                    <h3>Bahasa</h3>
                    <p>Pengecaman huruf, pembinaan perkataan, perbendaharaan kata dan kemahiran membaca.</p>
                </div>

                <!-- 3. Logik -->
                <div class="category-card cat-logic">
                    <div class="category-icon-box">
                        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#8B5CF6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-2.04z"/>
                            <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-2.04z"/>
                        </svg>
                    </div>
                    <h3>Logik</h3>
                    <p>Penyelesaian masalah bertahap, pola berturutan dan pemikiran analitikal kreatif.</p>
                </div>

                <!-- 4. Memori -->
                <div class="category-card cat-memory">
                    <div class="category-icon-box">
                        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#F59E0B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                        </svg>
                    </div>
                    <h3>Memori</h3>
                    <p>Latihan ingatan visual berperingkat, padanan kad simbol dan daya tumpuan aktif.</p>
                </div>

                <!-- 5. Visual -->
                <div class="category-card cat-visual">
                    <div class="category-icon-box">
                        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#F43F5E" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"/>
                            <circle cx="12" cy="12" r="4"/>
                        </svg>
                    </div>
                    <h3>Visual</h3>
                    <p>Diskriminasi warna, pengecaman bentuk geometri dan orientasi spatial anak.</p>
                </div>

                <!-- 6. Kreativiti -->
                <div class="category-card cat-creative">
                    <div class="category-icon-box">
                        <svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#0D9488" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 19l7-7 3 3-7 7-3-3z"/>
                            <path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/>
                            <path d="M2 2l7.586 7.586"/>
                            <circle cx="11" cy="11" r="2"/>
                        </svg>
                    </div>
                    <h3>Kreativiti</h3>
                    <p>Aktiviti berasaskan imaginasi, eksplorasi idea bebas dan ekspresi pemikiran positif.</p>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 6: REAL PRODUCT DEMONSTRATION
    html.append("""
    <section class="demo-section">
        <div class="container">
            <div class="section-header">
                <h2>Ini Bukan Sekadar Gambar Cantik — Ini Antara Aktiviti Yang Anak Anda Akan Main</h2>
                <p>“Lihat sendiri bagaimana pengalaman KiddiesSmart+ kelihatan.”</p>
            </div>

            <div class="demo-grid">
                <!-- Visual A: Laptop Pilih Permainan -->
                <div class="demo-item">
                    <h3>Pilih Permainan <span class="demo-badge">Paparan Laptop</span></h3>
                    <div class="demo-frame">
                        """ + get_demo_laptop_selection_svg() + """
                    </div>
                </div>

                <!-- Visual B: Laptop Pencapaian Anda -->
                <div class="demo-item">
                    <h3>Pencapaian Anda <span class="demo-badge">Sistem Ganjaran</span></h3>
                    <div class="demo-frame">
                        """ + get_demo_achievement_svg() + """
                    </div>
                </div>

                <!-- Visual C: Phone Cari Huruf -->
                <div class="demo-item">
                    <h3>Cari Huruf <span class="demo-badge">Paparan Telefon</span></h3>
                    <div class="demo-frame" style="max-width: 300px;">
                        """ + get_demo_phone_letters_svg() + """
                    </div>
                </div>

                <!-- Visual D: Phone Bentuk & Warna -->
                <div class="demo-item">
                    <h3>Bentuk &amp; Warna <span class="demo-badge">Paparan Telefon</span></h3>
                    <div class="demo-frame" style="max-width: 300px;">
                        """ + get_demo_phone_shapes_svg() + """
                    </div>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 7: BENEFITS
    html.append("""
    <section class="benefits-section">
        <div class="container">
            <div class="section-header">
                <h2>Kenapa Ibu Bapa Pilih KiddiesSmart+?</h2>
                <p>Direka khusus untuk memberi ketenangan minda kepada ibu bapa dan pengalaman yang menyeronokkan kepada anak.</p>
            </div>

            <div class="benefits-grid">
                <!-- Benefit 1 -->
                <div class="benefit-card">
                    <div class="benefit-icon">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#2563EB" stroke-width="2.2">
                            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
                        </svg>
                    </div>
                    <div>
                        <h3>Pembelajaran Adaptif</h3>
                        <p>Tahap kesukaran disesuaikan mengikut prestasi anak agar mereka tidak berasa terbeban atau bosan.</p>
                    </div>
                </div>

                <!-- Benefit 2 -->
                <div class="benefit-card">
                    <div class="benefit-icon">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#2563EB" stroke-width="2.2">
                            <circle cx="12" cy="12" r="10"/>
                            <polygon points="10 8 16 12 10 16 10 8"/>
                        </svg>
                    </div>
                    <div>
                        <h3>Belajar Melalui Permainan</h3>
                        <p>Gamifikasi, mata ganjaran dan pencapaian menjadikan pembelajaran lebih interaktif tanpa paksaan.</p>
                    </div>
                </div>

                <!-- Benefit 3 -->
                <div class="benefit-card">
                    <div class="benefit-icon">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#2563EB" stroke-width="2.2">
                            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                        </svg>
                    </div>
                    <div>
                        <h3>Pelbagai Kemahiran</h3>
                        <p>Merangkumi Matematik, Bahasa, Logik, Memori, Visual dan Kreativiti dalam satu platform bersepadu.</p>
                    </div>
                </div>

                <!-- Benefit 4 -->
                <div class="benefit-card">
                    <div class="benefit-icon">
                        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#2563EB" stroke-width="2.2">
                            <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
                        </svg>
                    </div>
                    <div>
                        <h3>Pantau Perkembangan</h3>
                        <p>Ibu bapa boleh melihat perkembangan melalui Ruangan Ibubapa secara langsung bila-bila masa.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 8: PARENT DASHBOARD
    html.append("""
    <section class="parent-section">
        <div class="container">
            <div class="section-header">
                <h2>Ibu Bapa Tak Perlu Tertanya-Tanya Lagi: Anak Dah Kuasai Apa?</h2>
                <p>“Daripada hanya berharap anak belajar, anda boleh melihat perkembangan mereka.”</p>
            </div>

            <div class="parent-laptop-wrap">
                """ + get_parent_dashboard_laptop_svg() + """
            </div>
        </div>
    </section>
    """)

    # SECTION 9: HOW IT WORKS
    html.append("""
    <section class="how-section">
        <div class="container">
            <div class="section-header">
                <h2>Bagaimana KiddiesSmart+ Berfungsi?</h2>
                <p>Langkah mudah yang membolehkan anak berdikari sambil ibu bapa kekal memegang kawalan.</p>
            </div>

            <div class="how-grid">
                <div class="how-card">
                    <span class="how-pill">Langkah 01</span>
                    <h3>Pilih Permainan</h3>
                    <p>Anak pilih aktiviti yang mereka mahu main mengikut subjek kegemaran.</p>
                </div>
                <div class="how-card">
                    <span class="how-pill">Langkah 02</span>
                    <h3>Anak Bermain</h3>
                    <p>Mereka menyelesaikan cabaran pembelajaran interaktif dengan gembira.</p>
                </div>
                <div class="how-card">
                    <span class="how-pill">Langkah 03</span>
                    <h3>Sistem Beradaptasi</h3>
                    <p>Pengalaman disesuaikan berdasarkan prestasi dan respons masa-nyata anak.</p>
                </div>
                <div class="how-card">
                    <span class="how-pill">Langkah 04</span>
                    <h3>Ibu Bapa Pantau</h3>
                    <p>Semak perkembangan serta pencapaian kemahiran melalui Ruangan Ibubapa.</p>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 10: WHAT CUSTOMER GETS (7 MOCKUPS + VALUES) + VALUE TOTAL
    html.append("""
    <section class="what-you-get-section">
        <div class="container">
            <div class="section-header">
                <h2>Apa Yang Anda Dapat Dengan RM45?</h2>
                <p>“Bukan sekadar satu game. Anda mendapat akses kepada pengalaman pembelajaran KiddiesSmart+.”</p>
            </div>

            <div class="items-stack">
                <!-- Item 1 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_1_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>1. KiddiesSmart+ Education Games</h3>
                        <p>Pusat permainan pembelajaran interaktif untuk anak dengan antaramuka mesra kanak-kanak, sistem bintang dan pilihan kategori aktiviti.</p>
                        <span class="get-value-tag">NILAI RM79</span>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_2_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>2. Matematik &amp; Number Skills</h3>
                        <p>Modul interaktif Kira &amp; Kumpul, pengiraan objek visual, operasi asas nombor dan kemahiran tambah tolak yang membina asas matematik kukuh.</p>
                        <span class="get-value-tag">NILAI RM79</span>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_3_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>3. Bahasa &amp; Word Skills</h3>
                        <p>Aktiviti Cari Huruf, pengenalan abjad, pengecaman bunyi huruf dan pembinaan kosa kata yang mempercepatkan kemahiran literasi anak.</p>
                        <span class="get-value-tag">NILAI RM59</span>
                    </div>
                </div>

                <!-- Item 4 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_4_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>4. Memory &amp; Logic Games</h3>
                        <p>Permainan padanan kad simbol, pencarian pola dan teka-teki pemikiran logik yang mengasah daya ingatan serta fokus minda anak.</p>
                        <span class="get-value-tag">NILAI RM49</span>
                    </div>
                </div>

                <!-- Item 5 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_5_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>5. Creative &amp; Visual Activities</h3>
                        <p>Aktiviti Bentuk &amp; Warna, pengecaman geometri, diskriminasi warna dan latihan orientasi visual yang menyuburkan koordinasi mata-tangan.</p>
                        <span class="get-value-tag">NILAI RM49</span>
                    </div>
                </div>

                <!-- Item 6 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_6_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>6. Adaptive Learning Experience</h3>
                        <p>Enjin pembelajaran pintar yang melaras kesukaran soalan secara automatik mengikut keupayaan anak — memberi bimbingan bila sukar dan mencabar bila mahir.</p>
                        <span class="get-value-tag">NILAI RM79</span>
                    </div>
                </div>

                <!-- Item 7 -->
                <div class="get-item-card">
                    <div class="get-visual-col">
                        """ + get_item_7_svg() + """
                    </div>
                    <div class="get-content-col">
                        <h3>7. Parent Progress Dashboard</h3>
                        <p>Ruangan Ibubapa khusus untuk memantau peratusan perkembangan kemahiran anak (Matematik, Bahasa, Logik) tanpa perlu teka-teki.</p>
                        <span class="get-value-tag">NILAI RM39</span>
                    </div>
                </div>
            </div>

            <!-- VALUE STACK TOTAL (NO BUTTON HERE!) -->
            <div class="value-total-box">
                <div class="value-total-label">Nilai Kumulatif Keseluruhan</div>
                <div class="value-total-amount">JUMLAH NILAI: RM433</div>
                <div class="value-contrast">
                    <span class="striked-price">Nilai Biasa: RM433</span>
                    <span class="highlight-price">ANDA DAPAT DENGAN HANYA RM45</span>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 11: PRICE ANCHOR
    html.append("""
    <section class="anchor-section">
        <div class="container">
            <div class="anchor-card">
                <h3>Kalau Nilainya RM433, Kenapa Hanya RM45?</h3>
                <p>
                    Kerana objektif kami adalah menjadikan pengalaman pembelajaran interaktif ini lebih mudah dicapai oleh ibu bapa di Malaysia tanpa bebanan yuran bulanan yang tinggi. Kami percaya setiap anak berhak menikmati kaedah pembelajaran moden yang menyeronokkan.
                </p>
                <div class="anchor-comparison">
                    <div class="anchor-comp-item">
                        <span>Nilai Keseluruhan Modul</span>
                        <strong style="color: #64748B; text-decoration: line-through;">RM433</strong>
                    </div>
                    <div class="anchor-comp-item">
                        <span>Harga Tawaran Rasmi</span>
                        <strong style="color: #2563EB;">RM45 Sahaja</strong>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 12: PRICING TABLE (THE ONLY SECTION WITH A CTA BUTTON!)
    html.append("""
    <section class="pricing-section" id="tempahan">
        <div class="container">
            <div class="pricing-card">
                <div class="pricing-popular-badge">Pakej Penuh Kanak-Kanak</div>
                <h2>Dapatkan KiddiesSmart+ Hari Ini</h2>
                <p class="pricing-sub">Akses pengalaman pembelajaran KiddiesSmart+ dengan harga RM45.</p>

                <div class="pricing-price-box">
                    <div class="pricing-old-val">Nilai Keseluruhan: RM433</div>
                    <div class="pricing-deal-price"><span>RM</span>45</div>
                    <div class="pricing-onetime">✓ Bayaran sekali untuk akses platform seperti yang ditawarkan</div>
                </div>

                <ul class="pricing-features-list">
                    <li><span class="check-icon">✓</span> KiddiesSmart+ Education Games</li>
                    <li><span class="check-icon">✓</span> Matematik &amp; Number Skills</li>
                    <li><span class="check-icon">✓</span> Bahasa &amp; Word Skills</li>
                    <li><span class="check-icon">✓</span> Memory &amp; Logic Games</li>
                    <li><span class="check-icon">✓</span> Creative &amp; Visual Activities</li>
                    <li><span class="check-icon">✓</span> Adaptive Learning Experience</li>
                    <li><span class="check-icon">✓</span> Parent Progress Dashboard</li>
                </ul>

                <!-- SATU-SATUNYA CTA BUTTON DI SELURUH PAGE -->
                <a href="#" class="cta-button">
                    DAPATKAN KIDDIESMART+ RM45
                </a>

                <div class="pricing-guarantee-note">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                    Akses selamat serta-merta selepas pembayaran selesai
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 13: OBJECTION HANDLING
    html.append("""
    <section class="objection-section">
        <div class="container">
            <div class="section-header">
                <h2>Mungkin Anda Sedang Terfikir...</h2>
                <p>Jawapan telus untuk kebimbangan lazim para ibu bapa.</p>
            </div>

            <div class="objection-grid">
                <div class="objection-card">
                    <h3>“Anak saya cepat bosan.”</h3>
                    <p>KiddiesSmart+ direka berasaskan gamifikasi interaktif — setiap aktiviti disertakan dengan visual bertenaga, sistem mata bintang dan lencana pencapaian supaya proses pembelajaran terasa seperti permainan santai.</p>
                </div>

                <div class="objection-card">
                    <h3>“Anak saya bukan pandai sangat guna komputer.”</h3>
                    <p>Antaramuka platform dibina seringkas mungkin dengan ikon visual yang jelas, navigasi satu klik dan elemen yang mudah disentuh pada skrin telefon atau tablet.</p>
                </div>

                <div class="objection-card">
                    <h3>“Boleh guna telefon?”</h3>
                    <p>Ya. Platform kami 100% responsif dan boleh diakses dengan lancar pada telefon pintar, tablet, iPad, komputer riba mahupun desktop komputer rumah anda.</p>
                </div>

                <div class="objection-card">
                    <h3>“Boleh saya pantau perkembangan?”</h3>
                    <p>Ya, anda boleh mengakses Ruangan Ibubapa pada bila-bila masa untuk melihat tahap kemahiran anak dalam Matematik, Bahasa dan Logik secara terperinci.</p>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 14: FAQ (ACCORDION - NO GUARANTEES)
    html.append("""
    <section class="faq-section">
        <div class="container container-narrow">
            <div class="section-header">
                <h2>Soalan Yang Mungkin Anda Nak Tanya</h2>
                <p>Segala maklumat yang anda perlukan mengenai platform KiddiesSmart+.</p>
            </div>

            <div class="faq-accordion">
                <!-- FAQ 1 -->
                <div class="faq-item active">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>1. KiddiesSmart+ sesuai untuk umur berapa?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        Direka untuk kanak-kanak sekitar 4–12 tahun, bergantung kepada tahap dan aktiviti. Konsep adaptif membolehkan soalan disesuaikan mengikut keupayaan individu anak.
                    </div>
                </div>

                <!-- FAQ 2 -->
                <div class="faq-item">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>2. Apa subjek yang ada?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        Matematik, Bahasa, Logik, Memori, Visual dan Kreativiti.
                    </div>
                </div>

                <!-- FAQ 3 -->
                <div class="faq-item">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>3. Boleh digunakan di telefon?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        Ya. Platform responsive dan boleh digunakan pada telefon pintar, tablet, laptop dan desktop.
                    </div>
                </div>

                <!-- FAQ 4 -->
                <div class="faq-item">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>4. Ibu bapa boleh pantau perkembangan anak?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        Ya, melalui Ruangan Ibubapa yang menunjukkan graf dan peratusan penguasaan kemahiran anak secara tepat.
                    </div>
                </div>

                <!-- FAQ 5 -->
                <div class="faq-item">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>5. Adakah ini menggantikan sekolah atau guru?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        Tidak. Ia adalah aktiviti pembelajaran tambahan yang melengkapi pendidikan formal anak di sekolah secara santai di rumah.
                    </div>
                </div>

                <!-- FAQ 6 -->
                <div class="faq-item">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>6. Berapa harga?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        RM45 sahaja (bayaran sekali untuk akses platform seperti yang ditawarkan).
                    </div>
                </div>

                <!-- FAQ 7 -->
                <div class="faq-item">
                    <div class="faq-header" onclick="toggleFaq(this)">
                        <span>7. Apa yang saya dapat?</span>
                        <span class="faq-toggle-icon">+</span>
                    </div>
                    <div class="faq-content">
                        Akses kepada modul permainan, Adaptive Learning Experience dan Parent Progress Dashboard seperti yang ditawarkan.
                    </div>
                </div>
            </div>
        </div>
    </section>
    """)

    # SECTION 15: FINAL EMOTIONAL CLOSE
    html.append("""
    <section class="closing-section">
        <div class="container">
            <div class="closing-box">
                <h2>Kadang-Kadang Anak Bukan Tak Suka Belajar.</h2>
                <h3>Mereka Cuma Perlukan Cara Belajar Yang Lebih Dekat Dengan Dunia Mereka.</h3>
                <p>
                    KiddiesSmart+ menggabungkan pembelajaran, permainan dan pemantauan dalam satu pengalaman yang lebih interaktif.
                </p>
                <p>
                    Biarkan anak bermain sambil membina kemahiran. Dan biarkan anda melihat perkembangan mereka.
                </p>
            </div>
        </div>
    </section>
    """)

    # FOOTER (NO MENU, NO CTA)
    html.append("""
    <footer>
        <div class="container">
            <div class="footer-brand">KiddiesSmart+</div>
            <div class="footer-sub">Education Game</div>
            <div class="footer-quote">“Pembelajaran yang menyeronokkan, satu permainan pada satu masa.”</div>
            <div class="copyright">© 2026 KiddiesSmart+. Hak Cipta Terpelihara.</div>
        </div>
    </footer>

    <!-- EMBEDDED JAVASCRIPT FOR ACCORDION (MINIMAL, ZERO EXTERNAL DEPENDENCY) -->
    <script>
        function toggleFaq(headerEl) {
            const item = headerEl.parentElement;
            const wasActive = item.classList.contains('active');
            
            // Close all other items
            const allItems = document.querySelectorAll('.faq-item');
            allItems.forEach(i => i.classList.remove('active'));
            
            if (!wasActive) {
                item.classList.add('active');
            }
        }
    </script>
</body>
</html>
    """)

    return "".join(html)

if __name__ == "__main__":
    output_html = build_full_html()
    with open("kiddiessmart-sales-page.html", "w", encoding="utf-8") as f:
        f.write(output_html)
    print(f"Generated kiddiessmart-sales-page.html (size: {len(output_html)} bytes)")
    
    # Also save in public folder and root index.html
    os.makedirs("public", exist_ok=True)
    with open("public/kiddiessmart-sales-page.html", "w", encoding="utf-8") as f:
        f.write(output_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output_html)
    print("Also copied to public/kiddiessmart-sales-page.html and index.html")
