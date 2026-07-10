---
hide:
  - navigation
  - toc
---

<div class="course-home">

<section class="course-hero" aria-labelledby="course-title">
  <div class="course-hero__copy">
    <p class="course-eyebrow">CoMPhy Lab · Open course</p>
    <h1 id="course-title">Think in Python.</h1>
    <p class="course-hero__lede">
      Learn to turn a physical question into trustworthy computation and a
      reproducible scientific figure. Syntax is the tool. Reasoning is the
      course.
    </p>
    <div class="course-actions">
      <a class="course-button course-button--primary" href="start/overview/">Choose a route</a>
      <a class="course-button" href="core/01-thinking/">Start lesson 01</a>
    </div>
  </div>

  <svg class="course-loop" viewBox="0 0 620 470" role="img" aria-labelledby="loop-title loop-desc">
    <title id="loop-title">The course reasoning loop</title>
    <desc id="loop-desc">A path connects question, representation, transformation, verification, and evidence.</desc>
    <path d="M78 238C102 90 254 61 342 132C431 204 377 333 477 341C551 347 577 271 542 206" fill="none" stroke="#2f6f9f" stroke-width="3" opacity=".35"/>
    <path class="course-loop__path" d="M78 238C102 90 254 61 342 132C431 204 377 333 477 341C551 347 577 271 542 206" fill="none" stroke="#0b5d5b" stroke-width="8" stroke-linecap="round"/>
    <g class="course-loop__node">
      <circle cx="78" cy="238" r="44" fill="#0b5d5b"/>
      <text x="78" y="243" fill="#fff" font-size="17" text-anchor="middle">question</text>
    </g>
    <g class="course-loop__node">
      <circle cx="174" cy="100" r="51" fill="#2f6f9f"/>
      <text x="174" y="105" fill="#fff" font-size="16" text-anchor="middle">represent</text>
    </g>
    <g class="course-loop__node">
      <circle cx="350" cy="139" r="53" fill="#0b5d5b"/>
      <text x="350" y="144" fill="#fff" font-size="16" text-anchor="middle">transform</text>
    </g>
    <g class="course-loop__node">
      <circle cx="468" cy="342" r="49" fill="#e45d3f"/>
      <text x="468" y="347" fill="#fff" font-size="16" text-anchor="middle">verify</text>
    </g>
    <g class="course-loop__node">
      <circle cx="542" cy="206" r="47" fill="#0b5d5b"/>
      <text x="542" y="211" fill="#fff" font-size="16" text-anchor="middle">evidence</text>
    </g>
    <path d="M51 323C147 391 261 410 369 384" fill="none" stroke="#13201f" stroke-width="2" stroke-dasharray="5 8" opacity=".5"/>
    <text x="52" y="351" fill="currentColor" font-family="IBM Plex Mono, monospace" font-size="16">predict before running</text>
  </svg>
</section>

<section class="course-section" aria-labelledby="routes-title">
  <div class="course-section__head">
    <p class="course-eyebrow">One source, two speeds</p>
    <h2 id="routes-title">Choose depth, not a different course.</h2>
    <p>
      The quick route selects six lessons from the full route. There is no
      second nano repository to drift out of date.
    </p>
  </div>
  <div class="course-routes">
    <article class="course-route">
      <span class="course-route__time">6–8 hours</span>
      <h3>Quick route</h3>
      <p>
        For students who have already written some Python and need the CoMPhy
        habits: functions, arrays, debugging, schemas, tools, and the log lab.
      </p>
      <a href="start/overview/#quick-route">See the six lessons →</a>
    </article>
    <article class="course-route">
      <span class="course-route__time">20–24 hours</span>
      <h3>Full route</h3>
      <p>
        For a first serious encounter with Python, including control flow,
        plotting, numerical verification, collaboration, and the capstone.
      </p>
      <a href="start/overview/#full-route">See the complete route →</a>
    </article>
  </div>
</section>

<section class="course-section" aria-labelledby="curriculum-title">
  <div class="course-section__head">
    <p class="course-eyebrow">Equation → evidence</p>
    <h2 id="curriculum-title">A scientific-computing spine.</h2>
    <p>
      Each lesson names the decision you are learning to make and the artefact
      you will leave behind.
    </p>
  </div>
  <div class="course-curriculum">
    <div class="course-lesson"><span class="course-lesson__number">01</span><a href="core/01-thinking/">Think like a program</a><span class="course-lesson__output">a traced data pipeline</span></div>
    <div class="course-lesson"><span class="course-lesson__number">02</span><a href="core/02-functions/">Functions are claims</a><span class="course-lesson__output">a unit-consistent contract</span></div>
    <div class="course-lesson"><span class="course-lesson__number">03</span><a href="core/03-arrays/">Arrays are the language</a><span class="course-lesson__output">a shape-safe transformation</span></div>
    <div class="course-lesson"><span class="course-lesson__number">05</span><a href="core/05-debugging/">Debugging and tests</a><span class="course-lesson__output">a smallest failing example</span></div>
    <div class="course-lesson"><span class="course-lesson__number">06</span><a href="core/06-data/">Data has a schema</a><span class="course-lesson__output">a validated reduction</span></div>
    <div class="course-lesson"><span class="course-lesson__number">08</span><a href="core/08-numerics/">Numerical verification</a><span class="course-lesson__output">an error or convergence argument</span></div>
    <div class="course-lesson"><span class="course-lesson__number">11</span><a href="comphy/11-basilisk-log/">Read a Basilisk log</a><span class="course-lesson__output">reduced evidence and a figure</span></div>
    <div class="course-lesson"><span class="course-lesson__number">13</span><a href="comphy/13-capstone/">Reproduction capsule</a><span class="course-lesson__output">one-command public science</span></div>
  </div>
</section>

<section class="course-section" aria-labelledby="principles-title">
  <div class="course-section__head">
    <p class="course-eyebrow">Taste is teachable</p>
    <h2 id="principles-title">What good code feels like.</h2>
  </div>
  <div class="course-manifesto">
    <div class="course-principle"><strong>Names carry physics.</strong><span>`radius_m` beats `r`; shape and units are part of the state.</span></div>
    <div class="course-principle"><strong>Failure should be loud.</strong><span>Reject an invalid schema before it becomes a smooth, wrong curve.</span></div>
    <div class="course-principle"><strong>I/O is not analysis.</strong><span>Keep reading, transforming, and plotting separate enough to test.</span></div>
    <div class="course-principle"><strong>Tests are scientific claims.</strong><span>Use limits, invariants, benchmarks, and regression values.</span></div>
    <div class="course-principle"><strong>A plot is an argument.</strong><span>Axes, normalisation, and omissions must serve the stated question.</span></div>
    <div class="course-principle"><strong>Rebuild beats remember.</strong><span>A fresh clone should reproduce the result without folklore.</span></div>
  </div>
</section>

<section class="course-section">
  <div class="course-final">
    <div>
      <p class="course-eyebrow">Start with the question</p>
      <h2>Trace one program before writing one.</h2>
    </div>
    <div class="course-actions">
      <a class="course-button course-button--primary" href="core/01-thinking/">Begin lesson 01</a>
      <a class="course-button" href="https://github.com/comphy-lab/comphy-python101">Open the repository</a>
    </div>
  </div>
</section>

</div>
