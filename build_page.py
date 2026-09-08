# build_page.py
import os

def get_head_and_styles():
    return """<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KiddiesSmart+ Education Game — Adaptive Learning Untuk Anak</title>
    <meta name="description" content="Bantu anak belajar melalui permainan interaktif dengan Adaptive Learning, pelbagai aktiviti dan Parent Progress Dashboard. Dapatkan KiddiesSmart+ dengan RM45.">
    <meta property="og:title" content="KiddiesSmart+ Education Game — Adaptive Learning Untuk Anak">
    <meta property="og:description" content="Bantu anak belajar melalui permainan interaktif dengan Adaptive Learning, pelbagai aktiviti dan Parent Progress Dashboard. Dapatkan KiddiesSmart+ dengan RM45.">
    <meta property="og:type" content="website">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2563EB;
            --primary-dark: #1D4ED8;
            --primary-light: #EFF6FF;
            --secondary: #38BDF8;
            --accent: #FACC15;
            --accent-red: #EF4444;
            --accent-red-hover: #DC2626;
            --success: #10B981;
            --dark: #1E293B;
            --dark-surface: #0F172A;
            --muted: #64748B;
            --border: #E2E8F0;
            --bg-light: #F8FAFC;
            --white: #FFFFFF;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Nunito', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-light);
            color: var(--dark);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        .container {
            width: 100%;
            max-width: 1120px;
            margin-left: auto;
            margin-right: auto;
            padding-left: 20px;
            padding-right: 20px;
        }

        .container-narrow {
            max-width: 820px;
        }

        /* Top Brand Mark - No Navigation */
        .brand-header {
            padding: 24px 0 16px 0;
            text-align: center;
            background: transparent;
        }

        .brand-logo {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            font-weight: 900;
            font-size: 26px;
            color: var(--primary);
            letter-spacing: -0.5px;
            text-decoration: none;
        }

        .brand-logo .plus {
            color: var(--accent-red);
            font-size: 28px;
        }

        /* Attention Badge */
        .audience-badge {
            display: inline-block;
            background-color: var(--accent-red);
            color: #FFFFFF;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            padding: 8px 18px;
            border-radius: 9999px;
            margin-bottom: 24px;
            box-shadow: 0 4px 14px rgba(239, 68, 68, 0.28);
        }

        /* Hero Section */
        .hero {
            padding: 20px 0 60px 0;
            text-align: center;
        }

        .hero h1 {
            font-size: 40px;
            line-height: 1.25;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 20px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero p.subheadline {
            font-size: 20px;
            color: var(--muted);
            line-height: 1.6;
            max-width: 780px;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 40px;
            font-weight: 600;
        }

        /* Device Showcase */
        .hero-mockup-wrapper {
            position: relative;
            max-width: 980px;
            margin: 0 auto;
            padding-bottom: 30px;
        }

        .hero-laptop-box {
            width: 88%;
            margin-left: 0;
            filter: drop-shadow(0 25px 35px rgba(15, 23, 42, 0.12));
        }

        .hero-phone-box {
            position: absolute;
            right: 0;
            bottom: 0;
            width: 28%;
            filter: drop-shadow(0 20px 30px rgba(15, 23, 42, 0.2));
            z-index: 2;
        }

        svg {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Sections General */
        section {
            padding: 72px 0;
        }

        .section-header {
            text-align: center;
            margin-bottom: 48px;
        }

        .section-header h2 {
            font-size: 34px;
            font-weight: 900;
            color: var(--dark);
            line-height: 1.3;
            margin-bottom: 14px;
        }

        .section-header p {
            font-size: 18px;
            color: var(--muted);
            max-width: 720px;
            margin: 0 auto;
            font-weight: 600;
        }

        /* Section: Trust Signals */
        .trust-signals-section {
            background-color: #FFFFFF;
            padding: 20px 0 40px 0;
            position: relative;
            z-index: 5;
        }

        .trust-signals-wrapper {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05);
            padding: 28px 36px;
        }

        .trust-signals-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
            align-items: center;
        }

        .trust-signal-card {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .trust-icon-box {
            flex-shrink: 0;
            width: 56px;
            height: 56px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .trust-icon-box.secure {
            background: #EFF6FF;
            border: 1px solid #BFDBFE;
            color: #2563EB;
        }

        .trust-icon-box.instant {
            background: #FEF3C7;
            border: 1px solid #FDE68A;
            color: #D97706;
        }

        .trust-icon-box.privacy {
            background: #ECFDF5;
            border: 1px solid #A7F3D0;
            color: #059669;
        }

        .trust-signal-card:hover .trust-icon-box {
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
        }

        .trust-signal-text h3 {
            font-size: 17px;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 4px;
            line-height: 1.3;
        }

        .trust-signal-text p {
            font-size: 13.5px;
            color: var(--muted);
            line-height: 1.45;
            margin: 0;
            font-weight: 600;
        }

        /* Section: Problem */
        .problem-section {
            background-color: #FFFFFF;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
        }

        .problem-intro {
            font-size: 19px;
            font-style: italic;
            color: var(--muted);
            text-align: center;
            margin-bottom: 36px;
        }

        .problem-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
        }

        .problem-card {
            background: #FFF5F5;
            border: 1px solid #FECACA;
            border-radius: 16px;
            padding: 28px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .problem-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(239, 68, 68, 0.08);
        }

        .problem-icon-wrap {
            width: 52px;
            height: 52px;
            background: #FEE2E2;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 18px;
        }

        .problem-card h3 {
            font-size: 20px;
            font-weight: 800;
            color: #991B1B;
            margin-bottom: 10px;
        }

        .problem-card p {
            color: #4B5563;
            font-size: 16px;
            line-height: 1.6;
        }

        /* Section: Desire */
        .desire-section {
            background: linear-gradient(180deg, #F8FAFC 0%, #EFF6FF 100%);
            text-align: center;
        }

        .desire-box {
            background: #FFFFFF;
            border: 1px solid #BFDBFE;
            border-radius: 24px;
            padding: 48px 36px;
            max-width: 880px;
            margin: 0 auto;
            box-shadow: 0 20px 40px rgba(37, 99, 235, 0.06);
        }

        .desire-box h2 {
            font-size: 34px;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 24px;
            line-height: 1.3;
        }

        .desire-quote {
            font-size: 20px;
            color: var(--primary-dark);
            font-weight: 700;
            margin-bottom: 16px;
        }

        .desire-copy {
            font-size: 18px;
            color: var(--muted);
            max-width: 680px;
            margin: 0 auto 32px auto;
            line-height: 1.7;
        }

        .desire-pills {
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .desire-pill {
            background: var(--primary-light);
            border: 1px solid #BFDBFE;
            color: var(--primary);
            padding: 10px 20px;
            border-radius: 9999px;
            font-weight: 800;
            font-size: 15px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        /* Section: Unique Mechanism */
        .mechanism-section {
            background: #FFFFFF;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
        }

        .diagram-container {
            background: #F8FAFC;
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 32px;
            margin-top: 36px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.03);
        }

        .steps-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 36px;
        }

        .step-item {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 22px;
            text-align: center;
            position: relative;
        }

        .step-number {
            width: 38px;
            height: 38px;
            background: var(--primary);
            color: #FFFFFF;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            font-size: 16px;
            margin-bottom: 12px;
        }

        .step-item h4 {
            font-size: 17px;
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 8px;
        }

        .step-item p {
            font-size: 14px;
            color: var(--muted);
            line-height: 1.5;
        }

        /* Section: Ecosystem */
        .categories-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }

        .category-card {
            background: #FFFFFF;
            border-radius: 18px;
            padding: 28px;
            border: 1px solid var(--border);
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
        }

        .category-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 30px rgba(0,0,0,0.06);
        }

        .category-icon-box {
            width: 58px;
            height: 58px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 18px;
        }

        .cat-math { background: #EFF6FF; border-top: 4px solid #2563EB; }
        .cat-math .category-icon-box { background: #DBEAFE; }

        .cat-lang { background: #F0FDF4; border-top: 4px solid #10B981; }
        .cat-lang .category-icon-box { background: #DCFCE7; }

        .cat-logic { background: #FAF5FF; border-top: 4px solid #8B5CF6; }
        .cat-logic .category-icon-box { background: #F3E8FF; }

        .cat-memory { background: #FFFBEB; border-top: 4px solid #F59E0B; }
        .cat-memory .category-icon-box { background: #FEF3C7; }

        .cat-visual { background: #FFF1F2; border-top: 4px solid #F43F5E; }
        .cat-visual .category-icon-box { background: #FFE4E6; }

        .cat-creative { background: #F0FDFA; border-top: 4px solid #0D9488; }
        .cat-creative .category-icon-box { background: #CCFBF1; }

        .category-card h3 {
            font-size: 21px;
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 8px;
        }

        .category-card p {
            color: var(--muted);
            font-size: 15px;
            line-height: 1.5;
        }

        /* Section: Product Demo */
        .demo-section {
            background: #FFFFFF;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
        }

        .demo-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 32px;
        }

        .demo-item {
            background: var(--bg-light);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 24px;
            text-align: center;
        }

        .demo-item h3 {
            font-size: 20px;
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .demo-badge {
            background: #E2E8F0;
            color: var(--dark);
            font-size: 12px;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 999px;
        }

        .demo-frame {
            max-width: 440px;
            margin: 0 auto;
            filter: drop-shadow(0 12px 20px rgba(0,0,0,0.06));
        }

        /* Section: Benefits */
        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
        }

        .benefit-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 32px;
            display: flex;
            gap: 20px;
            align-items: flex-start;
            transition: all 0.2s ease;
        }

        .benefit-card:hover {
            border-color: var(--primary);
            box-shadow: 0 10px 25px rgba(37, 99, 235, 0.08);
            transform: translateY(-2px);
        }

        .benefit-icon {
            width: 52px;
            height: 52px;
            background: var(--primary-light);
            border-radius: 12px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .benefit-card h3 {
            font-size: 20px;
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 8px;
        }

        .benefit-card p {
            color: var(--muted);
            font-size: 15px;
            line-height: 1.6;
        }

        /* Section: Parent Dashboard */
        .parent-section {
            background: linear-gradient(180deg, #EFF6FF 0%, #FFFFFF 100%);
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
        }

        .parent-laptop-wrap {
            max-width: 820px;
            margin: 0 auto;
            filter: drop-shadow(0 25px 35px rgba(30, 41, 59, 0.12));
        }

        /* Section: How It Works */
        .how-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }

        .how-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px 20px;
            text-align: center;
            position: relative;
        }

        .how-pill {
            display: inline-block;
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 900;
            font-size: 13px;
            padding: 4px 12px;
            border-radius: 999px;
            margin-bottom: 16px;
            border: 1px solid #BFDBFE;
        }

        .how-card h3 {
            font-size: 18px;
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 10px;
        }

        .how-card p {
            color: var(--muted);
            font-size: 14px;
            line-height: 1.5;
        }

        /* Section: What Customer Gets (Conversion Core) */
        .what-you-get-section {
            background: #F8FAFC;
        }

        .items-stack {
            display: flex;
            flex-direction: column;
            gap: 28px;
            max-width: 900px;
            margin: 0 auto;
        }

        .get-item-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 28px;
            display: grid;
            grid-template-columns: 240px 1fr;
            gap: 32px;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            transition: all 0.25s ease;
        }

        .get-item-card:hover {
            box-shadow: 0 14px 30px rgba(0,0,0,0.07);
            border-color: #CBD5E1;
            transform: translateY(-2px);
        }

        .get-visual-col {
            display: flex;
            align-items: center;
            justify-content: center;
            background: #F1F5F9;
            border-radius: 14px;
            padding: 16px;
            min-height: 190px;
        }

        .get-content-col h3 {
            font-size: 22px;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 8px;
        }

        .get-content-col p {
            color: var(--muted);
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 16px;
        }

        .get-value-tag {
            display: inline-block;
            background: #FEF3C7;
            color: #92400E;
            font-weight: 900;
            font-size: 15px;
            padding: 6px 16px;
            border-radius: 8px;
            border: 1px solid #FDE68A;
        }

        /* Value Total Stack */
        .value-total-box {
            background: #1E293B;
            color: #FFFFFF;
            border-radius: 24px;
            padding: 48px 32px;
            text-align: center;
            max-width: 900px;
            margin: 48px auto 0 auto;
            box-shadow: 0 20px 40px rgba(15, 23, 42, 0.25);
        }

        .value-total-label {
            font-size: 18px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: #94A3B8;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .value-total-amount {
            font-size: 48px;
            font-weight: 900;
            color: #FACC15;
            line-height: 1.1;
            margin-bottom: 20px;
        }

        .value-contrast {
            display: inline-flex;
            align-items: center;
            gap: 16px;
            background: rgba(255,255,255,0.08);
            padding: 12px 28px;
            border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.15);
        }

        .striked-price {
            text-decoration: line-through;
            font-size: 24px;
            color: #94A3B8;
            font-weight: 700;
        }

        .highlight-price {
            font-size: 32px;
            font-weight: 900;
            color: #38BDF8;
        }

        /* Section: Price Anchor */
        .anchor-section {
            background: #FFFFFF;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            text-align: center;
        }

        .anchor-card {
            max-width: 760px;
            margin: 0 auto;
            background: #F8FAFC;
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 40px 32px;
        }

        .anchor-card h3 {
            font-size: 28px;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 16px;
        }

        .anchor-card p {
            font-size: 18px;
            color: #475569;
            line-height: 1.7;
            margin-bottom: 24px;
        }

        .anchor-comparison {
            display: flex;
            justify-content: center;
            gap: 32px;
            border-top: 1px dashed #CBD5E1;
            padding-top: 24px;
        }

        .anchor-comp-item {
            text-align: center;
        }

        .anchor-comp-item span {
            display: block;
            font-size: 14px;
            color: var(--muted);
            font-weight: 700;
            margin-bottom: 4px;
        }

        .anchor-comp-item strong {
            font-size: 26px;
            font-weight: 900;
            color: var(--dark);
        }

        /* Section: Pricing Table (ONLY BUTTON HERE!) */
        .pricing-section {
            background: linear-gradient(180deg, #F8FAFC 0%, #EFF6FF 100%);
            padding: 90px 0;
        }

        .pricing-card {
            background: #FFFFFF;
            border: 3px solid var(--primary);
            border-radius: 28px;
            padding: 56px 40px;
            max-width: 680px;
            margin: 0 auto;
            box-shadow: 0 25px 60px rgba(37, 99, 235, 0.15);
            text-align: center;
            position: relative;
        }

        .pricing-popular-badge {
            position: absolute;
            top: -18px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--primary);
            color: #FFFFFF;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 8px 24px;
            border-radius: 9999px;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
        }

        .pricing-card h2 {
            font-size: 34px;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 10px;
        }

        .pricing-card .pricing-sub {
            font-size: 18px;
            color: var(--muted);
            margin-bottom: 28px;
            font-weight: 600;
        }

        .pricing-price-box {
            background: #F8FAFC;
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 32px;
            border: 1px solid var(--border);
        }

        .pricing-old-val {
            font-size: 18px;
            color: var(--muted);
            text-decoration: line-through;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .pricing-deal-price {
            font-size: 64px;
            font-weight: 900;
            color: var(--dark);
            line-height: 1;
            margin-bottom: 8px;
        }

        .pricing-deal-price span {
            font-size: 32px;
            vertical-align: top;
            margin-right: 2px;
            color: var(--primary);
        }

        .pricing-onetime {
            font-size: 15px;
            color: var(--success);
            font-weight: 800;
            background: #ECFDF5;
            display: inline-block;
            padding: 4px 14px;
            border-radius: 999px;
        }

        .pricing-features-list {
            list-style: none;
            text-align: left;
            margin-bottom: 40px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .pricing-features-list li {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 17px;
            font-weight: 700;
            color: #334155;
        }

        .pricing-features-list .check-icon {
            width: 24px;
            height: 24px;
            background: #DCFCE7;
            color: #16A34A;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            font-size: 14px;
            font-weight: 900;
        }

        /* THE SINGLE CTA BUTTON ON ENTIRE PAGE */
        .cta-button {
            display: block;
            width: 100%;
            background: linear-gradient(180deg, #EF4444 0%, #DC2626 100%);
            color: #FFFFFF;
            font-size: 22px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
            padding: 22px 32px;
            border-radius: 16px;
            text-decoration: none;
            box-shadow: 0 12px 28px rgba(239, 68, 68, 0.4);
            transition: all 0.2s ease;
            cursor: pointer;
            border: none;
        }

        .cta-button:hover {
            background: linear-gradient(180deg, #DC2626 0%, #B91C1C 100%);
            transform: translateY(-2px);
            box-shadow: 0 16px 36px rgba(239, 68, 68, 0.5);
            color: #FFFFFF;
        }

        .cta-button:active {
            transform: translateY(1px);
            box-shadow: 0 6px 18px rgba(239, 68, 68, 0.3);
        }

        .pricing-guarantee-note {
            margin-top: 18px;
            font-size: 14px;
            color: var(--muted);
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        /* Section: Objection Handling */
        .objection-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 24px;
        }

        .objection-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 28px;
        }

        .objection-card h3 {
            font-size: 19px;
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .objection-card p {
            color: var(--muted);
            font-size: 15px;
            line-height: 1.6;
        }

        /* Section: FAQ */
        .faq-section {
            background: #FFFFFF;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
        }

        .faq-accordion {
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .faq-item {
            border: 1px solid var(--border);
            border-radius: 14px;
            background: #F8FAFC;
            overflow: hidden;
            transition: border-color 0.2s;
        }

        .faq-item.active {
            border-color: var(--primary);
            background: #FFFFFF;
        }

        .faq-header {
            padding: 20px 24px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 800;
            font-size: 17px;
            color: var(--dark);
            user-select: none;
        }

        .faq-toggle-icon {
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: 700;
            color: var(--primary);
            transition: transform 0.2s ease;
        }

        .faq-item.active .faq-toggle-icon {
            transform: rotate(45deg);
            color: var(--accent-red);
        }

        .faq-content {
            display: none;
            padding: 0 24px 22px 24px;
            color: #475569;
            font-size: 16px;
            line-height: 1.65;
            border-top: 1px solid #F1F5F9;
            padding-top: 16px;
        }

        .faq-item.active .faq-content {
            display: block;
        }

        /* Section: Emotional Close */
        .closing-section {
            background: linear-gradient(180deg, #EFF6FF 0%, #DBEAFE 100%);
            text-align: center;
            padding: 80px 0;
        }

        .closing-box {
            max-width: 760px;
            margin: 0 auto;
        }

        .closing-box h2 {
            font-size: 32px;
            font-weight: 900;
            color: var(--dark);
            margin-bottom: 8px;
            line-height: 1.3;
        }

        .closing-box h3 {
            font-size: 24px;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 24px;
            line-height: 1.4;
        }

        .closing-box p {
            font-size: 18px;
            color: #334155;
            line-height: 1.7;
            margin-bottom: 16px;
        }

        /* Footer */
        footer {
            background: #0F172A;
            color: #94A3B8;
            padding: 40px 0;
            text-align: center;
            font-size: 15px;
        }

        footer .footer-brand {
            font-size: 22px;
            font-weight: 900;
            color: #FFFFFF;
            margin-bottom: 6px;
        }

        footer .footer-sub {
            color: #38BDF8;
            font-weight: 700;
            margin-bottom: 12px;
        }

        footer .footer-quote {
            font-style: italic;
            margin-bottom: 16px;
            color: #CBD5E1;
        }

        footer .copyright {
            font-size: 13px;
            color: #64748B;
        }

        /* Responsive */
        @media (max-width: 900px) {
            .hero h1 { font-size: 32px; }
            .hero p.subheadline { font-size: 18px; }
            .section-header h2 { font-size: 28px; }
            .trust-signals-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            .trust-signals-wrapper {
                padding: 24px 20px;
            }
            .get-item-card { grid-template-columns: 1fr; gap: 20px; }
            .get-visual-col { min-height: 200px; }
            .problem-grid, .categories-grid, .demo-grid, .benefits-grid, .objection-grid {
                grid-template-columns: 1fr;
            }
            .steps-grid, .how-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .hero-laptop-box { width: 100%; }
            .hero-phone-box { width: 38%; }
        }

        @media (max-width: 600px) {
            .hero h1 { font-size: 28px; }
            .hero p.subheadline { font-size: 16px; }
            .trust-signals-section {
                padding: 10px 0 30px 0;
            }
            .trust-signals-wrapper {
                padding: 18px 16px;
                border-radius: 16px;
            }
            .trust-signal-card {
                gap: 14px;
            }
            .trust-icon-box {
                width: 48px;
                height: 48px;
                border-radius: 12px;
            }
            .trust-signal-text h3 {
                font-size: 16px;
            }
            .hero-phone-box {
                position: relative;
                width: 65%;
                margin: -40px auto 0 auto;
            }
            .steps-grid, .how-grid {
                grid-template-columns: 1fr;
            }
            .pricing-card { padding: 40px 20px; }
            .cta-button { font-size: 18px; padding: 18px 20px; }
            .pricing-deal-price { font-size: 52px; }
            .value-total-amount { font-size: 38px; }
            .value-contrast { flex-direction: column; gap: 6px; }
            .anchor-comparison { flex-direction: column; gap: 16px; }
        }
    </style>
</head>
<body>
"""

print("Head and styles ready")
