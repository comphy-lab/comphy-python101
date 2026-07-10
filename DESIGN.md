# Website design brief

## Visual thesis

A computational lab notebook meets a scientific atlas: warm paper, deep ink,
capillary-blue flow lines, and one sharp coral annotation colour.

## Content plan

1. **Hero** — one promise: learn to reason with code rather than memorise
   syntax; the five-step reasoning loop is the dominant visual.
2. **Support** — show the quick and full routes, with the same course spine.
3. **Detail** — map each lesson to a scientific decision and a tangible output.
4. **Final action** — start lesson zero, inspect the repository, or teach the
   course.

## Interaction thesis

- The hero copy enters as one calm staggered sequence.
- The reasoning-loop path draws once, turning an abstract workflow into motion.
- Curriculum rows reveal their output on hover or keyboard focus; the route
  spine remains sticky on wide screens.

All motion respects `prefers-reduced-motion`.

## Purpose

Give future CoMPhy students enough computational judgement to enter a real
research repository without treating Python as a bag of spells. The interface
should feel rigorous, open, and unintimidating.

## Tone

Editorial scientific field notebook, with a restrained Swiss grid and a small
amount of capillary-flow character.

## Constraints

- Static MkDocs site deployed by GitHub Actions.
- Canonical URL: `https://comphy-lab.org/comphy-python101/`.
- Responsive from 320 px upwards, keyboard navigable, WCAG AA contrast.
- Minimal JavaScript and no decorative dependency bundle.
- Fast enough to remain useful on institutional Wi-Fi.

## Differentiation

The memorable object is the reasoning loop:

**question → representation → transformation → verification → evidence**

It appears in the hero, lesson structure, exercises, and capstone assessment.
