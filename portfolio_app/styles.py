import streamlit as st

def render_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,650;9..144,760&family=Source+Sans+3:wght@400;520;650;760&display=swap');

        :root {
            --ink: #263238;
            --muted: #6f7d7b;
            --paper: #f5f8f6;
            --surface: rgba(255, 255, 255, 0.84);
            --line: rgba(65, 91, 84, 0.14);
            --teal: #78a99a;
            --teal-deep: #3f7769;
            --sage: #dcebe4;
            --button: #7faf9f;
            --button-hover: #6aa190;
            --chat-input-bottom: 0px;
            --chat-sidebar-offset: 0px;
            --chat-main-gutter-left: 36px;
            --chat-main-gutter-right: 42px;
            --chat-content-start: max(
                var(--chat-main-gutter-left),
                calc((100vw - var(--chat-sidebar-offset) - 1208px) / 2)
            );
            --chat-input-left: calc(var(--chat-sidebar-offset) + var(--chat-content-start));
            --chat-input-width: min(
                calc(100vw - var(--chat-sidebar-offset) - var(--chat-main-gutter-left) - var(--chat-main-gutter-right)),
                1208px
            );
            --chat-main-layer-width: calc(100vw - var(--chat-sidebar-offset));
            --chat-input-layer-height: 126px;
            --chat-layer: 2147483600;
            --chat-layer-backdrop: 2147483590;
            --sidebar-layer: 2147483647;
        }

        @media (min-width: 900px) {
            body:has(section[data-testid="stSidebar"][aria-expanded="true"]) {
                --chat-sidebar-offset: 336px;
            }
        }

        .stApp {
            background:
                linear-gradient(120deg, rgba(246, 249, 247, 0.98), rgba(225, 239, 232, 0.82)),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.035) 0, rgba(63, 119, 105, 0.035) 1px, transparent 1px, transparent 72px);
            color: var(--ink);
            font-family: "Source Sans 3", sans-serif;
        }

        .block-container {
            max-width: 1280px;
            width: min(100%, 1280px);
            padding-top: 100px;
            padding-left: 36px;
            padding-right: 36px;
            padding-bottom: 40px;
            position: relative;
            z-index: 1;
        }

        header[data-testid="stHeader"],
        div[data-testid="stToolbar"] {
            z-index: 2147483000 !important;
            pointer-events: auto !important;
        }

        div[data-testid="collapsedControl"],
        button[data-testid="collapsedControl"] {
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
            position: fixed !important;
            top: 18px !important;
            left: 18px !important;
            z-index: 2147483647 !important;
            pointer-events: auto !important;
        }

        div[data-testid="collapsedControl"] button {
            width: 42px !important;
            height: 42px !important;
            border-radius: 10px !important;
            background: rgba(255, 255, 255, 0.94) !important;
            border: 1px solid rgba(63, 119, 105, 0.18) !important;
            box-shadow: 0 10px 28px rgba(38, 50, 56, 0.14) !important;
            color: var(--teal-deep) !important;
        }

        div[data-testid="collapsedControl"] button:hover {
            background: #ffffff !important;
            border-color: rgba(63, 119, 105, 0.32) !important;
        }

        h1, h2, h3, .portfolio-title {
            font-family: "Fraunces", Georgia, serif;
            letter-spacing: 0;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #163f3a 0%, #0d2825 100%);
            border-right: none;
            padding: 20px 0 16px;
            z-index: var(--sidebar-layer) !important;
            pointer-events: auto !important;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-wrapper {
            padding: 0 16px;
            margin-bottom: 8px;
        }

        section[data-testid="stSidebar"] .sidebar-title-wrapper {
            padding: 0 16px;
            margin-bottom: 12px;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] {
            padding: 0;
            margin: 0;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] > label {
            padding: 0;
            margin: 0;
        }

        section[data-testid="stSidebar"] * {
            color: rgba(255, 255, 255, 0.92);
            font-family: "Times New Roman", "SimSun", serif;
        }

        section[data-testid="stSidebar"] .sidebar-avatar {
            display: block;
            width: 130px;
            height: 130px;
            border-radius: 50%;
            object-fit: cover;
            margin: 12px auto 16px;
            border: 4px solid rgba(255, 255, 255, 0.25);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
            image-rendering: -webkit-optimize-contrast;
            image-rendering: crisp-edges;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-shell {
            width: fit-content;
            margin: 12px auto 16px;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-toggle {
            position: absolute;
            opacity: 0;
            pointer-events: none;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-trigger {
            display: block;
            width: 130px;
            height: 130px;
            border-radius: 50%;
            cursor: zoom-in;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-trigger .sidebar-avatar {
            margin: 0;
            transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-trigger:hover .sidebar-avatar {
            transform: translateY(-2px) scale(1.02);
            border-color: rgba(255, 255, 255, 0.42);
            box-shadow: 0 16px 38px rgba(0, 0, 0, 0.48);
        }

        section[data-testid="stSidebar"] .sidebar-avatar-lightbox {
            position: fixed;
            inset: 0;
            display: none;
            background: rgba(6, 18, 17, 0.76);
            backdrop-filter: blur(8px);
            z-index: 2147483646;
            cursor: zoom-out;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-toggle:checked ~ .sidebar-avatar-lightbox {
            display: block;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-lightbox-inner {
            position: fixed;
            left: 50%;
            top: 50%;
            display: none;
            align-items: center;
            justify-content: center;
            width: min(72vw, 680px);
            height: min(82vh, 780px);
            padding: 18px;
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.96);
            box-shadow: 0 28px 80px rgba(0, 0, 0, 0.42);
            cursor: default;
            transform: translate(-50%, -50%);
            z-index: 2147483647;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-toggle:checked ~ .sidebar-avatar-lightbox-inner {
            display: flex;
        }

        section[data-testid="stSidebar"] .sidebar-avatar-full {
            display: block;
            max-width: 100%;
            max-height: 100%;
            border-radius: 14px;
            object-fit: contain;
        }

        section[data-testid="stSidebar"] .sidebar-profile {
            text-align: center;
            padding: 0 12px;
            margin-bottom: 8px;
        }

        section[data-testid="stSidebar"] .sidebar-name {
            font-family: "Times New Roman", "SimSun", serif;
            font-size: 28px;
            color: #ffffff;
            font-weight: 700;
            margin-bottom: 6px;
        }

        section[data-testid="stSidebar"] .sidebar-title {
            font-size: 15px;
            color: rgba(255, 255, 255, 0.60);
            margin-bottom: 14px;
            font-weight: 500;
        }

        section[data-testid="stSidebar"] .sidebar-contact {
            font-size: 15px;
            line-height: 2.0;
        }

        section[data-testid="stSidebar"] .contact-link {
            color: rgba(120, 169, 154, 0.95);
            text-decoration: none;
            transition: color 200ms ease;
        }

        section[data-testid="stSidebar"] .contact-link:hover {
            color: #ffffff;
            text-decoration: underline;
        }

        section[data-testid="stSidebar"] .contact-text {
            color: rgba(255, 255, 255, 0.55);
        }

        section[data-testid="stSidebar"] .sidebar-section-title {
            font-size: 12px;
            color: rgba(255, 255, 255, 0.50);
            font-weight: 650;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 8px;
            padding-left: 12px;
        }

        section[data-testid="stSidebar"] h1 {
            font-family: "Times New Roman", "SimSun", serif;
            font-size: 24px;
            color: #ffffff;
            margin-bottom: 6px;
            text-align: center;
            font-weight: 700;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label,
        section[data-testid="stSidebar"] [data-testid="stTextInput"] label,
        section[data-testid="stSidebar"] [data-testid="stSlider"] label {
            color: rgba(255, 255, 255, 0.65);
            font-weight: 600;
            font-size: 16px;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] {
            display: flex;
            flex-direction: column;
            gap: 0;
            padding: 0 12px;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            background: rgba(255, 255, 255, 0.06);
            border: none;
            border-radius: 8px;
            padding: 16px 18px;
            margin: 4px 0;
            transition: all 200ms ease;
            cursor: pointer;
            width: 100%;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            font-size: 17px;
            font-weight: 600;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: rgba(255, 255, 255, 0.12);
            transform: none;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
            background: rgba(33, 124, 111, 0.45);
            border-left: 3px solid rgba(33, 124, 111, 0.9);
        }

        section[data-testid="stSidebar"] .stButton button {
            background: rgba(33, 124, 111, 0.9);
            border: none;
            border-radius: 8px;
            color: white;
            font-weight: 650;
            padding: 10px 14px;
            transition: all 200ms ease;
            box-shadow: 0 7px 17px rgba(63, 119, 105, 0.16);
        }

        section[data-testid="stSidebar"] .stButton button:hover {
            background: rgba(33, 124, 111, 1);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(33, 124, 111, 0.40);
        }

        section[data-testid="stSidebar"] .stDivider {
            border-color: rgba(255, 255, 255, 0.10);
            margin: 16px 0;
        }

        section[data-testid="stSidebar"] .stSlider [role="slider"] {
            background-color: rgba(33, 124, 111, 0.6);
        }

        section[data-testid="stSidebar"] .stSlider [role="track"] {
            background-color: rgba(255, 255, 255, 0.15);
        }

        section[data-testid="stSidebar"] .key-status {
            font-size: 13px;
            line-height: 1.6;
            padding: 10px 12px;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 8px;
            text-align: center;
        }

        section[data-testid="stSidebar"] .small-note {
            font-size: 12px;
            color: rgba(255, 255, 255, 0.55) !important;
            line-height: 1.6;
        }

        section[data-testid="stSidebar"] .vector-status-card {
            margin: 12px 12px 14px;
            padding: 12px 13px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.10);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.06);
        }

        section[data-testid="stSidebar"] .vector-status-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 7px;
        }

        section[data-testid="stSidebar"] .vector-status-row strong {
            padding: 3px 8px;
            border-radius: 999px;
            font-size: 11px;
            line-height: 1.2;
            white-space: nowrap;
        }

        section[data-testid="stSidebar"] .status-ready {
            color: #dff8ef !important;
            background: rgba(47, 168, 126, 0.28);
            border: 1px solid rgba(139, 221, 190, 0.25);
        }

        section[data-testid="stSidebar"] .status-missing {
            color: #ffe7c2 !important;
            background: rgba(222, 145, 45, 0.28);
            border: 1px solid rgba(255, 204, 128, 0.25);
        }

        section[data-testid="stSidebar"] .vector-status-meta,
        section[data-testid="stSidebar"] .control-hint {
            color: rgba(255, 255, 255, 0.58) !important;
            font-size: 12px;
            line-height: 1.55;
        }

        section[data-testid="stSidebar"] .control-hint {
            margin: -4px 12px 12px;
            padding: 8px 10px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.045);
        }

        section[data-testid="stSidebar"] code {
            background: rgba(255, 255, 255, 0.10);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 11px;
        }

        .hero-shell {
            position: relative;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: clamp(28px, 3.2vw, 52px) clamp(32px, 4vw, 72px);
            background:
                linear-gradient(105deg, rgba(255,255,255,0.92) 0%, rgba(255,255,255,0.72) 48%, rgba(22,117,111,0.13) 100%),
                linear-gradient(180deg, rgba(196,138,44,0.08), rgba(255,255,255,0));
            box-shadow: 0 18px 48px rgba(20, 33, 61, 0.10);
            margin-bottom: 18px;
            min-height: 260px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .hero-kicker {
            color: var(--teal-deep);
            font-size: 13px;
            font-weight: 760;
            text-transform: uppercase;
            letter-spacing: .08em;
            margin-bottom: 8px;
        }

        .hero-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(36px, 4.4vw, 62px);
            font-weight: 760;
            line-height: 1.02;
            color: var(--ink);
            max-width: 980px;
            margin-bottom: 12px;
        }

        .hero-subtitle {
            color: var(--muted);
            font-size: 18px;
            line-height: 1.58;
            max-width: 1050px;
        }

        .portfolio-card {
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: clamp(18px, 2.2vw, 30px);
            background: var(--surface);
            box-shadow: 0 10px 26px rgba(20, 33, 61, 0.07);
            margin-bottom: 16px;
        }

        .portfolio-title {
            font-size: 22px;
            font-weight: 650;
            color: var(--ink);
            margin-bottom: 12px;
        }

        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: 14px;
        }

        .profile-hero {
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(33, 124, 111, 0.12);
            border-radius: 18px;
            padding: 34px;
            margin-bottom: 18px;
            box-shadow: 0 16px 42px rgba(33, 124, 111, 0.09);
        }

        .profile-hero-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 30px;
            width: 100%;
        }

        .profile-avatar {
            width: 96px;
            height: 96px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid rgba(33, 124, 111, 0.12);
            box-shadow: 0 8px 22px rgba(33, 124, 111, 0.16);
            flex: 0 0 auto;
        }

        .profile-hero-text {
            min-width: 0;
            display: block;
        }

        .profile-text-main {
            min-width: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding-top: 2px;
        }

        .profile-kicker,
        .profile-title,
        .profile-subtitle {
            grid-column: auto;
        }

        .profile-kicker {
            color: #217c6f;
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 8px;
        }

        .profile-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(38px, 3vw, 52px);
            font-weight: 700;
            color: #1f2e2b;
            margin-bottom: 8px;
            line-height: 1.05;
        }

        .profile-subtitle {
            font-size: clamp(16px, 1.2vw, 20px);
            color: #667873;
            margin-bottom: 0;
        }

        .profile-stats {
            display: grid;
            grid-template-columns: repeat(3, minmax(138px, 1fr));
            gap: 12px;
            align-items: stretch;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
            min-width: 0;
        }

        .profile-stat {
            position: relative;
            min-height: 76px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            text-align: left;
            color: #3a4f4b;
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.96), rgba(248, 253, 250, 0.94));
            border: 1px solid rgba(33, 124, 111, 0.15);
            border-radius: 12px;
            padding: 14px 18px;
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.06);
            transition: all 200ms ease;
            box-sizing: border-box;
            min-width: 0;
            overflow: hidden;
        }

        .profile-stat:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 24px rgba(33, 124, 111, 0.12);
            border-color: rgba(33, 124, 111, 0.25);
        }

        .stat-icon {
            font-size: 24px;
            margin-right: 12px;
            flex-shrink: 0;
            transition: transform 200ms ease;
        }

        .profile-stat:hover .stat-icon {
            transform: scale(1.1);
        }

        .stat-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            min-width: 0;
            overflow: hidden;
        }

        .profile-stat strong {
            display: block;
            color: #1a2f2c;
            font-family: "Times New Roman", Times, serif;
            font-size: clamp(19px, 1.55vw, 23px);
            line-height: 1.3;
            margin-bottom: 3px;
            letter-spacing: 0;
            overflow-wrap: normal;
            white-space: nowrap;
            font-weight: 700;
        }

        .profile-stat-label {
            display: block;
            padding: 0;
            font-size: 10px;
            color: #6a7f7a;
            line-height: 1.2;
            font-weight: 600;
            white-space: nowrap;
            text-transform: uppercase;
            letter-spacing: 0.015em;
            max-width: 100%;
            overflow: visible;
            text-overflow: clip;
        }

        .achievement-section {
            margin: 18px 0 34px;
            padding: 22px 24px 30px;
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(33, 124, 111, 0.11);
            border-radius: 16px;
            box-shadow: 0 10px 26px rgba(33, 124, 111, 0.08);
        }

        .achievement-title {
            font-family: "Times New Roman", Times, serif;
            font-size: 26px;
            font-weight: 700;
            color: #1f2e2b;
            margin-bottom: 18px;
            text-align: center;
        }

        .achievement-medals {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 20px;
        }

        .achievement-medal {
            position: relative;
            min-height: 196px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            text-align: center;
            padding: 0 10px;
            transition: transform 220ms ease;
        }

        .achievement-medal:hover {
            transform: translateY(-8px) scale(1.045);
        }

        .medal-wrap {
            position: relative;
            width: 112px;
            height: 132px;
            margin-bottom: 4px;
            display: grid;
            justify-items: center;
            transition: transform 220ms ease;
        }

        .achievement-medal:hover .medal-wrap {
            transform: rotate(-3deg);
        }

        .medal-ribbons {
            position: absolute;
            top: 78px;
            left: 50%;
            width: 70px;
            height: 56px;
            transform: translateX(-50%);
            z-index: 0;
        }

        .medal-ribbons::before,
        .medal-ribbons::after {
            content: "";
            position: absolute;
            top: 0;
            width: 30px;
            height: 56px;
            background: linear-gradient(180deg, #d8232a 0%, #a70f16 100%);
            box-shadow: inset 8px 0 0 rgba(255,255,255,0.18);
        }

        .medal-ribbons::before {
            left: 8px;
            transform: skewX(-13deg);
            clip-path: polygon(0 0, 100% 0, 82% 100%, 48% 76%, 14% 100%);
        }

        .medal-ribbons::after {
            right: 8px;
            transform: skewX(13deg);
            clip-path: polygon(0 0, 100% 0, 86% 100%, 52% 76%, 18% 100%);
            background: linear-gradient(180deg, #f0c445 0%, #c89415 100%);
        }

        .medal-face {
            position: relative;
            z-index: 2;
            width: 102px;
            height: 102px;
            border-radius: 50%;
            display: grid;
            place-items: center;
            color: #d71920;
            font-family: "Times New Roman", Times, serif;
            font-size: clamp(34px, 3vw, 48px);
            font-weight: 700;
            line-height: 1;
            background:
                radial-gradient(circle at 34% 24%, rgba(255,255,255,0.95) 0 12%, rgba(255,245,190,0.95) 13% 28%, transparent 29%),
                radial-gradient(circle at 50% 54%, #fff1a7 0 43%, #f1ca57 44% 60%, #c78a1d 78%, #8d5d0b 100%);
            border: 2px solid #fff1a0;
            box-shadow:
                inset 0 0 0 6px rgba(255,255,255,0.32),
                inset 0 0 0 10px rgba(157,96,8,0.18),
                inset 0 -12px 18px rgba(110,70,9,0.18),
                0 16px 30px rgba(112,80,15,0.30);
        }

        .medal-face::before {
            content: "";
            position: absolute;
            inset: 11px;
            border-radius: 50%;
            border: 2px solid rgba(150, 93, 16, 0.45);
        }

        .medal-face::after {
            content: "";
            position: absolute;
            inset: 19px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.70);
        }

        .achievement-label {
            position: relative;
            z-index: 2;
            display: block;
            max-width: 190px;
            padding: 0 8px;
            font-size: 12px;
            color: #374d49;
            line-height: 1.22;
            font-weight: 700;
            overflow-wrap: anywhere;
        }

        .profile-stat-divider {
            display: none;
        }

        .profile-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 16px;
            margin-bottom: 18px;
            align-items: stretch;
        }

        .profile-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 8px 24px rgba(33, 124, 111, 0.07);
            border: 1px solid rgba(33, 124, 111, 0.10);
            min-width: 0;
        }

        .profile-card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(0, 0, 0, 0.06);
        }

        .profile-card-icon {
            font-size: 12px;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.08);
            border-radius: 999px;
            padding: 4px 9px;
            font-weight: 700;
        }

        .profile-card-title {
            font-family: "Times New Roman", Times, serif;
            font-size: 23px;
            font-weight: 700;
            color: #1a2f2c;
        }

        .profile-info-grid {
            display: flex;
            flex-direction: column;
            gap: 0;
        }

        .info-item {
            display: grid;
            grid-template-columns: 260px 1fr;
            align-items: center;
            gap: 18px;
            padding: 18px 8px;
            background: transparent;
            border-radius: 0;
            border-left: none;
            border-bottom: 1px solid rgba(33, 124, 111, 0.13);
            min-width: 0;
            transition: background 180ms ease, transform 180ms ease, padding-left 180ms ease;
        }

        .info-item:hover {
            background: rgba(33, 124, 111, 0.045);
            transform: translateX(4px);
            padding-left: 14px;
        }

        .info-item:last-child {
            border-bottom: none;
        }

        .info-key {
            font-family: "Times New Roman", Times, serif;
            font-size: 17px;
            color: #3c6760;
            margin-bottom: 0;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .03em;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-value {
            font-family: "Times New Roman", Times, serif;
            font-size: 19px;
            color: var(--ink);
            font-weight: 500;
            line-height: 1.5;
            overflow-wrap: anywhere;
            word-break: normal;
        }

        .info-emoji {
            font-size: 22px;
            line-height: 1;
            display: inline-block;
            transition: transform 180ms ease;
        }

        .info-item:hover .info-emoji {
            transform: scale(1.18) rotate(-4deg);
        }

        .school-value {
            display: flex;
            align-items: center;
            gap: 9px;
        }

        .school-icon {
            width: 26px;
            height: 26px;
            object-fit: contain;
            flex: 0 0 auto;
            border-radius: 5px;
        }

        .courses-list {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
        }

        .course-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 16px 20px;
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.96), rgba(245, 252, 249, 0.94));
            border-radius: 12px;
            border: 1px solid rgba(33, 124, 111, 0.12);
            box-shadow: 0 4px 14px rgba(33, 124, 111, 0.05);
            transition: all 200ms ease;
            min-width: 0;
        }

        .course-item:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(33, 124, 111, 0.12);
            border-color: rgba(33, 124, 111, 0.25);
        }

        .course-icon {
            font-size: 24px;
            flex: 0 0 auto;
            transition: transform 200ms ease;
        }

        .course-item:hover .course-icon {
            transform: scale(1.15) rotate(-5deg);
        }

        .course-content {
            flex: 1;
            min-width: 0;
        }

        .course-name {
            font-family: "Times New Roman", Times, serif;
            font-size: 16px;
            color: #1f2e2b;
            font-weight: 600;
            line-height: 1.4;
            min-width: 0;
            overflow-wrap: anywhere;
        }

        .course-score-badge {
            flex: 0 0 auto;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 16px;
            font-weight: 700;
            font-family: "Times New Roman", Times, serif;
            min-width: 48px;
            text-align: center;
        }

        .research-section {
            margin-top: 18px;
        }

        .research-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 16px;
            margin-top: 20px;
        }

        .research-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
            border: 1px solid rgba(33, 124, 111, 0.1);
            transition: all 200ms ease;
        }

        .research-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 28px rgba(33, 124, 111, 0.12);
        }

        .research-title {
            font-size: 17px;
            font-weight: 700;
            color: #1a2f2c;
            margin-bottom: 9px;
        }

        .research-desc {
            font-size: 14px;
            color: #5a6f6a;
            line-height: 1.6;
            margin-bottom: 12px;
        }

        .research-projects {
            font-size: 12px;
            color: #217c6f;
            font-weight: 600;
            padding-top: 12px;
            border-top: 1px solid rgba(0, 0, 0, 0.06);
        }

        .internship-section {
            margin: 32px 0 8px;
            padding: 0;
            background: transparent;
        }

        .internship-timeline {
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 0;
            margin-top: 28px;
            padding-left: 36px;
            padding-bottom: 10px;
            z-index: 1;
        }

        .internship-timeline::before {
            content: "";
            position: absolute;
            left: 10px;
            top: 0;
            bottom: 10px;
            width: 3px;
            background: linear-gradient(180deg, rgba(33, 124, 111, 0.08), rgba(33, 124, 111, 0.35) 30%, rgba(33, 124, 111, 0.35) 70%, rgba(33, 124, 111, 0.08));
            border-radius: 999px;
            z-index: 0;
        }

        .internship-card {
            position: relative;
            display: flex;
            gap: 20px;
            border-radius: 20px;
            border: 1px solid rgba(33, 124, 111, 0.12);
            background:
                linear-gradient(145deg, rgba(255, 255, 255, 0.98), rgba(248, 253, 250, 0.96)),
                radial-gradient(circle at 92% 8%, rgba(33, 124, 111, 0.06), transparent 30%);
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 8px 28px rgba(33, 124, 111, 0.06);
            transition: all 280ms cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 1;
        }

        .internship-card:last-child {
            margin-bottom: 0;
        }

        .internship-card::before {
            content: "";
            position: absolute;
            left: -30px;
            top: 32px;
            width: 14px;
            height: 14px;
            background: white;
            border: 3px solid #217c6f;
            border-radius: 50%;
            box-shadow: 0 4px 12px rgba(33, 124, 111, 0.3);
            z-index: 2;
            transition: all 280ms ease;
        }

        .internship-card:hover {
            transform: translateY(-6px) translateX(4px);
            border-color: rgba(33, 124, 111, 0.3);
            box-shadow: 0 18px 42px rgba(33, 124, 111, 0.14);
        }

        .internship-card:hover::before {
            transform: scale(1.3);
            box-shadow: 0 0 0 6px rgba(33, 124, 111, 0.15), 0 6px 16px rgba(33, 124, 111, 0.35);
        }

        .internship-icon-wrapper {
            flex-shrink: 0;
            width: 72px;
            height: 72px;
            display: flex;
            align-items: center;
            justify-content: center;
            background:
                linear-gradient(145deg, rgba(33, 124, 111, 0.08), rgba(33, 124, 111, 0.03)),
                radial-gradient(circle at 30% 30%, rgba(33, 124, 111, 0.15), transparent 50%);
            border-radius: 18px;
            border: 1px solid rgba(33, 124, 111, 0.12);
            transition: all 280ms ease;
        }

        .internship-card:hover .internship-icon-wrapper {
            transform: scale(1.1) rotate(-5deg);
            background:
                linear-gradient(145deg, rgba(33, 124, 111, 0.12), rgba(33, 124, 111, 0.06)),
                radial-gradient(circle at 30% 30%, rgba(33, 124, 111, 0.22), transparent 50%);
        }

        .internship-icon-emoji {
            font-size: 36px;
            line-height: 1;
            transition: transform 280ms ease;
        }

        .internship-icon-img {
            width: 48px;
            height: 48px;
            object-fit: contain;
            transition: transform 280ms ease;
        }

        .internship-card:hover .internship-icon-emoji,
        .internship-card:hover .internship-icon-img {
            transform: scale(1.15);
        }

        .internship-content {
            flex: 1;
            min-width: 0;
        }

        .internship-head {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 16px;
            align-items: start;
            padding-bottom: 16px;
            border-bottom: 2px solid rgba(33, 124, 111, 0.1);
            margin-bottom: 16px;
        }

        .internship-org-row {
            display: flex;
            align-items: flex-start;
            gap: 8px;
        }

        .internship-org {
            font-family: "Fraunces", Georgia, serif;
            color: #1a2f2c;
            font-size: 22px;
            font-weight: 760;
            line-height: 1.3;
        }

        .internship-org-accent {
            color: #217c6f;
            font-size: 20px;
        }

        .internship-role {
            color: #3a6b5f;
            font-size: 15px;
            font-weight: 650;
            margin-top: 6px;
            letter-spacing: .03em;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .internship-role::before {
            content: "•";
            color: #217c6f;
            font-size: 12px;
        }

        .internship-period {
            color: #ffffff;
            background: linear-gradient(135deg, #217c6f, #1a5c52);
            border-radius: 999px;
            padding: 8px 16px;
            font-family: "Times New Roman", Times, serif;
            font-size: 14px;
            font-weight: 650;
            white-space: nowrap;
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.3);
            transition: all 200ms ease;
        }

        .internship-card:hover .internship-period {
            transform: scale(1.05);
            box-shadow: 0 8px 22px rgba(33, 124, 111, 0.4);
        }

        .internship-columns {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }

        .internship-column {
            background: rgba(33, 124, 111, 0.02);
            border-radius: 14px;
            padding: 18px;
            border: 1px solid rgba(33, 124, 111, 0.06);
        }

        .internship-subtitle {
            color: #217c6f;
            font-size: 14px;
            font-weight: 760;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .internship-subtitle::after {
            content: "";
            flex: 1;
            height: 2px;
            background: linear-gradient(90deg, rgba(33, 124, 111, 0.3), transparent);
            max-width: 60px;
        }

        .internship-list {
            margin: 0;
            padding-left: 0;
            color: #4a5f5a;
            font-size: 14px;
            line-height: 1.7;
        }

        .internship-list li {
            position: relative;
            padding-left: 20px;
            margin-bottom: 10px;
            list-style: none;
        }

        .internship-list li:last-child {
            margin-bottom: 0;
        }

        .internship-list li::before {
            content: "▸";
            position: absolute;
            left: 0;
            top: 4px;
            color: #217c6f;
            font-size: 14px;
            font-weight: 700;
            line-height: 1;
            transition: transform 200ms ease;
        }

        .internship-card:hover .internship-list li::before {
            transform: translateX(4px);
        }

        .metric-strip {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 14px;
            margin: 14px 0 18px;
        }

        .metric {
            background: #14213d;
            background: linear-gradient(135deg, #eef6f2, #ffffff);
            color: var(--ink);
            border-radius: 8px;
            padding: 14px 16px;
            border: 1px solid rgba(63,119,105,0.14);
            box-shadow: 0 8px 20px rgba(63, 119, 105, 0.08);
        }

        .metric-number {
            font-family: "Fraunces", Georgia, serif;
            font-size: 28px;
            font-weight: 760;
            line-height: 1;
        }

        .metric-label {
            font-size: 13px;
            color: var(--muted);
            margin-top: 5px;
        }

        .workspace-status {
            border: 1px solid rgba(22, 117, 111, 0.22);
            background: rgba(22, 117, 111, 0.08);
            border-radius: 8px;
            padding: 12px 14px;
            color: var(--ink);
            margin: 8px 0 16px;
            font-weight: 650;
        }

        div[data-testid="stChatMessage"] {
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(33, 124, 111, 0.15);
            border-radius: 20px;
            padding: 16px 20px;
            box-shadow: 0 8px 24px rgba(33, 124, 111, 0.08);
            margin-bottom: 14px;
            position: relative;
        }

        div[data-testid="stChatMessage"]:last-of-type {
            margin-bottom: 120px;
        }

        div[data-testid="stChatMessage"].st-emotion-cache-1c7y2kd {
            border-radius: 20px 20px 6px 20px;
            background:
                linear-gradient(135deg, rgba(33, 124, 111, 0.06), rgba(255,255,255,0.95)),
                radial-gradient(circle at 8% 12%, rgba(33,124,111,0.10), transparent 30%);
            border-color: rgba(33, 124, 111, 0.20);
        }

        div[data-testid="stChatMessage"].st-emotion-cache-1c7y2kd::before {
            content: "";
            position: absolute;
            left: 16px;
            top: -6px;
            width: 12px;
            height: 12px;
            background: rgba(33, 124, 111, 0.06);
            border-left: 1px solid rgba(33, 124, 111, 0.20);
            border-top: 1px solid rgba(33, 124, 111, 0.20);
            transform: rotate(45deg);
        }

        .chat-panel {
            position: relative;
            margin: 0 0 28px;
            padding: 26px 28px;
            border-radius: 18px;
            border: 1px solid rgba(33, 124, 111, 0.16);
            background:
                linear-gradient(135deg, rgba(255,255,255,0.98), rgba(240,248,244,0.94)),
                radial-gradient(circle at 100% 0%, rgba(33,124,111,0.12), transparent 34%);
            box-shadow: 
                0 22px 54px rgba(33, 124, 111, 0.10),
                0 2px 8px rgba(33, 124, 111, 0.06);
            overflow: hidden;
        }

        .chat-panel::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 8px;
            background: linear-gradient(180deg, #217c6f, #5a9f8f, #9cc8b8);
            border-radius: 999px 0 0 999px;
        }

        .chat-panel::after {
            content: "🤖";
            position: absolute;
            right: 32px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 56px;
            opacity: 0.08;
            pointer-events: none;
        }

        .chat-panel::before {
            left: 0;
            top: 0;
            right: 0;
            bottom: auto;
            width: auto;
            height: 4px;
            background: rgba(33, 124, 111, 0.72);
            border-radius: 0;
        }

        .chat-panel::after {
            content: "";
            right: -36px;
            top: -48px;
            width: 160px;
            height: 160px;
            transform: none;
            border-radius: 50%;
            border: 34px solid rgba(33, 124, 111, 0.06);
            font-size: 0;
            opacity: 1;
        }

        .chat-panel-inner {
            position: relative;
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            align-items: center;
            gap: 24px;
            z-index: 1;
        }

        .chat-panel-kicker {
            color: #217c6f;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: .14em;
            text-transform: uppercase;
            margin-bottom: 9px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .chat-panel-kicker::before {
            content: "";
            width: 20px;
            height: 3px;
            background: linear-gradient(90deg, #217c6f, rgba(33,124,111,0.5));
            border-radius: 999px;
        }

        .chat-panel-title {
            font-family: "Fraunces", Georgia, serif;
            color: #1a2f2c;
            font-size: clamp(28px, 2.5vw, 40px);
            font-weight: 760;
            line-height: 1.1;
            margin-bottom: 10px;
            max-width: 760px;
        }

        .chat-panel-copy {
            color: #58706a;
            font-size: 16px;
            line-height: 1.6;
            max-width: 780px;
            margin-bottom: 0;
        }

        .chat-scope-pill {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 0;
            min-width: 214px;
            padding: 14px 18px;
            border-radius: 12px;
            color: #1f4a42;
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid rgba(33, 124, 111, 0.15);
            font-size: 13px;
            font-weight: 700;
            box-shadow: 0 12px 28px rgba(33, 124, 111, 0.08);
            transition: all 200ms ease;
        }

        .chat-scope-pill:hover {
            background: rgba(33, 124, 111, 0.12);
            border-color: rgba(33, 124, 111, 0.25);
            transform: translateY(-1px);
        }

        .portfolio-answer-links {
            margin-top: 16px;
        }

        .portfolio-answer-links p {
            margin: 0 0 8px;
            font-weight: 650;
            color: #243b37;
        }

        .portfolio-answer-links ul {
            margin: 0;
            padding-left: 22px;
        }

        .portfolio-answer-links li {
            margin: 5px 0;
        }

        .portfolio-answer-links a {
            color: #006edb;
            text-decoration: underline;
            text-underline-offset: 3px;
        }

        .web-answer-sources {
            margin-top: 14px;
            padding-top: 12px;
            border-top: 1px solid rgba(36, 59, 55, 0.12);
        }

        .web-answer-sources p {
            margin: 0 0 8px;
            font-weight: 650;
            color: #37423f;
        }

        .web-answer-sources ul {
            margin: 0;
            padding-left: 22px;
        }

        .web-answer-sources li {
            margin: 5px 0;
        }

        .web-answer-sources a {
            color: #6b4e00;
            text-decoration: underline;
            text-underline-offset: 3px;
        }

        .thinking-card {
            display: flex;
            align-items: center;
            gap: 12px;
            width: fit-content;
            max-width: 100%;
            padding: 15px 18px;
            border-radius: 16px;
            color: #234f47;
            background:
                linear-gradient(135deg, rgba(232, 246, 239, 0.98), rgba(255, 255, 255, 0.96)),
                radial-gradient(circle at 8% 50%, rgba(63,119,105,0.12), transparent 26%);
            border: 1px solid rgba(63, 119, 105, 0.20);
            box-shadow: 0 12px 30px rgba(63, 119, 105, 0.13);
            font-size: 14px;
            font-weight: 700;
            position: relative;
        }

        .thinking-card::before {
            content: "";
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: #3f7769;
            box-shadow: 0 0 0 0 rgba(63,119,105,0.35);
            animation: thinkingBeacon 1.2s infinite ease-out;
        }

        .thinking-dots {
            display: inline-flex;
            gap: 4px;
            align-items: center;
        }

        .thinking-dots span {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #3f7769;
            animation: thinkingPulse 1.1s infinite ease-in-out;
        }

        .thinking-dots span:nth-child(2) {
            animation-delay: 0.16s;
        }

        .thinking-dots span:nth-child(3) {
            animation-delay: 0.32s;
        }

        @keyframes thinkingPulse {
            0%, 80%, 100% {
                transform: translateY(0);
                opacity: 0.42;
            }
            40% {
                transform: translateY(-5px);
                opacity: 1;
            }
        }

        @keyframes thinkingBeacon {
            0% {
                box-shadow: 0 0 0 0 rgba(63,119,105,0.35);
            }
            70% {
                box-shadow: 0 0 0 9px rgba(63,119,105,0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(63,119,105,0);
            }
        }

        /* ======================================================
           CHAT INPUT — FIXED TO TOP
           ====================================================== */
        div[data-testid="stChatInput"],
        .stChatInput {
            position: fixed !important;
            top: auto !important;
            bottom: var(--chat-input-bottom) !important;
            left: calc(
                var(--chat-sidebar-offset) + max(
                    var(--chat-main-gutter-left),
                    calc((100vw - var(--chat-sidebar-offset) - 1208px) / 2)
                )
            ) !important;
            right: auto !important;
            transform: none !important;
            width: min(
                calc(100vw - var(--chat-sidebar-offset) - var(--chat-main-gutter-left) - var(--chat-main-gutter-right)),
                1208px
            ) !important;
            max-width: 1208px !important;
            box-sizing: border-box !important;
            background: rgba(255, 255, 255, 0.96) !important;
            border: 1px solid rgba(33, 124, 111, 0.26) !important;
            border-radius: 18px !important;
            padding: 12px 16px !important;
            margin: 0 !important;
            box-shadow: 0 14px 38px rgba(33, 124, 111, 0.20) !important;
            z-index: var(--chat-layer) !important;
            overflow: visible !important;
            clip-path: none !important;
            isolation: isolate !important;
            pointer-events: auto !important;
        }

        .stChatInput {
            z-index: var(--chat-layer) !important;
        }

        div[data-testid="stBottomBlockContainer"],
        div[data-testid="stBottom"],
        .stBottomBlockContainer {
            position: fixed !important;
            inset: auto 0 0 0 !important;
            left: var(--chat-sidebar-offset) !important;
            right: 0 !important;
            width: calc(100vw - var(--chat-sidebar-offset)) !important;
            height: var(--chat-input-layer-height) !important;
            min-height: var(--chat-input-layer-height) !important;
            max-height: none !important;
            background: transparent !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
            transform: none !important;
            z-index: var(--chat-layer-backdrop) !important;
            isolation: isolate !important;
            pointer-events: auto !important;
            overflow: visible !important;
            clip-path: none !important;
            contain: none !important;
        }

        div[data-testid="stBottomBlockContainer"]::before,
        .stBottomBlockContainer::before {
            content: "";
            position: fixed;
            left: var(--chat-sidebar-offset);
            right: 0;
            bottom: 0;
            height: var(--chat-input-layer-height);
            background: linear-gradient(180deg, rgba(246, 249, 247, 0), rgba(246, 249, 247, 0.94) 58%, rgba(246, 249, 247, 0.98));
            pointer-events: none;
            z-index: calc(var(--chat-layer-backdrop) - 1);
        }

        div[data-testid="stChatInput"] [data-testid="stChatInputContainer"] {
            position: static !important;
            width: 100% !important;
            background: transparent !important;
            box-shadow: none !important;
            padding: 0 !important;
        }

        div[data-testid="stBottomBlockContainer"] div[data-testid="stChatInput"] {
            pointer-events: auto !important;
            z-index: var(--chat-layer) !important;
        }

        div[data-testid="stBottom"] > div,
        div[data-testid="stBottomBlockContainer"] [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stBottomBlockContainer"] [data-testid="stVerticalBlock"],
        div[data-testid="stBottomBlockContainer"] [data-testid="element-container"] {
            position: relative !important;
            inset: auto !important;
            width: calc(100vw - var(--chat-sidebar-offset)) !important;
            height: 0 !important;
            margin: 0 !important;
            overflow: visible !important;
            z-index: var(--chat-layer) !important;
            pointer-events: none !important;
            transform: none !important;
            contain: none !important;
        }

        div[data-testid="stChatInput"] > div {
            max-width: 100%;
            margin: 0 auto;
            padding: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
            position: relative !important;
            z-index: 2147483647 !important;
        }

        div[data-testid="stChatInput"] form {
            min-height: 64px !important;
            border-radius: 16px !important;
            padding: 6px 8px 6px 16px !important;
            background: #ffffff !important;
            border: 1px solid rgba(33, 124, 111, 0.18) !important;
            box-shadow:
                0 10px 24px rgba(33, 124, 111, 0.08),
                inset 0 1px 0 rgba(255,255,255,0.95) !important;
            display: flex !important;
            align-items: center !important;
            gap: 10px !important;
            position: relative !important;
            z-index: 2147483647 !important;
            outline: none !important;
        }

        div[data-testid="stChatInput"] form::before {
            content: "";
            width: 4px;
            height: 34px;
            flex: 0 0 auto;
            border-radius: 999px;
            background: linear-gradient(180deg, #217c6f, #9bc8b6);
        }

        .stChatInput textarea {
            min-height: 50px !important;
            height: 50px !important;
            border-radius: 14px !important;
            border: none !important;
            background: transparent !important;
            color: #1f2e2b !important;
            font-size: 17px !important;
            font-weight: 560 !important;
            box-shadow: none !important;
            padding-top: 14px !important;
            line-height: 1.35 !important;
            transition: none !important;
        }

        div[data-testid="stChatInput"] [data-baseweb="textarea"],
        div[data-testid="stChatInput"] [data-baseweb="base-input"],
        div[data-testid="stChatInput"] textarea,
        div[data-testid="stChatInput"] textarea:focus,
        div[data-testid="stChatInput"] textarea:focus-visible,
        div[data-testid="stChatInput"] textarea:active {
            border-color: rgba(16, 82, 73, 0.72) !important;
            outline: none !important;
            box-shadow: none !important;
        }

        div[data-testid="stChatInput"] [data-baseweb="textarea"]:focus-within,
        div[data-testid="stChatInput"] [data-baseweb="base-input"]:focus-within,
        div[data-testid="stChatInput"] [data-baseweb="textarea"]:hover,
        div[data-testid="stChatInput"] [data-baseweb="base-input"]:hover {
            border-color: rgba(16, 82, 73, 0.82) !important;
            outline: none !important;
            box-shadow: 0 0 0 1px rgba(16, 82, 73, 0.72) !important;
        }

        div[data-testid="stChatInput"] form:focus-within {
            border-color: rgba(16, 82, 73, 0.72) !important;
            box-shadow: 0 14px 34px rgba(16, 82, 73, 0.18) !important;
        }

        div[data-testid="stChatInput"]:hover form {
            transform: translateY(2px);
            box-shadow: 0 20px 46px rgba(63, 119, 105, 0.30) !important;
        }

        .stChatInput button {
            width: 52px !important;
            height: 52px !important;
            min-width: 52px !important;
            min-height: 52px !important;
            border-radius: 14px !important;
            background:
                linear-gradient(135deg, #1f7468, #74b19d),
                radial-gradient(circle at 30% 25%, rgba(255,255,255,0.55), transparent 26%) !important;
            color: #ffffff !important;
            box-shadow:
                0 12px 24px rgba(33, 124, 111, 0.30),
                inset 0 1px 0 rgba(255,255,255,0.32) !important;
            transition: transform 160ms ease, box-shadow 160ms ease !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            padding: 0 !important;
            margin: 0 !important;
            align-self: center !important;
            font-size: 24px !important;
        }

        .stChatInput button:hover {
            transform: translateY(2px);
            box-shadow:
                0 16px 30px rgba(33, 124, 111, 0.34),
                0 0 0 5px rgba(33,124,111,0.10) !important;
        }

        .stButton button {
            border-radius: 7px;
            border: 1px solid rgba(63, 119, 105, 0.20);
            background: linear-gradient(135deg, var(--button), #b8d7cd);
            color: #18332d;
            font-weight: 760;
            box-shadow: 0 8px 18px rgba(63, 119, 105, 0.16);
            transition: transform 150ms ease, box-shadow 150ms ease, background 150ms ease;
        }

        .stButton button:hover {
            transform: translateY(-3px) scale(1.015);
            border-color: rgba(63, 119, 105, 0.34);
            background: linear-gradient(135deg, var(--button-hover), #c8e2d9);
            color: #10231f;
            box-shadow: 0 14px 26px rgba(63, 119, 105, 0.24);
        }

        .stButton button:active {
            transform: translateY(-1px) scale(0.995);
            box-shadow: 0 7px 16px rgba(63, 119, 105, 0.16);
        }

        .small-note {
            color: #61716e;
            font-size: 13px;
            line-height: 1.6;
        }

        .small-note code {
            color: var(--teal-deep);
            background: rgba(63,119,105,0.08);
            border-radius: 4px;
            padding: 1px 4px;
        }

        .key-status {
            border: 1px solid rgba(63,119,105,0.16);
            background: rgba(255,255,255,0.58);
            border-radius: 7px;
            padding: 10px 12px;
            margin: 10px 0 14px;
            color: #526663;
            font-size: 13px;
            line-height: 1.45;
        }

        .section-header {
            margin: 18px 0 14px;
            padding: 18px 20px;
            border: 1px solid rgba(63,119,105,0.14);
            border-radius: 8px;
            background: rgba(255,255,255,0.72);
            box-shadow: 0 10px 24px rgba(63,119,105,0.07);
        }

        .section-kicker {
            color: var(--teal-deep);
            font-size: 13px;
            font-weight: 760;
            text-transform: uppercase;
            letter-spacing: .08em;
            margin-bottom: 5px;
        }

        .section-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 30px;
            font-weight: 760;
            color: var(--ink);
            line-height: 1.15;
            margin-bottom: 6px;
        }

        .section-copy {
            color: var(--muted);
            font-size: 16px;
            line-height: 1.58;
        }

        .paper-card {
            height: 100%;
            border-radius: 18px;
            overflow: hidden;
            background:
                linear-gradient(180deg, #ffffff 0%, #fbfdfc 100%);
            box-shadow: 0 8px 28px rgba(28, 62, 55, 0.08);
            transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(33, 124, 111, 0.1);
        }

        .paper-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 48px rgba(28, 90, 78, 0.16);
            border-color: rgba(33, 124, 111, 0.22);
        }

        .paper-image {
            width: 100%;
            height: auto;
            aspect-ratio: 1.34 / 1;
            object-fit: contain;
            object-position: center center;
            display: block;
            padding: 6px;
            box-sizing: border-box;
            background:
                linear-gradient(135deg, rgba(230, 242, 238, 0.82) 0%, rgba(255, 255, 255, 0.96) 58%, rgba(242, 247, 244, 0.92) 100%);
            border-bottom: 1px solid rgba(33, 124, 111, 0.1);
        }

        .paper-fallback {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 12px;
            padding: 0;
            background:
                linear-gradient(135deg, #f8fdfb 0%, #ffffff 100%);
        }

        .paper-fallback-mark {
            width: 64px;
            height: 64px;
            border-radius: 16px;
            display: grid;
            place-items: center;
            color: #ffffff;
            background: linear-gradient(135deg, #217c6f 0%, #1a5f56 100%);
            font-family: "Fraunces", Georgia, serif;
            font-size: 26px;
            font-weight: 760;
            box-shadow: 0 8px 20px rgba(33, 124, 111, 0.3);
        }

        .paper-fallback-topic {
            color: #217c6f;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.12em;
        }

        .paper-body {
            padding: 20px;
        }

        .paper-tag {
            display: inline-block;
            color: #ffffff;
            background: linear-gradient(135deg, #217c6f 0%, #1a5f56 100%);
            border-radius: 6px;
            padding: 5px 12px;
            font-size: 11px;
            font-weight: 600;
            margin-bottom: 12px;
            letter-spacing: 0.05em;
        }

        .paper-title {
            color: #1a2f2c;
            font-size: 17px;
            font-weight: 700;
            line-height: 1.4;
            margin-bottom: 8px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .paper-venue {
            color: #217c6f;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 14px;
        }

        .paper-text {
            display: none;
        }

        .paper-highlights {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 16px;
        }

        .paper-chip {
            font-size: 11px;
            color: #4a6b65;
            background: rgba(33, 124, 111, 0.08);
            border-radius: 4px;
            padding: 4px 9px;
            font-weight: 500;
        }

        .paper-actions {
            display: flex;
            gap: 8px;
            margin-top: 12px;
            padding-top: 16px;
            border-top: 1px solid rgba(0, 0, 0, 0.06);
        }

        .paper-btn {
            flex: 1;
            text-align: center;
            padding: 10px 12px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 200ms ease;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        .paper-btn-primary {
            background: linear-gradient(135deg, #217c6f 0%, #1a5f56 100%);
            color: #ffffff;
        }

        .paper-btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.4);
        }

        .paper-btn-secondary {
            background: rgba(0, 0, 0, 0.04);
            color: #4a5f5a;
        }

        .paper-btn-secondary:hover {
            background: rgba(0, 0, 0, 0.08);
        }

        .competition-filter-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(246, 251, 248, 0.94)),
                radial-gradient(circle at 0% 0%, rgba(33, 124, 111, 0.06), transparent 30%);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 16px;
            padding: 16px 24px;
            margin-bottom: 24px;
            box-shadow: 0 8px 24px rgba(38, 50, 56, 0.05);
        }

        .competition-filter-left {
            display: flex;
            align-items: center;
        }

        .competition-filter-right {
            display: flex;
            align-items: center;
        }

        .competition-filter-section ~ [data-testid="stSelectbox"] {
            width: fit-content;
            margin-top: -54px;
            margin-bottom: 28px;
        }

        .competition-filter-section ~ [data-testid="stSelectbox"] label {
            display: none;
        }

        .competition-filter-section ~ [data-testid="stSelectbox"] div[data-baseweb="select"] {
            border-radius: 12px;
            border: 2px solid rgba(63, 119, 105, 0.16);
            background: rgba(255, 255, 255, 0.92);
            padding: 10px 32px 10px 16px;
            font-size: 14px;
            font-weight: 700;
            color: #217c6f;
            transition: all 200ms ease;
            box-shadow: 0 4px 12px rgba(38, 50, 56, 0.06);
        }

        .competition-filter-section ~ [data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
            border-color: rgba(33, 124, 111, 0.30);
            background: rgba(33, 124, 111, 0.04);
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.08);
        }

        .competition-filter-section ~ [data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within {
            border-color: #217c6f;
            box-shadow: 0 0 0 3px rgba(33, 124, 111, 0.12);
        }

        .competition-filter-section ~ [data-testid="stSelectbox"] svg {
            color: #217c6f;
            width: 20px;
            height: 20px;
        }

        .competition-card-container {
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .competition-card {
            border-radius: 16px;
            overflow: hidden;
            background: #ffffff;
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.06);
            transition: all 280ms cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(63, 119, 105, 0.08);
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .competition-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 48px rgba(63, 119, 105, 0.16);
            border-color: rgba(63, 119, 105, 0.18);
        }

        .competition-image-wrapper {
            position: relative;
            width: 100%;
            height: 240px;
            overflow: hidden;
            background: #f5f7f6;
        }

        .competition-image {
            width: 100%;
            height: 100%;
            object-fit: contain;
            object-position: center;
        }

        .competition-image-placeholder {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            background: #f5f7f6;
        }

        .competition-year-badge {
            position: absolute;
            top: 12px;
            right: 12px;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(8px);
            padding: 5px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            color: #217c6f;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        }

        .competition-body {
            padding: 18px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .competition-category {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }

        .competition-category-icon {
            font-size: 16px;
        }

        .competition-category-text {
            font-size: 12px;
            font-weight: 600;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .competition-level {
            padding: 3px 9px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            border: 1px solid;
        }

        .competition-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 16px;
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.4;
            margin-bottom: 4px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .competition-chinese-title {
            font-size: 13px;
            color: #6f7d7b;
            margin-bottom: 12px;
        }

        .competition-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .competition-chip {
            font-size: 11px;
            color: #4a6b65;
            background: rgba(33, 124, 111, 0.08);
            border-radius: 4px;
            padding: 4px 9px;
            font-weight: 500;
        }

        .competition-detail-header {
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 16px;
            padding: 24px;
            background:
                linear-gradient(115deg, rgba(255, 255, 255, 0.94), rgba(236, 247, 242, 0.86)),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.035) 0, rgba(63, 119, 105, 0.035) 1px, transparent 1px, transparent 52px);
            box-shadow: 0 20px 46px rgba(63, 119, 105, 0.12);
            margin-bottom: 18px;
        }

        .competition-detail-category {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }

        .competition-detail-category-icon {
            font-size: 20px;
        }

        .competition-detail-category-text {
            font-size: 13px;
            font-weight: 600;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .competition-detail-level {
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            border: 1px solid;
        }

        .competition-detail-year {
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            background: rgba(33, 124, 111, 0.10);
            color: #217c6f;
        }

        .competition-detail-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 32px;
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.15;
            margin-bottom: 6px;
        }

        .competition-detail-chinese-title {
            font-size: 18px;
            color: #6f7d7b;
            margin-bottom: 14px;
        }

        .competition-detail-description {
            font-size: 16px;
            color: #4a5f5a;
            line-height: 1.6;
        }

        .competition-detail-image-container {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 16px;
            border: 1px solid #e9ecef;
        }

        .competition-detail-image {
            max-width: 100%;
            max-height: 70vh;
            object-fit: contain;
            border-radius: 12px;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.14);
            border: 1px solid #dee2e6;
        }

        .competition-detail-image-placeholder {
            width: 100%;
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 72px;
            background: #f5f7f6;
            border-radius: 12px;
            border: 1px solid #dee2e6;
        }

        .competition-detail-panel {
            border: 1px solid rgba(63, 119, 105, 0.13);
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.95);
            padding: 24px;
            box-shadow: 0 12px 28px rgba(63, 119, 105, 0.08);
            height: fit-content;
            position: sticky;
            top: 30px;
        }

        .competition-detail-panel h3 {
            font-family: "Fraunces", Georgia, serif;
            color: var(--teal-deep);
            font-size: 22px;
            margin: 0 0 16px;
        }

        .competition-info-row {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid rgba(63, 119, 105, 0.08);
        }

        .competition-info-row:last-child {
            border-bottom: none;
        }

        .competition-info-label {
            font-size: 13px;
            font-weight: 600;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .competition-info-value {
            font-size: 15px;
            font-weight: 700;
            color: #1a2f2c;
        }

        .competition-detail-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 18px;
            padding-top: 18px;
            border-top: 1px solid rgba(63, 119, 105, 0.08);
        }

        .competition-detail-body {
            margin-top: 24px;
        }

        .competition-detail-section {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 16px;
            padding: 28px;
            margin-bottom: 20px;
            box-shadow: 0 8px 24px rgba(63, 119, 105, 0.06);
        }

        .competition-detail-section-header {
            display: flex;
            align-items: flex-start;
            gap: 16px;
            margin-bottom: 20px;
        }

        .competition-detail-section-icon {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
            color: white;
            border-radius: 12px;
            font-family: "Fraunces", Georgia, serif;
            font-size: 16px;
            font-weight: 760;
            flex-shrink: 0;
        }

        .competition-detail-section-kicker {
            font-size: 12px;
            font-weight: 650;
            color: #78a99a;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 4px;
        }

        .competition-detail-section-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 24px;
            font-weight: 760;
            color: #1a2f2c;
            margin: 0;
            line-height: 1.2;
        }

        .competition-detail-section-text {
            font-size: 16px;
            color: #4a5f5a;
            line-height: 1.8;
            margin: 0;
        }

        .competition-achievements-grid {
            display: grid;
            gap: 12px;
        }

        .competition-achievement-item {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            padding: 14px 18px;
            background: rgba(33, 124, 111, 0.04);
            border-radius: 12px;
            border-left: 3px solid #217c6f;
        }

        .competition-achievement-check {
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #217c6f;
            color: white;
            border-radius: 50%;
            font-size: 12px;
            font-weight: 700;
            flex-shrink: 0;
        }

        .competition-achievement-text {
            font-size: 15px;
            color: #263238;
            line-height: 1.6;
            font-weight: 520;
        }

        @media (max-width: 1280px) {
            .profile-stats {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }

            .achievement-medals {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .info-item {
                grid-template-columns: 220px 1fr;
            }

            .courses-list {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 980px) {
            .block-container {
                padding-top: 100px;
                padding-left: 18px;
                padding-right: 18px;
                padding-bottom: 40px;
            }

            .portfolio-grid,
            .metric-strip,
            .profile-grid,
            .courses-list,
            .research-grid,
            .internship-columns {
                grid-template-columns: 1fr;
            }

            .info-item {
                grid-template-columns: 1fr;
                gap: 6px;
            }

            .hero-shell,
            .profile-hero {
                min-height: auto;
            }

            .profile-hero-content {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .profile-hero-text {
                flex-direction: column;
                justify-content: center;
                text-align: center;
            }

            .profile-stats {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .achievement-medals {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .internship-head {
                grid-template-columns: 1fr;
                gap: 10px;
            }

            .internship-period {
                width: fit-content;
            }

            .internship-timeline {
                padding-left: 28px;
            }

            .internship-card {
                flex-direction: column;
                padding: 20px;
            }

            .internship-card::before {
                left: -24px;
                top: 28px;
            }

            .chat-panel {
                padding: 24px 22px;
            }

            .chat-panel-inner {
                grid-template-columns: 1fr;
                gap: 18px;
            }

            .chat-scope-pill {
                width: fit-content;
                min-width: 0;
            }

            .internship-icon-wrapper {
                width: 64px;
                height: 64px;
            }

            .internship-icon {
                font-size: 32px;
            }
        }

        @media (max-width: 620px) {
            :root {
                --chat-input-bottom: 0px;
                --chat-sidebar-offset: 0px;
                --chat-main-gutter-left: 18px;
                --chat-main-gutter-right: 18px;
                --chat-input-width: calc(100vw - 36px);
                --chat-main-layer-width: 100vw;
                --chat-input-layer-height: 118px;
            }

            .profile-stats,
            .achievement-medals {
                grid-template-columns: 1fr;
            }

            div[data-testid="stChatInput"] {
                top: auto !important;
                bottom: var(--chat-input-bottom) !important;
                padding: 10px !important;
                border-radius: 16px !important;
            }

            div[data-testid="stBottomBlockContainer"]::before {
                top: auto;
                bottom: 0;
                height: 110px;
            }

            div[data-testid="stChatInput"] form {
                min-height: 64px !important;
                padding: 5px 6px 5px 12px !important;
            }

            .stChatInput textarea {
                font-size: 15px !important;
            }

            .stChatInput button {
                width: 48px !important;
                height: 48px !important;
                min-width: 48px !important;
                min-height: 48px !important;
            }
        }

        .paper-detail-cover {
            width: 100%;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            margin-bottom: 16px;
        }

        [data-testid="stButton"] button {
            background: linear-gradient(135deg, #217c6f 0%, #1a5f56 100%) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            font-size: 13px !important;
            transition: all 200ms ease !important;
        }

        [data-testid="stButton"] button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.4) !important;
        }

        [data-testid="stDownloadButton"] button {
            background: rgba(0, 0, 0, 0.04) !important;
            color: #4a5f5a !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            font-size: 13px !important;
            transition: all 200ms ease !important;
        }

        [data-testid="stDownloadButton"] button:hover {
            background: rgba(0, 0, 0, 0.08) !important;
        }

        .paper-detail-hero {
            border: 1px solid rgba(63,119,105,0.14);
            border-radius: 16px;
            padding: 24px;
            background:
                linear-gradient(115deg, rgba(255,255,255,0.94), rgba(236,247,242,0.86)),
                repeating-linear-gradient(90deg, rgba(63,119,105,0.035) 0, rgba(63,119,105,0.035) 1px, transparent 1px, transparent 52px);
            box-shadow: 0 20px 46px rgba(63,119,105,0.12);
            margin-bottom: 18px;
        }

        .paper-detail-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 36px;
            line-height: 1.12;
            color: var(--ink);
            font-weight: 760;
            margin: 8px 0 10px;
        }

        .paper-detail-grid {
            display: grid;
            grid-template-columns: 1.15fr .85fr;
            gap: 18px;
            align-items: start;
        }

        .detail-panel {
            border: 1px solid rgba(63,119,105,0.13);
            border-radius: 14px;
            background: rgba(255,255,255,0.86);
            padding: 16px;
            box-shadow: 0 12px 28px rgba(63,119,105,0.08);
            margin-bottom: 14px;
        }

        .detail-panel h3 {
            font-family: "Fraunces", Georgia, serif;
            color: var(--teal-deep);
            font-size: 22px;
            margin: 0 0 8px;
        }

        .detail-panel p {
            color: #43514e;
            font-size: 15px;
            line-height: 1.62;
            margin: 0;
        }

        .page-shot {
            width: 100%;
            border-radius: 12px;
            border: 1px solid rgba(63,119,105,0.14);
            box-shadow: 0 12px 28px rgba(63,119,105,0.10);
            background: white;
        }

        .figure-caption {
            color: #60736f;
            font-size: 13px;
            line-height: 1.5;
            margin: 7px 0 14px;
        }

        @media (max-width: 900px) {
            .paper-detail-grid {
                grid-template-columns: 1fr;
            }
        }

        .chat-divider {
            margin: 32px 0 18px;
            color: var(--teal-deep);
            font-family: "Fraunces", Georgia, serif;
            font-size: 24px;
            font-weight: 650;
        }

        .project-card {
            border-radius: 16px;
            overflow: hidden;
            background: #ffffff;
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.06);
            transition: all 280ms cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(63, 119, 105, 0.08);
            display: flex;
            flex-direction: column;
            height: 100%;
            padding: 22px;
        }

        .project-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 18px 42px rgba(63, 119, 105, 0.14);
            border-color: rgba(63, 119, 105, 0.18);
        }

        .project-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 8px;
        }

        .project-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 19px;
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.35;
            flex: 1;
            margin-right: 12px;
        }

        .project-github-link {
            flex-shrink: 0;
            color: #6f7d7b;
            transition: color 200ms ease;
        }

        .project-github-link:hover {
            color: #217c6f;
        }

        .project-chinese-title {
            font-size: 14px;
            color: #6f7d7b;
            margin-bottom: 12px;
            font-weight: 500;
        }

        .project-description {
            font-size: 14px;
            color: #4a5f5a;
            line-height: 1.6;
            margin-bottom: 14px;
            flex: 1;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 12px;
        }

        .project-chip {
            font-size: 11px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 999px;
            border: 1px solid;
            transition: all 200ms ease;
        }

        .project-chip:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .project-tech-preview {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            padding-top: 12px;
            border-top: 1px solid rgba(63, 119, 105, 0.08);
        }

        .project-tech-label {
            font-size: 11px;
            font-weight: 600;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .tech-chip {
            font-size: 11px;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.08);
            border-radius: 4px;
            padding: 3px 8px;
            font-weight: 500;
            transition: all 200ms ease;
        }

        .tech-chip:hover {
            background: rgba(33, 124, 111, 0.15);
        }

        .project-detail-header {
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 16px;
            padding: 28px;
            background:
                linear-gradient(115deg, rgba(255, 255, 255, 0.94), rgba(236, 247, 242, 0.86)),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.035) 0, rgba(63, 119, 105, 0.035) 1px, transparent 1px, transparent 52px);
            box-shadow: 0 20px 46px rgba(63, 119, 105, 0.12);
            margin-bottom: 22px;
        }

        .project-detail-title-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
        }

        .project-detail-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 34px;
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.15;
            margin-bottom: 6px;
        }

        .project-detail-chinese-title {
            font-size: 18px;
            color: #6f7d7b;
        }

        .project-detail-github {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 18px;
            background: rgba(33, 124, 111, 0.10);
            color: #217c6f;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 650;
            font-size: 14px;
            transition: all 200ms ease;
            flex-shrink: 0;
        }

        .project-detail-github:hover {
            background: rgba(33, 124, 111, 0.18);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.25);
        }

        .project-detail-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 18px;
        }

        .project-detail-description {
            font-size: 16px;
            color: #4a5f5a;
            line-height: 1.65;
            max-width: 900px;
        }

        .project-detail-section {
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 16px;
            padding: 26px;
            box-shadow: 0 10px 28px rgba(63, 119, 105, 0.08);
            margin-bottom: 18px;
        }

        .project-detail-section h3 {
            font-family: "Fraunces", Georgia, serif;
            color: var(--teal-deep);
            font-size: 22px;
            margin: 0 0 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .project-architecture {
            font-size: 15px;
            color: #4a5f5a;
            line-height: 1.7;
            background: rgba(33, 124, 111, 0.04);
            border-radius: 10px;
            padding: 16px 20px;
            border-left: 4px solid #217c6f;
            font-family: "Times New Roman", Times, serif;
        }

        .project-features {
            margin: 0;
            padding-left: 0;
        }

        .project-features li {
            position: relative;
            padding-left: 24px;
            margin-bottom: 12px;
            font-size: 15px;
            color: #4a5f5a;
            line-height: 1.6;
            list-style: none;
        }

        .project-features li:last-child {
            margin-bottom: 0;
        }

        .project-features li::before {
            content: "▸";
            position: absolute;
            left: 0;
            top: 2px;
            color: #217c6f;
            font-size: 15px;
            font-weight: 700;
        }

        .project-features-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
        }

        .feature-card {
            background: rgba(33, 124, 111, 0.03);
            border: 1px solid rgba(33, 124, 111, 0.08);
            border-radius: 12px;
            padding: 18px;
            transition: all 200ms ease;
        }

        .feature-card:hover {
            background: rgba(33, 124, 111, 0.06);
            border-color: rgba(33, 124, 111, 0.15);
            transform: translateY(-2px);
        }

        .feature-name {
            font-family: "Fraunces", Georgia, serif;
            font-size: 16px;
            font-weight: 760;
            color: #1a2f2c;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .feature-name::before {
            content: "✓";
            color: #217c6f;
            font-size: 14px;
            font-weight: 700;
        }

        .feature-description {
            font-size: 14px;
            color: #4a5f5a;
            line-height: 1.6;
        }

        .project-highlights {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .project-highlight-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            background:
                linear-gradient(135deg, rgba(33, 124, 111, 0.12), rgba(33, 124, 111, 0.04)),
                radial-gradient(circle at 30% 30%, rgba(33, 124, 111, 0.18), transparent 50%);
            color: #217c6f;
            border-radius: 999px;
            font-size: 13px;
            font-weight: 650;
            border: 1px solid rgba(33, 124, 111, 0.15);
            transition: all 200ms ease;
        }

        .project-highlight-tag:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.25);
            border-color: rgba(33, 124, 111, 0.25);
        }

        .project-detail-panel {
            border: 1px solid rgba(63, 119, 105, 0.13);
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.95);
            padding: 26px;
            box-shadow: 0 12px 28px rgba(63, 119, 105, 0.08);
            height: fit-content;
            position: sticky;
            top: 30px;
        }

        .project-detail-panel h3 {
            font-family: "Fraunces", Georgia, serif;
            color: var(--teal-deep);
            font-size: 22px;
            margin: 0 0 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .tech-category {
            margin-bottom: 20px;
        }

        .tech-category:last-child {
            margin-bottom: 0;
        }

        .tech-category-label {
            font-size: 12px;
            font-weight: 760;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .tech-category-label::before {
            content: "";
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #217c6f;
        }

        .tech-category-items {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .tech-stack-chip {
            font-size: 13px;
            color: #1a2f2c;
            background: linear-gradient(135deg, rgba(33, 124, 111, 0.10), rgba(33, 124, 111, 0.04));
            border-radius: 8px;
            padding: 7px 14px;
            font-weight: 650;
            border: 1px solid rgba(33, 124, 111, 0.15);
            transition: all 200ms ease;
        }

        .tech-stack-chip:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.20);
            background: linear-gradient(135deg, rgba(33, 124, 111, 0.15), rgba(33, 124, 111, 0.06));
        }

        @media (max-width: 900px) {
            .project-detail-title-row {
                flex-direction: column;
                gap: 14px;
            }

            .project-detail-github {
                align-self: flex-start;
            }

            .project-detail-header {
                padding: 20px;
            }

            .project-features-grid {
                grid-template-columns: 1fr;
            }
        }

        .internships-container {
            max-width: 900px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .internship-card {
            background: #ffffff;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(63, 119, 105, 0.06);
            border: 1px solid rgba(63, 119, 105, 0.08);
            display: flex;
            transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
        }

        .internship-card:hover {
            box-shadow: 0 12px 40px rgba(63, 119, 105, 0.15);
            border-color: rgba(33, 124, 111, 0.2);
            transform: translateY(-4px);
        }

        .internship-card.pending {
            opacity: 0.6;
            filter: grayscale(0.5);
        }

        .internship-card-image-wrapper {
            position: relative;
            width: 200px;
            flex-shrink: 0;
        }

        .internship-card-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            min-height: 220px;
        }

        .internship-card-image-placeholder {
            width: 100%;
            height: 220px;
            background: linear-gradient(135deg, #f0f4f2 0%, #e8efe9 100%);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .placeholder-icon {
            font-size: 48px;
            opacity: 0.4;
        }

        .internship-card-badge {
            position: absolute;
            top: 12px;
            left: 12px;
            font-size: 11px;
            font-weight: 700;
            color: white;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
            padding: 6px 14px;
            border-radius: 20px;
            box-shadow: 0 2px 8px rgba(33, 124, 111, 0.3);
        }

        .internship-card-content {
            flex: 1;
            padding: 24px;
            display: flex;
            flex-direction: column;
        }

        .internship-card-header {
            margin-bottom: 8px;
        }

        .internship-card-company {
            font-family: "Fraunces", Georgia, serif;
            font-size: 22px;
            font-weight: 760;
            color: #1a2f2c;
            margin: 0;
            line-height: 1.2;
        }

        .internship-card-position {
            font-size: 16px;
            font-weight: 650;
            color: #217c6f;
            margin-bottom: 4px;
        }

        .internship-card-location {
            font-size: 13px;
            color: #6f7d7b;
            margin-bottom: 14px;
        }

        .internship-card-description {
            font-size: 14px;
            color: #4a5f5a;
            line-height: 1.6;
            flex: 1;
            margin: 0 0 16px;
        }

        .internship-card-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 16px;
        }

        .internship-tag {
            font-size: 11px;
            font-weight: 650;
            padding: 5px 12px;
            border-radius: 20px;
            border: 1px solid;
            transition: all 200ms ease;
        }

        .internship-tag:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }

        .internship-card-btn,
        .internship-card-btn:link,
        .internship-card-btn:visited,
        .internship-card-btn:active {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            align-self: flex-start;
            padding: 10px 24px;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
            color: white !important;
            border: none;
            border-radius: 10px;
            font-weight: 650;
            font-size: 13px;
            cursor: pointer;
            transition: all 200ms ease;
            margin-top: auto;
            text-decoration: none !important;
        }

        .internship-card-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(33, 124, 111, 0.4);
            color: #ffffff;
            text-decoration: none;
        }

        .section-divider {
            display: flex;
            align-items: center;
            gap: 16px;
            margin: 36px 0;
        }

        .section-divider-line {
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(33, 124, 111, 0.25), transparent);
        }

        .section-divider-label {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background: rgba(33, 124, 111, 0.06);
            border-radius: 24px;
            font-size: 14px;
            font-weight: 650;
            color: #217c6f;
            white-space: nowrap;
        }

        .section-divider-icon {
            font-size: 16px;
        }

        .internship-card.practice-card {
            border-color: rgba(33, 124, 111, 0.12);
            background: linear-gradient(115deg, rgba(255, 255, 255, 0.96), rgba(236, 247, 242, 0.88));
        }

        .internships-container {
            max-width: 1120px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 22px;
        }

        .experience-track-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 16px;
            margin-bottom: 4px;
        }

        .experience-track-card {
            display: flex;
            flex-direction: column;
            min-height: 164px;
            padding: 22px 24px;
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 8px;
            background:
                linear-gradient(145deg, rgba(255, 255, 255, 0.96), rgba(247, 252, 249, 0.90)),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.025) 0, rgba(63, 119, 105, 0.025) 1px, transparent 1px, transparent 56px);
            box-shadow: 0 12px 30px rgba(38, 50, 56, 0.07);
        }

        .experience-track-label,
        .experience-group-eyebrow,
        .experience-card-track {
            color: #217c6f;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .experience-track-title {
            margin-top: 6px;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: 30px;
            font-weight: 760;
            line-height: 1.12;
        }

        .experience-track-copy {
            margin-top: 10px;
            color: #4a5f5a;
            font-size: 14.5px;
            line-height: 1.58;
            flex: 1;
        }

        .experience-track-count {
            width: fit-content;
            margin-top: 16px;
            padding: 6px 10px;
            border: 1px solid rgba(33, 124, 111, 0.14);
            border-radius: 999px;
            color: #3f7769;
            background: rgba(33, 124, 111, 0.055);
            font-size: 12px;
            font-weight: 700;
            line-height: 1.2;
        }

        .experience-group {
            padding: 24px;
            border: 1px solid rgba(63, 119, 105, 0.13);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.62);
            box-shadow: 0 10px 28px rgba(38, 50, 56, 0.055);
        }

        .experience-group-header {
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            gap: 18px;
            align-items: start;
            padding-bottom: 18px;
            margin-bottom: 18px;
            border-bottom: 1px solid rgba(63, 119, 105, 0.12);
        }

        .experience-group-title {
            margin: 4px 0 0;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(28px, 2.7vw, 40px);
            font-weight: 760;
            line-height: 1.12;
        }

        .experience-group-summary {
            max-width: 760px;
            margin: 8px 0 0;
            color: #4a5f5a;
            font-size: 15px;
            line-height: 1.6;
        }

        .experience-group-count {
            padding: 8px 12px;
            border: 1px solid rgba(33, 124, 111, 0.14);
            border-radius: 999px;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.055);
            font-size: 12px;
            font-weight: 760;
            white-space: nowrap;
        }

        .experience-filter-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(246, 251, 248, 0.94)),
                radial-gradient(circle at 100% 0%, rgba(33, 124, 111, 0.06), transparent 30%);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 16px;
            padding: 16px 24px;
            margin-bottom: 20px;
            box-shadow: 0 8px 24px rgba(38, 50, 56, 0.05);
        }

        .internships-container [data-testid="stSelectbox"] {
            width: fit-content;
        }

        .internships-container [data-testid="stSelectbox"] label {
            display: none;
        }

        .internships-container [data-testid="stSelectbox"] div[data-baseweb="select"] {
            border-radius: 12px;
            border: 2px solid rgba(63, 119, 105, 0.16);
            background: rgba(255, 255, 255, 0.92);
            padding: 10px 32px 10px 16px;
            font-size: 14px;
            font-weight: 700;
            color: #217c6f;
            transition: all 200ms ease;
            box-shadow: 0 4px 12px rgba(38, 50, 56, 0.06);
        }

        .internships-container [data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
            border-color: rgba(33, 124, 111, 0.30);
            background: rgba(33, 124, 111, 0.04);
            box-shadow: 0 6px 16px rgba(33, 124, 111, 0.08);
        }

        .internships-container [data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within {
            border-color: #217c6f;
            box-shadow: 0 0 0 3px rgba(33, 124, 111, 0.12);
        }

        .internships-container [data-testid="stSelectbox"] svg {
            color: #217c6f;
            width: 20px;
            height: 20px;
        }

        .experience-filter-info {
            display: flex;
            align-items: center;
        }

        .experience-filter-count {
            font-size: 13px;
            font-weight: 650;
            color: #6f7d7b;
        }

        .experience-card-list {
            display: grid;
            grid-template-columns: 1fr;
            gap: 16px;
            align-items: stretch;
        }

        .experience-card {
            display: grid;
            grid-template-columns: minmax(250px, 32%) minmax(0, 1fr);
            height: 480px;
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 8px;
            overflow: hidden;
            background: rgba(255, 255, 255, 0.96);
            box-shadow: 0 8px 22px rgba(38, 50, 56, 0.06);
            transition: border-color 200ms ease, box-shadow 200ms ease, transform 200ms ease;
            align-items: stretch;
        }

        .experience-card:hover {
            transform: translateY(-3px);
            border-color: rgba(33, 124, 111, 0.22);
            box-shadow: 0 16px 34px rgba(38, 50, 56, 0.10);
        }

        .experience-card.pending {
            opacity: 0.68;
            filter: grayscale(0.35);
        }

        .experience-card-media {
            position: relative;
            display: flex;
            align-items: stretch;
            justify-content: center;
            min-width: 0;
            min-height: 276px;
            background:
                linear-gradient(135deg, rgba(242, 248, 245, 0.98), rgba(229, 241, 235, 0.92)),
                repeating-linear-gradient(45deg, rgba(63, 119, 105, 0.035) 0, rgba(63, 119, 105, 0.035) 1px, transparent 1px, transparent 12px);
        }

        .experience-card-image-frame {
            width: 100%;
            height: 100%;
            padding: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
        }

        .experience-card-image {
            width: 100%;
            height: 100%;
            min-height: 248px;
            max-height: 330px;
            object-fit: contain;
            display: block;
            border-radius: 6px;
            background: #ffffff;
            box-shadow: 0 8px 20px rgba(38, 50, 56, 0.10);
        }

        .experience-card-document {
            border: 1px solid rgba(63, 119, 105, 0.14);
        }

        .experience-card-placeholder {
            width: 100%;
            height: 100%;
            min-height: 248px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px dashed rgba(63, 119, 105, 0.20);
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.62);
        }

        .experience-card-badge {
            position: absolute;
            left: 14px;
            top: 14px;
            max-width: calc(100% - 28px);
            padding: 6px 11px;
            border-radius: 999px;
            color: #ffffff;
            background: rgba(26, 95, 86, 0.92);
            box-shadow: 0 6px 16px rgba(38, 50, 56, 0.16);
            font-size: 11px;
            font-weight: 760;
            line-height: 1.2;
            white-space: nowrap;
        }

        .experience-card-body {
            min-width: 0;
            padding: 24px;
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .experience-card-title {
            margin: 6px 0 7px;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(22px, 2vw, 28px);
            font-weight: 760;
            line-height: 1.16;
            overflow-wrap: anywhere;
        }

        .experience-card-role {
            color: #217c6f;
            font-size: 15px;
            font-weight: 700;
            line-height: 1.35;
        }

        .experience-card-location {
            margin-top: 5px;
            color: #6f7d7b;
            font-size: 13px;
            font-weight: 650;
            line-height: 1.35;
        }

        .experience-card-description {
            margin: 14px 0 16px;
            color: #4a5f5a;
            font-size: 14.5px;
            line-height: 1.64;
            flex: 1;
        }

        .experience-card-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 16px;
        }

        .experience-card-btn,
        .experience-card-btn:link,
        .experience-card-btn:visited,
        .experience-card-btn:active {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            align-self: flex-start;
            min-height: 38px;
            padding: 9px 18px;
            border: 1px solid rgba(33, 124, 111, 0.20);
            border-radius: 8px;
            color: #ffffff !important;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
            font-size: 13px;
            font-weight: 700;
            line-height: 1.2;
            text-decoration: none !important;
            transition: transform 200ms ease, box-shadow 200ms ease;
        }

        .experience-card-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 18px rgba(33, 124, 111, 0.26);
            color: #ffffff !important;
            text-decoration: none !important;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
        }

        .gallery-item {
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(33, 124, 111, 0.12);
            background: linear-gradient(180deg, rgba(247, 251, 249, 0.96), rgba(232, 242, 237, 0.86));
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .gallery-item:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(33, 124, 111, 0.15);
        }

        .gallery-image {
            width: 100%;
            height: 180px;
            object-fit: contain;
            display: block;
            background: rgba(255, 255, 255, 0.72);
        }

        .detail-page-container {
            max-width: 1120px;
            margin: 0 auto;
        }

        .detail-topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
            margin: 2px 0 14px;
            color: #6f7d7b;
        }

        .detail-eyebrow {
            color: #217c6f;
            font-size: 12px;
            font-weight: 760;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .detail-index {
            font-size: 12px;
            font-weight: 650;
            color: rgba(74, 95, 90, 0.76);
        }

        .detail-hero {
            background:
                linear-gradient(118deg, rgba(255, 255, 255, 0.97) 0%, rgba(246, 251, 248, 0.92) 54%, rgba(220, 235, 228, 0.82) 100%),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.035) 0, rgba(63, 119, 105, 0.035) 1px, transparent 1px, transparent 58px);
            border: 1px solid rgba(63, 119, 105, 0.16);
            border-radius: 16px;
            padding: clamp(26px, 3.2vw, 42px);
            margin-bottom: 18px;
            box-shadow: 0 22px 54px rgba(38, 50, 56, 0.11);
            display: grid;
            grid-template-columns: minmax(0, 1fr) 274px;
            align-items: stretch;
            gap: clamp(24px, 3vw, 38px);
            overflow: hidden;
            position: relative;
        }

        .detail-hero::before {
            content: "";
            position: absolute;
            inset: 0;
            border-top: 4px solid rgba(33, 124, 111, 0.72);
            pointer-events: none;
        }

        .detail-company {
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(34px, 4vw, 52px);
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.04;
            max-width: 760px;
            margin-bottom: 12px;
        }

        .detail-position {
            display: inline-flex;
            width: fit-content;
            align-items: center;
            min-height: 34px;
            font-size: 15px;
            font-weight: 650;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.09);
            border: 1px solid rgba(33, 124, 111, 0.14);
            border-radius: 8px;
            padding: 7px 12px;
            margin-bottom: 16px;
        }

        .detail-lede {
            max-width: 760px;
            color: #4a5f5a;
            font-size: 16px;
            line-height: 1.68;
            margin: 0 0 22px;
        }

        .detail-meta-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(130px, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }

        .detail-meta-card {
            background: rgba(255, 255, 255, 0.74);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 10px;
            padding: 12px 14px;
            box-shadow: 0 8px 18px rgba(63, 119, 105, 0.05);
        }

        .detail-meta-card span {
            display: block;
            color: #6f7d7b;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 5px;
        }

        .detail-meta-card strong {
            display: block;
            color: #1f3733;
            font-size: 14px;
            line-height: 1.35;
            font-weight: 760;
        }

        .detail-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .detail-hero-doc {
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid rgba(63, 119, 105, 0.13);
            border-radius: 14px;
            padding: 14px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.82), 0 14px 28px rgba(38, 50, 56, 0.10);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            min-height: 346px;
        }

        .detail-doc-label,
        .detail-doc-caption {
            width: 100%;
            text-align: center;
            color: #6f7d7b;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .detail-doc-caption {
            letter-spacing: 0;
            text-transform: none;
            font-weight: 650;
            color: rgba(74, 95, 90, 0.72);
        }

        .detail-doc-frame {
            width: 100%;
            height: 260px;
            margin: 12px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            background:
                linear-gradient(180deg, rgba(247, 251, 249, 0.92), rgba(232, 242, 237, 0.74));
            border: 1px solid rgba(63, 119, 105, 0.11);
            overflow: hidden;
        }

        .detail-doc-preview {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 8px;
            border: 1px solid rgba(63, 119, 105, 0.13);
            box-shadow: 0 10px 22px rgba(38, 50, 56, 0.13);
            background: #ffffff;
        }

        .doc-placeholder {
            width: 100%;
            height: 100%;
            background:
                linear-gradient(135deg, rgba(240, 246, 243, 0.92), rgba(223, 236, 230, 0.86));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(63, 119, 105, 0.14);
        }

        .doc-icon {
            color: rgba(33, 124, 111, 0.40);
            font-size: 26px;
            font-weight: 760;
            letter-spacing: 0.08em;
        }

        .detail-body-grid {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(280px, 340px);
            gap: 18px;
            align-items: start;
        }

        .detail-main-column,
        .detail-side-column {
            display: flex;
            flex-direction: column;
            gap: 18px;
        }

        .detail-side-column {
            position: sticky;
            top: 24px;
        }

        .detail-section {
            background: rgba(255, 255, 255, 0.90);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 14px;
            padding: clamp(22px, 2.4vw, 30px);
            box-shadow: 0 12px 30px rgba(38, 50, 56, 0.07);
            transition: all 200ms ease;
        }

        .detail-section:hover {
            border-color: rgba(33, 124, 111, 0.20);
            box-shadow: 0 16px 34px rgba(38, 50, 56, 0.10);
        }

        .detail-section-header {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            margin-bottom: 18px;
        }

        .detail-section-header.compact {
            margin-bottom: 14px;
        }

        .section-icon {
            width: 38px;
            height: 38px;
            border-radius: 10px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            color: #ffffff;
            background: linear-gradient(135deg, #217c6f, #4f9386);
            font-size: 12px;
            font-weight: 760;
            box-shadow: 0 8px 18px rgba(33, 124, 111, 0.22);
        }

        .detail-section-kicker {
            color: #6f7d7b;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 2px;
        }

        .detail-section-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 22px;
            font-weight: 760;
            color: #1a2f2c;
            margin: 0;
            line-height: 1.18;
        }

        .detail-section-text {
            font-size: 16px;
            color: #4a5f5a;
            line-height: 1.78;
            margin: 0;
        }

        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
        }

        .achievement-item {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            min-height: 86px;
            padding: 15px 16px;
            background: linear-gradient(135deg, rgba(33, 124, 111, 0.055), rgba(255, 255, 255, 0.86));
            border: 1px solid rgba(33, 124, 111, 0.10);
            border-radius: 10px;
            transition: all 200ms ease;
        }

        .achievement-item:hover {
            background: rgba(33, 124, 111, 0.075);
            border-color: rgba(33, 124, 111, 0.18);
            transform: translateY(-2px);
        }

        .achievement-check {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: rgba(33, 124, 111, 0.11);
            color: #217c6f;
            font-size: 11px;
            font-weight: 760;
            flex-shrink: 0;
        }

        .achievement-text {
            font-size: 14.5px;
            color: #4a5f5a;
            line-height: 1.6;
        }

        .detail-stats {
            display: grid;
            gap: 10px;
        }

        .detail-stat {
            display: grid;
            grid-template-columns: 54px minmax(0, 1fr);
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: rgba(33, 124, 111, 0.045);
            border: 1px solid rgba(33, 124, 111, 0.10);
            border-radius: 10px;
        }

        .detail-stat strong {
            color: #217c6f;
            font-family: "Fraunces", Georgia, serif;
            font-size: 28px;
            line-height: 1;
        }

        .detail-stat span {
            color: #4a5f5a;
            font-size: 13px;
            font-weight: 650;
            line-height: 1.3;
        }

        .skills-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .skill-chip {
            font-size: 12px;
            font-weight: 650;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.075);
            padding: 7px 11px;
            border-radius: 8px;
            border: 1px solid rgba(33, 124, 111, 0.15);
            transition: all 200ms ease;
            line-height: 1.25;
        }

        .skill-chip:hover {
            background: rgba(33, 124, 111, 0.14);
            border-color: rgba(33, 124, 111, 0.25);
            transform: translateY(-2px);
        }

        .practice-detail-container {
            max-width: 1000px;
            margin: 0 auto;
        }

        .practice-detail-topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
            margin: 2px 0 20px;
            color: #6f7d7b;
        }

        .practice-detail-eyebrow {
            color: #217c6f;
            font-size: 12px;
            font-weight: 760;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .practice-detail-index {
            font-size: 12px;
            font-weight: 650;
            color: rgba(74, 95, 90, 0.76);
        }

        .practice-detail-hero {
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(240, 250, 246, 0.94) 50%, rgba(228, 242, 236, 0.88) 100%),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.03) 0, rgba(63, 119, 105, 0.03) 1px, transparent 1px, transparent 60px);
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 20px;
            padding: 32px;
            margin-bottom: 24px;
            box-shadow: 0 24px 56px rgba(38, 50, 56, 0.09);
            display: grid;
            grid-template-columns: minmax(0, 1fr) 280px;
            gap: 32px;
            position: relative;
            overflow: hidden;
        }

        .practice-detail-hero::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #217c6f, #78a99a, #217c6f);
        }

        .practice-detail-hero-left {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .practice-detail-organization {
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(28px, 3.5vw, 42px);
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.1;
            margin: 0;
        }

        .practice-detail-role {
            display: inline-flex;
            align-items: center;
            font-size: 14px;
            font-weight: 650;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.08);
            border: 1px solid rgba(33, 124, 111, 0.14);
            border-radius: 8px;
            padding: 6px 14px;
            width: fit-content;
        }

        .practice-detail-lede {
            font-size: 16px;
            color: #4a5f5a;
            line-height: 1.7;
            margin: 0;
            max-width: 600px;
        }

        .practice-detail-meta {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
        }

        .practice-meta-item {
            display: grid;
            grid-template-columns: auto minmax(0, 1fr);
            align-items: center;
            column-gap: 10px;
            row-gap: 2px;
            padding: 10px 16px;
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(63, 119, 105, 0.1);
            border-radius: 10px;
        }

        .practice-meta-label {
            font-size: 11px;
            font-weight: 760;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .practice-meta-value {
            font-size: 14px;
            font-weight: 700;
            color: #1a2f2c;
            min-width: 0;
        }

        .practice-detail-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 4px;
        }

        .practice-tag {
            font-size: 12px;
            font-weight: 650;
            padding: 6px 12px;
            border-radius: 8px;
            border: 1px solid;
            line-height: 1.3;
        }

        .practice-detail-hero-right {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .practice-detail-doc-card {
            width: 100%;
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 14px;
            padding: 16px;
            box-shadow: 0 12px 28px rgba(38, 50, 56, 0.08);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }

        .practice-doc-label {
            font-size: 11px;
            font-weight: 760;
            color: #6f7d7b;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .practice-doc-frame {
            width: 100%;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            background: linear-gradient(180deg, rgba(247, 251, 249, 0.92), rgba(232, 242, 237, 0.74));
            border: 1px solid rgba(63, 119, 105, 0.1);
            overflow: hidden;
        }

        .practice-detail-doc-preview {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 8px;
            background: #ffffff;
        }

        .practice-doc-placeholder {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(240, 246, 243, 0.92), rgba(223, 236, 230, 0.86));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .practice-doc-icon {
            color: rgba(33, 124, 111, 0.4);
            font-size: 24px;
        }

        .practice-doc-caption {
            font-size: 12px;
            font-weight: 650;
            color: rgba(74, 95, 90, 0.7);
        }

        .practice-detail-content {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .practice-detail-section {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(63, 119, 105, 0.1);
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 12px 32px rgba(38, 50, 56, 0.06);
            transition: all 200ms ease;
        }

        .practice-detail-section:hover {
            border-color: rgba(33, 124, 111, 0.18);
            box-shadow: 0 16px 36px rgba(38, 50, 56, 0.09);
        }

        .practice-section-header {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            margin-bottom: 18px;
        }

        .practice-section-icon {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
            color: white;
            border-radius: 12px;
            font-family: "Fraunces", Georgia, serif;
            font-size: 16px;
            font-weight: 760;
            flex-shrink: 0;
        }

        .practice-section-kicker {
            font-size: 11px;
            font-weight: 760;
            color: #78a99a;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 4px;
        }

        .practice-section-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 22px;
            font-weight: 760;
            color: #1a2f2c;
            margin: 0;
            line-height: 1.2;
        }

        .practice-section-text {
            font-size: 16px;
            color: #4a5f5a;
            line-height: 1.78;
            margin: 0;
        }

        .practice-achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 14px;
        }

        .practice-achievement-item {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            padding: 16px;
            background: linear-gradient(135deg, rgba(33, 124, 111, 0.04), rgba(255, 255, 255, 0.9));
            border: 1px solid rgba(33, 124, 111, 0.08);
            border-radius: 12px;
            transition: all 200ms ease;
            border-left: 3px solid #217c6f;
        }

        .practice-achievement-item:hover {
            background: linear-gradient(135deg, rgba(33, 124, 111, 0.08), rgba(255, 255, 255, 0.95));
            border-color: rgba(33, 124, 111, 0.18);
            transform: translateX(4px);
        }

        .practice-achievement-icon {
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #217c6f;
            color: white;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 760;
            flex-shrink: 0;
        }

        .practice-achievement-text {
            font-size: 15px;
            color: #263238;
            line-height: 1.6;
            font-weight: 520;
        }

        .practice-gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 14px;
        }

        .practice-gallery-item {
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(63, 119, 105, 0.1);
            background: linear-gradient(180deg, rgba(247, 251, 249, 0.96), rgba(232, 242, 237, 0.86));
            box-shadow: 0 6px 16px rgba(38, 50, 56, 0.06);
            transition: all 200ms ease;
        }

        .practice-gallery-item:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 28px rgba(33, 124, 111, 0.15);
        }

        .practice-gallery-image {
            width: 100%;
            height: 180px;
            object-fit: contain;
            display: block;
            background: rgba(255, 255, 255, 0.72);
        }

        .practice-skills-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .practice-skill-chip {
            font-size: 13px;
            font-weight: 650;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.06);
            padding: 8px 14px;
            border-radius: 20px;
            border: 1px solid rgba(33, 124, 111, 0.12);
            transition: all 200ms ease;
        }

        .practice-skill-chip:hover {
            background: rgba(33, 124, 111, 0.12);
            border-color: rgba(33, 124, 111, 0.22);
            transform: translateY(-2px);
        }

        @media (max-width: 1040px) {
            .experience-card {
                grid-template-columns: minmax(220px, 36%) minmax(0, 1fr);
            }

            .detail-hero {
                grid-template-columns: 1fr;
            }

            .detail-hero-doc {
                max-width: 420px;
            }

            .detail-body-grid {
                grid-template-columns: 1fr;
            }

            .detail-side-column {
                position: static;
            }
        }

        @media (max-width: 900px) {
            .experience-track-grid {
                grid-template-columns: 1fr;
            }

            .experience-group-header {
                grid-template-columns: 1fr;
            }

            .experience-group-count {
                width: fit-content;
            }

            .experience-card {
                grid-template-columns: 1fr;
            }

            .experience-card-image-frame {
                height: 260px;
                min-height: 260px;
            }

            .experience-card-image {
                max-height: 232px;
            }

            .achievements-grid {
                grid-template-columns: 1fr;
            }

            .detail-meta-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .internships-container {
                gap: 16px;
            }

            .experience-track-card,
            .experience-group {
                padding: 18px;
            }

            .experience-track-title {
                font-size: 26px;
            }

            .experience-card-body {
                padding: 20px;
            }

            .experience-card-title {
                font-size: 22px;
            }

            .experience-card-image-frame {
                height: 230px;
                min-height: 230px;
                padding: 12px;
            }

            .experience-card-image {
                max-height: 206px;
            }

            .internship-card {
                flex-direction: column;
            }

            .internship-card-image-wrapper {
                width: 100%;
            }

            .internship-card-image {
                min-height: 180px;
            }

            .internship-card-image-placeholder {
                height: 180px;
            }

            .detail-topbar {
                align-items: flex-start;
                flex-direction: column;
                gap: 4px;
            }

            .detail-hero {
                padding: 24px 20px;
                border-radius: 14px;
            }

            .detail-hero-doc {
                width: 100%;
                min-height: auto;
            }

            .detail-doc-frame {
                height: 240px;
            }

            .doc-placeholder {
                width: 100%;
            }

            .detail-section {
                padding: 22px 18px;
            }

            .practice-card {
                flex-direction: column;
                text-align: center;
            }
        }
        /* Refined competitions section */
        .competition-overview {
            display: grid;
            grid-template-columns: minmax(0, 1.35fr) minmax(360px, 0.65fr);
            gap: 18px;
            align-items: stretch;
            margin: 6px 0 14px;
            padding: 22px;
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 8px;
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.96), rgba(246, 250, 248, 0.90)),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.028) 0, rgba(63, 119, 105, 0.028) 1px, transparent 1px, transparent 58px);
            box-shadow: 0 12px 30px rgba(38, 50, 56, 0.07);
        }

        .competition-overview-main {
            min-width: 0;
        }

        .competition-overview-kicker,
        .competition-filter-label,
        .experience-control-kicker,
        .experience-filter-label {
            color: #217c6f;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.08em;
            line-height: 1.25;
            text-transform: uppercase;
        }

        .competition-overview-title {
            margin-top: 5px;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(28px, 2.8vw, 40px);
            font-weight: 760;
            line-height: 1.12;
        }

        .competition-overview-copy {
            max-width: 760px;
            margin-top: 9px;
            color: #4a5f5a;
            font-size: 15px;
            line-height: 1.58;
        }

        .competition-overview-stats {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 10px;
            align-content: stretch;
        }

        .competition-stat-card {
            min-width: 0;
            padding: 16px 14px;
            border: 1px solid rgba(63, 119, 105, 0.13);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.74);
        }

        .competition-stat-card span,
        .experience-control-stat span {
            display: block;
            color: #6f7d7b;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.05em;
            line-height: 1.2;
            text-transform: uppercase;
        }

        .competition-stat-card strong,
        .experience-control-stat strong {
            display: block;
            margin-top: 7px;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: 28px;
            font-weight: 760;
            line-height: 1;
        }

        .competition-filter-tabs,
        .experience-filter-tabs {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 22px;
            margin: -4px 0 18px;
            padding: 0 2px 10px;
            border-bottom: 1px solid rgba(63, 119, 105, 0.13);
        }

        .competition-filter-tab,
        .competition-filter-tab:link,
        .competition-filter-tab:visited,
        .experience-filter-tab,
        .experience-filter-tab:link,
        .experience-filter-tab:visited {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 7px;
            min-height: 32px;
            padding: 0 0 8px;
            border: 0;
            border-radius: 0;
            color: #6f7d7b !important;
            background: transparent;
            text-decoration: none !important;
            box-shadow: none;
            transition: color 180ms ease;
        }

        .competition-filter-tab::after,
        .experience-filter-tab::after {
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            bottom: -11px;
            height: 2px;
            border-radius: 999px;
            background: transparent;
            transition: background 180ms ease;
        }

        .competition-filter-tab:hover,
        .experience-filter-tab:hover {
            transform: none;
            border-color: transparent;
            background: transparent;
            box-shadow: none;
            color: #217c6f !important;
            text-decoration: none !important;
        }

        .competition-filter-tab.active,
        .experience-filter-tab.active {
            border-color: transparent;
            background: transparent;
            box-shadow: none;
            color: #1a5f56 !important;
        }

        .competition-filter-tab.active::after,
        .experience-filter-tab.active::after {
            background: #217c6f;
        }

        .competition-filter-tab span,
        .experience-filter-tab span {
            min-width: 0;
            overflow: hidden;
            color: inherit;
            font-size: 14px;
            font-weight: 760;
            line-height: 1.2;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .competition-filter-tab strong,
        .experience-filter-tab strong {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 24px;
            height: 22px;
            padding: 0 7px;
            border-radius: 999px;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.075);
            font-size: 12px;
            font-weight: 760;
        }

        .competition-filter-panel,
        .experience-filter-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            margin: 0 0 16px;
            padding: 14px 16px;
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.70);
            box-shadow: 0 8px 18px rgba(38, 50, 56, 0.045);
        }

        .competition-filter-title,
        .experience-filter-title {
            margin-top: 4px;
            color: #1a2f2c;
            font-size: 18px;
            font-weight: 760;
            line-height: 1.2;
        }

        .competition-filter-count,
        .experience-filter-count {
            flex: 0 0 auto;
            padding: 7px 10px;
            border: 1px solid rgba(33, 124, 111, 0.12);
            border-radius: 8px;
            color: #3f7769;
            background: rgba(33, 124, 111, 0.055);
            font-size: 12px;
            font-weight: 760;
            line-height: 1.2;
            white-space: nowrap;
        }

        .competition-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 18px;
            align-items: stretch;
        }

        .competition-card {
            display: flex;
            min-width: 0;
            min-height: 100%;
            flex-direction: column;
            overflow: hidden;
            border: 1px solid rgba(63, 119, 105, 0.12);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.96);
            box-shadow: 0 8px 22px rgba(38, 50, 56, 0.06);
            transition: transform 200ms ease, box-shadow 200ms ease, border-color 200ms ease;
        }

        .competition-card:hover {
            transform: translateY(-4px);
            border-color: rgba(33, 124, 111, 0.22);
            box-shadow: 0 16px 34px rgba(38, 50, 56, 0.10);
        }

        .competition-image-wrapper {
            position: relative;
            width: 100%;
            height: 260px;
            padding: 12px;
            overflow: hidden;
            box-sizing: border-box;
            background:
                linear-gradient(135deg, rgba(242, 248, 245, 0.98), rgba(229, 241, 235, 0.90)),
                repeating-linear-gradient(45deg, rgba(63, 119, 105, 0.035) 0, rgba(63, 119, 105, 0.035) 1px, transparent 1px, transparent 12px);
        }

        .competition-image {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: contain;
            object-position: center;
            border-radius: 6px;
            background: #ffffff;
            box-shadow: 0 8px 20px rgba(38, 50, 56, 0.10);
        }

        .competition-image-placeholder {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px dashed rgba(63, 119, 105, 0.22);
            border-radius: 6px;
            color: rgba(33, 124, 111, 0.48);
            background: rgba(255, 255, 255, 0.66);
            font-size: 22px;
            font-weight: 760;
            letter-spacing: 0.08em;
        }

        .competition-year-badge,
        .competition-level-badge {
            position: absolute;
            z-index: 1;
            max-width: calc(100% - 28px);
            padding: 6px 10px;
            border-radius: 8px;
            font-size: 11px;
            font-weight: 760;
            line-height: 1.2;
            white-space: nowrap;
            box-shadow: 0 6px 16px rgba(38, 50, 56, 0.14);
            backdrop-filter: blur(8px);
        }

        .competition-year-badge {
            top: 14px;
            right: 14px;
            color: #217c6f;
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(33, 124, 111, 0.12);
        }

        .competition-level-badge {
            left: 14px;
            bottom: 14px;
            border: 1px solid;
            background: rgba(255, 255, 255, 0.90);
        }

        .competition-body {
            display: flex;
            min-width: 0;
            flex: 1;
            flex-direction: column;
            padding: 18px 18px 14px;
        }

        .competition-category {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
            min-width: 0;
        }

        .competition-category-mark,
        .competition-detail-category-mark {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            flex: 0 0 auto;
            height: 24px;
            min-width: 36px;
            padding: 0 8px;
            border: 1px solid rgba(33, 124, 111, 0.16);
            border-radius: 7px;
            color: #217c6f;
            background: rgba(33, 124, 111, 0.07);
            font-size: 10px;
            font-weight: 760;
            letter-spacing: 0.06em;
        }

        .competition-category-text,
        .competition-detail-category-text {
            min-width: 0;
            overflow: hidden;
            color: #6f7d7b;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.08em;
            line-height: 1.2;
            text-overflow: ellipsis;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .competition-title {
            display: -webkit-box;
            margin: 0 0 10px;
            overflow: hidden;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: 19px;
            font-weight: 760;
            line-height: 1.22;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 2;
        }

        .competition-description {
            display: -webkit-box;
            margin: 0 0 14px;
            overflow: hidden;
            color: #4a5f5a;
            font-size: 14px;
            line-height: 1.55;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 3;
        }

        .competition-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 7px;
            margin-top: auto;
        }

        .competition-chip {
            display: inline-flex;
            align-items: center;
            min-height: 24px;
            padding: 4px 9px;
            border: 1px solid rgba(33, 124, 111, 0.12);
            border-radius: 7px;
            color: #3f7769;
            background: rgba(33, 124, 111, 0.06);
            font-size: 11px;
            font-weight: 650;
            line-height: 1.2;
        }

        .competition-card-btn,
        .competition-card-btn:link,
        .competition-card-btn:visited,
        .competition-card-btn:active {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 42px;
            margin: 0 18px 18px;
            border: 1px solid rgba(33, 124, 111, 0.18);
            border-radius: 8px;
            color: #ffffff !important;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
            font-size: 13px;
            font-weight: 760;
            line-height: 1.2;
            text-decoration: none !important;
            transition: transform 180ms ease, box-shadow 180ms ease;
        }

        .competition-card-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 18px rgba(33, 124, 111, 0.24);
            color: #ffffff !important;
            text-decoration: none !important;
        }

        .competition-detail-header,
        .competition-detail-image-container,
        .competition-detail-panel,
        .competition-detail-section {
            border-radius: 8px;
        }

        .competition-detail-image-container {
            background:
                linear-gradient(135deg, rgba(242, 248, 245, 0.98), rgba(229, 241, 235, 0.90));
            border-color: rgba(63, 119, 105, 0.13);
        }

        .competition-detail-image {
            width: 100%;
            max-height: 72vh;
            object-fit: contain;
            border-radius: 6px;
        }

        .competition-achievement-item {
            border-radius: 8px;
        }

        .competition-achievement-check,
        .competition-detail-section-icon {
            border-radius: 8px;
        }

        /* Refined internships and practices type control */
        .internships-container {
            max-width: 1120px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 18px;
        }

        .experience-control-panel {
            display: grid;
            grid-template-columns: minmax(0, 1.25fr) minmax(340px, 0.75fr);
            gap: 18px;
            align-items: stretch;
            padding: 22px;
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 8px;
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.96), rgba(246, 250, 248, 0.90)),
                repeating-linear-gradient(90deg, rgba(63, 119, 105, 0.026) 0, rgba(63, 119, 105, 0.026) 1px, transparent 1px, transparent 58px);
            box-shadow: 0 12px 30px rgba(38, 50, 56, 0.07);
        }

        .experience-control-copy {
            min-width: 0;
        }

        .experience-control-title {
            margin-top: 5px;
            color: #1a2f2c;
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(28px, 2.8vw, 40px);
            font-weight: 760;
            line-height: 1.12;
        }

        .experience-control-text {
            max-width: 760px;
            margin-top: 9px;
            color: #4a5f5a;
            font-size: 15px;
            line-height: 1.58;
        }

        .experience-control-stats {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 10px;
        }

        .experience-control-stat {
            min-width: 0;
            padding: 16px 14px;
            border: 1px solid rgba(63, 119, 105, 0.13);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.74);
        }

        .experience-filter-tabs {
            grid-template-columns: repeat(3, minmax(0, 1fr));
            margin-bottom: 0;
        }

        .experience-filter-tabs {
            display: flex;
            margin-bottom: 18px;
        }

        .experience-card {
            min-height: 288px;
        }

        .experience-card-image-frame {
            min-height: 288px;
        }

        @media (max-width: 1040px) {
            .competition-overview,
            .experience-control-panel {
                grid-template-columns: 1fr;
            }

            .competition-overview-stats,
            .experience-control-stats {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }
        }

        @media (max-width: 900px) {
            .competition-filter-tabs {
                display: flex;
                gap: 18px;
            }

            .competition-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            }

            .competition-image-wrapper {
                height: 240px;
            }

            .experience-filter-tabs {
                display: flex;
                gap: 18px;
            }
        }

        @media (max-width: 680px) {
            .competition-overview,
            .experience-control-panel {
                padding: 18px;
            }

            .competition-overview-stats,
            .experience-control-stats {
                grid-template-columns: 1fr;
            }

            .competition-filter-panel,
            .experience-filter-section {
                align-items: flex-start;
                flex-direction: column;
            }

            .competition-filter-count,
            .experience-filter-count {
                white-space: normal;
            }

            .competition-filter-tabs {
                display: flex;
                gap: 16px;
            }
        }

        /* Final card alignment overrides for Internships & Practices. */
        .internships-container > .experience-card-list {
            display: grid;
            grid-template-columns: 1fr;
            gap: 18px;
            align-items: stretch;
        }

        .internships-container .experience-card {
            display: grid;
            grid-template-columns: minmax(260px, 34%) minmax(0, 1fr);
            height: auto;
            min-height: 332px;
            align-items: stretch;
        }

        .internships-container .experience-card-media {
            height: 100%;
            min-height: 332px;
        }

        .internships-container .experience-card-image-frame {
            height: 100%;
            min-height: 0;
            padding: 14px;
        }

        .internships-container .experience-card-image,
        .internships-container .experience-card-placeholder {
            width: 100%;
            height: 100%;
            min-height: 0;
            max-height: none;
        }

        .internships-container .experience-card-body {
            min-height: 100%;
            height: auto;
            padding: 24px;
        }

        .internships-container .experience-card-title {
            margin: 6px 0 7px;
            font-size: 24px;
            line-height: 1.18;
        }

        .internships-container .experience-card-description {
            flex: 1 1 auto;
            margin: 14px 0 16px;
        }

        .internships-container .experience-card-tags {
            min-height: 34px;
            margin-top: auto;
            margin-bottom: 16px;
        }

        @media (max-width: 900px) {
            .internships-container .experience-card {
                grid-template-columns: 1fr;
                min-height: 0;
            }

            .internships-container .experience-card-media {
                min-height: 260px;
            }

            .internships-container .experience-card-image-frame {
                height: 260px;
                min-height: 260px;
            }

            .internships-container .experience-card-image,
            .internships-container .experience-card-placeholder {
                max-height: 232px;
            }
        }

        @media (max-width: 680px) {
            .internships-container .experience-card-body {
                padding: 20px;
            }

            .internships-container .experience-card-title {
                font-size: 22px;
            }

            .internships-container .experience-card-image-frame {
                height: 230px;
                min-height: 230px;
                padding: 12px;
            }

            .internships-container .experience-card-image,
            .internships-container .experience-card-placeholder {
                max-height: 206px;
            }
        }

        .gallery-cover-card {
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 14px;
            overflow: hidden;
            background: linear-gradient(160deg, rgba(248, 252, 250, 0.98), rgba(234, 245, 240, 0.92));
            box-shadow: 0 14px 36px rgba(38, 50, 56, 0.08);
            padding: 16px 16px 18px;
        }

        .gallery-cover-label {
            display: inline-block;
            margin-bottom: 12px;
            padding: 5px 11px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 760;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #ffffff;
            background: linear-gradient(135deg, #217c6f, #1a5f56);
        }

        .gallery-cover-image {
            width: 100%;
            border-radius: 10px;
            display: block;
            background: #ffffff;
            box-shadow: 0 8px 22px rgba(38, 50, 56, 0.10);
            margin-bottom: 14px;
        }

        .gallery-cover-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 19px;
            font-weight: 700;
            line-height: 1.25;
            color: #1a2f2c;
        }

        .gallery-section-header {
            margin: 22px 0 14px;
            padding-bottom: 12px;
            border-bottom: 1px solid rgba(63, 119, 105, 0.10);
        }

        .gallery-section-kicker {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            background: rgba(33, 124, 111, 0.10);
            color: #1a5f56;
            font-size: 10.5px;
            font-weight: 760;
            letter-spacing: 0.10em;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .gallery-section-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 26px;
            font-weight: 760;
            color: #1a2f2c;
            line-height: 1.15;
        }

        .gallery-card {
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding: 16px;
            border: 1px solid rgba(63, 119, 105, 0.14);
            border-radius: 14px;
            background: #ffffff;
            box-shadow: 0 8px 24px rgba(38, 50, 56, 0.06);
            transition: transform 200ms ease, box-shadow 200ms ease, border-color 200ms ease;
            margin-bottom: 16px;
        }

        .gallery-card:hover {
            transform: translateY(-2px);
            border-color: rgba(33, 124, 111, 0.28);
            box-shadow: 0 14px 32px rgba(38, 50, 56, 0.10);
        }

        .gallery-card-table {
            background: linear-gradient(180deg, #ffffff, rgba(248, 252, 250, 0.70));
        }

        .gallery-card-expanded {
            border: 1px solid rgba(33, 124, 111, 0.30);
            box-shadow: 0 20px 44px rgba(33, 124, 111, 0.14);
        }

        .gallery-card-section-tag {
            display: inline-block;
            padding: 3px 9px;
            border-radius: 6px;
            background: rgba(63, 119, 105, 0.08);
            color: #4a5f5a;
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            align-self: flex-start;
        }

        .gallery-card-image {
            width: 100%;
            border-radius: 10px;
            display: block;
            background: #ffffff;
            box-shadow: 0 6px 18px rgba(38, 50, 56, 0.10);
            border: 1px solid rgba(63, 119, 105, 0.10);
        }

        .gallery-card-image-lg {
            width: 100%;
            border-radius: 12px;
            display: block;
            background: #ffffff;
            box-shadow: 0 10px 28px rgba(38, 50, 56, 0.12);
            border: 1px solid rgba(63, 119, 105, 0.12);
            margin: 6px 0 10px;
        }

        .gallery-card-placeholder {
            width: 100%;
            min-height: 180px;
            border-radius: 10px;
            background: rgba(33, 124, 111, 0.06);
            border: 1px dashed rgba(63, 119, 105, 0.20);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #6f7d7b;
            font-weight: 650;
            font-size: 13px;
        }

        .gallery-card-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 17px;
            font-weight: 720;
            color: #1a2f2c;
            line-height: 1.25;
            margin-top: 4px;
        }

        .gallery-card-desc-short {
            color: #5a6d69;
            font-size: 13px;
            line-height: 1.55;
            font-weight: 500;
        }

        .gallery-card-description {
            color: #4a5f5a;
            font-size: 14px;
            line-height: 1.68;
            font-weight: 500;
            margin-top: 8px;
            padding-top: 10px;
            border-top: 1px dashed rgba(63, 119, 105, 0.14);
        }

        @media (max-width: 768px) {
            .gallery-card {
                padding: 12px;
            }
            .gallery-section-title {
                font-size: 22px;
            }
        }

        .portfolio-hero {
            margin-bottom: 8px;
            padding-bottom: 8px;
            border-bottom: 1.25px solid #1a2f2c;
            position: relative;
        }

        .portfolio-hero-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 3px 8px;
            margin-bottom: 5px;
        }

        .portfolio-hero-tag {
            display: inline-block;
            padding: 1px 6px;
            font-size: 9.5px;
            font-weight: 720;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #1a5f56;
            border-left: 2px solid #1a5f56;
            padding-left: 8px;
        }

        .portfolio-hero-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(18px, 2.2vw, 28px);
            font-weight: 760;
            line-height: 1.12;
            margin: 0 0 5px;
            color: #11221f;
            letter-spacing: -0.005em;
        }

        .portfolio-hero-sub {
            font-size: 12.5px;
            font-weight: 500;
            line-height: 1.6;
            max-width: 880px;
            color: #435854;
            margin-bottom: 8px;
        }

        .portfolio-hero-stats {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0;
            padding-top: 6px;
            border-top: 1px solid rgba(26, 47, 44, 0.22);
        }

        .portfolio-stat {
            padding: 1px 12px 1px 0;
            border-right: 1px solid rgba(26, 47, 44, 0.16);
        }
        .portfolio-stat:last-child {
            border-right: none;
        }

        .portfolio-stat span {
            display: block;
            font-size: 8.5px;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #7a8d89;
            margin-bottom: 1px;
        }

        .portfolio-stat strong {
            display: block;
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(13px, 1.5vw, 17px);
            font-weight: 720;
            color: #11221f;
            line-height: 1.05;
        }

        .eng-hero {
            margin-bottom: 6px;
        }

        .eng-section {
            padding: 7px 0;
        }

        .eng-grid {
            display: grid;
            grid-template-columns: repeat(12, minmax(0, 1fr));
            gap: 8px 12px;
            align-items: stretch;
        }

        .eng-grid-summary {
            margin-top: 8px;
            padding-top: 7px;
            border-top: 1px solid rgba(26, 47, 44, 0.14);
        }

        .eng-grid-after-phone {
            margin-top: 8px;
        }

        .eng-span-2 { grid-column: span 2; }
        .eng-span-3 { grid-column: span 3; }
        .eng-span-4 { grid-column: span 4; }
        .eng-span-5 { grid-column: span 5; }
        .eng-span-6 { grid-column: span 6; }
        .eng-span-7 { grid-column: span 7; }
        .eng-span-8 { grid-column: span 8; }
        .eng-span-9 { grid-column: span 9; }
        .eng-span-12 { grid-column: 1 / -1; }

        .eng-stack {
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
            align-content: start;
            min-width: 0;
        }

        .eng-note {
            min-height: 100%;
            padding: 8px 10px 7px;
            border-top: 1px solid rgba(26, 47, 44, 0.18);
            border-bottom: 1px solid rgba(26, 47, 44, 0.12);
            background: rgba(245, 248, 246, 0.50);
        }

        .eng-note-compact {
            padding: 7px 9px 6px;
        }

        .eng-note h4 {
            font-size: 12.5px;
            margin-bottom: 3px;
        }

        .eng-note p,
        .eng-note li {
            font-size: 11.2px;
            line-height: 1.43;
        }

        .eng-note p:last-child,
        .eng-note ul:last-child {
            margin-bottom: 0;
        }

        .eng-note a {
            color: #1a5f56;
            font-weight: 720;
            text-decoration: none;
            word-break: break-word;
        }

        .eng-phone-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 12px;
            align-items: start;
        }

        .eng-phone-grid-mixed {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }

        .portfolio-section {
            margin: 0;
            padding: 8px 0;
            border-bottom: 1px solid rgba(26, 47, 44, 0.16);
        }
        .portfolio-section:last-of-type {
            border-bottom: none;
            padding-bottom: 0;
        }

        .portfolio-section-header {
            display: flex;
            align-items: flex-start;
            gap: 0;
            margin-bottom: 6px;
            padding-bottom: 4px;
            border-bottom: 1px solid rgba(26, 47, 44, 0.14);
        }

        .portfolio-section-num { display: none; }

        .portfolio-section-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(15px, 1.7vw, 21px);
            font-weight: 760;
            line-height: 1.18;
            color: #11221f;
            margin: 0;
            letter-spacing: -0.003em;
        }

        .portfolio-section-kicker {
            display: block;
            margin-bottom: 2px;
            color: #1a5f56;
            font-size: 8.5px;
            font-weight: 760;
            letter-spacing: 0.22em;
            text-transform: uppercase;
        }

        /* ===== 多列布局混搭（图文自由组合）===== */
        .pg {
            display: grid;
            gap: 8px 14px;
            align-items: start;
        }
        .pg-2 { grid-template-columns: 1fr 1fr; }
        .pg-3 { grid-template-columns: repeat(3, 1fr); }
        .pg-4 { grid-template-columns: repeat(4, 1fr); }
        .pg-5 { grid-template-columns: repeat(5, 1fr); }
        .pg-23 { grid-template-columns: 2fr 1fr; }
        .pg-32 { grid-template-columns: 1fr 2fr; }
        .pg-single { grid-template-columns: 1fr; }
        .pg-showcase-architecture {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 7px 12px;
        }
        .pg-hypergraph {
            grid-template-columns: minmax(250px, 0.72fr) minmax(0, 1.9fr);
            gap: 8px 20px;
            align-items: stretch;
        }
        .pg-results-top {
            grid-template-columns: minmax(0, 0.86fr) minmax(400px, 1.62fr) minmax(0, 0.92fr);
            gap: 8px 14px;
            align-items: stretch;
        }
        .pg-results-visuals {
            grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
            gap: 10px 16px;
            align-items: start;
            margin: 7px 0 6px;
        }
        .pg-qualitative {
            grid-template-columns: minmax(0, 1.55fr) minmax(280px, 0.95fr);
            gap: 8px 18px;
            align-items: stretch;
        }
        .pg-analysis {
            grid-template-columns: minmax(0, 1.35fr) minmax(0, 0.72fr) minmax(0, 0.72fr);
            gap: 8px 14px;
        }
        .pg-surgi-framework {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 14px;
            align-items: stretch;
        }
        .pg-surgi-synthesis {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 14px;
            align-items: stretch;
        }
        .pg-surgi-table-row {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 14px;
            align-items: stretch;
            margin-top: 7px;
        }
        .pg-surgi-implant {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 14px;
            align-items: start;
        }
        .pg-scolioldm-overview,
        .pg-scolioldm-results,
        .pg-scolioldm-table-row,
        .pg-scolioldm-ablation {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 14px;
            align-items: start;
        }
        .pg-scolioldm-framework {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px 14px;
            align-items: stretch;
        }
        .portfolio-span-2 { grid-column: span 2; }
        .portfolio-span-3 { grid-column: span 3; }
        .portfolio-span-4 { grid-column: 1 / -1; }

        .portfolio-grid {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
            gap: 10px 18px;
            align-items: start;
        }

        .portfolio-grid-reverse > *:first-child { order: 2; }
        .portfolio-grid-reverse > *:last-child  { order: 1; }

        .portfolio-figure {
            width: 100%;
            display: flex;
            flex-direction: column;
            margin: 0;
            min-width: 0;
        }

        .portfolio-media {
            width: 100%;
            line-height: 0;
            background: transparent;
            border: 1px solid rgba(26, 47, 44, 0.08);
            border-radius: 2px;
            overflow: hidden;
            mix-blend-mode: multiply;
        }
        .portfolio-media-clean {
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent;
            border-color: transparent;
            mix-blend-mode: normal;
        }
        .portfolio-media svg { width: 100%; height: auto; display: block; }
        .portfolio-media img {
            width: 100%;
            display: block;
            border-radius: 0;
            background: transparent;
            border: none;
            mix-blend-mode: multiply;
        }

        .project-shot {
            min-width: 0;
            height: 100%;
        }

        .project-shot .portfolio-media {
            height: auto;
            display: block;
            background: transparent;
        }

        .project-shot .portfolio-media img {
            width: 100%;
            height: auto;
            object-fit: contain;
            object-position: top center;
        }

        .project-shot-main .portfolio-media {
            height: auto;
        }

        .project-shot-wide .portfolio-media {
            height: auto;
        }

        .project-shot-compact .portfolio-media {
            height: auto;
        }

        .project-shot-strip .portfolio-media {
            height: auto;
        }

        .project-shot-tall .portfolio-media {
            height: auto;
        }

        .project-shot-phone {
            height: auto;
        }

        .project-shot-phone .portfolio-media {
            height: auto;
            aspect-ratio: auto;
            max-width: 100%;
            margin: 0 auto;
            border-radius: 6px;
            box-shadow: 0 8px 18px rgba(38, 50, 56, 0.09);
            mix-blend-mode: normal;
        }

        .project-shot-phone .portfolio-media img {
            height: auto;
            object-fit: contain;
            object-position: top center;
            mix-blend-mode: normal;
        }

        .project-shot-phone-small .portfolio-media {
            max-width: 190px;
        }

        .project-shot .portfolio-figure-caption {
            margin-top: 3px;
            padding-top: 2px;
            font-size: 9.6px;
            line-height: 1.32;
        }

        .portfolio-media-clean img {
            width: auto;
            max-width: 100%;
            max-height: 310px;
            object-fit: contain;
            mix-blend-mode: normal;
        }
        .portfolio-span-3 .portfolio-media-clean img {
            width: 100%;
            max-height: 275px;
        }
        .portfolio-span-2 .portfolio-media-clean img {
            width: 100%;
            max-height: 285px;
        }
        .portfolio-tall-figure .portfolio-media-clean img {
            width: 100%;
            max-height: 330px;
        }
        .portfolio-qualitative-figure .portfolio-media-clean img {
            width: 100%;
            max-height: 300px;
        }
        .portfolio-qualitative-figure .portfolio-figure-caption {
            margin-top: 3px;
            padding-top: 2px;
            font-size: 9.8px;
            line-height: 1.35;
        }
        .portfolio-qualitative-notes {
            display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: repeat(3, minmax(0, 1fr));
            gap: 7px;
            height: 100%;
        }
        .portfolio-qualitative-notes .portfolio-content {
            min-width: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .portfolio-qualitative-notes .portfolio-content p {
            font-size: 11.4px;
            line-height: 1.46;
        }
        .pg-hypergraph .portfolio-tall-figure {
            grid-row: auto;
        }
        .portfolio-hypergraph-notes {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            grid-template-rows: repeat(2, minmax(0, 1fr));
            gap: 8px 16px;
            align-items: stretch;
            height: 100%;
        }
        .portfolio-hypergraph-notes .portfolio-content,
        .portfolio-hypergraph-notes .portfolio-insight-box {
            min-width: 0;
            margin-top: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            padding-right: 8px;
        }
        .portfolio-hypergraph-notes .portfolio-content p,
        .portfolio-hypergraph-notes .portfolio-insight-box p,
        .portfolio-hypergraph-notes li {
            font-size: 11.5px;
            line-height: 1.48;
        }

        .portfolio-figure-caption {
            margin-top: 4px;
            padding-top: 3px;
            border-top: 1px solid rgba(26, 47, 44, 0.14);
            color: #5a6a68;
            font-size: 10.5px;
            font-weight: 540;
            line-height: 1.48;
            letter-spacing: 0.005em;
        }

        .portfolio-content h4 {
            margin: 0 0 4px;
            padding-left: 8px;
            border-left: 2px solid #1a5f56;
            font-family: "Fraunces", Georgia, serif;
            font-size: 13.5px;
            font-weight: 720;
            color: #11221f;
            line-height: 1.3;
        }
        .portfolio-section-compact .portfolio-content {
            min-width: 0;
        }

        .portfolio-content p {
            margin: 0 0 5px;
            color: #3d5350;
            font-size: 12px;
            line-height: 1.58;
            font-weight: 500;
            text-align: justify;
            hyphens: auto;
        }

        .portfolio-content ul {
            margin: 2px 0 2px;
            padding-left: 16px;
        }

        .portfolio-content li {
            margin: 2px 0;
            color: #3d5350;
            font-size: 11.8px;
            line-height: 1.55;
            font-weight: 500;
        }
        .portfolio-content-lead p {
            font-size: 12.4px;
            line-height: 1.56;
            font-weight: 560;
        }

        .portfolio-content li::marker {
            color: #1a5f56;
            font-weight: 760;
        }

        .portfolio-insight-box {
            margin-top: 6px;
            padding: 6px 10px;
            background: rgba(26, 95, 86, 0.04);
            border-top: 1px solid rgba(26, 95, 86, 0.28);
            border-bottom: 1px solid rgba(26, 95, 86, 0.28);
        }
        .portfolio-fill-box {
            margin-top: 0;
            align-self: stretch;
        }

        .portfolio-insight-box strong {
            display: block;
            margin-bottom: 2px;
            color: #1a5f56;
            font-size: 8.5px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            font-weight: 760;
        }

        .portfolio-insight-box p {
            margin: 0;
            color: #2f4945;
            font-size: 11.5px;
            line-height: 1.58;
            font-weight: 560;
        }
        .surgi-note-stack {
            display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: repeat(3, minmax(0, 1fr));
            gap: 7px;
            height: 100%;
        }
        .surgi-note-stack .portfolio-content,
        .surgi-note-stack .portfolio-insight-box {
            min-width: 0;
            margin-top: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .surgi-note-stack .portfolio-content p,
        .surgi-note-stack .portfolio-insight-box p,
        .surgi-note-stack li {
            font-size: 11.4px;
            line-height: 1.46;
        }
        .surgi-hero {
            margin-bottom: 6px;
        }
        .surgi-framework .portfolio-media,
        .surgi-synthesis .portfolio-media,
        .surgi-implant .portfolio-media {
            border: none;
            background: transparent;
            mix-blend-mode: normal;
        }
        .surgi-framework .portfolio-media-clean img,
        .surgi-synthesis .portfolio-media-clean img,
        .surgi-implant .portfolio-media-clean img {
            width: 100%;
            max-height: none;
        }
        .surgi-framework-figure .portfolio-figure-caption,
        .surgi-synthesis-figure .portfolio-figure-caption,
        .surgi-figure-strip .portfolio-figure-caption {
            margin-top: 3px;
            padding-top: 2px;
            font-size: 9.9px;
            line-height: 1.34;
        }
        .surgi-figure-wide,
        .surgi-figure-strip {
            min-width: 0;
        }
        .surgi-figure-wide .portfolio-media-clean img {
            width: 100%;
            max-height: none;
        }
        .surgi-figure-strip .portfolio-media-clean img {
            width: 100%;
            max-height: none;
        }
        .surgi-data-table .data-table-caption-title {
            margin-bottom: 3px;
        }
        .surgi-data-table table.data-table {
            font-size: 10.2px;
        }
        .surgi-data-table table.data-table thead th,
        .surgi-data-table table.data-table td {
            padding: 3px 5px;
        }
        .surgi-data-table table.data-table th.th-method {
            min-width: 110px;
        }
        .surgi-data-table td.td-ds {
            width: 104px;
        }
        .surgi-conclusion {
            padding-top: 2px;
        }
        .scolioldm-hero {
            margin-bottom: 6px;
        }
        .scolioldm-note-stack {
            display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: repeat(3, minmax(0, 1fr));
            gap: 7px;
            height: 100%;
        }
        .scolioldm-note-stack .portfolio-content,
        .scolioldm-note-stack .portfolio-insight-box {
            min-width: 0;
            margin-top: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .scolioldm-note-stack .portfolio-content p,
        .scolioldm-note-stack .portfolio-insight-box p,
        .scolioldm-note-stack li {
            font-size: 11.4px;
            line-height: 1.46;
        }
        .scolioldm-dense-stack {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 7px 12px;
            align-content: start;
            min-width: 0;
            height: 100%;
        }
        .scolioldm-dense-stack .data-table-wrap {
            grid-column: 1 / -1;
        }
        .scolioldm-dense-stack .portfolio-content,
        .scolioldm-dense-stack .portfolio-insight-box {
            min-width: 0;
            margin-top: 0;
            padding-right: 6px;
        }
        .scolioldm-dense-stack .portfolio-content p,
        .scolioldm-dense-stack .portfolio-insight-box p,
        .scolioldm-dense-stack li {
            font-size: 11.15px;
            line-height: 1.42;
        }
        .scolioldm-dense-stack .portfolio-content ul {
            margin-top: 1px;
        }
        .scolioldm-dense-stack .portfolio-content li {
            margin: 1px 0;
        }
        .scolioldm-mgcm-notes {
            grid-template-rows: repeat(3, minmax(0, 1fr));
            align-content: stretch;
            align-items: stretch;
            height: 100%;
        }
        .scolioldm-mgcm-notes .portfolio-content,
        .scolioldm-mgcm-notes .portfolio-insight-box {
            border-top: 1px solid rgba(26, 47, 44, 0.18);
            border-bottom: 1px solid rgba(26, 47, 44, 0.08);
            background: rgba(245, 248, 246, 0.44);
            padding: 7px 9px 6px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .scolioldm-mgcm-notes h4 {
            font-size: 12.2px;
            margin-bottom: 3px;
        }
        .scolioldm-mgcm-notes .portfolio-insight-box strong {
            margin-bottom: 3px;
        }
        .scolioldm-mgcm-notes .portfolio-content p,
        .scolioldm-mgcm-notes .portfolio-insight-box p,
        .scolioldm-mgcm-notes li {
            font-size: 10.85px;
            line-height: 1.36;
        }
        .scolioldm-ablation-notes {
            grid-template-rows: auto minmax(0, 1fr) minmax(0, 1fr) auto;
            align-content: stretch;
        }
        .scolioldm-overview .portfolio-media,
        .scolioldm-framework .portfolio-media,
        .scolioldm-results .portfolio-media,
        .scolioldm-ablation .portfolio-media {
            border: none;
            background: transparent;
            mix-blend-mode: normal;
        }
        .scolioldm-overview .portfolio-media-clean img,
        .scolioldm-framework .portfolio-media-clean img,
        .scolioldm-results .portfolio-media-clean img,
        .scolioldm-ablation .portfolio-media-clean img,
        .scolioldm-figure-wide .portfolio-media-clean img,
        .scolioldm-figure-module .portfolio-media-clean img,
        .scolioldm-failure-strip .portfolio-media-clean img {
            width: 100%;
            max-height: none;
        }
        .scolioldm-framework-figure .portfolio-figure-caption,
        .scolioldm-results-figure .portfolio-figure-caption,
        .scolioldm-ablation-figure .portfolio-figure-caption,
        .scolioldm-figure-module .portfolio-figure-caption,
        .scolioldm-failure-strip .portfolio-figure-caption {
            margin-top: 3px;
            padding-top: 2px;
            font-size: 9.9px;
            line-height: 1.34;
        }
        .scolioldm-figure-wide,
        .scolioldm-figure-module,
        .scolioldm-failure-strip {
            min-width: 0;
        }
        .scolioldm-failure-strip {
            margin-top: 1px;
        }
        .scolioldm-failure-compact .portfolio-media-clean img {
            max-height: 255px;
            object-fit: contain;
        }
        .scolioldm-data-table .data-table-caption-title {
            margin-bottom: 3px;
        }
        .scolioldm-data-table table.data-table {
            font-size: 10.1px;
        }
        .scolioldm-data-table table.data-table thead th,
        .scolioldm-data-table table.data-table td {
            padding: 3px 5px;
        }
        .scolioldm-data-table table.data-table th.th-method {
            min-width: 112px;
        }
        .scolioldm-ablation-notes .scolioldm-data-table table.data-table {
            font-size: 9.6px;
        }
        .scolioldm-ablation-notes .scolioldm-data-table table.data-table thead th,
        .scolioldm-ablation-notes .scolioldm-data-table table.data-table td {
            padding: 2px 4px;
        }
        .scolioldm-ablation-notes .data-table-cap {
            font-size: 9.7px;
            line-height: 1.34;
        }
        .scolioldm-conclusion {
            padding-top: 2px;
        }

        .portfolio-table-figure {
            width: 100%;
            display: flex;
            flex-direction: column;
            min-width: 0;
            overflow: visible;
        }

        .portfolio-table-label {
            display: inline-block;
            margin-bottom: 4px;
            font-size: 9px;
            font-weight: 760;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #7a8d89;
        }

        /* ======= 学术风格手绘表格 ======= */
        .portfolio-table-figure .portfolio-media-clean img {
            width: auto;
            max-height: none;
            max-width: 100%;
        }
        .portfolio-tight-notes {
            margin-top: 5px;
        }

        .data-table-wrap { width: 100%; }
        .portfolio-section-compact > .data-table-wrap {
            margin-top: 6px;
        }

        .data-table-caption-title {
            font-family: "Fraunces", Georgia, serif;
            font-size: 13px;
            font-weight: 720;
            color: #11221f;
            margin-bottom: 4px;
            padding-bottom: 2px;
            border-bottom: 1px solid rgba(26, 47, 44, 0.16);
        }

        .data-table-scroll {
            width: 100%;
            overflow-x: auto;
            overflow-y: hidden;
            -webkit-overflow-scrolling: touch;
        }

        table.data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 10.8px;
            color: #233532;
            line-height: 1.32;
            background: transparent;
            border-top: 1.4px solid #1a2f2c;
            border-bottom: 1.4px solid #1a2f2c;
        }

        table.data-table thead th {
            background: rgba(26, 95, 86, 0.06);
            color: #11221f;
            font-weight: 740;
            text-align: right;
            padding: 4px 6px;
            vertical-align: bottom;
            border-bottom: 0.8px solid #1a2f2c;
            font-size: 10px;
            letter-spacing: 0.005em;
        }
        table.data-table thead th:first-child,
        table.data-table td.td-method,
        table.data-table td.td-setting,
        table.data-table td.td-ds { text-align: left; }

        table.data-table th.th-method { min-width: 130px; }
        table.data-table th.th-grp { text-align: center; background: rgba(26, 95, 86, 0.08); }
        table.data-table tr.tr-subh th {
            font-size: 9.8px;
            font-weight: 680;
            color: #3d5350;
            background: rgba(26, 95, 86, 0.08);
            padding: 3px 6px;
        }
        table.data-table th.th-rank { background: rgba(26, 95, 86, 0.12); }

        table.data-table td {
            padding: 3px 6px;
            text-align: right;
            font-variant-numeric: tabular-nums;
            border: none;
            vertical-align: middle;
            color: #304441;
        }

        table.data-table tbody tr:nth-child(even) td {
            background: rgba(26, 95, 86, 0.03);
        }

        table.data-table tbody tr.tr-best td {
            background: rgba(26, 95, 86, 0.14) !important;
            color: #0d2b27;
            font-weight: 700;
            border-top: 0.8px dashed rgba(26, 95, 86, 0.42);
            border-bottom: 0.8px dashed rgba(26, 95, 86, 0.42);
        }

        table.data-table td.td-method strong { font-weight: 680; }

        .yr-tag {
            display: inline-block;
            padding: 0.5px 4px;
            margin-right: 4px;
            font-size: 8.8px;
            font-weight: 720;
            color: #5a6a68;
            border: 1px solid rgba(26, 47, 44, 0.20);
            border-radius: 2px;
            letter-spacing: 0.02em;
            vertical-align: middle;
        }
        .yr-tag-ours {
            background: #1a5f56;
            color: #ffffff;
            border-color: #1a5f56;
        }

        td.td-ds {
            font-family: "Fraunces", Georgia, serif;
            font-weight: 720;
            color: #1a5f56;
            font-size: 11.2px;
            border-right: 1px solid rgba(26, 47, 44, 0.14);
        }
        td.td-setting { font-weight: 560; font-size: 10.6px; }

        .data-table-cap {
            margin-top: 3px;
            padding-top: 2px;
            border-top: 1px solid rgba(26, 47, 44, 0.12);
            font-size: 10.4px;
            line-height: 1.5;
            color: #5a6a68;
            font-weight: 540;
        }

        .portfolio-conclusion {
            margin: 0;
            padding: 6px 0 0;
            border-top: none;
        }

        .portfolio-conclusion h3 {
            margin: 0 0 6px;
            font-family: "Fraunces", Georgia, serif;
            font-size: clamp(16px, 1.8vw, 21px);
            font-weight: 760;
            color: #11221f;
            line-height: 1.15;
            letter-spacing: -0.005em;
        }

        .portfolio-conclusion p {
            margin: 0 0 5px;
            color: #3d5350;
            font-size: 12px;
            line-height: 1.65;
            font-weight: 500;
            text-align: justify;
            hyphens: auto;
            max-width: 900px;
        }

        .portfolio-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 3px;
            margin-top: 5px;
            padding-top: 5px;
            border-top: 1px solid rgba(26, 47, 44, 0.18);
        }

        .portfolio-chip {
            padding: 2px 7px;
            font-size: 10.5px;
            font-weight: 620;
            color: #1a5f56;
            border: 1px solid rgba(26, 95, 86, 0.30);
            border-radius: 2px;
            background: transparent;
            letter-spacing: 0.01em;
        }

        @media (max-width: 900px) {
            .pg-2, .pg-3, .pg-4, .pg-23, .pg-32,
            .pg-showcase-architecture, .pg-hypergraph, .pg-results-top,
            .pg-results-visuals, .pg-qualitative, .pg-analysis,
            .pg-surgi-framework, .pg-surgi-synthesis, .pg-surgi-table-row, .pg-surgi-implant,
            .pg-scolioldm-overview, .pg-scolioldm-framework, .pg-scolioldm-results,
            .pg-scolioldm-table-row, .pg-scolioldm-ablation,
            .eng-grid, .eng-grid-summary,
            .portfolio-grid, .portfolio-grid-reverse,
            .portfolio-hypergraph-notes,
            .portfolio-qualitative-notes,
            .scolioldm-dense-stack {
                grid-template-columns: 1fr;
                gap: 8px 0;
            }
            .eng-phone-grid,
            .eng-phone-grid-mixed {
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 8px 10px;
            }
            .eng-span-2, .eng-span-3, .eng-span-4, .eng-span-5,
            .eng-span-6, .eng-span-7, .eng-span-8, .eng-span-9,
            .eng-span-12 {
                grid-column: 1 / -1;
            }
            .portfolio-span-2,
            .portfolio-span-3,
            .portfolio-span-4 {
                grid-column: auto;
            }
            .portfolio-grid-reverse > *:first-child { order: 1; }
            .portfolio-grid-reverse > *:last-child  { order: 2; }
            .portfolio-hero-stats {
                grid-template-columns: repeat(2, 1fr);
                gap: 6px 0;
            }
            .portfolio-stat:nth-child(2) { border-right: none; }
            .portfolio-section { padding: 6px 0; }
            .portfolio-section-header { margin-bottom: 6px; padding-bottom: 3px; }
            .portfolio-media-clean img,
            .portfolio-span-2 .portfolio-media-clean img,
            .portfolio-span-3 .portfolio-media-clean img,
            .portfolio-tall-figure .portfolio-media-clean img {
                width: 100%;
                max-height: none;
            }
            .project-shot .portfolio-media,
            .project-shot-main .portfolio-media,
            .project-shot-wide .portfolio-media,
            .project-shot-compact .portfolio-media,
            .project-shot-strip .portfolio-media,
            .project-shot-tall .portfolio-media {
                height: auto;
                aspect-ratio: auto;
            }
            .project-shot .portfolio-media img,
            .project-shot-main .portfolio-media img,
            .project-shot-wide .portfolio-media img,
            .project-shot-compact .portfolio-media img,
            .project-shot-strip .portfolio-media img,
            .project-shot-tall .portfolio-media img {
                height: auto;
                object-fit: contain;
            }
            .project-shot-phone .portfolio-media,
            .project-shot-phone-small .portfolio-media {
                height: auto;
                aspect-ratio: auto;
                max-width: none;
            }
            .project-shot-phone .portfolio-media img,
            .project-shot-phone-small .portfolio-media img {
                height: auto;
                object-fit: contain;
            }
            table.data-table { font-size: 10px; }
            table.data-table thead th, table.data-table td { padding: 3px 4px; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
