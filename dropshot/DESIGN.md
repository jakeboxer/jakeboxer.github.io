---
name: Dropshot
description: Electric blue rave flyer for a tiny Mac utility.
colors:
  blue: "#001bdb"
  ink: "#080b21"
  ice: "#ffffff"
  acid: "#e5ff00"
  line: "rgba(237,243,255,.35)"
typography:
  display:
    fontFamily: "Anton, sans-serif"
    fontSize: "clamp(100px,15.8vw,245px)"
    fontWeight: 400
    lineHeight: 0.94
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Anton, sans-serif"
    fontSize: "clamp(40px,5vw,76px)"
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: "-.01em"
  body:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "11px"
    fontWeight: 700
    letterSpacing: ".08em"
rounded:
  square: "0"
  key: "4px"
  circle: "50%"
spacing:
  gutter: "3.7%"
  gutter-mobile: "6%"
  small: "8px"
  medium: "24px"
  large: "40px"
components:
  download-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.acid}"
    rounded: "{rounded.square}"
    padding: "20px 19px"
    width: "100%"
  motion-button:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.ice}"
    rounded: "{rounded.square}"
    padding: "9px 12px"
  format-sticker:
    backgroundColor: "{colors.acid}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "20px 18px"
    width: "166px"
---

# Design System: Dropshot

## Homemade rave flyer

The user explicitly requested a jankier revision after the first polished poster. Preserve deliberately mismatched Anton, Georgia italic, Courier and Arial; crooked cut-paper strips; clashing pink (#ff9edd) and acid yellow; dashed borders; hard offset shadows; and the old-style bevel on the unavailable download button. These are intentional exceptions to a polished interface treatment.

## Composition

The blue field is continuous. Oversized DROP / CONVERT / PASTE dominates; CONVERT is an italic yellow strip. The real app icon rocks slowly beside it. The hero explanations use pasted-on white and dark scraps. The repeating format banner leads directly into the footer; the how-it-works and download sections were removed at the user’s request. The header retains a disabled download-coming-soon control.

## Assets

`assets/app-icon.png` is copied unchanged from the user-provided raw PNG. The earlier screenshot is reference-only. Anton and its license are self-hosted under assets.

## Behavior

The icon rocks continuously without a pause button, as explicitly requested by the user. Reduced-motion preference still stops movement. No flashing or audio. Anchor navigation and keyboard focus remain available. The 700px breakpoint stacks content and reduces type; keep page width contained despite rotations.

## Constraints

Keep product instructions and actual availability clear. Do not turn the download into a working link until a published installer is verified. Do not straighten the composition or harmonize the typography merely to make it more conventional.

The ticker repeats crossed-out HEIC, a star, JPEG, a star, PNG, and a star.

The hero headline is reduced to clamp(70px,9vw,130px), or 17vw on mobile, to leave room for a future screen recording. The iPhone-photos box and icon size caption are removed. No demo section goes below the banner.

The remaining hero summary is removed. A 16:9 screen-recording placeholder now sits inside the hero above the banner, without an external label. It is a static placeholder, not a playable video.

The original layout is retained: headline upper left, full-size app icon upper right, and recording below the headline. Only the headline is reduced; the icon retains its previous 29% desktop and 32% mobile width.

The headline reads “i hate .HEICs” on one line with white condensed, yellow italic, and pink condensed treatments. The recording caption reads “Drag a .HEIC out of Messages.app, convert it to a REAL image format, and paste it ANYWHERE.”. Pink JPEG and yellow PNG stickers form a pair.

Header, hero and footer are centered with a 1200px maximum width and responsive gutters. The format ticker remains full-width.

The user requested invariant element sizes while resizing. Header, hero and footer now use a fixed 1200px canvas, with 40px content gutters, 96px headline, 348px icon and 640px recording. Width breakpoints are removed; narrow windows scroll horizontally. The ticker remains full-bleed and reduced-motion preferences remain supported.

The fixed canvas is now 1024px with a 520px recording placeholder. The 348px icon and 96px headline retain their sizes; the full-width ticker is unchanged.

Touch-first devices (`hover: none` and `pointer: coarse`) use a separate single-column layout in either orientation: header, headline, recording and caption, app icon, JPEG/PNG stickers, format ticker, then footer. This layout has a 600px content maximum with phone-sized gutters and type. Desktop window resizing continues to use the fixed 1024px canvas and invariant element sizes; viewport width alone never activates the mobile layout.
