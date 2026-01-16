# Lumina Position Sizer - Development Guide

This document is for future developers or AI agents working on this project.

## Project Overview
Lumina is a TradingView extension that provides a floating risk calculator.

## Recent Major Fixes & Features
- **Unpacked Build**: A `dist/` folder was created containing all prepared files for Chrome/Edge extension loading.
- **CSP Compliance**: Inline scripts in `popup.html` were moved to `popup.js` to satisfy Manifest V3 requirements.
- **Permissions**: `manifest.json` was updated to `<all_urls>` for testing, though it's optimized for TradingView.
- **Auto-Show on TradingView**: The widget is configured to appear automatically on `tradingview.com` and hidden on other sites.
- **Symbol Auto-Detection**: Restored the `MutationObserver` on the page title to detect symbol changes (e.g., BTCUSD -> ETHUSD).
- **Minimal View Toggle**: Clicking the "Lumina" logo toggles between a "Full Calculator" and a "Minimal View" (Sponsors only).
- **Positioning**: Default position is set to the bottom-right of the screen.

## How to Continue Development
1. **Source Files**: Edit files in the root directory (`extension_entry.js`, `popup.html`, etc.).
2. **Build/Dist**: After editing, YOU MUST COPY the files to the `dist/` folder using:
   `Copy-Item <filename> -Destination dist -Force`
3. **Testing**:
   - Load the `dist/` folder in `chrome://extensions`.
   - Always reload the extension after making changes.
   - Test on `tradingview.com/chart`.

## Known State
- Bundle: `extension_entry.js` is a pre-minified/bundled file. We have edited it directly to add patches.
- Logic: The calculator logic is consider "done" by the user. Current focus is on UI/UX and visibility behavior.
